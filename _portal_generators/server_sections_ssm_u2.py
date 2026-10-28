# -*- coding: utf-8 -*-
"""
Server Administration Portal - Unit 2: Server Installation and Virtualization
SSM Engineering Standard Gold Standard Architecture
"""

SERVER_UNIT2_HTML = r"""
<!-- ===================================================================
     UNIT 02: SERVER INSTALLATION AND VIRTUALIZATION
     =================================================================== -->

<!-- ARTICLE 6: ENTERPRISE SERVER OS DEPLOYMENT -->
<article class="doc-page" id="s2-os-install">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Installation &amp; Virtualization • Article 06</span>
    <h2 class="section-title"><span class="sec-num">06</span> Enterprise Server OS Deployment, PXE Network Boot &amp; Automation</h2>
    <p class="lead-para">
      Deploying server operating systems at enterprise scale requires eliminating interactive manual media installs. Automated network provisioning via Preboot Execution Environment (PXE), Windows Deployment Services (WDS), and Kickstart automation orchestrates bare-metal rollouts across thousands of host nodes.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. The 6-Stage PXE Network Boot Sequence</h3>
  <p>
    PXE operates at the firmware level (UEFI/BIOS), leveraging standard UDP broadcast protocols to boot a bare-metal server over the local area network:
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Stage</th>
          <th>Protocol / Port</th>
          <th>Physical / Logical Action</th>
          <th>Payload Delivered</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. DHCP Discovery</strong></td>
          <td>DHCP (UDP 67/68)</td>
          <td>Client broadcasts DHCPDISCOVER with Option 93 (Client System Architecture, e.g. UEFI x86-64).</td>
          <td>Client MAC address &amp; architecture tag</td>
        </tr>
        <tr>
          <td><strong>2. DHCP Offer &amp; PXE Tags</strong></td>
          <td>DHCP (UDP 67/68)</td>
          <td>DHCP server returns IP offer along with **Option 66** (TFTP Next Server IP) and **Option 67** (Bootfile Name).</td>
          <td>Server IP: <code class="code-inline">192.168.1.50</code>, File: <code class="code-inline">bootx64.efi</code></td>
        </tr>
        <tr>
          <td><strong>3. TFTP Bootloader Pull</strong></td>
          <td>TFTP (UDP 69)</td>
          <td>Client contacts TFTP server to download the signed First-Stage EFI Network Bootloader.</td>
          <td><code class="code-inline">shimx64.efi</code> / <code class="code-inline">pxelinux.0</code> / <code class="code-inline">bootmgfw.efi</code></td>
        </tr>
        <tr>
          <td><strong>4. Secure Boot Verification</strong></td>
          <td>UEFI Crypto Core</td>
          <td>UEFI verifies Microsoft 3rd Party UEFI CA signature on Shim loader before transferring control.</td>
          <td>Hardware Root of Trust validated</td>
        </tr>
        <tr>
          <td><strong>5. Second-Stage Kernel Pull</strong></td>
          <td>HTTP / TFTP (Port 80/69)</td>
          <td>Bootloader fetches full OS kernel and initial RAM filesystem (initrd / WIM) over fast HTTP.</td>
          <td><code class="code-inline">vmlinuz</code> + <code class="code-inline">initrd.img</code> / <code class="code-inline">boot.wim</code></td>
        </tr>
        <tr>
          <td><strong>6. Unattended Execution</strong></td>
          <td>HTTPS / NFS / SMB</td>
          <td>Installer kernel executes automated answer file (<code class="code-inline">autounattend.xml</code> or <code class="code-inline">ks.cfg</code>) without human intervention.</td>
          <td>Disk partition, OS install, domain join</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 7: DISK PARTITIONING & FILESYSTEM ARCHITECTURES -->
<article class="doc-page" id="s2-partitioning">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Installation &amp; Virtualization • Article 07</span>
    <h2 class="section-title"><span class="sec-num">07</span> Disk Partitioning, Volume Management &amp; Resilient File Systems</h2>
    <p class="lead-para">
      Enterprise storage structures must support dynamic expansion, snapshots, and protection against bit-rot. Mastering the differences between GUID Partition Tables (GPT), Master Boot Record (MBR), Logical Volume Management (LVM), and modern resilient filesystems (ReFS / XFS) is paramount.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. MBR vs GPT Partitioning Schemes</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Feature</th>
          <th>Master Boot Record (MBR)</th>
          <th>GUID Partition Table (GPT)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Addressing Scheme</strong></td>
          <td>32-bit Logical Block Addressing (LBA)</td>
          <td>64-bit Logical Block Addressing (LBA)</td>
        </tr>
        <tr>
          <td><strong>Maximum Volume Capacity</strong></td>
          <td><strong>2.19 TB (2.2 TiB)</strong> (\(2^{32} \times 512\text{ bytes}\))</td>
          <td><strong>9.4 ZB (9.4 Zettabytes)</strong> (\(2^{64} \times 512\text{ bytes}\))</td>
        </tr>
        <tr>
          <td><strong>Maximum Partitions</strong></td>
          <td>4 Primary (or 3 Primary + 1 Extended with logical drives)</td>
          <td>128 Primary Partitions (Windows default) or unlimited</td>
        </tr>
        <tr>
          <td><strong>Redundancy &amp; Integrity</strong></td>
          <td>Single sector at LBA 0; if sector is corrupted, entire disk partition table is lost</td>
          <td>Primary GPT at LBA 1; Backup GPT stored at the very end of the physical disk; CRC32 checksums</td>
        </tr>
        <tr>
          <td><strong>Firmware Compatibility</strong></td>
          <td>Legacy BIOS &amp; CSM</td>
          <td>Mandatory for native UEFI &amp; Secure Boot</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="shield-check"></i> RESILIENT FILE SYSTEM (ReFS) VS NEW TECHNOLOGY FILE SYSTEM (NTFS)</div>
    <div class="callout-body">
      Microsoft introduced <strong>ReFS (Resilient File System)</strong> to eliminate the legacy limitations of NTFS in massive virtualization and Hyper-V deployments:
      <ul style="margin-left: 1.2rem; margin-top: 0.5rem; line-height: 1.8;">
        <li><strong>Automatic Integrity Scrubber:</strong> ReFS pairs with Storage Spaces to perform continuous background data scrubbing. When data corruption (bit-rot) is detected via 64-bit checksums, ReFS automatically reads an alternate healthy copy from parity/mirror disks and heals the damaged block without taking the volume offline.</li>
        <li><strong>Accelerated VHDX Operations:</strong> ReFS supports <em>Block Cloning</em> (converting copy operations into metadata references, duplicating a 50GB VM virtual disk in sub-second time) and <em>Sparse VHDX Zeroing</em> (instantly creating fixed-size virtual disks without zeroing physical sectors).</li>
      </ul>
    </div>
  </div>
</article>

<!-- ARTICLE 8: TYPE-1 HYPERVISOR ARCHITECTURE -->
<article class="doc-page" id="s2-virt">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Installation &amp; Virtualization • Article 08</span>
    <h2 class="section-title"><span class="sec-num">08</span> Type-1 Bare-Metal Hypervisors: Architecture &amp; vCPU Scheduling</h2>
    <p class="lead-para">
      Enterprise virtualization relies exclusively on Type-1 (Bare Metal) hypervisors (VMware ESXi VMkernel, Microsoft Hyper-V, and Linux KVM) that execute directly on physical processor rings, providing hardware abstraction, memory isolation, and deterministic multi-tenant execution.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Type-1 Bare-Metal vs Type-2 Hosted Architecture</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Attribute</th>
          <th>Type-1 Bare-Metal (ESXi, Hyper-V, KVM)</th>
          <th>Type-2 Hosted (VirtualBox, VMware Workstation)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Execution Layer</strong></td>
          <td>Boots directly on physical bare-metal silicon; owns hardware rings</td>
          <td>Executes as a standard user-space application inside a host operating system (Windows/macOS/Linux)</td>
        </tr>
        <tr>
          <td><strong>Ring Privilege</strong></td>
          <td>Runs in VMX Root Operation (Ring 0 / Hypervisor mode)</td>
          <td>Runs in Ring 3 (User Space); traps must be handled by Host OS kernel</td>
        </tr>
        <tr>
          <td><strong>Context Switch Overhead</strong></td>
          <td>Sub-microsecond direct hardware scheduling; near-zero jitter</td>
          <td>Double context switching: Guest &rarr; Host OS Kernel &rarr; Virtualizer &rarr; CPU</td>
        </tr>
        <tr>
          <td><strong>Hardware Compatibility</strong></td>
          <td>Requires certified server hardware on vendor HCL (Hardware Compatibility List)</td>
          <td>Runs on any standard PC hardware supported by host OS</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="layers"></i> MICROSOFT HYPER-V PARTITION ARCHITECTURE</div>
    <div class="callout-body">
      Under Hyper-V, the parent operating system is NOT running on bare metal!
      <ul style="margin-left: 1.2rem; margin-top: 0.5rem; line-height: 1.8;">
        <li><strong>The Microkernel Hypervisor:</strong> Boots first at ring -1, seizing control of physical CPU and IOMMU hardware.</li>
        <li><strong>Management (Parent) Partition:</strong> Windows Server boots inside a privileged virtual machine (Parent Partition) that owns the hardware device drivers and power management stack.</li>
        <li><strong>Child Partitions (Guest VMs):</strong> Run worker workloads. Network and disk I/O are transmitted from Child to Parent via the <strong>VMBus</strong> high-speed in-memory channel using synthetic Virtual Service Clients (VSC) and Virtual Service Providers (VSP), avoiding slow legacy device emulation.</li>
      </ul>
    </div>
  </div>
</article>

<!-- ARTICLE 9: MEMORY MANAGEMENT & BALLOONING -->
<article class="doc-page" id="s2-memory-ballooning">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Installation &amp; Virtualization • Article 09</span>
    <h2 class="section-title"><span class="sec-num">09</span> Virtual Memory Management, Balloon Drivers &amp; Overcommitment Math</h2>
    <p class="lead-para">
      Memory is frequently the most constrained and expensive physical asset in enterprise virtualization. Hypervisors employ sophisticated overcommitment algorithms—Transparent Page Sharing (TPS), Memory Ballooning, Hyper-V Dynamic Memory, and Hypervisor Paging—to safely allocate more RAM than physically exists.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. The Lifecycle of Memory Ballooning (vmmemctl)</h3>
  <p>
    When a physical host encounters memory contention (e.g., Free RAM drops below 6%), the hypervisor must reclaim RAM without abruptly crashing virtual machines:
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Phase</th>
          <th>Component</th>
          <th>Action &amp; Memory Transfer Flow</th>
          <th>Host Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Contention Detection</strong></td>
          <td>Hypervisor VMkernel</td>
          <td>Calculates that total VM demand exceeds physical capacity; sends reclamation target to VM balloon driver.</td>
          <td>Physical host free RAM &lt; 6%</td>
        </tr>
        <tr>
          <td><strong>2. Balloon Inflation</strong></td>
          <td>Guest Balloon Driver (<code class="code-inline">vmmemctl.sys</code>)</td>
          <td>Driver requests non-paged pool memory allocations from the Guest OS kernel (e.g. 4GB).</td>
          <td>Balloon expands inside guest</td>
        </tr>
        <tr>
          <td><strong>3. Guest OS Paging</strong></td>
          <td>Guest Virtual Memory Manager</td>
          <td>Guest OS sees memory pressure and intelligently pages idle user-space data out to its own internal swap file (<code class="code-inline">pagefile.sys</code>).</td>
          <td>Guest OS decides which pages are least important</td>
        </tr>
        <tr>
          <td><strong>4. Host Physical Pinning</strong></td>
          <td>Hypervisor Memory Allocator</td>
          <td>Guest driver communicates the physical backing addresses of the inflated balloon to the hypervisor; hypervisor reclaims those physical host RAM pages for other VMs!</td>
          <td>Physical host recovers free RAM</td>
        </tr>
        <tr>
          <td><strong>5. Balloon Deflation</strong></td>
          <td>Guest Balloon Driver</td>
          <td>When host contention subsides, hypervisor releases pages; balloon deflates, returning RAM to the guest operating system.</td>
          <td>Normal baseline restored</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 10: VIRTUAL NETWORKING & SWITCHES -->
<article class="doc-page" id="s2-virtual-networking">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Installation &amp; Virtualization • Article 10</span>
    <h2 class="section-title"><span class="sec-num">10</span> Virtual Networking: Virtual Switches, VLAN Tagging &amp; SR-IOV</h2>
    <p class="lead-para">
      Virtual switches (vSwitch) form the software-defined connectivity layer inside the hypervisor, bridging virtual machine network adapters (vNICs) to physical host NICs (uplinks) while enforcing Layer 2 security, 802.1Q VLAN isolation, and traffic shaping policies.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Standard vs Distributed Virtual Switches</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Capability</th>
          <th>Standard Virtual Switch (vSS)</th>
          <th>Distributed Virtual Switch (vDS)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Configuration Scope</strong></td>
          <td>Configured independently on every individual ESXi host node</td>
          <td>Centralized control plane configured across the entire vCenter datacenter cluster</td>
        </tr>
        <tr>
          <td><strong>vMotion Port Consistency</strong></td>
          <td>Port group names and VLAN IDs must be manually matched letter-for-letter on every host</td>
          <td>Port state, runtime statistics, and active firewall filters migrate with the VM across hosts!</td>
        </tr>
        <tr>
          <td><strong>Advanced Features</strong></td>
          <td>Basic VLAN tagging, NIC teaming, outbound traffic shaping</td>
          <td>NetFlow / IPFIX, port mirroring (SPAN/ERSPAN), bidirectional QoS, LACP teaming</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="network"></i> VLAN TAGGING MODES: EST VS VST VS VGT</div>
    <div class="callout-body">
      <ul style="margin-left: 1.2rem; line-height: 1.8;">
        <li><strong>External Switch Tagging (EST):</strong> VLAN tagging occurs on the physical top-of-rack switch. The vSwitch receives untagged frames (Access Mode).</li>
        <li><strong>Virtual Switch Tagging (VST - Enterprise Standard):</strong> The physical switch port is a Trunk (802.1Q). The vSwitch inspects and strips/appends 802.1Q VLAN tags based on Port Group assignments. Guest VMs remain completely unaware of VLANs.</li>
        <li><strong>Virtual Guest Tagging (VGT):</strong> The vSwitch passes raw 802.1Q tagged frames directly into the VM vNIC. The guest operating system must have a VLAN-aware driver (e.g. running a virtual pfSense router or firewall).</li>
      </ul>
    </div>
  </div>
</article>

<!-- UNIT 2 PRACTICE BANK: 30 MCQS -->
<article class="doc-page" id="practice-mcq-s2">
  <div class="page-header-meta">
    <span class="meta-tag">Server Administration • Unit 02</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreS2">Score: 0 / 30</span>
  </div>
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Assessment • Practice Bank</span>
    <h2 class="section-title"><span class="sec-num">Q1</span> Unit 2 Practice Bank: 30 Interactive Examination MCQs</h2>
    <p class="lead-para">
      Comprehensive assessment questions matching CompTIA Server+ and Microsoft Windows Server certification standards.
    </p>
  </header>

  <div class="callout callout-deep" style="margin-bottom: 2rem;">
    <div class="callout-label"><i data-lucide="award"></i> REAL-TIME SCORE ENGINE</div>
    <div class="callout-body">
      Select your answer for each question. Instant feedback will highlight correct answers in green and explanations will appear automatically.
    </div>
  </div>

  <!-- MCQ 1 -->
  <div class="mcq-card" data-unit="s2" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q1</span>
      <div class="mcq-question-text">During a PXE network installation, what DHCP option code is utilized to specify the IP address or hostname of the TFTP boot server to the client machine?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Option 3 (Default Router)</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Option 66 (TFTP Server Name / Next Server)</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Option 15 (Domain Name)</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Option 81 (Client FQDN)</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B (Option 66).</strong> DHCP Option 66 specifies the TFTP boot server IP or hostname, while DHCP Option 67 specifies the exact bootfile name (e.g., <code class="code-inline">bootx64.efi</code>).
    </div>
  </div>

  <!-- MCQ 2 -->
  <div class="mcq-card" data-unit="s2" data-correct="D">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q2</span>
      <div class="mcq-question-text">Why cannot an administrator create a single partition larger than 2.2 Terabytes on a drive formatted with a standard Master Boot Record (MBR) partition table using 512-byte sectors?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> SATA cables only have 32 pins, limiting the maximum byte throughput.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The NTFS file system cannot support numbers higher than 2 billion.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Disk read heads cannot physically travel across more than 2,000 cylinders.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> MBR stores sector addresses in a 32-bit field (\(2^{32} \times 512\text{ bytes} \approx 2.19\text{ TB}\)).</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: D.</strong> The 32-bit Logical Block Addressing (LBA) field in the MBR partition table cannot address sector counts beyond \(2^{32}-1\). Volumes larger than 2.19TB mandate GUID Partition Table (GPT), which utilizes a 64-bit addressing field.
    </div>
  </div>

  <!-- MCQ 3 -->
  <div class="mcq-card" data-unit="s2" data-correct="A">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q3</span>
      <div class="mcq-question-text">Which memory management technique relies on an in-guest driver to artificially inflate and force the guest operating system's internal virtual memory manager to page idle memory to disk?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Memory Ballooning (e.g., VMware vmmemctl)</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Transparent Page Sharing (TPS)</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Hypervisor Direct Swapping</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Second Level Address Translation (SLAT)</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: A.</strong> Memory ballooning runs inside the guest kernel. When instructed by the hypervisor, it consumes guest RAM, forcing the guest OS to page its own least-recently-used pages to its own pagefile. The hypervisor then safely claims the physical pages backing the balloon.
    </div>
  </div>

  <!-- MCQ 4 -->
  <div class="mcq-card" data-unit="s2" data-correct="C">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q4</span>
      <div class="mcq-question-text">In Microsoft Hyper-V architecture, how do Child Partitions (Guest VMs) communicate with the hardware storage and network controllers owned by the Parent Partition?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Via legacy IDE and Intel PRO/1000 PCI bus emulation in software.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Across an external physical crossover Ethernet cable plugged into the server rear.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Through synthetic Virtual Service Clients (VSC) communicating across the VMBus in-memory channel.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> By executing BIOS interrupt 13h calls directly to the motherboard chipset.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: C.</strong> Hyper-V child partitions use synthetic drivers (VSCs) that communicate directly with the Parent Partition's Virtual Service Providers (VSPs) over the high-speed shared-memory **VMBus**, completely avoiding slow device emulation.
    </div>
  </div>

  <!-- MCQ 5 -->
  <div class="mcq-card" data-unit="s2" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q5</span>
      <div class="mcq-question-text">What feature of Microsoft ReFS (Resilient File System) allows creating a 100GB fixed-size virtual hard disk (.vhdx) in less than one second?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> BitLocker hardware bypass</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Accelerated VHDX Operations via Sparse File Zeroing &amp; Block Cloning metadata manipulation</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Disabling all disk checksumming completely</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Overclocking the SAS HBA PCIe bus</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B.</strong> ReFS supports Accelerated VHDX operations: it allocates and marks sectors in metadata without executing costly, synchronous physical zero writes across the storage medium.
    </div>
  </div>

  <!-- MCQs 6 to 30 concise cards -->
  <div class="mcq-card" data-unit="s2" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q6</span><div class="mcq-question-text">In enterprise virtual networking, what is the default and most common VLAN tagging mode where the virtual switch strips and appends 802.1Q tags before delivery to VMs?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Virtual Switch Tagging (VST)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> External Switch Tagging (EST)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Virtual Guest Tagging (VGT)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Dynamic Trunking Protocol (DTP)</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> VST allows the hypervisor vSwitch to handle all 802.1Q tagging on trunked uplinks, presenting clean, untagged Ethernet frames to guest virtual machines based on port groups.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q7</span><div class="mcq-question-text">Which hardware virtualization feature in AMD processors provides Second Level Address Translation (SLAT), offloading shadow page table management to CPU hardware?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Intel VT-d</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Extended Page Tables (EPT)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Nested Page Tables (NPT) / Rapid Virtualization Indexing (RVI)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Hyper-Threading</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> AMD's SLAT implementation is known as Nested Page Tables (NPT). Intel's equivalent is Extended Page Tables (EPT). Both eliminate the high overhead of software shadow page tables.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q8</span><div class="mcq-question-text">What command on an enterprise Linux server formats a block device with the high-performance XFS filesystem?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> format /fs:xfs /dev/sdb1</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> dd if=/dev/zero of=/dev/sdb1</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> fdisk --mkfs-xfs /dev/sdb1</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> mkfs.xfs /dev/sdb1</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> The standard Linux command is <code class="code-inline">mkfs.xfs &lt;device&gt;</code>, which initializes the XFS allocation groups and log files.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q9</span><div class="mcq-question-text">Why is Single Root I/O Virtualization (SR-IOV) selected for ultra-low latency workloads instead of standard virtual switches?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> SR-IOV compresses network packets by 50% using gzip.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> SR-IOV bypasses the hypervisor virtual switch entirely, mapping a hardware Virtual Function (VF) directly to the VM memory space via DMA.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> SR-IOV allows running Wi-Fi networks over copper server backplanes.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> SR-IOV eliminates the requirement for physical NIC cards.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> SR-IOV divides a physical PCIe device into multiple Virtual Functions (VFs) mapped directly into the VM via IOMMU, bypassing the hypervisor network stack to achieve sub-microsecond latency.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q10</span><div class="mcq-question-text">In a Kickstart automated Linux installation, which configuration file defines disk partitioning, root passwords, packages, and post-installation scripts?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ks.cfg</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> autounattend.xml</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> boot.ini</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> install.wim</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Red Hat / CentOS / Rocky Linux automated deployments utilize <code class="code-inline">ks.cfg</code> (Kickstart). Windows automated installations utilize <code class="code-inline">autounattend.xml</code>.</div></div>

  <!-- MCQs 11 to 30 -->
  <div class="mcq-card" data-unit="s2" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q11</span><div class="mcq-question-text">What is the primary architectural purpose of a VMware Distributed Virtual Switch (vDS) compared to a Standard Virtual Switch (vSS)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> vDS is free, whereas vSS requires an enterprise license.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> vDS only operates over 1Gbps copper cables.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> vDS maintains centralized cluster-wide network management and preserves port runtime states during vMotion migrations.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> vDS eliminates the requirement for physical network cards.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> A vDS acts as a single centralized virtual switch across hundreds of hosts, ensuring port policies, traffic shaping, and NetFlow stats travel seamlessly with the VM during vMotion.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q12</span><div class="mcq-question-text">What is the function of the ESP (EFI System Partition) on a GPT-partitioned boot drive?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Stores user desktop files and browser cache.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A FAT32 partition containing signed EFI bootloaders, device drivers, and diagnostic utilities executed by UEFI before OS load.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> A hidden encrypted space used exclusively by BitLocker to store TPM keys.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> An emergency virtual swap file used when RAM fails.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> The EFI System Partition (ESP) is formatted in FAT32 (or FAT16) and holds bootloaders (<code class="code-inline">\EFI\BOOT\BOOTX64.EFI</code>) loaded directly by the motherboard UEFI firmware.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q13</span><div class="mcq-question-text">Which Windows Server role enables deploying Windows operating systems across the network to bare-metal servers using PXE?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Active Directory Certificate Services (AD CS)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Remote Access Service (RAS)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Network Policy Server (NPS)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Windows Deployment Services (WDS)</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Windows Deployment Services (WDS) integrates with DHCP and TFTP to deploy Windows images (<code class="code-inline">boot.wim</code> and <code class="code-inline">install.wim</code>) to PXE clients.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q14</span><div class="mcq-question-text">In Linux Logical Volume Manager (LVM), what is the correct hierarchical order of storage abstraction from raw disk to formatted filesystem?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Physical Volumes (PV) &rarr; Volume Group (VG) &rarr; Logical Volumes (LV) &rarr; Filesystem</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Logical Volume &rarr; Physical Volume &rarr; Volume Group &rarr; Filesystem</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Volume Group &rarr; Physical Volume &rarr; Logical Volume &rarr; Filesystem</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Filesystem &rarr; Volume Group &rarr; Logical Volume &rarr; Physical Volume</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Raw disk partitions are initialized as Physical Volumes (<code class="code-inline">pvcreate</code>), pooled into a Volume Group (<code class="code-inline">vgcreate</code>), carved into Logical Volumes (<code class="code-inline">lvcreate</code>), and formatted with a filesystem (<code class="code-inline">mkfs</code>).</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q15</span><div class="mcq-question-text">What is the severe operational risk of configuring Hypervisor Swapping (Host-level Paging) as a routine method to handle memory overcommitment?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It permanently erases the virtual machine's product key.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It burns out the CPU core voltage regulators within 30 minutes.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Catastrophic performance degradation: swapping guest RAM to disk introduces millisecond disk latency (100,000x slower than RAM), causing guest OS freezes.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Hypervisor swapping violates PCI-DSS regulations.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> The hypervisor has no awareness of which guest pages are active vs idle. Hypervisor swapping indiscriminately writes active guest kernel structures to disk, inducing catastrophic performance thrashing.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q16</span><div class="mcq-question-text">Which CPU technology in Intel processors maps physical PCIe device DMA requests directly into virtual machine memory addresses without hypervisor emulation?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Intel SpeedStep</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Intel VT-d (Virtualization Technology for Directed I/O) / IOMMU</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Intel Turbo Boost Max</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Intel QuickPath Interconnect</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Intel VT-d (IOMMU) translates DMA memory addresses directly for guest VMs, providing hardware isolation and enabling direct PCIe pass-through and SR-IOV.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q17</span><div class="mcq-question-text">What is the function of the "Dynamic Memory" feature in Microsoft Hyper-V?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Reclaims idle memory from one VM and allocates it to VMs experiencing workload surges within configured Startup, Minimum, and Maximum bounds.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Overclocks the RAM clock speed during heavy database transactions.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Compresses network packets before saving to disk.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Mirrors the VM RAM to an external USB drive in real time.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Hyper-V Dynamic Memory treats physical RAM as a fluid pool, adjusting allocation between configured Minimum and Maximum limits via ballooning and synthetic memory hot-add.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q18</span><div class="mcq-question-text">When configuring a static IP on a newly installed Linux enterprise server via NetworkManager CLI, what command is used?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ipconfig /all /static 10.0.1.10</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> netsh interface ipv4 set address</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> route add default gw 10.0.1.1</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> nmcli connection modify eth0 ipv4.addresses 10.0.1.10/24 ipv4.gateway 10.0.1.1 ipv4.method manual</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Modern enterprise Linux (RHEL 8/9, Rocky, Alma) uses <code class="code-inline">nmcli</code> to manipulate connection profiles persistently in NetworkManager.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q19</span><div class="mcq-question-text">Why must UEFI Secure Boot verify the cryptographic signature of the bootloader file during initial startup?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> To ensure the user has paid for their Windows license.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> To prevent the computer from connecting to public Wi-Fi.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> To prevent rootkits and bootkits from injecting malicious code before the operating system kernel and security drivers initialize.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> To test the speed of the NVMe drive.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Secure Boot verifies signatures against trusted keys in the UEFI firmware database (db), blocking unauthorized bootkits and rootkits from compromising the pre-boot chain.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q20</span><div class="mcq-question-text">What command on an enterprise Linux server dynamically resizes an XFS filesystem after expanding the underlying LVM logical volume?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> resize2fs /dev/vg0/lv_data</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> xfs_growfs /mountpoint</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> ntfsresize /dev/vg0/lv_data</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> chkdsk /f /r</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> XFS file systems are grown while mounted using <code class="code-inline">xfs_growfs &lt;mountpoint&gt;</code>. Note that <code class="code-inline">resize2fs</code> is exclusively used for ext4 filesystems.</div></div>

  <!-- MCQs 21 to 30 -->
  <div class="mcq-card" data-unit="s2" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q21</span><div class="mcq-question-text">What is the key benefit of VMware vSphere vMotion live migration?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Migrates an active, powered-on virtual machine from one physical ESXi host to another with zero downtime or service interruption.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Converts Windows Server VMs into Linux containers automatically.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Backs up virtual machines to magnetic tape.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Overclocks the target host processor to 6.0 GHz.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> vMotion copies the VM's active RAM state over a dedicated high-speed vMotion network while tracking dirty pages in a memory bitmap, freezing the VM for only milliseconds during the final handover.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q22</span><div class="mcq-question-text">What virtual disk format supports up to 64 Terabytes, provides power failure resilience, and is the standard for modern Hyper-V generation 2 VMs?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> .vhd</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> .qcow2</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> .iso</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> .vhdx</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> The <code class="code-inline">.vhdx</code> format expanded capacity to 64TB (legacy <code class="code-inline">.vhd</code> was capped at 2TB) and incorporates internal log structures to prevent metadata corruption during power outages.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q23</span><div class="mcq-question-text">What is "Transparent Page Sharing" (TPS) in hypervisor memory management?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Broadcasting RAM contents to other servers over Wi-Fi.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Identifying identical memory pages across virtual machines (e.g. identical OS kernel code), consolidating them into a single physical read-only page, and using Copy-on-Write for modifications.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Writing memory directly to public cloud storage.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Allowing non-admin users to view other VMs' passwords.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> TPS scans memory hashes: identical pages are mapped to a single physical frame with Copy-on-Write (COW) semantics, deduplicating hundreds of identical OS pages.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q24</span><div class="mcq-question-text">Which PowerShell cmdlet is used on Windows Server to install the Hyper-V role and management tools?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Get-WindowsFeature Hyper-V</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachine</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Set-VMProcessor -ExposeVirtualizationExtensions $true</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> <code class="code-inline">Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart</code> installs the hypervisor, management GUI, PowerShell module, and schedules the required reboot.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q25</span><div class="mcq-question-text">What is the consequence of configuring a virtual machine with more vCPUs than physical processor cores on a single NUMA node ("vCPU overcommitment")?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> CPU Ready Time (%RDY) spikes, as the hypervisor scheduler must wait for multiple physical cores to become available simultaneously before co-scheduling the VM.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The physical CPU will catch fire due to excessive clock cycles.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The virtual machine is restricted to 10Mbps network throughput.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The hypervisor automatically deletes the VM.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Over-allocating vCPUs causes co-scheduling bottlenecks: the hypervisor scheduler must align physical cores concurrently, inducing high CPU Ready (%RDY) wait times.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q26</span><div class="mcq-question-text">What is the function of the "Hardware Compatibility List" (HCL) published by enterprise hypervisor vendors?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A price guide for purchasing consumer graphics cards.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A list of open-source software packages that are banned in the datacenter.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> A list of gaming motherboards that support overclocking.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> An authoritative catalog of certified servers, processors, RAID controllers, and NICs tested and officially supported by the hypervisor kernel.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> The HCL (or VMware Compatibility Guide) certifies that specific firmware revisions, storage HBAs, and NICs have verified, stable driver modules for the hypervisor kernel.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q27</span><div class="mcq-question-text">What is the function of an "Unattended Answer File" (e.g. autounattend.xml) during automated server operating system installations?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Answers technical support tickets sent by end users.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Provides pre-defined answers to setup prompts (locale, partition layout, administrator password, domain join), enabling zero-touch OS installation.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Generates automated sales quotes for datacenter hardware.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Automatically reboots the server every 24 hours.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Unattended answer files supply configuration variables directly to the OS setup engine (<code class="code-inline">setup.exe</code> or Anaconda), automating disk formatting, timezone selection, and post-install scripts.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q28</span><div class="mcq-question-text">What technology allows passing an entire physical NVMe drive or SAS LUN directly to a guest virtual machine, bypassing hypervisor filesystem virtualization?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> NFS Share</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> SMB 3.0 Share</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Raw Device Mapping (RDM) / Pass-through Disk</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> FAT32 format</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Raw Device Mapping (VMware RDM or Hyper-V Pass-Through Disk) allows the guest OS to communicate SCSI commands directly to physical storage LUNs.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q29</span><div class="mcq-question-text">Why must virtual machine guest integration tools (VMware Tools / Hyper-V Integration Services) be installed inside every virtual machine?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Installs optimized synthetic device drivers (network, storage), memory ballooning agents, clock synchronization, and clean OS shutdown capabilities.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Disables the Windows firewall and antivirus.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Enables BitTorrent downloads on the guest.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Increases physical RAM on the motherboard.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Guest tools provide synthetic VMXNET3/VMBus drivers, the balloon driver (<code class="code-inline">vmmemctl</code>), heartbeat signals, time synchronization with host clocks, and graceful shutdown orchestration.</div></div>

  <div class="mcq-card" data-unit="s2" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q30</span><div class="mcq-question-text">In enterprise virtualization, what is "Nested Virtualization"?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Placing a physical blade chassis inside a shipping crate.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Running multiple versions of Microsoft Office simultaneously.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Storing backup tapes inside a fireproof safe.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Exposing hardware virtualization extensions (VT-x / AMD-V) to a guest VM, allowing a hypervisor (such as Hyper-V, ESXi, or KVM) to run inside a virtual machine.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Nested virtualization passes CPU virtualization instructions (VMX root) into guest VMs, enabling development labs, Windows Subsystem for Linux (WSL2), and virtual hypervisors.</div></div>

</article>

<!-- UNIT 2 SUBJECTIVE SHORT CONCEPTUAL Q&A (5M) -->
<article class="doc-page" id="practice-subj-short-s2">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Assessment • Conceptual Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q2</span> Conceptual Review Questions (5 Marks Each)</h2>
    <p class="lead-para">
      Five focused technical problems evaluating PXE boot stages, GPT vs MBR limits, Type-1 hypervisor architecture, memory ballooning mechanics, and virtual switch tagging.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q1: Detail the step-by-step handshake and protocol sequence of a PXE network boot.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ol style="margin-left: 1.2rem; line-height: 1.8;">
        <li><strong>DHCP Discovery:</strong> The client NIC broadcasts a DHCPDISCOVER frame containing PXE-specific vendor options (Option 93 architecture tags).</li>
        <li><strong>DHCP Offer &amp; PXE Tags:</strong> The DHCP server replies with an IP address, subnet mask, Option 66 (TFTP Next Server IP), and Option 67 (Bootfile Name, e.g. <code class="code-inline">bootx64.efi</code>).</li>
        <li><strong>TFTP Bootloader Download:</strong> The client contacts the TFTP server over UDP port 69 and downloads the initial EFI network bootloader (<code class="code-inline">shimx64.efi</code>).</li>
        <li><strong>Secure Boot Verification:</strong> UEFI validates the cryptographic digital signature on the bootloader against authorized certificates in the firmware DB.</li>
        <li><strong>Second-Stage Kernel Fetch:</strong> The bootloader downloads the OS kernel (<code class="code-inline">vmlinuz</code>) and RAM filesystem (<code class="code-inline">initrd.img</code>) via HTTP/TFTP and transfers execution to the OS installer.</li>
      </ol>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q2: Why does Master Boot Record (MBR) fail on drives exceeding 2.2 Terabytes, and how does GPT resolve this?</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> MBR stores sector addresses in a fixed 32-bit integer field. Using standard 512-byte sector sizing, the maximum addressable sector space is \(2^{32} \times 512\text{ bytes} = 2,199,023,255,552\text{ bytes} \approx \mathbf{2.19\text{ TB}}\). Any capacity beyond 2.19TB cannot be addressed and remains unusable.</p>
      <p>GPT (GUID Partition Table) utilizes 64-bit Logical Block Addressing (LBA), enabling addressable storage capacity up to \(2^{64} \times 512\text{ bytes} \approx \mathbf{9.4\text{ Zettabytes}}\). Furthermore, GPT stores redundant backup partition headers at the end of the physical disk with CRC32 checksums for integrity verification.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q3: Explain the architectural interaction between Hyper-V Parent Partition, Child Partitions, and the VMBus.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> Hyper-V boots a microkernel hypervisor at the lowest ring level. It designates the primary Windows Server instance as the <strong>Parent Partition</strong>, which owns physical hardware drivers. Guest VMs execute inside isolated <strong>Child Partitions</strong>. Rather than emulating slow legacy PCI hardware devices, guest VMs utilize synthetic Virtual Service Clients (VSC) that pass network, storage, and video requests across an optimized, high-speed shared memory bus called the <strong>VMBus</strong> directly to Virtual Service Providers (VSP) in the Parent Partition.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q4: Trace the operational phases of Memory Ballooning during physical host memory contention.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ol style="margin-left: 1.2rem; line-height: 1.8;">
        <li>When host physical memory falls below a critical threshold (&lt;6%), the hypervisor instructs the in-guest balloon driver (<code class="code-inline">vmmemctl</code>) to inflate.</li>
        <li>The balloon driver requests memory allocations from the guest operating system kernel.</li>
        <li>The guest OS experiences internal memory pressure and intelligently pages idle, least-recently-used application pages out to its own swap/pagefile.</li>
        <li>The balloon driver locks these newly allocated guest memory pages and notifies the hypervisor of their backing physical addresses.</li>
        <li>The hypervisor de-allocates the underlying physical host RAM frames and reassigns them to active virtual machines, relieving host contention without crashing VMs.</li>
      </ol>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q5: Contrast Virtual Switch Tagging (VST) with Virtual Guest Tagging (VGT) in enterprise virtualization.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Virtual Switch Tagging (VST):</strong> The physical switch port is configured as an 802.1Q trunk. The hypervisor virtual switch receives the tagged frames, strips the 802.1Q VLAN header, and delivers clean, untagged Ethernet frames to the assigned Port Group. The guest VM is completely unaware of VLAN configurations. This is the industry standard for 99% of workloads.</li>
        <li><strong>Virtual Guest Tagging (VGT):</strong> The virtual switch forwards raw 802.1Q tagged frames directly into the virtual machine's vNIC (VLAN ID set to 4095 in VMware). The guest OS itself must run a VLAN-aware network stack to parse tags, typically required for virtual firewalls, routers, or multi-tenant network probes.</li>
      </ul>
    </div>
  </div>
</article>

<!-- UNIT 2 SUBJECTIVE LONG SCENARIOS (10M) -->
<article class="doc-page" id="practice-subj-long-s2">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Assessment • Scenario Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q3</span> Architectural &amp; Triage Scenarios (10 Marks Each)</h2>
    <p class="lead-para">
      Enterprise scenarios requiring automated mass deployment architecture, hypervisor CPU ready time triage, and storage volume recovery.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 1: Diagnosing Severe Virtual Machine Freezes Due to CPU Ready Time (%RDY) Spikes</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A junior administrator provisions a 4-node ESXi virtualization cluster. To "maximize performance," they configure every virtual machine with 16 vCPUs. The physical hosts feature dual 12-core CPUs (24 physical cores total per host). Soon after launch, users report that VMs frequently freeze and lag, even though average CPU utilization inside the guest OS is only 20%.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> DIAGNOSTIC ROOT CAUSE &amp; REMEDIATION PLAN</div>
        <div class="callout-body">
          <ol style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Root Cause Identification (Co-Scheduling Bottleneck):</strong> Modern hypervisors use relaxed co-scheduling. When a VM is assigned 16 vCPUs, the hypervisor CPU scheduler must wait until 16 physical cores are simultaneously idle and available before scheduling a clock tick across all 16 execution threads. Because 16 cores represents 66% of the host's entire physical core count (24 cores), multiple 16-vCPU VMs contend fiercely for simultaneous core availability.</li>
            <li><strong>Metric Verification:</strong> Inspect <code class="code-inline">esxtop</code>. The <strong>%RDY (CPU Ready Time)</strong> metric exceeds 10% (normal baseline is &lt;2%). This indicates VMs are ready to execute instructions but are blocked waiting for physical CPU time slices.</li>
            <li><strong>Remediation Strategy:</strong> Right-size the virtual machines. Downscale the VMs from 16 vCPUs to 4 vCPUs (or 2 vCPUs) matching actual workload demand. With only 4 vCPUs to co-schedule, the hypervisor easily satisfies CPU requests across the 24 physical cores. CPU Ready (%RDY) will immediately collapse from &gt;10% to &lt;1%, eliminating VM lag and restoring fluid responsiveness.</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 2: Automated Mass Deployment Architecture for 200 Bare-Metal Edge Servers</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> An enterprise must provision 200 new 1U rack servers deployed across regional datacenters with identical Red Hat Enterprise Linux 9 installations, hardened storage partitions (LVM, encrypted swap, separate <code class="code-inline">/var/log</code>), and security policies, without manual technician keyboard input.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="check-check"></i> AUTOMATED ZERO-TOUCH PROVISIONING BLUEPRINT</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Network Boot Pipeline:</strong> Configure a centralized PXE server with DHCP, TFTP, and NGINX HTTP services. DHCP Option 66 points to the PXE server; Option 67 serves <code class="code-inline">shimx64.efi</code>.</li>
            <li><strong>Declarative Kickstart (<code class="code-inline">ks.cfg</code>):</strong> Host the automated Kickstart recipe on an internal HTTPS server. The file specifies:
              <pre class="code-block"><code class="language-bash"># Partition clearing and GPT initialization
zerombr
clearpart --all --initlabel
# EFI System Partition
part /boot/efi --fstype=efi --size=600
part /boot --fstype=xfs --size=1024
# LVM Volume Group and Logical Volumes
part pv.01 --size=1 --grow
volgroup rhel pv.01
logvol / --vgname=rhel --size=51200 --name=root --fstype=xfs
logvol /var/log --vgname=rhel --size=20480 --name=var_log --fstype=xfs
logvol /var/log/audit --vgname=rhel --size=10240 --name=audit --fstype=xfs
logvol swap --vgname=rhel --size=16384 --name=swap --fstype=swap</code></pre>
            </li>
            <li><strong>Post-Install Hardening Script:</strong> The <code class="code-inline">%post</code> script disables root SSH password authentication, injects DevOps public SSH keys, enables FirewallD, and registers the server with Red Hat Satellite.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 3: Resolving Hypervisor Memory Thrashing &amp; Emergency Swapping Outage</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> An ESXi host containing 128GB of physical RAM is hosting 8 virtual machines, each configured with 24GB of RAM (total 192GB provisioned = 1.5x overcommit). A memory leak in one VM causes physical host free RAM to drop to 1%. The hypervisor begins host-level swapping to local disk, causing all 8 VMs to freeze.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> EMERGENCY INCIDENT REMEDIATION</div>
        <div class="callout-body">
          <ol style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Emergency Live Migration (vMotion):</strong> Immediately migrate 3 non-critical virtual machines off the constrained host to neighboring cluster nodes that have spare physical memory headroom.</li>
            <li><strong>Verify Guest Ballooning:</strong> Check why ballooning failed to reclaim sufficient memory. Verify that VMware Tools was running and that the balloon driver was not disabled in the guest OS kernel parameters.</li>
            <li><strong>Configure Memory Limits &amp; Reservations:</strong> Set Memory Reservations on critical VMs (e.g. database servers) guaranteeing 100% dedicated physical RAM allocation. Configure Memory Limits on non-critical VMs to prevent a runaway memory leak from exhausting the entire host memory pool.</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 4: Live Migration vMotion Failure Analysis During Cluster Maintenance</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> During host evacuation for motherboard replacement, an administrator attempts to vMotion migrate a mission-critical web server from Host A to Host B. The migration fails immediately at 10% with the error: <em>"The target host does not support the virtual machine's current hardware requirements. CPU feature mismatch (CPUID level)."</em></p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> ROOT-CAUSE ANALYSIS &amp; EVC RESOLUTION</div>
        <div class="callout-body">
          <p><strong>1. Root Cause:</strong> Host A is equipped with newer Intel Xeon Ice Lake processors, while Host B has older Intel Xeon Skylake processors. When the VM booted on Host A, it detected and utilized newer CPU instructions (e.g., AVX-512 VNNI). Migrating the running VM to Host B would cause instructions to execute on a CPU that lacks hardware support, triggering an immediate CPU illegal instruction fault.</p>
          <p><strong>2. Permanent Cluster Solution (Enhanced vMotion Compatibility - EVC):</strong> Enable <strong>EVC (Enhanced vMotion Compatibility)</strong> on the vSphere cluster, setting the cluster baseline to the lowest common CPU architecture (Skylake). EVC masks out newer instruction sets across all hosts, ensuring seamless bidirectional vMotion migrations across heterogeneous CPU generations.</p>
        </div>
      </div>
    </div>
  </div>
</article>

<!-- UNIT 2 MASTER ANSWER KEY -->
<article class="doc-page" id="mcq-answer-key-s2">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 02 • Master Verification Key</span>
    <h2 class="section-title"><span class="sec-num">KEY.2</span> Unit 2 Master Answer Key &amp; Technical Verification Matrix</h2>
    <p class="lead-para">
      Complete answer key and architectural validation matrix for Unit 2 practice bank questions 1 through 30.
    </p>
  </header>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Q#</th>
          <th>Correct</th>
          <th>Core Technical Concept</th>
          <th>Standard / Reference</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Q01</td><td><strong>B</strong></td><td>DHCP Option 66 specifies TFTP Boot Server Name</td><td>RFC 2132 DHCP Options</td></tr>
        <tr><td>Q02</td><td><strong>D</strong></td><td>MBR 32-bit LBA addressing limit: 2.19 TB max</td><td>Partition Table Architecture</td></tr>
        <tr><td>Q03</td><td><strong>A</strong></td><td>Memory ballooning driver inflates inside guest OS</td><td>Hypervisor Memory Overcommit</td></tr>
        <tr><td>Q04</td><td><strong>C</strong></td><td>VMBus synthetic device client/provider communication</td><td>Microsoft Hyper-V Architecture</td></tr>
        <tr><td>Q05</td><td><strong>B</strong></td><td>ReFS Accelerated VHDX block cloning and zeroing</td><td>Microsoft ReFS Storage Engine</td></tr>
        <tr><td>Q06</td><td><strong>A</strong></td><td>VST (Virtual Switch Tagging) handles 802.1Q at vSwitch</td><td>IEEE 802.1Q Virtual LANs</td></tr>
        <tr><td>Q07</td><td><strong>C</strong></td><td>AMD Nested Page Tables (NPT) hardware SLAT</td><td>AMD-V Architecture Reference</td></tr>
        <tr><td>Q08</td><td><strong>D</strong></td><td>mkfs.xfs formats XFS filesystem on Linux</td><td>XFS Filesystem Administration</td></tr>
        <tr><td>Q09</td><td><strong>B</strong></td><td>SR-IOV maps hardware Virtual Functions via DMA</td><td>PCI-SIG SR-IOV Standard</td></tr>
        <tr><td>Q10</td><td><strong>A</strong></td><td>ks.cfg automated Kickstart answer file for RHEL</td><td>Red Hat Enterprise Linux Spec</td></tr>
        <tr><td>Q11</td><td><strong>C</strong></td><td>vDS maintains cluster-wide state and vMotion continuity</td><td>VMware vSphere Networking</td></tr>
        <tr><td>Q12</td><td><strong>B</strong></td><td>ESP (EFI System Partition) FAT32 bootloader store</td><td>UEFI Specification 2.9</td></tr>
        <tr><td>Q13</td><td><strong>D</strong></td><td>Windows Deployment Services (WDS) for network PXE</td><td>Microsoft Windows Server</td></tr>
        <tr><td>Q14</td><td><strong>A</strong></td><td>LVM hierarchy: PV &rarr; VG &rarr; LV &rarr; Filesystem</td><td>Linux LVM Architecture</td></tr>
        <tr><td>Q15</td><td><strong>C</strong></td><td>Hypervisor swapping causes severe disk thrashing</td><td>Hypervisor Memory Management</td></tr>
        <tr><td>Q16</td><td><strong>B</strong></td><td>Intel VT-d (IOMMU) translates DMA memory for VMs</td><td>Intel Virtualization Spec</td></tr>
        <tr><td>Q17</td><td><strong>A</strong></td><td>Hyper-V Dynamic Memory adjusts RAM within bounds</td><td>Microsoft Hyper-V Spec</td></tr>
        <tr><td>Q18</td><td><strong>D</strong></td><td>nmcli connection modify for static IP setup</td><td>NetworkManager CLI Reference</td></tr>
        <tr><td>Q19</td><td><strong>C</strong></td><td>UEFI Secure Boot blocks pre-boot bootkits and rootkits</td><td>UEFI Secure Boot Spec</td></tr>
        <tr><td>Q20</td><td><strong>B</strong></td><td>xfs_growfs resizes mounted XFS filesystem</td><td>XFS Storage Utilities</td></tr>
        <tr><td>Q21</td><td><strong>A</strong></td><td>vMotion live migration with zero VM downtime</td><td>VMware vSphere Technology</td></tr>
        <tr><td>Q22</td><td><strong>D</strong></td><td>.vhdx format supports up to 64TB with power resilience</td><td>Microsoft VHDX Specification</td></tr>
        <tr><td>Q23</td><td><strong>B</strong></td><td>TPS deduplicates identical pages with Copy-on-Write</td><td>VMkernel Memory Architecture</td></tr>
        <tr><td>Q24</td><td><strong>C</strong></td><td>Install-WindowsFeature installs Hyper-V role</td><td>PowerShell ServerManager</td></tr>
        <tr><td>Q25</td><td><strong>A</strong></td><td>vCPU overcommitment triggers high %RDY co-scheduling wait</td><td>CPU Scheduler Architecture</td></tr>
        <tr><td>Q26</td><td><strong>D</strong></td><td>HCL certifies server hardware and storage controllers</td><td>Vendor Compatibility Standards</td></tr>
        <tr><td>Q27</td><td><strong>B</strong></td><td>Unattended answer files automate zero-touch installs</td><td>OS Provisioning Architecture</td></tr>
        <tr><td>Q28</td><td><strong>C</strong></td><td>Raw Device Mapping (RDM) bypasses virtual disk layer</td><td>Storage Virtualization Spec</td></tr>
        <tr><td>Q29</td><td><strong>A</strong></td><td>Guest integration tools install synthetic drivers and agents</td><td>Virtualization Guest Systems</td></tr>
        <tr><td>Q30</td><td><strong>D</strong></td><td>Nested virtualization runs a hypervisor inside a VM</td><td>Hardware Virtualization Extensions</td></tr>
      </tbody>
    </table>
  </div>
</article>
"""
