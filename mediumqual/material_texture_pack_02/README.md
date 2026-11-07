# Material Texture Pack 02 — medium-quality candidates

**Stage:** `mediumqual`. This means reasonable-quality candidates appropriate for developing production-ready revisions, **not** production acceptance.  
**Source:** 46 original 1024×1024 PNG tiles from the Techrote IO material-fill pack (34 opaque surfaces + 12 alpha-backed ink overlays), preserved bit-for-bit.  
**Categories:** [`materials/metals/`](materials/metals/), [`materials/coatings/`](materials/coatings/), [`materials/soft/`](materials/soft/), [`materials/mineral/`](materials/mineral/), and [`fill_patterns/`](fill_patterns/).

These files are **featureless generic surface materials**, not models, screenshots, buttons, or per-object texture atlases. They encode no calibrated normal/roughness/displacement data and no directional lighting. Tiling algorithms use wrapping noise and repeat-compatible drawing; cross-edge seam ratios are stored in [`metadata/source_manifest.json`](metadata/source_manifest.json) and indexed in [`catalog.jsonl`](catalog.jsonl). They still warrant a human 2×2 repeat visual check at the final working scale.

**Why there are no giant raw `.pat` duplicates:** Native GIMP `.pat` files are 4 MiB apiece and duplicate the PNG pixel information. Run [`tools/generate_gimp_pat.py`](tools/generate_gimp_pat.py) to reconstruct **all 46 original GIMP PAT files byte-for-byte**, with output SHA-256 validation against the original pack's PAT manifest stored in [`catalog.jsonl`](catalog.jsonl). This ensures exact reproducibility and avoids ~192 MiB of uncompressed duplicate assets in Git. The original upstream pack is also retained separately by the user.

**GIMP painting process:** load PNGs as separate layers below a multiply-blended or transparent black-ink line drawing; mask each texture layer black and paint white into selected regions. Keep ink-only geometry patterns as independent overlay layers; recolour them with alpha lock or a clipping layer. Rotate directional metal grain as required, and supply volume with separate shading layers rather than baked gradients.

**Search / RAG:** [`RAG.md`](RAG.md), [`catalog.jsonl`](catalog.jsonl), individual category `RAG.md` files. **QA:** [`metadata/`](metadata/), [`tools/verify_assets.py`](tools/verify_assets.py). **Previews:** [`previews/`](previews/).

**Provenance:** algorithmically generated periodic 2D texture illustrations following the Techrote IO line-art material brief, 2026-11-07; contact-sheet art direction involved an image generator but these periodic source tiles were synthesized independently. No measured material capture and no asserted standalone license.
