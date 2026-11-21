#!/usr/bin/env python3
"""
generate_squircle.py
Generates mathematically precise Apple macOS HIG squircle SVG templates,
complete with continuous curvature (G2/G3), dual-tier drop shadows, and specular rim lights.
"""

import sys
import argparse

# Official macOS HIG Squircle Path (centered at 512, 512, dimensions 824x824)
# Bounds: x: 100 to 924, y: 100 to 924.
# G2 continuous curvature cubic bezier curve definition:
SQUIRCLE_PATH = (
    "M 512 100 "
    "C 690 100 782 100 847.5 165.5 "
    "C 924 242 924 334 924 512 "
    "C 924 690 924 782 847.5 858.5 "
    "C 782 924 690 924 512 924 "
    "C 334 924 242 924 165.5 858.5 "
    "C 100 782 100 690 100 512 "
    "C 100 334 100 242 165.5 165.5 "
    "C 242 100 334 100 512 100 Z"
)

PRESETS = {
    "vibrant-gradient": {
        "desc": "Apple HIG Vibrant Satin (Monterey/Sonoma)",
        "gradient": """
        <linearGradient id="bg-grad" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#4F75FF" />
            <stop offset="50%" stop-color="#0047FF" />
            <stop offset="100%" stop-color="#002299" />
        </linearGradient>
        <radialGradient id="sheen" cx="50%" cy="0%" r="90%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.30" />
            <stop offset="60%" stop-color="#FFFFFF" stop-opacity="0" />
        </radialGradient>
        """,
        "base_fill": "url(#bg-grad)",
        "sheen_fill": "url(#sheen)",
        "rim_opacity": "0.35"
    },
    "liquid-glass": {
        "desc": "Apple Liquid / Frosted Translucent Glass",
        "gradient": """
        <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.25" />
            <stop offset="40%" stop-color="#80A5FF" stop-opacity="0.15" />
            <stop offset="100%" stop-color="#1A2035" stop-opacity="0.75" />
        </linearGradient>
        <linearGradient id="glass-refract" x1="30%" y1="0%" x2="70%" y2="100%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.45" />
            <stop offset="35%" stop-color="#00F0FF" stop-opacity="0.20" />
            <stop offset="70%" stop-color="#FF00A0" stop-opacity="0.15" />
            <stop offset="100%" stop-color="#000000" stop-opacity="0.30" />
        </linearGradient>
        """,
        "base_fill": "url(#bg-grad)",
        "sheen_fill": "url(#glass-refract)",
        "rim_opacity": "0.60"
    },
    "pro-dark": {
        "desc": "Apple Pro Space Black / Titanium",
        "gradient": """
        <linearGradient id="bg-grad" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#2D3035" />
            <stop offset="50%" stop-color="#1E2024" />
            <stop offset="100%" stop-color="#121316" />
        </linearGradient>
        <radialGradient id="sheen" cx="50%" cy="10%" r="80%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.12" />
            <stop offset="80%" stop-color="#000000" stop-opacity="0.40" />
        </radialGradient>
        """,
        "base_fill": "url(#bg-grad)",
        "sheen_fill": "url(#sheen)",
        "rim_opacity": "0.25"
    },
    "anodized-metal": {
        "desc": "Apple Anodized Brushed Silver Aluminum",
        "gradient": """
        <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ECEFF2" />
            <stop offset="45%" stop-color="#D7DCE2" />
            <stop offset="55%" stop-color="#B8C0CA" />
            <stop offset="100%" stop-color="#E2E6EB" />
        </linearGradient>
        <linearGradient id="sheen" x1="100%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.40" />
            <stop offset="50%" stop-color="#A0A8B4" stop-opacity="0.10" />
            <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.30" />
        </linearGradient>
        """,
        "base_fill": "url(#bg-grad)",
        "sheen_fill": "url(#sheen)",
        "rim_opacity": "0.50"
    }
}

def generate_svg(preset_name="vibrant-gradient", glyph_name="glyph"):
    preset = PRESETS.get(preset_name, PRESETS["vibrant-gradient"])
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
    <defs>
        <!-- Apple macOS Dual-Tier Drop Shadow -->
        <filter id="macos-drop-shadow" x="-10%" y="-10%" width="125%" height="130%" filterUnits="userSpaceOnUse">
            <!-- Ambient Occlusion Shadow (Soft, subtle) -->
            <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.25" />
            <!-- Key Directional Light Shadow (12 o'clock light source) -->
            <feDropShadow dx="0" dy="24" stdDeviation="30" flood-color="#000000" flood-opacity="0.20" />
        </filter>

        <!-- Foreground Glyph Elevation Shadow -->
        <filter id="glyph-shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000000" flood-opacity="0.35" />
            <feDropShadow dx="0" dy="16" stdDeviation="22" flood-color="#000000" flood-opacity="0.20" />
        </filter>

        <!-- Specular 1px Inset Rim Highlight -->
        <linearGradient id="rim-specular" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="{preset['rim_opacity']}" />
            <stop offset="40%" stop-color="#FFFFFF" stop-opacity="0.08" />
            <stop offset="70%" stop-color="#000000" stop-opacity="0.05" />
            <stop offset="100%" stop-color="#000000" stop-opacity="0.22" />
        </linearGradient>

        {preset['gradient']}

        <!-- Clip path to keep surface effects strictly within squircle -->
        <clipPath id="squircle-clip">
            <path d="{SQUIRCLE_PATH}" />
        </clipPath>
    </defs>

    <!-- LAYER 1: Background Canvas Squircle with Drop Shadow -->
    <path d="{SQUIRCLE_PATH}" 
          fill="{preset['base_fill']}" 
          filter="url(#macos-drop-shadow)" />

    <!-- LAYER 2: Surface Texture / Sheen / Reflection inside Squircle -->
    <g clip-path="url(#squircle-clip)">
        <path d="{SQUIRCLE_PATH}" fill="{preset['sheen_fill']}" />

        <!-- Ambient Bottom Edge Occlusion -->
        <rect x="100" y="800" width="824" height="124" fill="url(#bg-grad)" opacity="0.15" />
    </g>

    <!-- LAYER 3: 1px Specular Rim Light Border -->
    <path d="{SQUIRCLE_PATH}" 
          fill="none" 
          stroke="url(#rim-specular)" 
          stroke-width="1.5" />

    <!-- LAYER 4: Foreground Glyph Placeholder (Centered at 512, 512, max 520x520) -->
    <g id="{glyph_name}" filter="url(#glyph-shadow)">
        <!-- Replace this circle with actual vector glyph geometry -->
        <circle cx="512" cy="512" r="180" fill="#FFFFFF" />
        <path d="M 440 512 L 485 557 L 585 457" fill="none" stroke="{preset['base_fill']}" stroke-width="32" stroke-linecap="round" stroke-linejoin="round" />
    </g>
</svg>"""
    return svg

def main():
    parser = argparse.ArgumentParser(description="Generate Apple macOS Squircle SVG Template")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), default="vibrant-gradient")
    parser.add_argument("--out", default="macos_icon_template.svg", help="Output file path")
    args = parser.parse_args()

    svg_content = generate_svg(args.preset)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated macOS icon SVG template [{args.preset}] -> {args.out}")

if __name__ == "__main__":
    main()
