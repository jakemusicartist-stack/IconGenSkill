# Apple macOS Human Interface Guidelines (HIG) Icon Specifications

## 1. Geometry & Coordinate Space

* **Master Canvas**: `1024 x 1024 px` (`viewBox="0 0 1024 1024"`)
* **Squircle Body Size**: `824 x 824 px`
* **Squircle Origin**: `x: 100, y: 100` (Centered at `512, 512`)
* **Safety Margin**: `100 px` padding on all 4 sides reserved for drop shadows and slight tool overhangs.
* **Curvature Formula**: Continuous curvature (G2/G3 continuity superellipse $(x/a)^n + (y/b)^n = 1$ with $n \approx 4.5$).

### The Exact G2 Continuous Curvature Path
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

## 2. Lighting & Shadow Architecture

Apple macOS icons are designed as physical slabs floating directly above the macOS desktop and Dock. They use a consistent **12 o'clock overhead key light source** (`dx="0"`, `dy > 0`).

### The Dual-Tier Base Drop Shadow
Never use a single flat shadow. Apple icons use two distinct shadow levels:
1. **Contact / Ambient Occlusion Shadow**:
   * Tight, dark, anchors the squircle to the dock surface.
   * `dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.25"`
2. **Directional Key Shadow**:
   * Diffuse, soft, spreads downwards.
   * `dx="0" dy="24" stdDeviation="30" flood-color="#000000" flood-opacity="0.20"`

### The 1px Specular Top Rim Highlight (Bevel Light)
Every authentic macOS icon features a micro-bevel highlight running along its top edge, catching the virtual overhead light:
* Inset 1px to 1.5px stroke along the squircle boundary.
* Stroke gradient: Top is pure white at `25% - 40%` opacity, fading to `5%` in mid-sides, and dark black `15% - 25%` opacity along the bottom edge.

### Foreground Depth & Glyph Elevation
Objects resting on the squircle canvas must cast their own realistic shadow onto the background:
* `dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.30"`

---

## 3. Five Signature Material Archetypes

### 1. Vibrant Apple Satin (Classic Big Sur / Sonoma)
* 2-3 stop linear gradient with deep chromatic resonance (e.g. Electric Azure `#4F75FF` to Indigo `#002299`).
* Subtle top radial sheen (white radial gradient, `cx="50%" cy="0%" r="80%"`, opacity `20%` to `0%`).
* Bottom ambient occlusion shelf (black to transparent gradient at bottom 15%).

### 2. Liquid Glass / Frosted Translucent (Sonoma / Sequoia Glass)
* Translucent backdrop (`opacity="0.2"` to `0.85"`) over dark or saturated layers.
* Prismatic rim refraction: diagonal gradient with cyan, magenta, and white caustic highlights.
* Glossy pill reflection across the upper quadrant.

### 3. Space Black / Dark Titanium (Apple Pro)
* Stealth deep charcoal gradients (`#2D3035` down to `#121316`).
* High-contrast neon or vibrant chromatic glyph (Cyan, Mint, Tangerine, or Hot Pink) that "pops" against the dark chassis.
* Metallic hairline rim light (`stroke-width="1"`).

### 4. Anodized Aluminum / Silver Hardware
* Multi-stop metallic gradient simulating brushed metal reflection (`#ECEFF2` -> `#B8C0CA` -> `#E2E6EB`).
* Recessed engraved glyphs (`inner shadow` / debossed feel).

### 5. Tactile Skeuomorphic (Tools & Real Objects)
* Paper, leather, wood, or ceramic textures.
* Tangible tools (pencils, magnifying glasses, camera lenses) that can optionally break slightly outside the squircle boundary (up to 960px).

---

## 4. Silhouette & Overhang Rules

* **Standard App**: Pure squircle. All artwork is contained within the 824x824 squircle.
* **Tool / Utility App**: An accessory element (e.g. pencil tip, hammer handle, needle, ribbon) may break out through the top or top-right boundary, protruding by at most 30-50 px into the 100px margin.
* **Never**: Extend graphics to the extreme 1024px canvas edge. The margins must remain transparent to allow the macOS system drop shadow to breathe.
