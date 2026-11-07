# Slopaterial — material references and fill textures

This repository sorts art references **by maturity**, rather than exclusively by material type. Existing folder-stage README files remain authoritative:

- [`roughref/`](roughref/readme.md): rough first outputs, experimental references. Contains [Texture Pack 01](roughref/material_texture_pack_01/README.md) (10 generated reference tiles).
- [`roughref/somewhatrefined/`](roughref/somewhatrefined/readme.md): multiple refinement passes not yet assessed for production. Do not automatically move imported work here.
- [`mediumqual/`](mediumqual/readme.md): plausible drafts that could be refined for production. Contains [Texture Pack 02](mediumqual/material_texture_pack_02/README.md) (34 materials + 12 ink patterns).
- [`heavilyrefined/`](heavilyrefined/readme.md): almost production-ready assets only, following independent acceptance. None of these imported packs is marked heavily refined.

**Start with [`RAG.md`](RAG.md) to locate assets semantically.** Packs store canonical source PNGs. Pack 02 includes a lossless deterministic GIMP `.pat` re-builder, original source manifest, SHA-256 per file, seam metrics, and category-level RAG indexes. All 56 texture pixel arrays are preserved. 55 PNG files are byte-for-byte identical to their source files; one pale-concrete PNG was losslessly re-encoded without changing any pixel values. Original and stored checksums are recorded for that exception. Material images are 2D colour fills, not item atlases or physically calibrated surface maps.
