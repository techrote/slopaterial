# RAG — Slopaterial retrieval / provenance guide

**Query terms:** seamless texture, material mask, GIMP layer masks, 2D surface fill, ink overlay, retro computer surfaces, CAD workstation, technical linework.

## Stages and authoritative routing

`roughref` contains first-pass generated imagery. `roughref/somewhatrefined` is for additional passes without readiness assessment. `mediumqual` contains quality candidates; do not treat this as production-certified. `heavilyrefined` is reserved for near-production assets **after** human assessment. Never infer quality from filenames such as `seamless` alone.

## Packs

- **Texture Pack 01:** [`roughref/material_texture_pack_01/RAG.md`](roughref/material_texture_pack_01/RAG.md) for 10 experimental 1254px PNG materials, first-generation art, gaps in tiling verification.
- **Texture Pack 02:** [`mediumqual/material_texture_pack_02/RAG.md`](mediumqual/material_texture_pack_02/RAG.md) for 46 mathematically periodized 1024px material and pattern fills; category routing and PAT generation instructions.

## Filtering and usage

Choose a tile by composition intent, material family, colour, contrast and grain frequency. For GIMP, place material PNGs below separate black line drawings, use opaque black masks with white-painted reveals, and keep transparent graphic patterns above base fill layers. Object volume/shadow should be a separate layer. `catalog.jsonl` entries can be read directly by search/RAG tools; per-category `RAG.md` provides human-readable retrieval context.

**Provenance:** both packs produced in user-directed Techrote IO line-art/material sessions, 2026-11-07; Pack 01 includes independently generated images; Pack 02 is algorithmically generated from established aesthetic direction. Neither is a measured PBR library. No licensing terms are created by this import.
