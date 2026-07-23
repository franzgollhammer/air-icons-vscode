# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2026-07-23

### Changed
- **Air File Icons** now uses the same console icon for the shell family, so all three themes share one shell icon
- Retired the `_shell` → `_material_console_*` mapping override added in 0.4.0 — the combined theme generator is back to the plain "Air wins, Material fills the gaps" rule now that both source icons are identical

## [0.4.0] - 2026-07-23

### Changed
- New console icon (green hexagon) for the shell family in **Air Material Icons** and **Air + Material Icons** — `sh`, `bash`, `zsh`, `fish`, `ksh`, `csh`, rc/profile files, and git hooks
- **Air + Material Icons** now prefers Material's console icon over Air's generic shell icon so the whole shell family renders consistently
- **Air File Icons** is unchanged and keeps its own shell icon

## [0.3.0] - 2026-06-15

### Added
- **Air + Material Icons** hybrid theme: prefers Air icons and fills every gap with Material icons (including Material's named-folder set)
- `scripts/build_combined_theme.py` generator (`npm run build:combined`) that deterministically merges the two source themes

## [0.2.0] - 2026-06-11

### Added
- Air Material Icons theme mirrored from the Air Icons Zed extension
- 1245 colorful Material icons with filename, extension, and named-folder mappings

## [0.1.1] - 2026-04-28

### Changed
- README preview image now shows full icon grid (dark + light variants)

## [0.1.0] - 2026-04-23

### Added
- Initial release
- 112 file type icons with dark and light variants
- File extension, file name, and language ID mappings
- Folder icons
- Marketplace metadata (README, icon, banner, keywords)
