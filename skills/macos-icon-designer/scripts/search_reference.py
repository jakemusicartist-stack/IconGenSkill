#!/usr/bin/env python3
"""
search_reference.py
Search macosicons.com for real-world macOS icon references, materials, and benchmarks.
"""

import sys
import argparse
import json
import urllib.request

DEFAULT_API_KEY = "c2cd0bd3cb24bd0e2af904c9bb76d0a652b08e1c8f226190a403895b0218bf46"
API_URL = "https://api.macosicons.com/api/v1/search"

def search_macos_icons(query, limit=6, dark_mode=None, api_key=DEFAULT_API_KEY):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "User-Agent": "Antigravity-MacOS-Icon-Skill/1.0"
    }
    payload = {
        "query": query,
        "searchOptions": {
            "hitsPerPage": limit,
            "offset": 0,
            "page": 1
        }
    }
    
    req = urllib.request.Request(API_URL, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            hits = data.get("hits", [])
            
            # Optional dark mode filter
            if dark_mode is not None:
                hits = [h for h in hits if h.get("isDarkMode") == dark_mode]
                
            return hits[:limit]
    except Exception as e:
        print(f"Error querying macosicons.com API: {e}", file=sys.stderr)
        return []

def main():
    parser = argparse.ArgumentParser(description="Search macosicons.com for design references")
    parser.add_argument("query", help="App name, keyword, or category (e.g. 'Terminal', 'WebBites', 'Music')")
    parser.add_argument("--limit", type=int, default=6, help="Maximum number of results to fetch")
    parser.add_argument("--dark", action="store_true", help="Filter for dark mode variants")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    parser.add_argument("--api-key", default=DEFAULT_API_KEY, help="API key for macosicons.com")
    
    args = parser.parse_args()
    
    dark_filter = True if args.dark else None
    hits = search_macos_icons(args.query, limit=args.limit, dark_mode=dark_filter, api_key=args.api_key)
    
    if args.json:
        print(json.dumps(hits, indent=2))
        return
        
    print(f"\nFound {len(hits)} reference macOS icons for '{args.query}':\n" + "="*60)
    for i, h in enumerate(hits, 1):
        app = h.get("appName", "Unknown")
        user = h.get("usersName", "Anonymous")
        downloads = h.get("downloads", 0)
        dark = "🌙 Dark Mode" if h.get("isDarkMode") else "☀️ Light/Standard"
        glass = " | 🧊 Liquid Glass" if h.get("isLiquidGlass") else ""
        png = h.get("lowResPngUrl") or h.get("iOSUrl") or "N/A"
        icns = h.get("icnsUrl") or "N/A"
        
        print(f"[{i}] {app} (by {user})")
        print(f"    Downloads: {downloads:,} | {dark}{glass}")
        print(f"    Preview:   {png}")
        print(f"    ICNS:      {icns}")
        print("-" * 60)

if __name__ == "__main__":
    main()
