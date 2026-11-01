#!/usr/bin/env python3
"""Verify candidate Sky menu label-to-command records in the 4.01 ROM."""
import hashlib, sys
from pathlib import Path
b=Path(sys.argv[1]).read_bytes()
expected='16295fb3c5a37de1faaadf718c55d1731f385be136c620d26b6eac224840ac86'
if hashlib.sha256(b).hexdigest()!=expected: raise SystemExit('Expected the verified 4.01 dump')
labels=['tv guide','box office','services','interactive','i','text','sky','rec']
values=[0x0c,0x0d,0x0e,0x0f,0x10,0x1a,0x0b,0x20]
for i,(label,value) in enumerate(zip(labels,values)):
 t=0xb68f+16*i; p=0x7c96+16*i
 assert b[t:t+16]==b[p:p+16]
 assert b[t]==0xc1+i and b[t+1]==value
 print(f'{label:12} tag={b[t]:02X} value={value:02X} Thomson={t:#x} Pace={p:#x}')
print('PASS: tags and values match across both profiles; command meaning remains unverified.')
