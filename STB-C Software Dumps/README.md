# Beovision STB-C Dumps (Set Top Box Controller)

## Summary

This page contains ROM dumps of STB-C software chips found in Beovision Televisions in the following (but not exclusively), sets:
- AV9000  
- MX7000  
- MX4000  
- AVANT 32  
- Beovision 3  
- Beosystem 2  
and more

There is potential that these chips work in the 28" chassis of the era, but i haven't got categoric proof of that. This is aimed at mainly 32" CRTs between 1995-2005 but also includes some 4:3 sets.

### SW_3.5_T_2.6
Device used to backup: TL866II Plus   
Original ROM part number:   
ROM Chip part:   

### SW_3.5_T_2.81
Device used to backup: TL866II Plus   
Original ROM part number:   
ROM Chip part: 

### 
Device used to backup: TL866II Plus   
Original ROM part number:   
ROM Chip part: 

### SW_3.6_T_4.01
Device used to backup: TL866II Plus   
Original ROM part number:   
ROM Chip part: 

## Reverse-engineering notes

The following observations come from analysis of the three 128 KiB images in this directory. Offsets are zero-based file offsets. They describe the images provided here; they do not establish that a replacement ROM is compatible with a particular television.

### Hardware

Photographs of STB-C boards show a Philips P80C652-family controller, consistent with the 8051 instruction patterns in the dumps. A separate photographed software chip is an ST M27C1001 (128 KiB), although the original chip markings for each dump have not been independently confirmed. The Avant fitting instructions identify the controller software as IC5.

### Image layout

Each image contains two observed table directories, beginning at `0x32F3` and `0x10000`. In these examples, the count is at directory offset `+3`; the following big-endian 16-bit values point to records relative to the directory base. A record has a name-length byte at `+12`, followed by the ASCII name at `+13`.

| Dump | First directory | Second directory | SHA-256 |
| --- | ---: | ---: | --- |
| SW 3.5 / table 2.6 | 40 records | 41 records | `c964aeed80b960ccae83bb8cf0b350176a640d4fbd17e813ad834edda3face56` |
| SW 3.5 / table 2.81 | 39 | 37 | `33c20242c696d3808b7ce9ee55067e1043e67b249ff2d43eae24c009ed649ce6` |
| SW 3.6 / table 4.01 | 25 | 25 | `16295fb3c5a37de1faaadf718c55d1731f385be136c620d26b6eac224840ac86` |

The 2.6 image contains records named SELECTOR, TF4000PVR, CASEMA SELECTOR and TELECLUB in addition to the 77 items listed in its text file. Whether these are selectable in a given TV has not been established.

### Beo4 menu and colour labels: table 4.01

The `Thomson SkyHD` record begins at `0xB491`. Its big-endian field at record offset `+6` is `0x849C`; adding the first directory base `0x32F3` points to `0xB78F`. There a count byte (`0x0C`) precedes 12 big-endian, base-relative pointers to label records. Each observed label record consists of a tag byte, a zero byte, a length byte and that many ASCII characters.

The first eight labels are `tv guide`, `box office`, `services`, `interactive`, `i`, `text`, `sky` and `rec`, matching the MENU/GO labels on the supplied Thomson SkyHD Beo4 reference. The last four are `YELLOW`, `GREEN`, `BLUE` and `RED`. The relationship between every tag and the controller's on-screen behaviour still needs runtime verification.

The `tv guide` label is also referenced by the `PACE SKY+` label table: label storage can be shared between devices. The Thomson table's colour-label pointers also lead outside its own device record. Consequently, changing a shared string in place could affect multiple devices, and moving or copying one record requires more than copying its apparent contiguous bytes. The relationship between labels, command mappings and IR waveforms remains under investigation.

### Candidate command mappings

In the 4.01 Thomson profile, the block pointed to by record field `+2` contains a series of 16-byte records. Eight consecutive records at `0xB68F` through `0xB6FF` begin with tags `C1` through `C8`, matching the tags of the eight menu label entries. Their second bytes are, respectively, `0C 0D 0E 0F 10 1A 0B 20`. This is strong evidence of a link between menu choices and a command table, but it is not yet proof of the exact meaning of those second bytes or the IR waveform they produce. The corresponding eight records in PACE SKY+ are byte-identical. The two pointed-to data blocks share a 656-byte prefix.

The user reports that their working Avant uses the dumped 4.01 chip and that MENU then 1 opens the Sky guide. This provides an expected hardware behaviour for testing the `C1` / `0C` candidate. It does not establish where MENU interception happens or that changing this byte is safe.

### Reproducing the checks

From this directory, using Python 3:

```sh
python3 tools/inspect_rom.py SW_3.6_T_4.01.BIN
python3 tools/check_skyhd_labels.py SW_3.6_T_4.01.BIN
python3 tools/check_sky_mappings.py SW_3.6_T_4.01.BIN
python3 tools/demo_label_patch.py SW_3.6_T_4.01.BIN
```

The first script lists records and verifies that joining the original raw sections recreates the input byte for byte. It can also write a CSV with `--csv records.csv`. It does not decompile the software or validate relocation. The second script checks the 4.01 SHA-256, follows the Thomson label pointers, verifies the 12 labels and confirms that the `tv guide` string is shared with PACE SKY+.

The third script demonstrates an eight-character case change in memory and verifies exactly which seven bytes changed. It does not write a ROM or prove the edit will display correctly on a TV.

These checks are offline analysis. No modified image, checksum algorithm, TV compatibility, on-screen result or infrared output has yet been verified on hardware. Preserve and independently verify the original ROM before experimenting.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

As people contribute their names will be added to this list, with thanks.

* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>
