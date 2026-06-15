#!/usr/bin/env python3
"""Build the combined "Air + Material" icon theme.

Strategy: prefer Air icons, fall back to Material icons to fill the gaps.

The Air theme and the Material theme use disjoint iconDefinition namespaces
(`_name` / `_name_light` vs. `_material_name_dark` / `_material_name_light`),
so their definitions can be merged without collisions. For every association
map (fileExtensions, fileNames, languageIds, ...) Air's entries win and
Material's entries fill anything Air does not define. Folder name maps come
from Material since Air only ships a single generic folder icon.

Run from the repo root:  python3 scripts/build_combined_theme.py
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AIR_PATH = os.path.join(ROOT, "air-icon-theme.json")
MATERIAL_PATH = os.path.join(ROOT, "air-material-icon-theme.json")
OUT_PATH = os.path.join(ROOT, "air-material-combined-icon-theme.json")


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def air_preferred(material_map, air_map):
    """Merge two association maps so Air wins and Material fills the gaps."""
    merged = dict(material_map or {})
    merged.update(air_map or {})
    return merged


def build(air, material):
    # Definitions live in disjoint namespaces; assert that stays true so a
    # future rename can never silently clobber an icon.
    collisions = set(air["iconDefinitions"]) & set(material["iconDefinitions"])
    if collisions:
        raise SystemExit(f"iconDefinition namespace collision: {sorted(collisions)}")

    combined = {
        "hidesExplorerArrows": air.get("hidesExplorerArrows", False),
        "iconDefinitions": {
            **material["iconDefinitions"],
            **air["iconDefinitions"],
        },
        # Generic file: Air is preferred. Folders come from Material because
        # Air ships no folder system to prefer (it never wires up a default
        # folder or any named folders), so Material fills that gap entirely.
        "file": air["file"],
        "folder": air.get("folder", material.get("folder")),
        "folderExpanded": air.get("folderExpanded", material.get("folderExpanded")),
        # Associations: Air wins, Material fills the gaps.
        "fileExtensions": air_preferred(
            material.get("fileExtensions"), air.get("fileExtensions")
        ),
        "fileNames": air_preferred(material.get("fileNames"), air.get("fileNames")),
        "languageIds": air_preferred(
            material.get("languageIds"), air.get("languageIds")
        ),
        # Air has no named folders, so these come entirely from Material.
        "folderNames": dict(material.get("folderNames", {})),
        "folderNamesExpanded": dict(material.get("folderNamesExpanded", {})),
    }

    air_light = air.get("light", {})
    material_light = material.get("light", {})
    combined["light"] = {
        "file": air_light.get("file", combined["file"]),
        "folder": air_light.get("folder", material_light.get("folder")),
        "folderExpanded": air_light.get(
            "folderExpanded", material_light.get("folderExpanded")
        ),
        "fileExtensions": air_preferred(
            material_light.get("fileExtensions"), air_light.get("fileExtensions")
        ),
        "fileNames": air_preferred(
            material_light.get("fileNames"), air_light.get("fileNames")
        ),
        "languageIds": air_preferred(
            material_light.get("languageIds"), air_light.get("languageIds")
        ),
        "folderNames": dict(material_light.get("folderNames", {})),
        "folderNamesExpanded": dict(material_light.get("folderNamesExpanded", {})),
    }
    # Drop empty optional maps to keep the file tidy.
    for scope in (combined, combined["light"]):
        for key in ("languageIds", "folderNames", "folderNamesExpanded"):
            if key in scope and not scope[key]:
                del scope[key]

    return combined


def main():
    air = load(AIR_PATH)
    material = load(MATERIAL_PATH)
    combined = build(air, material)

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(combined, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    air_exts = set(air.get("fileExtensions", {}))
    print(f"wrote {os.path.relpath(OUT_PATH, ROOT)}")
    print(f"  iconDefinitions: {len(combined['iconDefinitions'])}")
    print(f"  fileExtensions:  {len(combined['fileExtensions'])} "
          f"({len(air_exts)} from Air)")
    print(f"  fileNames:       {len(combined['fileNames'])}")
    print(f"  folderNames:     {len(combined.get('folderNames', {}))}")


if __name__ == "__main__":
    main()
