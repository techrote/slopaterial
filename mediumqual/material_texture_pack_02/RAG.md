# RAG — Pack 02: searchable generic materials

- **Identity:** Techrote Material Texture Pack 02, 46 featureless, repeatable 1024×1024 tiles.
- **Quality:** `mediumqual`; machine-tested seam behaviour, NOT declared production-ready.
- **Intended technique:** GIMP fill layers revealed through user-drawn masks under independent black line drawings.
- **Query intent:** retrieve by material class, desired base hue, microtexture/frequency, transparent ink vs opaque colour, or whether grain is directional.
- **Do not infer:** PBR compliance, photographic capture, object identity, material-specific mechanical properties, artist-approved final look.
- **Parent taxonomy:** `mediumqual/readme.md`. **Source provenance:** `metadata/source_manifest.json`.

## Category routing

| Query / intent | Directory | Notes |
|---|---|---|
| brushed/satin metal, brass, copper, nickel, steel, zinc, titanium | [`materials/metals`](materials/metals/RAG.md) | Directional fine grain; user should orient layer to geometry |
| enamel, Bakelite, acrylic, resin, polymer, ceramic | [`materials/coatings`](materials/coatings/RAG.md) | Understated smooth-to-fine-noise colour fills |
| neoprene, rubber, vinyl, weave, cloth, linen, canvas | [`materials/soft`](materials/soft/RAG.md) | Fine textile/soft-surface grain for masking |
| kraft, rag paper, gypsum, limestone, microcement, cork | [`materials/mineral`](materials/mineral/RAG.md) | Pulp, mineral, plaster and board textures |
| halftone dots, engineering grid, hatch, pinstripe, scanline, stipple | [`fill_patterns`](fill_patterns/RAG.md) | Transparent ink overlay; user selects underlying fill and colour |

## File records

Each entry in [`catalog.jsonl`](catalog.jsonl) contains searchable text, category, colour, 2D kind, exact PNG path and digest, seam metrics, pattern name and the verified expected GIMP PAT digest. Preserve those records when repackaging.
