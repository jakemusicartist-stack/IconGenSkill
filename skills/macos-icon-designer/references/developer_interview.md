# Developer Discovery Questionnaire: macOS App Icon

Before drafting any SVG code or choosing visual styles, the agent must guide the developer through an interactive discovery questionnaire. This ensures the resulting icon reflects the developer's exact taste, technical architecture, and brand identity rather than generic AI slop.

---

## The 6 Mandatory Question Dimensions

Present these questions to the developer clearly and concisely, offering recommended presets for quick selection while inviting custom details:

### 1. App Identity & Domain
* **App Name**: What is the official name of the app?
* **One-Sentence Core Purpose**: What is the primary utility, function, or joy this app delivers?
* **Category / Domain**:
  1. Developer Tools / CLI / Terminal
  2. Productivity / Utility / System
  3. Creative / Design / Audio / Video
  4. Web / Browser / Social / Communication
  5. Security / Privacy / Cloud Infrastructure
  6. Personal Finance / Analytics / Dashboard

### 2. Primary Visual Metaphor (Anchor Object)
* What is the single physical or symbolic object that best represents the app?
  *(Examples: Safari uses a compass, Xcode uses a blueprint & hammer, Mail uses a postal stamp, TextEdit uses a pen & pad, Terminal uses a prompt bracket `>_`, Docker uses a whale/container, 1Password uses a keyhole)*
* Do you want an **Abstract Geometric Crest**, a **Literal Tactile Tool**, or an **Engineered Technical Monogram**?

### 3. Materiality & Surface Texture
Which Apple material archetype fits the app's spirit?
* **[A] Vibrant Satin**: Classic Apple HIG rich chromatic gradient with soft ambient top sheen.
* **[B] Liquid / Frosted Glass**: Modern macOS Sonoma translucent acrylic with refractive edge caustics.
* **[C] Space Black / Dark Titanium**: Stealth Apple Pro dark charcoal with high-contrast glowing accents.
* **[D] Anodized Silver Aluminum**: Clean machined hardware look with subtle metallic reflections.
* **[E] Tactile Skeuomorphic**: Rich physical materials (embossed leather, notepad paper, brushed brass, camera lens glass).

### 4. Lighting & Depth Mode
* **Level 1 (Subtle / Clean HIG)**: Flat modern glyph with gentle soft drop shadow and top rim highlight.
* **Level 2 (Tactile 3D Slab)**: Foreground glyph has distinct extrusion, multi-stage cast shadow, and bevel.
* **Level 3 (Layered Overhang)**: Primary object breaks through the squircle boundary slightly (e.g. pencil or tool extending into the safety margin).
* **Level 4 (Engraved / Debossed)**: The glyph appears carved or stamped into the squircle surface with an inner shadow.

### 5. Color Palette & Dark Mode Bias
* **Primary Color Harmony**:
  * Azure / Deep Electric Cobalt
  * Emerald / Cyber Mint
  * Sunset Coral / Tangerine / Amber
  * Radiant Violet / Magenta / Neon Pink
  * Monochrome Stealth Charcoal / Space Gray / Pure White
* **Context Bias**: Standard Light Dock, Dark Mode Dock, or a universal dual-mode design?

### 6. Reference Peers & Benchmarks
* Are there any existing macOS icons (or apps from `macosicons.com`) that you love or consider your gold standard?
  *(The agent can run `python scripts/search_reference.py "<app_name>"` to fetch real-world references for inspiration).*
