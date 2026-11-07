# TECHROTE — MATERIAL TEXTURE PACK 02

A complementary set of **34 featureless material fills** and **12 transparent graphic fill patterns**. These are not equipment-specific; they have no bolts, buttons, scratches, labels, icons or object silhouettes. They are designed for filling manually painted masks under black-line illustrations.

## Files
- `01_Material_Surfaces_PNG/`: standalone, opaque 1024×1024 24-bit RGB texture tiles.
- `02_Transparent_Fill_Patterns_PNG/`: transparent 1024×1024 RGBA ink-only fills, suitable as mask-overlay layers.
- `03_GIMP_PAT/`: 46 ready-to-import GIMP patterns, including RGBA transparent patterns.
- `04_Previews/`: contact sheets and 2×2 repeat examples; these are not working tiles.
- `manifest.json`: materials, base colours, source parameters and cross-edge seam measurements.

## Painting workflow in GIMP
1. Place the line drawing above your texture layers; set the drawing layer to **Multiply**, or preserve it as a transparent ink-only layer where available.
2. Open a material PNG using **File > Open as Layers**. Place the material beneath the line drawing.
3. Add a **Layer Mask** to the texture layer, initialized to black (full transparency). Paint white into the mask to reveal the material inside selected surfaces.
4. For small regions, use the GIMP Patterns dock with the `.pat` entries in the Patterns directory instead of loading a full PNG layer.
5. For geometric fills, use the transparent PNG or pattern directly as an overlay on top of a base material. Recolour using alpha lock, Colourize or a solid-fill layer clipped to the pattern.
6. To get volume, use separate clipped shading/highlight layers rather than expecting a featureless texture to encode 3D lighting.

## Seamless tile guarantee
Random components use toroidal/wrapped Gaussian convolution; periodic patterns repeat with periods dividing 1024 exactly. This yields tiles intended for seamless regular repetition without prominent boundary jumps. The manifest records seam-vs-interior pixel differences for audit. The tiles do not contain pre-baked shadows, directional highlights, perspective, object edges or large-scale wear. Brushed metal is subtly directional; rotate the material layer independently before painting to orient the grain.

## Fidelity
These are deterministic, generated material illustrations; no claim is made that they are measured scans or calibrated PBR maps. Their purpose is flat colouring and surface richness in 2D artwork, particularly beneath black-line groupject illustrations. `ImageGen` was used to establish the broader material art direction; final independently tileable source tiles are generated algorithmically.
