#!/usr/bin/env python3
"""
preview_dock.py
Generates an interactive HTML preview test sheet for macOS vector icons.
Includes live macOS Dock simulation, wallpaper context, multi-resolution ladder, and squint test.
"""

import sys
import os
import argparse
import base64

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>macOS Icon Preview - {title}</title>
    <style>
        :root {{
            --bg-wallpaper: radial-gradient(circle at 50% 30%, #1e1b4b 0%, #0f172a 60%, #020617 100%);
            --dock-bg: rgba(255, 255, 255, 0.12);
            --dock-border: rgba(255, 255, 255, 0.2);
            --dock-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
            --text-color: #f8fafc;
            --card-bg: rgba(30, 41, 59, 0.7);
        }}
        [data-theme="light"] {{
            --bg-wallpaper: radial-gradient(circle at 50% 30%, #e0e7ff 0%, #f1f5f9 60%, #cbd5e1 100%);
            --dock-bg: rgba(255, 255, 255, 0.45);
            --dock-border: rgba(255, 255, 255, 0.6);
            --dock-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            --text-color: #0f172a;
            --card-bg: rgba(255, 255, 255, 0.85);
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif;
            background: var(--bg-wallpaper);
            color: var(--text-color);
            min-height: 100vh;
            padding: 30px;
            transition: background 0.3s ease;
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }}
        h1 {{ font-size: 24px; font-weight: 600; letter-spacing: -0.5px; }}
        .controls {{ display: flex; gap: 12px; align-items: center; }}
        button {{
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: inherit;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 13px;
            backdrop-filter: blur(10px);
            transition: all 0.2s;
        }}
        button:hover {{ background: rgba(255, 255, 255, 0.25); }}
        
        .section-title {{
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
            opacity: 0.7;
            margin-bottom: 16px;
            font-weight: 600;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px; }}
        
        /* DOCK SIMULATION */
        .dock-stage {{
            position: relative;
            background: rgba(0, 0, 0, 0.25);
            border-radius: 18px;
            padding: 60px 20px 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .dock-shelf {{
            display: flex;
            align-items: flex-end;
            gap: 14px;
            background: var(--dock-bg);
            border: 1px solid var(--dock-border);
            padding: 10px 18px 12px;
            border-radius: 22px;
            backdrop-filter: blur(25px) saturate(180%);
            -webkit-backdrop-filter: blur(25px) saturate(180%);
            box-shadow: var(--dock-shadow);
        }}
        .dock-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            transition: transform 0.25s cubic-bezier(0.2, 0.9, 0.3, 1.2);
        }}
        .dock-item:hover {{
            transform: scale(1.22) translateY(-10px);
        }}
        .dock-icon {{
            width: 72px;
            height: 72px;
            border-radius: 16px;
            display: block;
        }}
        .dock-item.active::after {{
            content: "";
            display: block;
            width: 4px;
            height: 4px;
            border-radius: 50%;
            background: #fff;
            margin-top: 5px;
            opacity: 0.9;
        }}
        .dock-divider {{
            width: 1px;
            height: 60px;
            background: rgba(255, 255, 255, 0.2);
            margin: 0 4px;
        }}
        
        /* SIZE LADDER */
        .ladder-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 20px;
        }}
        .ladder-card {{
            background: var(--card-bg);
            border-radius: 14px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 12px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
        }}
        .ladder-label {{
            font-size: 12px;
            opacity: 0.65;
            font-family: monospace;
        }}
        
        /* SQUINT TEST */
        .squint-box {{
            display: flex;
            gap: 24px;
            align-items: center;
            background: var(--card-bg);
            padding: 24px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .squint-slider {{ flex: 1; }}
        .squint-view {{
            width: 140px;
            height: 140px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            background: rgba(0, 0, 0, 0.2);
        }}
    </style>
</head>
<body>
    <header>
        <div>
            <h1>macOS App Icon Verification</h1>
            <p style="font-size: 13px; opacity: 0.7; margin-top: 4px;">File: {title}</p>
        </div>
        <div class="controls">
            <button onclick="toggleTheme()">Toggle Dark/Light Context</button>
            <button onclick="window.print()">Print / Export PDF</button>
        </div>
    </header>

    <div class="container">
        <!-- SECTION 1: macOS DOCK CONTEXT -->
        <div>
            <div class="section-title">1. Realistic macOS Dock Context</div>
            <div class="dock-stage">
                <div class="dock-shelf">
                    <!-- Standard Mac Apps for Benchmark Comparison -->
                    <div class="dock-item">
                        <img class="dock-icon" src="https://s3-new.macosicons.com/macosicons/parse/Finder_B7DXS2NKpM_lowResPng-71a7fb1936.png" alt="Finder">
                    </div>
                    <div class="dock-item">
                        <img class="dock-icon" src="https://s3-new.macosicons.com/macosicons/parse/Safari_XgMp9StcjA_lowResPng-9c26ba2595.png" alt="Safari">
                    </div>
                    
                    <!-- THE USER VECTOR ICON -->
                    <div class="dock-item active" style="transform: scale(1.08) translateY(-4px);">
                        <img class="dock-icon hero-icon" src="{data_uri}" alt="{title}">
                    </div>
                    
                    <div class="dock-item">
                        <img class="dock-icon" src="https://s3-new.macosicons.com/macosicons/parse/Xcode_fTW17LN0aO_lowResPng-2c63dc5809.png" alt="Xcode">
                    </div>
                    <div class="dock-divider"></div>
                    <div class="dock-item">
                        <img class="dock-icon" src="https://s3-new.macosicons.com/macosicons/parse/Slack_aUcVREHPGa_lowResPng-6feae8de5b.png" alt="Slack">
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION 2: MULTI-SCALE LADDER -->
        <div>
            <div class="section-title">2. Resolution Ladder (Optical Scale Test)</div>
            <div class="ladder-grid">
                <div class="ladder-card">
                    <img src="{data_uri}" style="width: 256px; height: 256px;">
                    <span class="ladder-label">256px (App Store / Large)</span>
                </div>
                <div class="ladder-card">
                    <img src="{data_uri}" style="width: 128px; height: 128px;">
                    <span class="ladder-label">128px (Launchpad / Finder)</span>
                </div>
                <div class="ladder-card">
                    <img src="{data_uri}" style="width: 64px; height: 64px;">
                    <span class="ladder-label">64px (Dock Standard)</span>
                </div>
                <div class="ladder-card">
                    <img src="{data_uri}" style="width: 32px; height: 32px;">
                    <span class="ladder-label">32px (Menu / Spotlight)</span>
                </div>
                <div class="ladder-card">
                    <img src="{data_uri}" style="width: 16px; height: 16px;">
                    <span class="ladder-label">16px (Favicon / Breadcrumb)</span>
                </div>
            </div>
        </div>

        <!-- SECTION 3: SQUINT BLUR TEST -->
        <div>
            <div class="section-title">3. Squint Silhouette Test (Blur Isolation)</div>
            <div class="squint-box">
                <div class="squint-view">
                    <img id="squint-img" src="{data_uri}" style="width: 100px; height: 100px; filter: blur(4px);">
                </div>
                <div class="squint-slider">
                    <label for="blur-range" style="font-size: 13px; display: block; margin-bottom: 8px;">
                        Squint Blur Level: <span id="blur-val">4px</span> (If the icon's core shape/color is still distinct at 4-6px, the silhouette passes)
                    </label>
                    <input id="blur-range" type="range" min="0" max="12" value="4" style="width: 100%;" oninput="updateBlur(this.value)">
                </div>
            </div>
        </div>
    </div>

    <script>
        function toggleTheme() {{
            const current = document.documentElement.getAttribute('data-theme');
            document.documentElement.setAttribute('data-theme', current === 'light' ? 'dark' : 'light');
        }}
        function updateBlur(val) {{
            document.getElementById('blur-val').textContent = val + 'px';
            document.getElementById('squint-img').style.filter = 'blur(' + val + 'px)';
        }}
    </script>
</body>
</html>
"""

def generate_preview(svg_path, output_html=None):
    if not os.path.isfile(svg_path):
        print(f"Error: SVG file not found: {svg_path}", file=sys.stderr)
        return False
        
    with open(svg_path, "rb") as f:
        svg_bytes = f.read()
        
    data_uri = "data:image/svg+xml;base64," + base64.b64encode(svg_bytes).decode("ascii")
    basename = os.path.basename(svg_path)
    
    if not output_html:
        output_html = os.path.splitext(svg_path)[0] + "_preview.html"
        
    html = HTML_TEMPLATE.format(title=basename, data_uri=data_uri)
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Generated interactive macOS icon preview sheet -> {output_html}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Create interactive macOS dock preview sheet for SVG icon")
    parser.add_argument("svg_file", help="Path to input SVG icon")
    parser.add_argument("--out", help="Output HTML file path (optional)")
    args = parser.parse_args()
    
    generate_preview(args.svg_file, args.out)

if __name__ == "__main__":
    main()
