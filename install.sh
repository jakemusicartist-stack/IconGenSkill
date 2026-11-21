#!/usr/bin/env bash
# macOS App Icon Designer - Multi-Agent Skill Installer (macOS / Linux)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_SKILL="$SCRIPT_DIR/skills/macos-icon-designer"

if [ ! -f "$SOURCE_SKILL/SKILL.md" ]; then
    if [ -f "$SCRIPT_DIR/SKILL.md" ]; then
        SOURCE_SKILL="$SCRIPT_DIR"
    else
        echo "❌ [ERROR] Could not find macos-icon-designer skill directory!"
        exit 1
    fi
fi

echo "======================================================================="
echo "   APPLE macOS APP ICON DESIGNER - MULTI-AGENT SKILL INSTALLER"
echo "======================================================================="
echo ""

copy_skill() {
    local target="$1"
    echo "  -> Installing to: $target"
    mkdir -p "$target"
    cp -R "$SOURCE_SKILL"/* "$target/"
    echo "  ✅ Installed cleanly."
}

install_all() {
    echo ""
    echo "[1/3] Installing to Google Antigravity & Gemini CLI..."
    copy_skill "$HOME/.gemini/config/skills/macos-icon-designer"
    
    echo ""
    echo "[2/3] Installing to Claude Code..."
    copy_skill "$HOME/.claude/skills/macos-icon-designer"
    
    echo ""
    echo "[3/3] Installing to Universal Agents Standard (.agents)..."
    copy_skill "$HOME/.agents/skills/macos-icon-designer"
}

# Flag-based non-interactive install
case "$1" in
    --all)
        install_all
        exit 0
        ;;
    --gemini)
        copy_skill "$HOME/.gemini/config/skills/macos-icon-designer"
        exit 0
        ;;
    --claude)
        copy_skill "$HOME/.claude/skills/macos-icon-designer"
        exit 0
        ;;
    --universal)
        copy_skill "$HOME/.agents/skills/macos-icon-designer"
        exit 0
        ;;
    --custom)
        if [ -z "$2" ]; then
            echo "❌ Error: --custom requires a destination directory path."
            exit 1
        fi
        copy_skill "$2/macos-icon-designer"
        exit 0
        ;;
esac

echo "Select target AI Agent environment:"
echo "  [1] Universal (Install to ALL supported AI agents) [Recommended]"
echo "  [2] Google Antigravity & Gemini CLI (~/.gemini/config/skills)"
echo "  [3] Claude Code (~/.claude/skills)"
echo "  [4] Universal Agents Standard (~/.agents/skills)"
echo "  [5] Custom folder"
echo "  [6] Cancel"
echo ""

read -rp "Enter choice [1-6, default 1]: " choice
choice="${choice:-1}"

case "$choice" in
    1) install_all ;;
    2) copy_skill "$HOME/.gemini/config/skills/macos-icon-designer" ;;
    3) copy_skill "$HOME/.claude/skills/macos-icon-designer" ;;
    4) copy_skill "$HOME/.agents/skills/macos-icon-designer" ;;
    5)
        read -rp "Enter destination path: " custom_dir
        copy_skill "$custom_dir/macos-icon-designer"
        ;;
    6)
        echo "Cancelled."
        exit 0
        ;;
    *)
        echo "Invalid choice. Defaulting to Universal install..."
        install_all
        ;;
esac

echo ""
echo "======================================================================="
echo "  ✅ INSTALLATION COMPLETED SUCCESSFULLY!"
echo "======================================================================="
echo "How to use in your AI Agent:"
echo "  Ask your agent:"
echo "  - 'Design a macOS app icon for my new project [AppName]'"
echo "  - 'Create a vector squircle icon in Apple HIG style for [Metaphor]'"
echo "======================================================================="
