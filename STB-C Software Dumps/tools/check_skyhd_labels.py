#!/usr/bin/env python3
"""Verify the known Thomson SkyHD label references in the 4.01 image."""
import hashlib
import sys
from pathlib import Path

EXPECTED_HASH = '16295fb3c5a37de1faaadf718c55d1731f385be136c620d26b6eac224840ac86'
base = 0x32f3
rom = Path(sys.argv[1]).read_bytes()
if hashlib.sha256(rom).hexdigest() != EXPECTED_HASH:
    raise SystemExit('This check requires the exact SW_3.6_T_4.01.BIN image')
record = 0xb491
name_length = rom[record + 12]
assert rom[record + 13:record + 13 + name_length] == b'Thomson SkyHD'
table = base + int.from_bytes(rom[record + 6:record + 8], 'big')
assert table == 0xb78f
expected = [(0xc1, b'tv guide'), (0xc2, b'box office'), (0xc3, b'services'),
            (0xc4, b'interactive'), (0xc5, b'i'), (0xc6, b'text'),
            (0xc7, b'sky'), (0xc8, b'rec'), (0xd4, b'YELLOW'),
            (0xd5, b'GREEN'), (0xd8, b'BLUE'), (0xd9, b'RED')]
assert rom[table] == len(expected)
for i, (tag, label) in enumerate(expected):
    pointer = int.from_bytes(rom[table + 1 + i * 2:table + 3 + i * 2], 'big')
    address = base + pointer
    assert rom[address:address + 3] == bytes((tag, 0, len(label)))
    assert rom[address + 3:address + 3 + len(label)] == label
    print(f'{i + 1:2}: tag {tag:02x}, offset {address:#07x}, {label.decode()}')
# The first Thomson text entry is shared with PACE SKY+.
pace = 0x7a9c
pace_table = base + int.from_bytes(rom[pace + 6:pace + 8], 'big')
assert int.from_bytes(rom[pace_table + 1:pace_table + 3], 'big') == int.from_bytes(rom[table + 1:table + 3], 'big')
print('PASS: 12 label references verified; tv guide is shared with PACE SKY+.')
