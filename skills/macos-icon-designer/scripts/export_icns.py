#!/usr/bin/env python3
"""
export_icns.py
Renders an SVG icon into a full macOS .icns multi-resolution bundle and PNG asset ladder.
Uses headless Edge/Chrome (or CairoSVG/ImageMagick if available) and Pillow.
"""

import sys
import os
import io
import struct
import argparse
import subprocess
from PIL import Image

ICNS_CHUNKS = {
    'ic07': 128,   # 128x128
    'ic08': 256,   # 256x256
    'ic09': 512,   # 512x512
    'ic10': 1024,  # 1024x1024 (or 512x512@2x)
    'ic11': 32,    # 16x16@2x
    'ic12': 64,    # 32x32@2x
    'ic13': 256,   # 128x128@2x
    'ic14': 512,   # 256x256@2x
}

PNG_SIZES = [16, 32, 64, 128, 256, 512, 1024]

def find_browser():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "google-chrome",
        "chromium",
        "msedge"
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None

def render_svg_to_png(svg_path, out_png_path, size=1024):
    browser = find_browser()
    if not browser:
        raise RuntimeError("No headless browser found to rasterize SVG. Please install Edge or Chrome.")
    
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--default-background-color=00000000",
        f"--window-size={size},{size}",
        f"--screenshot={out_png_path}",
        svg_path
    ]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0 or not os.path.exists(out_png_path):
        raise RuntimeError(f"Browser screenshot failed: {res.stderr.decode('utf-8', errors='ignore')}")
    return out_png_path

def build_icns(base_img, icns_path):
    chunks = []
    for tag, size in ICNS_CHUNKS.items():
        resized = base_img.resize((size, size), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format="PNG")
        data = buf.getvalue()
        chunk_len = len(data) + 8
        chunks.append(tag.encode("ascii") + struct.pack(">I", chunk_len) + data)

    total_len = 8 + sum(len(c) for c in chunks)
    icns_data = b"icns" + struct.pack(">I", total_len) + b"".join(chunks)

    with open(icns_path, "wb") as f:
        f.write(icns_data)
    return icns_path

def export_assets(svg_path, out_dir=None):
    if not os.path.isfile(svg_path):
        print(f"Error: {svg_path} does not exist.", file=sys.stderr)
        return False
        
    base_name = os.path.splitext(os.path.basename(svg_path))[0]
    if not out_dir:
        out_dir = os.path.join(os.path.dirname(svg_path), f"{base_name}_assets")
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"Rendering 1024x1024 master PNG from SVG...")
    master_png = os.path.join(out_dir, f"{base_name}_1024.png")
    render_svg_to_png(svg_path, master_png, 1024)
    
    base_img = Image.open(master_png).convert("RGBA")
    
    # Export PNG sizes
    print(f"Generating PNG asset ladder...")
    for sz in PNG_SIZES:
        p = os.path.join(out_dir, f"icon_{sz}x{sz}.png")
        resized = base_img.resize((sz, sz), Image.Resampling.LANCZOS)
        resized.save(p, "PNG")
        
        # Retina @2x
        if sz <= 512:
            p2x = os.path.join(out_dir, f"icon_{sz}x{sz}@2x.png")
            resized2x = base_img.resize((sz * 2, sz * 2), Image.Resampling.LANCZOS)
            resized2x.save(p2x, "PNG")
            
    # Export .icns
    icns_file = os.path.join(out_dir, f"{base_name}.icns")
    print(f"Building macOS .icns bundle...")
    build_icns(base_img, icns_file)
    
    print(f"\n[DONE] Exported all assets to:\n  {out_dir}")
    print(f"  - Master ICNS: {icns_file}")
    print(f"  - PNG Ladder:  16x16 up to 1024x1024 (@2x included)")
    return True

def main():
    parser = argparse.ArgumentParser(description="Export SVG to macOS .icns and PNG ladder")
    parser.add_argument("svg_file", help="Path to input SVG icon")
    parser.add_argument("--out-dir", help="Output directory (optional)")
    args = parser.parse_args()
    
    export_assets(args.svg_file, args.out_dir)

if __name__ == "__main__":
    main()
