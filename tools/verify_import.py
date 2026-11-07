#!/usr/bin/env python3
"""Verify all imported material PNG sources and stage routing (requires Pillow)."""
from pathlib import Path
import hashlib, json
from PIL import Image

root=Path(__file__).resolve().parents[1]
packs=[("roughref/material_texture_pack_01",10),("mediumqual/material_texture_pack_02",46)]
count=0
exceptions=[]
for pack,expected in packs:
    folder=root/pack
    rows=[json.loads(line) for line in (folder/"catalog.jsonl").read_text().splitlines() if line.strip()]
    assert len(rows)==expected,(pack,len(rows),expected)
    unique=set()
    for item in rows:
        name=item["path"]
        assert name not in unique,(pack,name)
        unique.add(name)
        path=(folder/name).resolve()
        assert path.is_relative_to(folder.resolve()),name
        assert path.is_file(),path
        raw=path.read_bytes()
        actual=hashlib.sha256(raw).hexdigest()
        expected_stored=item.get("stored_sha256",item["sha256"])
        assert actual==expected_stored,(name,"source/stored sha256 mismatch",actual,expected_stored)
        with Image.open(path) as im:
            assert list(im.size)==item["dimensions"],(name,im.size,item["dimensions"])
            assert im.mode==item["mode"],(name,im.mode,item["mode"])
            if "decoded_rgb_sha256" in item:
                assert im.mode=="RGB",name
                rgb_digest=hashlib.sha256(im.tobytes()).hexdigest()
                assert rgb_digest==item["decoded_rgb_sha256"],(name,"decoded pixels mismatch")
                assert item["sha256"]!=actual,(name,"redundant reencode exception")
                exceptions.append(name)
            else:
                assert actual==item["sha256"],(name,"not source-byte identical")
        count+=1
        print("PASS",pack,name)
assert count==56,count
assert exceptions==["source_png/seamless_pale_concrete_stone_texture.png"],exceptions
print(f"PASS: {count} individual PNG textures; 55 byte-identical originals, 1 verified lossless container re-encode")
