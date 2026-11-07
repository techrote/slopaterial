#!/usr/bin/env python3
"""Reproduce all 46 GIMP v1 GPAT files exactly from Pack 02 PNGs.
Usage: python tools/generate_gimp_pat.py --output ./exported_PAT
Requires Pillow. Reads catalog.jsonl, verifies every PNG digest, then
verifies GIMP PAT digest against original expected per-file SHA256.
No external libraries or calls needed beyond Pillow.
"""
from pathlib import Path
import argparse, hashlib, json, struct
from PIL import Image

def sha(data):return hashlib.sha256(data).hexdigest()
def build(tile, name):
    image=Image.open(tile).convert('RGBA')
    title=name.encode('utf-8')+b'\0'
    header=struct.pack('>5I',24+len(title),1,image.width,image.height,4)+b'GPAT'+title
    return header+image.tobytes()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='exported_PAT',help='PAT output directory')
    args=parser.parse_args();root=Path(__file__).resolve().parents[1]
    out=Path(args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    for line in (root/'catalog.jsonl').read_text(encoding='utf-8').splitlines():
        if not line.strip():continue
        r=json.loads(line);original=(root/r['path']).read_bytes()
        assert sha(original)==r['sha256'],r['path']+' PNG changed'
        pat=build(root/r['path'],r['pat_display_name'])
        assert sha(pat)==r['pat_sha256'],r['path']+' PAT mismatch'
        (out/r['pat_filename']).write_bytes(pat)
        print('OK',r['pat_filename'])
    print('GIMP PAT generation complete: 46 exact original patterns')
if __name__=='__main__':main()
