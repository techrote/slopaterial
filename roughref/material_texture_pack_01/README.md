# Material Texture Pack 01 — rough reference

**Stage:** `roughref` (intentionally experimental; no production acceptance claimed).  
**Assets:** 10 original 1254×1254 PNG materials and patterns from the Techrote IO/GIMP line-art workflow, preserved byte-for-byte in [`source_png/`](source_png/).  
**Index:** [`RAG.md`](RAG.md) and [`catalog.jsonl`](catalog.jsonl).

These are general-purpose, object-independent surface fills. Original filenames contain “seamless” where supplied, but that is **not a formal seamlessness guarantee**: the evaluated first/last edge discontinuities on some source images are several times stronger than their ordinary adjacent-pixel gradients (notably pearlescent and aluminium). Review repeat seams and repair or re-tile before shipping them in seamless applications. Avoid baking object silhouettes or lighting into derivatives.

**GIMP use:** import as layers beneath the black linework; add a black layer mask; paint white into the mask where each material should appear. Preserve originals here; place any genuinely refined derivatives under `roughref/somewhatrefined/` and reclassify only after documented visual and seam testing. Maintain texture scale and grain direction deliberately.

**Provenance:** generated as part of a 2026-11-07 user-directed Techrote IO texture exploration; neither physical-scanner measurements nor calibrated PBR data. No license is asserted by these metadata files.
