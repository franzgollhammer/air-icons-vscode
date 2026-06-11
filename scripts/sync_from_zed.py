#!/usr/bin/env python3
"""Sync the Air Material Icons theme and assets from the sibling Zed extension."""

import argparse
import json
import shutil
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
OUT_THEME = REPO / "air-material-icon-theme.json"
OUT_ICONS = REPO / "icons" / "air-material"


def definition_id(name: str, appearance: str) -> str:
    return f"_material_{name}_{appearance}"


def map_icons(mapping: dict[str, str], appearance: str) -> dict[str, str]:
    return {key: definition_id(icon, appearance) for key, icon in mapping.items()}


def icon_name(path: str) -> str:
    return Path(path).stem


def build_theme(dark: dict, light: dict) -> dict:
    definitions = {}
    for appearance, source in (("dark", dark), ("light", light)):
        for name, icon in source["file_icons"].items():
            definitions[definition_id(name, appearance)] = {
                "iconPath": icon["path"]
            }

    def directory_names(source: dict, key: str, appearance: str) -> dict[str, str]:
        return {
            name: definition_id(icon_name(paths[key]), appearance)
            for name, paths in source["named_directory_icons"].items()
        }

    def appearance_mappings(source: dict, appearance: str) -> dict:
        return {
            "file": definition_id("default", appearance),
            "folder": definition_id(
                icon_name(source["directory_icons"]["collapsed"]), appearance
            ),
            "folderExpanded": definition_id(
                icon_name(source["directory_icons"]["expanded"]), appearance
            ),
            "fileExtensions": map_icons(source["file_suffixes"], appearance),
            "fileNames": map_icons(source["file_stems"], appearance),
            "folderNames": directory_names(source, "collapsed", appearance),
            "folderNamesExpanded": directory_names(source, "expanded", appearance),
        }

    theme = {
        "hidesExplorerArrows": False,
        "iconDefinitions": definitions,
        **appearance_mappings(dark, "dark"),
        "light": appearance_mappings(light, "light"),
    }
    return theme


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "zed_repo",
        nargs="?",
        type=Path,
        default=REPO.parent / "air-icons-zed",
        help="path to the air-icons-zed repository",
    )
    args = parser.parse_args()
    zed_repo = args.zed_repo.resolve()

    source_theme = zed_repo / "icon_themes" / "air-material-icons.json"
    source_icons = zed_repo / "icons" / "air-material"
    if not source_theme.is_file() or not source_icons.is_dir():
        raise SystemExit(f"Air Material Icons source not found in {zed_repo}")

    zed_theme = json.loads(source_theme.read_text())
    appearances = {theme["appearance"]: theme for theme in zed_theme["themes"]}
    theme = build_theme(appearances["dark"], appearances["light"])

    if OUT_ICONS.exists():
        shutil.rmtree(OUT_ICONS)
    shutil.copytree(source_icons, OUT_ICONS)
    OUT_THEME.write_text(json.dumps(theme, indent=2) + "\n")

    print(f"wrote {OUT_THEME}")
    print(f"copied {sum(1 for path in OUT_ICONS.rglob('*') if path.is_file())} assets")


if __name__ == "__main__":
    main()
