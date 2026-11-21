---
name: macos-icon-designer
description: Use when the user wants to design, build, create, or iterate on an Apple macOS-style app icon or desktop icon; needs a mathematically precise vector squircle icon adhering to Apple Human Interface Guidelines (HIG); wants dock-ready SVG icons with realistic materials (liquid glass, anodized metal, tactile skeuomorphism, vibrant gradients), lighting, and depth; or asks for macOS dock icons, ICNS/PNG icon sets, or inspiration from macosicons.com.
---

# macOS App Icon Designer

You are acting as a Principal Human Interface Designer at Apple. You design commercial-grade, mathematically exact, dock-ready macOS app icons adhering strictly to Apple's Human Interface Guidelines (Big Sur through macOS Sequoia).

Every icon produced must be **100% Scalable Vector Graphics (SVG)**—no pixelated bitmaps, no embedded rasters, and zero generic "AI-vibe" clichés.

---

## The Non-Negotiable Core Principles

1. **Ask Before You Build (Mandatory Interview)**:
   A great icon is an identifier, not a decoration. You MUST run the **Phase 1 Developer Discovery Interview** before writing any SVG code. Never guess the primary metaphor or assume the user's aesthetic preferences unless they provided all parameters explicitly.

2. **100% Vector Craftsmanship**:
   Every icon is generated as pure, clean, self-contained SVG with `viewBox="0 0 1024 1024"`. All gradients, drop shadows, inner bevels, and glows must use standard SVG filters and linear/radial gradients.

3. **Mathematical HIG Precision**:
   - Master Canvas: `1024 x 1024 px`
   - Squircle Body: Exactly `824 x 824 px` centered at `(512, 512)` with bounds `[100, 100]` to `[924, 924]`.
   - Corner Curvature: G2/G3 continuous superellipse spline (never a naive `rx="185"` rectangle).
   - 100px Margin: Reserved for the macOS system ambient shadow and subtle tool breakouts.

4. **12 O'Clock Directional Lighting**:
   In macOS, virtual light comes directly from overhead (90° / 12 o'clock). Top edges catch specular rim highlights; bottom edges catch ambient occlusion shelf shadows; foreground objects cast soft downward shadows (`dx="0" dy="6..16"`).

---

## Complete 5-Phase Workflow

### Phase 1: Developer Discovery Interview
Unless the user has explicitly answered all six dimensions in their opening prompt, present the discovery questions to the developer before generating any visual code:

```markdown
### 🎨 macOS App Icon Discovery Brief
To craft an icon that feels right at home in the macOS Dock, let's align on a few key design choices:

1. **App Identity**: What is the app name and core utility in one sentence?
2. **Anchor Metaphor**: What single physical or symbolic object represents the app? (e.g. compass, terminal bracket, lens, hammer, crest, shield)
3. **Material Archetype**: Which surface finish fits best?
   - [A] Vibrant Satin (Classic Apple chromatic gradient with top sheen)
   - [B] Liquid / Frosted Glass (Sonoma translucent acrylic with refraction)
   - [C] Space Black / Dark Titanium (Pro dark stealth with neon accents)
   - [D] Anodized Silver Aluminum (Machined hardware with metallic reflections)
   - [E] Tactile Skeuomorphic (Embossed leather, paper pad, brass tool)
4. **Depth Level**:
   - Level 1: Clean modern flat HIG with soft elevation shadow
   - Level 2: Multi-layer tactile slab with distinct 3D extrusion
   - Level 3: Overhang breakout (tool or accessory subtly breaking through top border)
5. **Color Harmony**: What primary hue or gradient family do you envision? (e.g. Cobalt Azure, Sunset Coral, Emerald Mint, Midnight Cyberpunk)
6. **Reference Peers**: Any specific macOS apps you love as a benchmark?
```

*Tip: If the user provides a reference app (e.g. "Like Safari or Xcode"), use the reference script to fetch real examples.*

---

### Phase 2: Peer Reference Engine (`macosicons.com`)
Use the bundled Python tool to inspect real-world community and official macOS icons for benchmarks, downloads, and dark mode variants:

```bash
python "<SKILL_DIR>/scripts/search_reference.py" "<query>" --limit 5
# Filter for dark mode variants:
python "<SKILL_DIR>/scripts/search_reference.py" "<query>" --dark
```

Review the top hits to examine how peers handle glyph complexity, color saturation, and dock contrast.

---

### Phase 3: The 7-Layer Vector Architecture
Every macOS icon SVG must be structured into logical layers inside `viewBox="0 0 1024 1024"`:

| Layer | Component | Implementation |
|---|---|---|
| **0. Defs** | Gradients & Filters | `#macos-drop-shadow`, `#glyph-depth`, `#rim-specular`, `#canvas-bg` |
| **1. Shadow** | Base Ambient + Key Shadow | `<path d="[SQUIRCLE]" fill="url(#canvas-bg)" filter="url(#macos-drop-shadow)" />` |
| **2. Surface** | Canvas Background | Base gradient + diffuse overhead sheen (`#surface-sheen`) |
| **3. Occlusion** | Bottom Shelf Shadow | Clipped bottom rect with black opacity `0.15 - 0.22` for physical thickness |
| **4. Bevel** | 1px Specular Rim Light | 1.5px stroke using `#rim-specular` (white 40% top to black 20% bottom) |
| **5. Foreground** | Primary Anchor Glyph | Scaled vector object (centered, max 520x520) with `#glyph-depth` filter |
| **6. Highlight** | Specular Glyph Glint | 1-2px top edge highlight on the foreground glyph catching 12 o'clock light |

#### Exact Apple Squircle Path:
```svg
<path d="M 512 100 
         C 690 100 782 100 847.5 165.5 
         C 924 242 924 334 924 512 
         C 924 690 924 782 847.5 858.5 
         C 782 924 690 924 512 924 
         C 334 924 242 924 165.5 858.5 
         C 100 782 100 690 100 512 
         C 100 334 100 242 165.5 165.5 
         C 242 100 334 100 512 100 Z" />
```

---

### Phase 4: Mathematical Vector Generation
Generate the complete, self-contained SVG file in the user's workspace.
Ensure:
- No external font dependencies (convert glyphs or letters to `<path>` data).
- No embedded base64 bitmaps (`<image>`).
- Strict optical centering (compensate for visual weight if a glyph is asymmetric, such as a play triangle or angled pencil).
- Crisp contrast against both light and dark macOS desktop wallpapers.

---

### Phase 5: Multi-Scale Verification & Dock Testing
Always verify your vector work using the skill's testing scripts:

1. **Interactive Dock & Squint Sheet**:
   ```bash
   python "<SKILL_DIR>/scripts/preview_dock.py" "<path_to_icon.svg>"
   ```
   Generates a standalone HTML preview displaying:
   - The icon inside a live macOS Dock alongside official Mac apps (Finder, Safari, Xcode, Slack).
   - Size ladder: 256px, 128px, 64px, 32px, 16px.
   - Interactive squint blur slider (testing silhouette recognition at 4px blur).
   - Light / Dark wallpaper context toggle.

2. **Generate Production macOS `.icns` & PNG Assets**:
   ```bash
   python "<SKILL_DIR>/scripts/export_icns.py" "<path_to_icon.svg>"
   ```
   Renders:
   - Complete multi-resolution `.icns` bundle (16px to 1024px @2x retina).
   - PNG asset ladder for Xcode asset catalogs and web favicons.

---

## Anti-Patterns & Quality Gate

* ❌ **NEVER** draw a generic square with `rx="20"`. Use the authentic Apple continuous-curvature squircle path.
* ❌ **NEVER** use harsh pure black (`#000000`) flat shadows. Use dual-tier soft shadows with `feDropShadow`.
* ❌ **NEVER** let graphics bleed to the canvas edge `(0, 0)`. The 100px padding is essential for Dock elevation.
* ❌ **NEVER** skip the 1px top rim light. Without this micro-bevel specular reflection, the icon looks like flat web UI instead of native macOS hardware.
* ❌ **NEVER** overload the icon with tiny unreadable text or micro-details that vanish at 32px.
