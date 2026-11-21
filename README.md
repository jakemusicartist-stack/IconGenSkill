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

## 🤖 Universal Agent Prompt (One-Click Install)

Copy and paste this prompt directly into **any** AI agent chat (Google Antigravity, Gemini CLI, Claude Code, Cursor, Windsurf, Codex, OpenCode, or Copilot CLI) to install this skill automatically:

```text
Please download and install the macOS Icon Designer skill from:
https://github.com/jakemusicartist-stack/IconGenSkill

Instructions:
1. Clone or download the repository from https://github.com/jakemusicartist-stack/IconGenSkill
2. Install the `skills/macos-icon-designer` folder universally into this agent's active skill path:
   - On Windows: run `install.bat --all` from the repository root, or copy `skills/macos-icon-designer` into `~/.gemini/config/skills/`, `~/.claude/skills/`, `~/.agents/skills/`, or the active project's `.cursor/skills/`.
   - On macOS/Linux: run `bash install.sh --all` from the repository root, or copy `skills/macos-icon-designer` into `~/.gemini/config/skills/`, `~/.claude/skills/`, or `~/.agents/skills/`.
3. Verify that `SKILL.md`, `scripts/`, `references/`, and `templates/` are all present.
4. Confirm once installed and ready, then prompt me with the 6 discovery questions to design my macOS vector icon.
```

---

## One-Click Manual Installation

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

## License

MIT License. Free to use in personal and commercial projects.
