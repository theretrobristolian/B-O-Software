# Bang & Olufsen Peripheral Unit Controller (PUC) - Decoder tables (*.DEC files)

## Summary
This repository explores the structure, functionality, and practical applications of DEC (Decoder) files used in Bang & Olufsen (B&O) PUC (Peripheral Unit Controller) based solutions found in Bang & Olufsen products like the BeoSystem 3, BeoVision 6, BeoVision 8, and others, allowing these devices to control various third-party devices like set top boxes, DVD players and game consoles via the Beo4 remote - eliminating the need for additional remote controls. DEC files are integral to the B&O PUC system, which supersedes two older product implementations: the STB-C (Set Top Box - Controller) and DVD Controller, merging their functionalities into a software-updatable system. These updates are performed by B&O service technicians. 

This guide provides a comprehensive understanding of how DEC files are constructed, decoded, and utilized, enabling the creation of custom DEC files. Detailed case studies on the Apple Remote and the Thomson SkyHDmkII remote illustrate the concepts and demonstrate the practical implementation of DEC files in real-world scenarios. The aim is to equip readers with the knowledge to modify and create their own DEC files for enhanced control of third-party devices through B&O systems, using an IR blaster with PUC codes to allow a Beo4 remote to control these devices as if they were part of a heavily integrated B&O ecosystem.

## IR Protocols
This section provides an overview of the top 6 IR code protocols used in 3rd party devices, detailing their unique encoding methods and providing example codes for the "up arrow/button" function in each protocol.
### 1. NEC Protocol
- **Summary**: The NEC protocol is one of the most widely used IR protocols, especially in consumer electronics. It uses a pulse-distance encoding scheme, with each bit transmitted as a burst of IR followed by a space, where the length of the space determines whether the bit is a 1 or 0.
- **Brands/Models/Devices**: This protocol is used by brands such as Samsung, LG, and many other Asian manufacturers. Commonly found in TV remotes, audio equipment, and air conditioners.
- **Example**:
  ```plaintext
  NEC_UP_ARROW 0x20DF02FD
### 2. Sony SIRC (Sony Infrared Control)
- **Summary**: Sony's SIRC protocol uses a form of pulse-width modulation, where each bit is represented by a different length of the IR pulse. It supports multiple data lengths (12, 15, or 20 bits) to accommodate various command sets.
- **Brands/Models/Devices**: Predominantly used in Sony devices including TVs, DVD players, and stereo systems.
- **Example**:
  ```plaintext
  SONY_SIRC_UP_ARROW 0x1A
### 3. RC5 Protocol
- **Summary**: Developed by Philips, the RC5 protocol uses Manchester encoding, where each bit is represented by a transition in the middle of the bit period. It is known for its simplicity and robustness.
- **Brands/Models/Devices**: Used by Philips and several European manufacturers. Commonly found in TVs, VCRs, and audio systems from brands like Philips, Marantz, and some Grundig models.
- **Example**:
  ```plaintext
  RC5_UP_ARROW 0x1001
### 4. RC6 Protocol
- **Summary**: Also developed by Philips, the RC6 protocol is an evolution of the RC5 protocol. It uses a more complex bit encoding scheme and supports more commands by utilizing a longer bit sequence.
- **Brands/Models/Devices**: This protocol is used in more modern devices from Philips, Microsoft (e.g., for Media Center remote controls), and other advanced AV equipment.
- **Example**:
  ```plaintext
  RC6_UP_ARROW 0x0C00D000
### 5. Panasonic (Matsushita) Protocol
- **Summary**: The Panasonic IR protocol uses a pulse-distance encoding similar to the NEC protocol but with different timing characteristics. It is specifically designed to meet the needs of Panasonic devices.
- **Brands/Models/Devices**: Used exclusively by Panasonic for their range of televisions, home theater systems, and other consumer electronics.
- **Example**:
  ```plaintext
  PANASONIC_UP_ARROW 0x40040102FD
### 6. RAW Protocol
- **Summary**: The RAW protocol is not a specific standard but a way to represent IR signals as raw data. It captures the exact timing of the bursts and spaces of the IR signal, allowing any protocol to be represented and decoded. This method is used when dealing with non-standard or unknown protocols, or for learning and reproducing signals.
- **Brands/Models/Devices**: Used in universal remote controls and learning remotes that need to replicate signals from various devices, regardless of the original protocol. It can be applied to any device that uses an IR remote control, making it versatile for reverse engineering and custom applications.
- **Example**:
  ```plaintext
  RAW_UP_ARROW {9000, 4500, 560, 560, 560, 560, 560, 1690
## What is a DEC File?
A DEC file is a configuration file that provides instructions for generating and decoding infrared (IR) signals for different buttons on a remote control. These files enable B&O devices to communicate with a wide range of external electronics via IR blasters.

### The Bigger Picture: DEC Files in Context
DEC files are utilized in conjunction with B&O's Service Tool Mk2+ software and specialized hardware to program B&O systems like the BeoSystem 3. This process involves:

1. Using a USB to Serial adapter.
2. Connecting a special B&O serial cable containing a conversion chip.
3. Linking to a Masterlink pigtail cable that interfaces with the B&O system.

This setup updates the internal PUC tables, allowing the B&O system to control third-party devices effectively.

### Practical Application: Using DEC Files
1. **Creating DEC Files:** Users can create or modify DEC files to include specific IR commands for their devices. This involves defining metadata, mapping remote buttons to device functions, and specifying the IR signal for each button.

2. **Programming B&O Systems:** With the DEC file ready, it is loaded into the B&O system using the Service Tool Mk2+. The system is then capable of sending the appropriate IR signals to control external devices.

3. **Controlling Devices:** Once programmed, the B&O system can control third-party devices via IR blasters, effectively turning the B&O remote into a universal controller.

## Structure of a DEC File

DEC files used in Bang & Olufsen (B&O) systems follow a specific structure divided into several main sections. Each section serves a distinct purpose in defining how the remote controls external devices. The primary sections of a DEC file are as follows:

1. **Header Section**
2. **Associations Section**
3. **AlienSignals Section**
4. **Signal Definitions Section**

### 1. Header Section

The Header section contains metadata about the DEC file. This includes the device name, version, and author. It sets the basic parameters for the file.

**Example:**
```plaintext
  [Header]
  Name=Device Name
  Version=File Version
  Author=Author Name
```
- **Name:** The name of the device this DEC file is meant to control.
- **Version:** The version of the DEC file.
- **Author:** The author of the DEC file.
2. Associations Section

The Associations section maps the buttons on the Beo4 remote to the functions on the target device. Each mapping defines which button on the remote corresponds to which command on the controlled device.

Example:

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
BeoButtonX: The button on the Beo4 remote.
AlienButtonX: The function or command on the target device.
LineSpacingX: Defines the visual arrangement in the configuration file.
3. AlienSignals Section

The AlienSignals section lists the various signals that the DEC file will use to control the external device. Each signal corresponds to a specific function, and this section details the number of states and the signal names.

Example:

ini
Copy code
[AlienSignals]
NumStates=7
Signal1=Up
Signal2=Down
Signal3=Left
Signal4=Right
Signal5=Select
Signal6=Menu
Signal7=PlayPause
NumStates: Total number of different signals defined.
SignalX: The name of each signal, corresponding to a function on the device.
4. Signal Definitions Section

The Signal Definitions section provides the detailed IR signal instructions for each button. This section can use various IR protocols (e.g., NEC, RAW) to define the signals.

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
IRSEQUENCE: Indicates the protocol format (e.g., NEC, RAW).
Pause1 and Pause2: Delays between signals.
Carrier: Carrier frequency in kHz.
BITLEN: Lengths of bits in the signal.
PRESIGNALBITS: Bits sent before the main signal.
PRESIGNALHI and PRESIGNALLO: High and low durations for the pre-signal.
BITS: The binary sequence of the IR signal.
REPEATSIGNAL: Indicates if the signal should repeat.
Comment: Additional comments, often including the 32-bit hex representation of the signal.
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
IRSEQUENCE: Indicates the protocol format, here it's RAW.
Pause1 and Pause2: Delays between signals.
Carrier: Carrier frequency in kHz.
NumFlanks: Number of pulse transitions.
FlankListX: Lists of pulse durations in hexadecimal.
Detailed Explanation of Sections
Header Section

The header sets the context for the DEC file. It is crucial for identifying the purpose and origin of the file.

Associations Section

This section is pivotal for mapping the remote control's buttons to the corresponding functions on the target device. This mapping ensures that pressing a button on the remote sends the correct signal to the device.

AlienSignals Section

The AlienSignals section is used to declare all the possible signals that the remote can send to control the device. It acts as a reference list for the signal definitions provided later in the file.

Signal Definitions Section

The signal definitions are the core of the DEC file. They define how each button press translates into an IR signal. This section can vary significantly based on the IR protocol used (NEC, RAW, etc.). Understanding the specifics of each protocol is essential for accurate signal definition.

With this foundation, we can dive deeper into the nuances of specific cases, such as the custom protocol used by Apple Remotes, including inverting logic and parity checks, and the detailed construction of RAW signals for devices like the Thomson SkyHDmkII.

#
