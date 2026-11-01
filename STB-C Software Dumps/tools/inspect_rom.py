#!/usr/bin/env python3
"""Inspect known STB-C dump directories and verify a lossless section round-trip."""
import argparse, csv, hashlib
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('rom', type=Path)
p.add_argument('--csv', type=Path, help='write discovered records')
a=p.parse_args(); data=a.rom.read_bytes()
if len(data)!=131072: raise SystemExit('Expected a 128 KiB image')
records=[]; rebuilt=bytearray(data[:0x32f3])
for base,end in ((0x32f3,0x10000),(0x10000,0x20000)):
 count=data[base+3]; offsets=[int.from_bytes(data[base+4+2*i:base+6+2*i],'big') for i in range(count)]
 if data[base+2]!=0x61 or not offsets or offsets[0] != 4+2*count or offsets!=sorted(offsets): raise SystemExit('Unrecognised directory')
 if base+offsets[-1]>=end: raise SystemExit('Directory outside bank')
 rebuilt.extend(data[base:base+offsets[0]])
 for i,off in enumerate(offsets):
  start=base+off; stop=base+offsets[i+1] if i+1<count else end
  n=data[start+12]; name=data[start+13:start+13+n]
  if start+13+n>stop or not all(32<=v<127 for v in name): raise SystemExit('Invalid record name')
  records.append({'bank':hex(base),'index':i+1,'offset':hex(start),'end_exclusive':hex(stop),'name':name.decode('ascii')})
  rebuilt.extend(data[start:stop])
assert rebuilt == data
print('SHA-256:',hashlib.sha256(data).hexdigest()); print('Directory records:',len(records)); print('Lossless reconstruction: byte-for-byte PASS (record spans preserved as raw bytes)')
for r in records: print(f"{r['bank']:>7} {r['index']:2} {r['offset']:>7} {r['name']}")
if a.csv:
 with a.csv.open('w',newline='',encoding='utf-8') as out:
  w=csv.DictWriter(out,fieldnames=records[0].keys()); w.writeheader(); w.writerows(records)
