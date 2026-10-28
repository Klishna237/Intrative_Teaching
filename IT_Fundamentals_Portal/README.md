# IT Fundamentals Master Knowledge Portal & Interactive Learning Engine

A master-grade, responsive, self-contained educational web application and digital textbook built for The Department's **IT Fundamentals (Lectures 01–30)** curriculum.

---

## 🌟 Key Features

### 1. Master-Grade Depth across 30 Full Lectures
Synthesized directly from official Department of Computer Science & Engineering lecture slide decks (380+ slides), course syllabi, laboratory manuals, and CompTIA A+ core standards:
- **Unit 01: Computer Hardware & Motherboard Systems** (Lectures 01–05)
  - Form factors: ATX, Micro-ATX, Mini-ITX, E-ATX with standoff grounding physics.
  - Expansion buses: PCIe 3.0, 4.0, 5.0 lane encoding and bandwidth formulas ($B = L \times R \times E$).
  - Processor sockets: LGA vs PGA vs BGA, pin pitch, zero insertion force (ZIF).
  - Memory architectures: DDR4 vs DDR5 DIMM & SO-DIMM, dual-channel A2/B2 routing rules.
  - Power supplies: SMPS topology, rail tolerances, 80 Plus ratings, PS_ON# jumpering.
  - Firmware: Legacy BIOS vs modern UEFI, GPT GUID partition tables, CMOS CR2032 reset.
- **Unit 02: Computer Networks & Protocols** (Lectures 06–10)
  - Network classifications: PAN, LAN, HAN, CAN, MAN, WAN, SAN.
  - Topologies: Physical Bus, Star, Ring, Mesh, Hybrid; collision and broadcast domain isolation.
  - Transmission media: Cat5e, Cat6, Cat6a, Cat7, Cat8; T568A vs T568B; Single-Mode vs Multi-Mode fiber optics.
  - OSI 7-Layer Model vs TCP/IP Model with full Layer-7 to Layer-1 PDU encapsulation/decapsulation.
  - TCP 3-Way Handshake (SYN &rarr; SYN-ACK &rarr; ACK) vs UDP, socket addressing.
  - Subnetting mastery: CIDR notation, subnet masks, host formula ($2^H - 2$), worked VLSM problems.
  - Virtualization & Cloud: Type-1 (Bare-Metal) vs Type-2 (Hosted) hypervisors, IaaS, PaaS, SaaS.
- **Unit 03: Mobile Devices, Peripherals & Storage** (Lectures 11–15)
  - Mobile architecture: ARM big.LITTLE heterogeneous multi-processing SoC, OLED vs IPS LCD.
  - Laptop servicing: Keyboard replacement, SO-DIMM, M.2 NVMe SSD thermal pads, battery safety.
  - Enterprise mobility: MDM (Microsoft Intune), remote wipe, secure Knox containerization.
  - Peripheral interfaces: USB 2.0 through USB4/Thunderbolt 4 (40 Gbps, 240W EPR).
  - Laser printing mechanics: Full 7-stage electrophotographic cycle (Cleaning &rarr; Conditioning &rarr; Writing &rarr; Developing &rarr; Transferring &rarr; Fusing &rarr; Exposing).
  - Windows file sharing: Shared folder vs NTFS permissions, "Most Restrictive Wins" rule.
- **Unit 04: Operating Systems, Command-Line & Diagnostics** (Lectures 16–20)
  - Operating system architecture: Monolithic vs microkernel, CPU privilege rings (Ring 0 vs Ring 3).
  - 32-bit (x86, 4GB limit) vs 64-bit (x64, 16EB address space, mandatory driver signing).
  - File systems: NTFS, FAT32, exFAT, ReFS; MBR (2TB, 4 partitions) vs GPT (18EB, 128 partitions).
  - Windows boot flow: SEC &rarr; PEI &rarr; DXE &rarr; BDS &rarr; `bootmgfw.efi` &rarr; `winload.efi` &rarr; `ntoskrnl.exe`.
  - Microsoft Management Console (MMC): `compmgmt.msc`, `devmgmt.msc`, `diskmgmt.msc`, `services.msc`, `eventvwr.msc`.
  - Linux root directory structure (`/bin`, `/etc`, `/dev`, `/proc`, `/sys`, `/var`) and octal `chmod` permissions.
  - Diagnostic stop codes: BSOD troubleshooting, DISM component store repair, SFC scans.
- **Unit 05: SOHO Network Configuration & Wireless Security** (Lectures 21–25)
  - Multifunction SOHO Gateway: Router, 4-port switch, wireless AP, stateful firewall, NAT engine.
  - IPv4 Addressing: RFC 1918 Private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
  - NAT & PAT (Port Address Translation): Socket tracking and IP packet rewriting.
  - DHCP 4-Stage Handshake: DORA protocol (Discover &rarr; Offer &rarr; Request &rarr; Acknowledge).
  - Wireless security evolution: WEP (broken RC4), WPA, WPA2 (AES-CCMP), WPA3 (SAE Dragonfly handshake).
  - Wi-Fi bands: 2.4 GHz vs 5 GHz vs 6 GHz (Wi-Fi 6E/7), channel overlap analysis.
  - Inbound traffic control: Port Forwarding vs Port Triggering vs DMZ host exposure.
- **Unit 06: Operational Procedures, Security & Safety** (Lectures 26–30)
  - CompTIA 7-Step Malware Remediation Protocol: Identify &rarr; Quarantine &rarr; Disable System Restore &rarr; Remediate &rarr; Schedule Scans &rarr; Enable System Restore &rarr; Educate User.
  - Electrostatic Discharge (ESD): 100V gate breakdown paradox, ESD wrist straps, antistatic mats.
  - Physical safety: High-voltage SMPS and CRT capacitor hazards, Class C electrical fire extinguishers.
  - Workplace safety: OSHA standards, 16-section Safety Data Sheets (MSDS/SDS).
  - Professional IT communication: Incident lifecycle, SLA priority matrix, de-escalation scripts.
  - Digital forensics: Chain of custody, SHA-256 cryptographic hashing, RFC 3227 order of volatility.

---

### 2. Built-In Interactive Simulators & Sandboxes (Between Topics)
Students don't just read theory—they experiment live directly inside the browser:
1. **Front-Panel Header Pinout Inspector**: Click Power SW, Reset SW, HDD LED, and Power LED to inspect electrical triggers, polarities, and Super I/O signals.
2. **Motherboard POST Audio Simulator**: Audition and decode beep codes (Normal POST, DRAM failure, GPU error, Thermal siren).
3. **Thermal Paste Application Simulator**: Test pea-dot, excessive, manual spread, and plastic film errors with live temperature feedback.
4. **RAM Dual-Channel Slot Populator**: Test combinations ($A_2+B_2$, $A_1+A_2$, $A_1+B_1$, $B_1+B_2$) and observe memory bus bandwidth scaling.
5. **Ethernet Cable Wiring Inspector**: Examine T568A, T568B, straight-through, and crossover cable pinouts.
6. **Collision & Broadcast Domain Analyzer**: Test hubs, switches, and routers to observe domain segmentation.
7. **PDU Encapsulation Tracer**: Step through Layer 7 Data &rarr; Layer 4 Segment &rarr; Layer 3 Packet &rarr; Layer 2 Frame &rarr; Layer 1 Bits.
8. **Subnet & CIDR Calculator**: Calculate subnet masks, usable hosts, and block sizes across CIDR prefixes (/24, /26, /28, /30).
9. **Laptop Servicing & Diagnostics**: Inspect battery safety, SO-DIMM installation, NVMe SSD mounting, and heatsink removal rules.
10. **Laser Printer Defect Engine**: Diagnose ghosting, unfused toner smudges, blank pages, and solid black prints with physics explanations.
11. **NTFS vs Share Permission Evaluator**: Test permissions and see the "Most Restrictive Wins" rule calculated dynamically.
12. **Windows Event Viewer Security Simulator**: Inspect Event IDs 4624 (Logon), 4625 (Brute Force), 4720 (Account Created), and 1102 (Log Cleared).
13. **Linux Chmod Permission Calculator**: Interactively compute numeric modes (755, 644, 777, 600) and symbolic strings (`rwxr-xr-x`).
14. **SOHO Inbound Access Simulator**: Test stateful drop, NAT port forwarding, dynamic triggering, and DMZ host exposure.
15. **CompTIA 7-Step Malware Remediation**: Step through interactive quarantine and recovery workflows.
16. **Live Interactive Terminal Sandbox (CLI Reference)**: Authentic simulated command prompt (`C:\Users\Student>`) where students can run:
    - `ipconfig` & `ipconfig /all`
    - `ping 8.8.8.8`
    - `tracert 1.1.1.1`
    - `nslookup google.com`
    - `netstat -ano`
    - `sfc /scannow`
    - `chmod 755 app.sh`
    - `help` & `cls`

---

### 3. Comprehensive Assessments & Viva Voce
- **72 Interactive Unit MCQs**: 10+ questions per unit with instant feedback, explanations, and persistent score counters (`#u1-score` through `#u6-score`).
- **Exam Preparation Master Bank**: 2-Mark short conceptual definitions, 5-Mark analytical comparison tables, and 10-Mark comprehensive scenario-based questions with complete model answers.
- **10 Hands-On Laboratory Exercises**: Complete procedural manuals for PC assembly, cable crimping, packet capture, Linux CLI, and disk management.

---

### 4. UI Design & Offline Capability
- **Dark Zinc Theme**: Modern engineering documentation style styled with clean typography and custom scrollbars.
- **4 Dynamic Theme Palettes**: Emerald Mint, Electric Violet, Sunset Amber, and Cyber Cyan.
- **100% Offline Ready**: Single standalone file (`index.html`). Double-click to open in any web browser without local servers or external internet access.

---

## 🚀 Quick Start / How to Run

1. Open `index.html` in any web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).
2. Use the left navigation sidebar to explore Units 01 through 06, the Command-Line Arsenal, Exam Preparation, or the Laboratory Manual.
3. Test commands in the interactive terminal or solve practice MCQs at the end of each unit.
