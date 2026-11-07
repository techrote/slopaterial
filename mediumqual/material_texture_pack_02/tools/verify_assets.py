#!/usr/bin/env python3
"""Validate Pack 02 PNG manifest and seams (requires Pillow + NumPy)."""
from pathlib import Path
from PIL import Image
import numpy as np, hashlib,json
root=Path(__file__).resolve().parents[1]
items=[json.loads(l) for l in (root/'catalog.jsonl').read_text().splitlines() if l.strip()]
assert len(items)==46
for r in items:
    p=root/r['path'];raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'],p
    img=Image.open(p);assert list(img.size)==[1024,1024] and img.mode==r['mode'],p
    a=np.asarray(img).astype('int16');
    # Require a continuous seam comparable to an ordinary 1-pixel neighbour difference.
    if a.ndim==2:a=a[:,:,None]
    lr=float(np.abs(a[:,0]-a[:,-1]).mean())
    tb=float(np.abs(a[0]-a[-1]).mean())
    interior_lr=float(np.abs(a[:,1:]-a[:,:-1]).mean());interior_tb=float(np.abs(a[1:]-a[:-1]).mean())
    if max(lr/max(interior_lr,1),tb/max(interior_tb,1))>3.0:raise AssertionError(f'Unacceptable seam in {p}')
    print('PASS',r['category'],p.name)
print('Validated 46 individual PNG textures / fills')
