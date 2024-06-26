# Bang & Olufsen Peripheral Unit Controller (PUC) - Decoder tables (*.DEC files)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Summary

## 1. NEC Protocol
- **Summary**: The NEC protocol is one of the most widely used IR protocols, especially in consumer electronics. It uses a pulse-distance encoding scheme, with each bit transmitted as a burst of IR followed by a space, where the length of the space determines whether the bit is a 1 or 0.
- **Brands/Models/Devices**: This protocol is used by brands such as Samsung, LG, and many other Asian manufacturers. Commonly found in TV remotes, audio equipment, and air conditioners.
- **Example Code**:
  ```plaintext
  NEC_UP_ARROW 0x20DF02FD

## 2. Sony SIRC (Sony Infrared Control)
- **Summary**: Sony's SIRC protocol uses a form of pulse-width modulation, where each bit is represented by a different length of the IR pulse. It supports multiple data lengths (12, 15, or 20 bits) to accommodate various command sets.
- **Brands/Models/Devices**: Predominantly used in Sony devices including TVs, DVD players, and stereo systems.
- **Example Code**:
  ```plaintext
  SONY_SIRC_UP_ARROW 0x1A

## 3. RC5 Protocol
- **Summary**: Developed by Philips, the RC5 protocol uses Manchester encoding, where each bit is represented by a transition in the middle of the bit period. It is known for its simplicity and robustness.
- **Brands/Models/Devices**: Used by Philips and several European manufacturers. Commonly found in TVs, VCRs, and audio systems from brands like Philips, Marantz, and some Grundig models.
- **Example Code**:
  ```plaintext
  RC5_UP_ARROW 0x1001

## 4. RC6 Protocol
- **Summary**: Also developed by Philips, the RC6 protocol is an evolution of the RC5 protocol. It uses a more complex bit encoding scheme and supports more commands by utilizing a longer bit sequence.
- **Brands/Models/Devices**: This protocol is used in more modern devices from Philips, Microsoft (e.g., for Media Center remote controls), and other advanced AV equipment.
- **Example Code**:
  ```plaintext
  RC6_UP_ARROW 0x0C00D000

## 5. Panasonic (Matsushita) Protocol
- **Summary**: The Panasonic IR protocol uses a pulse-distance encoding similar to the NEC protocol but with different timing characteristics. It is specifically designed to meet the needs of Panasonic devices.
- **Brands/Models/Devices**: Used exclusively by Panasonic for their range of televisions, home theater systems, and other consumer electronics.
- **Example Code**:
  ```plaintext
  PANASONIC_UP_ARROW 0x40040102FD

## 6. RAW Protocol
- **Summary**: The RAW protocol is not a specific standard but a way to represent IR signals as raw data. It captures the exact timing of the bursts and spaces of the IR signal, allowing any protocol to be represented and decoded. This method is used when dealing with non-standard or unknown protocols, or for learning and reproducing signals.
- **Brands/Models/Devices**: Used in universal remote controls and learning remotes that need to replicate signals from various devices, regardless of the original protocol. It can be applied to any device that uses an IR remote control, making it versatile for reverse engineering and custom applications.
- **Example Code**:
  ```plaintext
  RAW_UP_ARROW {9000, 4500, 560, 560, 560, 560, 560, 1690, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 1690, 560, 560, 560, 1690, 560, 1690, 560, 1690, 560}
