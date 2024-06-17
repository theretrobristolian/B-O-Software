# B&O PUC DEC Files

This repository contains DEC (Device Control) files used by Bang & Olufsen (B&O) remote systems to control various third-party devices through IR signals. These files are an integral part of B&O's Programmable Universal Controller (PUC) system.

## What is a DEC File?

A DEC file is a configuration file that provides instructions for generating and decoding infrared (IR) signals for different buttons on a remote control. These files enable B&O devices to communicate with a wide range of external electronics via IR blasters.

## The Wider Picture: DEC Files in Context

DEC files are used in conjunction with B&O's Service Tool Mk2+ software and specialized hardware to program B&O systems like the BeoSystem 3. The process involves:
1. Using a USB to Serial adapter.
2. Connecting a special B&O serial cable containing a conversion chip.
3. Linking to a Masterlink pigtail cable that interfaces with the B&O system.

This setup updates the internal PUC tables, allowing the B&O system to control third-party devices effectively.

## Practical Application: Using DEC Files

1. **Creating DEC Files**: Users can create or modify DEC files to include specific IR commands for their devices. This involves defining metadata, mapping remote buttons to device functions, and specifying the IR signal for each button.
   
2. **Programming B&O Systems**: With the DEC file ready, it is loaded into the B&O system using the Service Tool Mk2+. The system is then capable of sending the appropriate IR signals to control external devices.

3. **Controlling Devices**: Once programmed, the B&O system can control third-party devices via IR blasters, effectively turning the B&O remote into a universal controller.

## Structure of a DEC File

### Header Information
Contains metadata about the file, including device name, version, and author.

```ini
[Header]
Name=Device Name
Version=File Version
Author=Author Name

Button Mapping
Maps Beo4 remote buttons to the functions on the target device.

ini
Copy code
[Associations]
BeoButton1=up
AlienButton1=Up
LineSpacing1=2
BeoButton2=down
AlienButton2=Down
LineSpacing2=2
...
Signal Definitions
Provides detailed IR signal instructions for each button, either in a standard protocol format (e.g., NEC) or RAW timings.

NEC Example:

ini
Copy code
[Signal_Menu]
IRSEQUENCE=NEC
Pause1=42040
Pause2=96558
Carrier=38
BITLEN=563 602 1723
PRESIGNALBITS=0 0
PRESIGNALHI=9027
PRESIGNALLO=4554
BITS=100010000001111010111111011110111
REPEATSIGNAL=1
Comment=NEC 32bits=881EBF7B
RAW Example:

ini
Copy code
[Signal_Menu]
IRSEQUENCE=RAW
Pause1=97636
Pause2=97615
Carrier=36
NumFlanks=71
FlankList1=$00A1,$34C5,$00A9,$03EE,$008D,$0871,$00A6,$0857,$008D,$0871,$00A9,$03EE
...
Comment=RAW FlankList:71 flanks
Case Study: Apple Remote

Protocol Overview
The Apple Remote uses a custom protocol based on the NEC standard. It modifies the standard by using 7 bits for the button code, 1 parity bit, and 8 bits for the remote ID.

Example: Menu Button
Expected Values:

Button Code (7 bits): 1000100 (0x44)
Parity Bit (1 bit): Calculated using XOR of button code and ID bits.
ID (8 bits): Specific to the remote, often 00000111 (0x07)
Combined Binary Sequence:

Button Code + Parity Bit + ID: 1000100 0 00000111
Given in DEC File:

ini
Copy code
[Signal_Menu]
IRSEQUENCE=NEC
Pause1=42040
Pause2=96558
Carrier=38
BITLEN=563 602 1723
PRESIGNALBITS=0 0
PRESIGNALHI=9027
PRESIGNALLO=4554
BITS=100010000001111010111111011110111
REPEATSIGNAL=1
Comment=NEC 32bits=881EBF7B
Inverting Logic and Parity Check
Apple's protocol includes specific modifications such as inverting bits and adding a parity check. The parity bit ensures data integrity, and inversion may be used to match Apple's custom IR transmission requirements.

Case Study: Thomson SkyHDmkII

Protocol Overview
The Thomson SkyHDmkII uses RAW IR signals rather than a standard protocol like NEC. RAW format specifies the exact pulse durations.

Example: Menu Button
RAW Example:

ini
Copy code
[Signal_Menu]
IRSEQUENCE=RAW
Pause1=97636
Pause2=97615
Carrier=36
NumFlanks=71
FlankList1=$00A1,$34C5,$00A9,$03EE,$008D,$0871,$00A6,$0857,$008D,$0871,$00A9,$03EE
...
Comment=RAW FlankList:71 flanks
Button Mappings

The button mappings define the correspondence between buttons on the Beo4 remote and the functions on the target device. This section details the specific IR signals for each button.

Example Mappings for Beo4 Remote
ini
Copy code
[Associations]
BeoButton1=up
AlienButton1=Up
LineSpacing1=2
BeoButton2=down
AlienButton2=Down
LineSpacing2=2
BeoButton3=rewind
AlienButton3=Left
LineSpacing3=2
BeoButton4=wind
AlienButton4=Right
LineSpacing4=2
BeoButton5=play(go)
AlienButton5=Select
Constructing Your Own DEC File

Define Metadata: Include device name, version, and author.
Map Buttons: Create associations between Beo4 buttons and device functions.
Define Signals: Use NEC, RAW, or other protocol formats to specify IR signals.
For NEC, include standard timings and check for Apple-specific modifications.
For RAW, specify exact pulse durations.
References

HiFiDuino: Apple Aluminum Remote
IR Protocol Documentation: NEC Protocol
B&O DEC File Examples: GitHub Repository