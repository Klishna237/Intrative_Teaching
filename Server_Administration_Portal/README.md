# CSC204: Server Administration — Master University Knowledge Portal

> **Department of Computer Science & Engineering**  
> **Course Code:** CSC204 • **Domain:** Cyber Security & Enterprise Infrastructure  
> **Format:** 100% Self-Contained Offline Single-Page Academic Publication (Master Gold Standard)

---

## 🌟 Executive Overview

The **Server Administration Knowledge Portal** is an enterprise-grade academic master reference designed to the rigorous publication standards of the external gold-standard benchmark (`CSC104: IT Fundamentals`). It encapsulates the complete curriculum of Enterprise Server Administration with unmatched technical depth, register- and silicon-level execution traces, structured comparison matrices, 180 interactive MCQs with instant feedback and scoring engines, subjective analysis questions, 10 fully verified hands-on laboratory manuals, interactive engineering calculators, and an embedded dual Windows PowerShell and Linux Bash terminal sandbox.

---

## 📊 Portal Metrics & Blueprint

| Metric | Measurement | Description |
| :--- | :--- | :--- |
| **Total Artifact Size** | **550.8 KB** | 100% Self-contained single-page web application (`index.html`) |
| **Source Code Scale** | **7,072 Lines** | Clean, semantic, validated HTML5 / CSS3 / ES6 |
| **Curricular Units** | **6 Core + 4 Specialized** | Units 1 to 6, Deep Traces, Lab Manual, Simulators, Exam Bank |
| **Technical Articles** | **30 Core Deep-Dives** | Comprehensive theoretical and practical server systems coverage |
| **Practice Bank (MCQs)** | **180 Questions** | 30 MCQs per unit with scoring engine & master answer keys |
| **Subjective Problems** | **69 Card Scenarios** | 30 Conceptual (5M) & 24 Scenarios (10M) + MST & Final papers |
| **Laboratory Practicals** | **10 Full Experiments** | Production CLI commands, expected outputs & Viva Voce questions |
| **Interactive Simulators** | **4 Calculators + CLI** | RAID Sizer, Write Penalty IOPS, Base-10 Discrepancy & Dual Terminal |

---

## 🗂️ Curricular Structure & Syllabus Alignment

### Unit 01: Server Hardware Fundamentals & Power Architecture
- **s1-hardware:** Server Form Factors (EIA-310 standard 1U/2U/4U rack enclosures, Blade Servers & midplanes, Tower pedestal systems, Baseboard Management Controllers - BMC iDRAC/iLO).
- **s1-cpu:** Multi-Socket Processors & NUMA Architecture (Intel Xeon Scalable UPI vs AMD EPYC Infinity Fabric, NUMA node topology, local vs remote memory access latencies, vNUMA alignment).
- **s1-ram:** Server Memory Subsystems (DDR4/DDR5 ECC Registered RDIMMs vs LRDIMMs, SECDED Hamming Code bit-correction math, Chipkill multi-bit protection).
- **s1-expansion:** High-Speed I/O & Expansion (PCIe 5.0 riser cards, OCP NIC 3.0 mezzanine cards, Tri-Mode U.2/U.3 NVMe backplanes, SAS-3 12Gbps HBAs).
- **s1-power-cooling:** Power Redundancy & Data Center Thermal Dynamics (N+1 vs 2N concurrent maintainability, CRPS modules, Hot/Cold aisle airflow containment, ASHRAE A1-A4 guidelines).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 02: Server Installation, Filesystems & Virtualization
- **s2-os-install:** Automated OS Deployment (The 6-stage PXE network boot sequence, DHCP Option 66/67, WDS, and Red Hat Kickstart `ks.cfg` automation).
- **s2-partitioning:** Partitioning & Resilient Filesystems (MBR 2.2TB limits vs GPT 64-bit LBA, LVM PV/VG/LV hierarchies, Microsoft ReFS Block Cloning & Accelerated VHDX).
- **s2-virt:** Type-1 Hypervisors & Hyper-V Architecture (VMware ESXi VMkernel, Microsoft Hyper-V Parent Partition, Child Partitions, and in-memory VMBus).
- **s2-memory-ballooning:** Virtual Memory Management (Memory overcommitment, Balloon drivers `vmmemctl`, Hyper-V Dynamic Memory, Transparent Page Sharing TPS).
- **s2-virtual-networking:** Virtual Switching & VLAN Modes (Standard vs Distributed Virtual Switches, VST vs EST vs VGT tagging, SR-IOV direct memory assignment).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 03: Server Roles, Maintenance & High Availability
- **s3-ad-roles:** Active Directory Architecture & The 5 FSMO Roles (Schema Master, Domain Naming Master, RID Master pool allocation, PDC Emulator time master, Infrastructure Master, role seizure).
- **s3-network-services:** Enterprise Network Services (Active Directory DNS SRV records, DHCP Failover Load-Sharing vs Hot-Standby MCLT).
- **s3-web-app:** Web & Application Servers (Microsoft IIS HTTP.sys kernel listener, Application Pool worker process isolation `w3wp.exe`, Linux NGINX).
- **s3-patching:** Enterprise Patch Management (WSUS staging rings, Patch Tuesday, Change Advisory Board RFCs, Cluster-Aware Updating CAU).
- **s3-clustering:** Windows Server Failover Clustering (WSFC Quorum majority formula \(\lfloor N/2 \rfloor + 1\), File Share Witness, Azure Cloud Witness, Split-Brain prevention).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 04: Storage Technologies & RAID Architecture
- **s4-storage-arch:** Storage Topologies (DAS vs NAS vs SAN, block-level vs file-level access, clustered filesystems).
- **s4-protocols:** Storage Protocols & Transport Fabrics (iSCSI IQNs, portals, Jumbo Frames 9000 MTU, Fibre Channel WWPNs, MPIO Round-Robin load balancing).
- **s4-raid:** RAID Engine Architecture (RAID 0, 1, 5, 6, 10, Boolean XOR parity math \(P = D_1 \oplus D_2 \oplus D_3\), hot spares).
- **s4-write-penalty:** The RAID Write Penalty (4-IOPS RAID 5 penalty, 6-IOPS RAID 6 penalty, SSD Wear Leveling, SLC/MLC/TLC/QLC).
- **s4-capacity:** Capacity Planning & Storage Economics (Decimal Base-10 vs Binary Base-2 storage discrepancy, 1TB = 931.32 GiB, FSRM directory quotas).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 05: Server Security, Hardening & Compliance
- **s5-hardening:** Server OS Hardening & CIS Benchmarks (Disabling unneeded services, Windows Defender Credential Guard VBS LSASS isolation, Linux PAM `/etc/pam.d/`, visudo).
- **s5-auth-pki:** Authentication Protocols & PKI (The 6-stage Kerberos v5 ticket-granting sequence: AS-REQ &rarr; AS-REP &rarr; TGS-REQ &rarr; TGS-REP &rarr; AP-REQ, OCSP Responder).
- **s5-network-security:** Host Firewalls & Micro-Segmentation (FirewallD/nftables, Windows Defender Firewall, DMZ dual-firewall architecture, IPsec Transport vs Tunnel modes).
- **s5-storage-encryption:** Storage Encryption & Media Sanitization (BitLocker TPM 2.0 Network Unlock, Linux LUKS2, NIST SP 800-88 Clear/Purge/Destroy vs DoD 5220.22-M).
- **s5-audit-compliance:** Security Event Auditing (Windows Event IDs: 4624, 4625, 4720, 4728, 1102; Linux auditd SIEM ingestion).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 06: Networking, Disaster Recovery & Troubleshooting
- **s6-networking:** Enterprise Server Networking (NIC Teaming: Switch Independent vs LACP 802.3ad, Address Hash vs Hyper-V Port, Cat6a/Cat8, OM4/OS2 fiber).
- **s6-ports:** Master Enterprise Well-Known Port Matrix (DNS 53, DHCP 67/68, Kerberos 88, NTP 123, SNMP 161, LDAP 389, HTTPS 443, SMB 445, LDAPS 636, iSCSI 3260, RDP 3389, WinRM 5986).
- **s6-dr:** Disaster Recovery Principles & Site Topologies (Hot Site, Warm Site, Cold Site, Mobile Site, Synchronous vs Asynchronous storage replication).
- **s6-backups:** Enterprise Backup Methodologies (The 3-2-1-1-0 Backup Rule, Full vs Differential vs Incremental backup math, RPO and RTO SLA calculations, VSS snapshots).
- **s6-triage:** Diagnostic Triage & BSOD Crash Analysis (CompTIA 7-Step Troubleshooting Model, Windows Blue Screen MEMORY.DMP WinDbg `!analyze -v`, Stop Codes: `IRQL_NOT_LESS_OR_EQUAL`, `PAGE_FAULT_IN_NONPAGED_AREA`).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 07: Special Architectural Deep Traces
- **server-trace-packet:** End-to-End Silicon & Wire Trace: (1) Active Directory Enterprise Kerberos v5 Authentication and PAC SID evaluation; (2) Microsecond Lifecycle of a Degraded RAID 5 Disk Failure and Online Parity XOR Rebuild.

### Unit 08: Hands-On Enterprise Laboratory Manual
- Complete step-by-step guides for 10 university practicals with Windows PowerShell and Linux Bash scripts, outputs, and Viva Voce questions.

### Unit 09: Engineering Simulators & Dual CLI Sandbox
- Interactive client-side tools: RAID Capacity & Efficiency Calculator, Write Penalty IOPS Sizer, Base-10 to Base-2 Storage Discrepancy converter, and an embedded interactive Dual Windows PowerShell 7.4 / Linux RHEL 9 Bash terminal sandbox.

### Unit 10: Master Comprehensive Examination Bank
- Mid-Semester Tests (MST-1 & MST-2) and End-Semester Final Examination papers mapped directly to Course Outcomes (CO1–CO5) and Bloom's Revised Taxonomy levels.

---

## 🚀 How to Access & Deploy

1. **Local Offline Access**: Open `d:\CU - Teach\Server_Administration_Portal\index.html` in any modern web browser (Chrome, Edge, Firefox, Safari). Zero Internet connectivity or web server required.
2. **Search Shortcut**: Press `Ctrl + K` or `/` to launch the interactive instant keyword search.
3. **Table of Contents**: Press `Ctrl + B` or click the menu icon in the top left to toggle the collapsible course navigator.
4. **Theme Customization**: Toggle between Light, Sepia, and Dark themes using the header theme switcher dots.
