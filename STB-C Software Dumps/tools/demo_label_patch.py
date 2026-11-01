#!/usr/bin/env python3
"""Demonstrate a same-length label edit in memory; never writes a ROM."""
import hashlib, sys
from pathlib import Path
b=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(b).hexdigest()=='16295fb3c5a37de1faaadf718c55d1731f385be136c620d26b6eac224840ac86'
p=0x7dde
assert b[p:p+8]==b'tv guide'
changed=bytearray(b); changed[p:p+8]=b'TV GUIDE'
diff=[i for i,(a,c) in enumerate(zip(b,changed)) if a!=c]
assert diff==[p,p+1,p+3,p+4,p+5,p+6,p+7]
assert len(changed)==len(b)
print('PASS: in-memory tv guide -> TV GUIDE; changed offsets:', ', '.join(hex(i) for i in diff))
print('This shared text is referenced by Thomson SkyHD and PACE SKY+; hardware behaviour and checksums are unverified.')
print('No ROM file written.')
