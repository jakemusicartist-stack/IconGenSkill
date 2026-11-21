# macOS Icon Designer Skill

A specialized AI agent skill for designing vector desktop app icons following desktop squircle styling, layered depth, and multi-resolution export.

Compatible with **Google Antigravity**, **Gemini CLI**, **Claude Code**, **Cursor**, **Codex**, and universal agent environments.

---

## Features

- **100% Vector Output**: Generates clean, standalone SVG icons with standard SVG gradients and filter effects.
- **Continuous Curvature Squircle**: Accurately shapes the icon canvas using superellipse cubic bezier geometry.
- **Dual-Tier Shadows**: Combines contact ambient occlusion with directional soft drop shadows.
- **Interactive Discovery Questionnaire**: Guides developers through metaphor, materials, depth, and color choices before generating artwork.
- **Live Dock & Multi-Scale Verification**: Includes scripts to generate interactive HTML previews in dock contexts and size ladders (16px to 1024px).
- **Automated Asset Export**: Exports master SVGs to multi-resolution `.icns` packages and PNG ladders.

---

## One-Click Installation

### Windows
Run the installer script:
```cmd
install.bat
```
To install silently for a specific platform:
```cmd
install.bat --all
install.bat --gemini
install.bat --claude
install.bat --universal
```

### macOS / Linux
Run the installer script:
```bash
chmod +x install.sh
./install.sh
```
Or with flags:
```bash
./install.sh --all
```

---

## Target Directories

| Environment | Installation Path |
|---|---|
| **Google Antigravity / Gemini CLI** | `~/.gemini/config/skills/macos-icon-designer` |
| **Claude Code** | `~/.claude/skills/macos-icon-designer` |
| **Universal Agents Standard** | `~/.agents/skills/macos-icon-designer` |

---

## How to Use

Once installed, invoke your AI agent with prompts such as:
- *"Design a macOS-style app icon for my application called [AppName]."*
- *"Create a vector squircle icon with liquid glass materials for [Concept]."*
- *"Generate a dark mode desktop icon for [Tool]."*

The agent will prompt you with the design questionnaire, review peer benchmarks, and assemble your production SVG.

---

## Publishing to GitHub

To publish this repository to your GitHub account:
1. Run `publish_to_github.bat`
2. Follow the on-screen prompt to link your GitHub repository URL.

---

## License

MIT License. Free to use in personal and commercial projects.
