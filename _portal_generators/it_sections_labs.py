# -*- coding: utf-8 -*-
"""
Unit 6: Laboratory Manual (10 Practical Experiments)
Formatted in Engineering Standard .doc-page style with tables, callouts, and viva questions.
"""

IT_LABS_HTML = """
<!-- ==========================================================================
     UNIT 06: HANDS-ON LABORATORY PRACTICUM (10 EXPERIMENTS)
     ========================================================================== -->

<article class="doc-page" id="it-labs">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 06 • Practical Manual</span>
    <span class="meta-tag">10 Experiments • Syllabus Mapped</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">45.</span> Complete Hands-On Engineering Laboratory Practicum
  </h2>

  <p class="lead-para">
    Rigorous step-by-step engineering procedures, safety precautions, hardware tooling, terminal execution commands, and viva voce assessment sets for all 10 laboratory experiments mandated by Course Syllabus.
  </p>

  <div class="subj-grid">
    <!-- Lab 01 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 01</span> PC Disassembly, Motherboard Standoff Verification &amp; Component Reassembly</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Safely disassemble a modular desktop PC down to the bare chassis, verify brass standoff physical grounding alignment, inspect motherboard trace integrity, and reassemble to a clean successful POST.</p>
        <p><strong>Required Tooling:</strong> Magnetic tip #2 Phillips screwdriver, anti-static ESD wrist strap with grounding alligator clip, thermal paste (5+ W/mK), isopropyl alcohol 99%, lint-free wipes.</p>
        <p><strong>Procedure &amp; Safety Protocol:</strong></p>
        <ol>
          <li>Disconnect AC power cord; press the chassis power switch for 10 seconds to fully discharge SMPS bulk filter capacitors.</li>
          <li>Affix ESD wrist strap to an unpainted metal chassis frame (ensuring zero potential difference).</li>
          <li>Disconnect 24-pin ATX power and 8-pin EPS12V CPU harness with latch depressed; remove discrete GPU PCIe bracket screws.</li>
          <li>Unscrew CPU cooler mounting brackets diagonally in an alternating "X" pattern (half-turn increments) to relieve uneven mechanical tension on the CPU die.</li>
          <li>Inspect chassis tray: verify that exactly 9 standoffs correspond to standard ATX mounting holes. Remove any rogue standoffs under non-drilled PCB traces to eliminate short-circuit hazards.</li>
          <li>Reassemble: clean old thermal paste using 99% IPA, apply pea-sized bead of thermal paste, reinstall cooler, reconnect all power rails, and verify POST beep/LED.</li>
        </ol>
        <p><strong>Viva Assessment:</strong> <em>Why must cooler screws be loosened in an alternating X pattern?</em> To prevent localized mechanical torque from cracking fragile silicon corners or bending socket pins.</p>
      </div>
    </div>

    <!-- Lab 02 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 02</span> BIOS / UEFI Setup, NVRAM Boot Priority Configuration &amp; Hardware Health Monitoring</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Access UEFI firmware, configure boot order, enable XMP/EXPO memory profiles, configure fan pulse-width modulation (PWM) thermal curves, and verify voltage rail health.</p>
        <p><strong>Procedure:</strong></p>
        <ol>
          <li>Power on system and press the dedicated firmware interrupt key (`DEL` or `F2`) repeatedly before Windows Boot Manager loads.</li>
          <li>Navigate to <em>Advanced Frequency Settings</em>: enable XMP (Extreme Memory Profile) Profile 1 to load certified memory timings (e.g. DDR4-3600 CL16 @ 1.35V).</li>
          <li>Navigate to <em>Hardware Health Monitor</em>: observe real-time sensor telemetry. Verify:
            <br>&bull; CPU Core Vcore: Between 1.05V and 1.30V
            <br>&bull; +12V Rail: 11.90V to 12.15V (Within strict &plusmn;5% tolerance)
            <br>&bull; CPU Package Temperature: &le;42&deg;C at idle
          </li>
          <li>Navigate to <em>Boot Options</em>: set UEFI USB Drive as Boot Option #1, NVMe SSD as Boot Option #2. Disable legacy CSM (Compatibility Support Module) to enforce pure UEFI GPT boot.</li>
          <li>Save changes to NVRAM (`F10`) and restart.</li>
        </ol>
        <p><strong>Viva Assessment:</strong> <em>What is the architectural difference between UEFI and legacy BIOS?</em> BIOS executes in 16-bit real mode and is limited to 2.2TB MBR disks; UEFI executes in 32/64-bit protected mode, boots from GPT partitions up to 9.4 ZB, and incorporates cryptographic Secure Boot.</p>
      </div>
    </div>

    <!-- Lab 03 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 03</span> Operating System Installation &amp; Storage Partitioning: MBR vs GPT Initialization</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Initialize a raw NVMe SSD using modern GUID Partition Table (GPT) architecture, create standard UEFI partitions via `diskpart`, and install Windows 11 Enterprise.</p>
        <p><strong>Terminal Procedure (`diskpart` via Shift+F10 in Windows Setup):</strong></p>
        <div class="terminal-block">
          <div class="terminal-bar">
            <div class="term-dots"><span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span class="term-dot dot-green"></span></div>
            <div class="term-title">DISKPART Partitioning Shell</div>
            <div class="term-actions">
              <button class="btn-term-action btn-copy-code" type="button"><i data-lucide="copy"></i><span>Copy</span></button>
            </div>
          </div>
          <pre class="code-pre"><code>diskpart
list disk
select disk 0
clean
convert gpt
create partition efi size=100
format quick fs=fat32 label="System"
create partition msr size=16
create partition primary
format quick fs=ntfs label="Windows"
exit</code></pre>
        </div>
        <p><strong>Viva Assessment:</strong> <em>Why must the EFI System Partition (ESP) be formatted as FAT32 rather than NTFS?</em> The UEFI specification defines FAT12/16/32 as the mandatory filesystem drivers embedded in motherboard ROM. UEFI cannot natively read NTFS without proprietary third-party EFI drivers.</p>
      </div>
    </div>

    <!-- Lab 04 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 04</span> Structured Cabling: Straight-Through &amp; Crossover RJ-45 Cable Crimping &amp; Certification</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Strip, untwist, sequence, and crimp Cat 6 UTP cable into 8P8C modular RJ-45 plugs following TIA/EIA T568A and T568B pinout standards; verify pin-to-pin electrical continuity using a hardware cable tester.</p>
        <p><strong>Procedure:</strong></p>
        <ol>
          <li>Strip 1.25 inches of outer PVC jacket using a rotary cable stripper, being careful not to nick the interior copper insulation.</li>
          <li>Cut away the internal plastic spline. Untwist pairs by <strong>no more than 0.5 inches</strong>.</li>
          <li>Sequence conductors for T568B: <em>White/Orange, Orange, White/Green, Blue, White/Blue, Green, White/Brown, Brown</em>.</li>
          <li>Flatten and trim wires flush at 0.5 inches (12.7 mm) from jacket edge using flush cutters.</li>
          <li>Insert conductors into RJ-45 plug until copper tips contact the end wall; verify outer jacket extends past the internal strain-relief wedge.</li>
          <li>Crimp firmly using ratcheting modular crimper. Repeat on opposite end to create a straight-through cable (or use T568A for a crossover cable).</li>
          <li>Connect to cable tester: verify all 8 LED indicators illuminate sequentially from 1 to 8 without open, crossed, or shorted pins.</li>
        </ol>
        <p><strong>Viva Assessment:</strong> <em>What is Near-End Crosstalk (NEXT) and how does pair twist pitch prevent it?</em> NEXT occurs when high-frequency signals in one pair bleed into an adjacent pair. Different twist pitches keep magnetic fields out of phase, allowing differential receivers to cancel out common-mode noise.</p>
      </div>
    </div>

    <!-- Lab 05 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 05</span> SOHO Wireless Gateway Configuration: WPA3-Personal, SSID Cloaking &amp; MAC Filtering</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Configure an enterprise/SOHO wireless access point: establish isolated 2.4 GHz and 5 GHz SSIDs, enforce WPA3-SAE encryption, allocate DHCP scope, and audit rogue Wi-Fi clients.</p>
        <p><strong>Procedure:</strong></p>
        <ol>
          <li>Connect administrative PC to LAN Port 1; open browser and navigate to Gateway IP `192.168.1.1`. Authenticate using default administrator credentials and immediately replace default password.</li>
          <li>Navigate to <em>Wireless Settings</em> &rarr; <em>5 GHz Radio</em>: set Channel Width to 80 MHz, select clean non-DFS channel (e.g. Channel 36 or 149). Set Security Mode to <strong>WPA3-Personal (SAE)</strong> with 20+ character passphrase.</li>
          <li>Navigate to <em>Guest Network</em>: enable Guest SSID with client isolation (prevents guests from scanning internal LAN servers or printers).</li>
          <li>Navigate to <em>DHCP Server</em>: set IP Pool to `192.168.1.100` - `192.168.1.200` (reserving `.1` to `.99` for static servers/printers). Set lease time to 24 hours.</li>
          <li>Verify client connection and observe negotiated cipher in OS terminal: verify `WPA3-Personal` and `AES-GCMP-256`.</li>
        </ol>
        <p><strong>Viva Assessment:</strong> <em>Why is MAC filtering considered obsolete security?</em> MAC addresses are transmitted in unencrypted plaintext 802.11 frame headers. Any attacker with Wireshark can capture a valid client MAC and clone it to bypass the filter in under 10 seconds.</p>
      </div>
    </div>

    <!-- Lab 06 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 06</span> Windows Management Consoles: MMC Customization, Event Viewer Auditing &amp; Disk Management</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Build a custom Microsoft Management Console (.msc), configure security audit logging for logon failures, and create a stripped RAID 0 software volume in Disk Management.</p>
        <p><strong>Procedure:</strong></p>
        <ol>
          <li>Press `Win + R`, type `mmc.exe`, and press Enter to launch an empty console root.</li>
          <li>Click <em>File</em> &rarr; <em>Add/Remove Snap-in...</em>: add <strong>Event Viewer</strong>, <strong>Disk Management</strong>, <strong>Device Manager</strong>, and <strong>Services</strong>. Save as `AdminToolkit.msc`.</li>
          <li>Open `secpol.msc` (Local Security Policy): navigate to <em>Security Settings</em> &rarr; <em>Local Policies</em> &rarr; <em>Audit Policy</em>. Double-click <strong>Audit logon events</strong> and check both <em>Success</em> and <em>Failure</em>.</li>
          <li>Test audit logging: lock workstation and intentionally enter an incorrect password. Unlock with correct credentials.</li>
          <li>Open Event Viewer &rarr; <em>Windows Logs</em> &rarr; <em>Security</em>: filter for <strong>Event ID 4625</strong> (An account failed to log on). Inspect failure reason, target user name, and caller process.</li>
        </ol>
        <p><strong>Viva Assessment:</strong> <em>What is the difference between Event ID 4624 and Event ID 4625 in Windows?</em> Event ID 4624 indicates a successful logon; Event ID 4625 indicates a failed logon attempt (vital for detecting brute-force attacks).</p>
      </div>
    </div>

    <!-- Lab 07 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 07</span> Linux Administration: System User Creation, Sudoers Privileges &amp; Octal Chmod Permissions</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Create system users, assign secondary administrative groups, enforce POSIX octal file permissions, and configure SUID/SGID bits in a Linux terminal.</p>
        <p><strong>Terminal Execution Trace:</strong></p>
        <div class="terminal-block">
          <div class="terminal-bar">
            <div class="term-dots"><span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span class="term-dot dot-green"></span></div>
            <div class="term-title">Bash Terminal • Root Shell</div>
            <div class="term-actions">
              <button class="btn-term-action btn-copy-code" type="button"><i data-lucide="copy"></i><span>Copy</span></button>
            </div>
          </div>
          <pre class="code-pre"><code># 1. Create developer user with home directory and bash shell
sudo useradd -m -s /bin/bash devops_user
sudo passwd devops_user

# 2. Grant administrative sudo privileges via wheel/sudo group
sudo usermod -aG sudo devops_user

# 3. Create shared engineering project directory
sudo mkdir -p /srv/engineering
sudo chown -R devops_user:developers /srv/engineering

# 4. Enforce read/write/execute for owner, read/execute for group, zero access for others
sudo chmod 750 /srv/engineering
ls -ld /srv/engineering
# Output: drwxr-x--- 2 devops_user developers 4096 Oct 27 15:00 /srv/engineering

# 5. Set SGID bit so newly created files automatically inherit the parent group
sudo chmod 2770 /srv/engineering
ls -ld /srv/engineering
# Output: drwxrws--- 2 devops_user developers 4096 Oct 27 15:00 /srv/engineering</code></pre>
        </div>
        <p><strong>Viva Assessment:</strong> <em>What does the SGID bit (chmod 2770) do when applied to a directory?</em> It forces all newly created files inside that directory to automatically inherit the group ownership of the directory rather than the primary group of the creating user.</p>
      </div>
    </div>

    <!-- Lab 08 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 08</span> Command-Line Network Diagnostics: Packet Capture, Path MTU Discovery &amp; ARP Cache Poisoning Analysis</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Utilize administrative CLI utilities (`ipconfig`, `arp`, `ping`, `tracert`, `netstat`, `nslookup`) to diagnose routing failures, discover maximum transmission units (MTU), and inspect active TCP sockets.</p>
        <p><strong>Terminal Execution Trace:</strong></p>
        <div class="terminal-block">
          <div class="terminal-bar">
            <div class="term-dots"><span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span class="term-dot dot-green"></span></div>
            <div class="term-title">PowerShell / Command Prompt</div>
            <div class="term-actions">
              <button class="btn-term-action btn-copy-code" type="button"><i data-lucide="copy"></i><span>Copy</span></button>
            </div>
          </div>
          <pre class="code-pre"><code># 1. Inspect complete TCP/IP stack configuration & DNS servers
ipconfig /all

# 2. Flush corrupted local DNS resolver cache
ipconfig /flushdns

# 3. Path MTU Discovery: Ping without fragmentation to find maximum packet size
ping 8.8.8.8 -f -l 1472
# If successful: 1472 (data) + 20 (IP header) + 8 (ICMP header) = 1500 Byte MTU!

# 4. View active Layer 2 ARP cache table
arp -a

# 5. Inspect all listening and established TCP sockets with owning Process ID (PID)
netstat -ano | findstr "ESTABLISHED"</code></pre>
        </div>
        <p><strong>Viva Assessment:</strong> <em>Why does pinging with a 1473-byte buffer fail when the `DontFragment` (-f) flag is set on a standard Ethernet connection?</em> Ethernet has an MTU of 1500 bytes. A 1473-byte payload plus 28 bytes of headers equals 1501 bytes, requiring fragmentation. With `-f` enabled, the router drops the packet with "Packet needs to be fragmented but DF set".</p>
      </div>
    </div>

    <!-- Lab 09 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 09</span> Laser Printer Disassembly, Maintenance Kit Installation &amp; Fuser Calibration</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Perform preventative maintenance on an enterprise workgroup laser printer: replace the transfer roller, paper pickup rollers, separation pads, and fuser unit; reset the internal page count maintenance odometer.</p>
        <p><strong>Procedure:</strong></p>
        <ol>
          <li>Power off printer and allow the fuser assembly to cool for 30 minutes (operating temperature &ge;180&deg;C).</li>
          <li>Release rear cover latches; extract fuser assembly by depressing the blue release levers. Inspect Teflon heat sleeve for gouges or toner buildup. Install new fuser unit until latches click.</li>
          <li>Open toner door; extract toner cartridge/imaging drum and immediately place in an opaque light-blocking bag to prevent light shock to the OPC drum.</li>
          <li>Use specialized plastic extraction tool to lift out the Transfer Roller. <strong>Warning: Never touch the sponge surface of the transfer roller with bare fingers; skin oils prevent uniform +600V electrostatic charge transfer!</strong></li>
          <li>Replace rubber paper-feed pickup rollers and separation pads in Paper Tray 2 using snap-fit tabs.</li>
          <li>Power on printer, enter Service Menu, and reset the <em>Maintenance Count</em> to 0. Execute an internal Configuration / Quality Test Page.</li>
        </ol>
        <p><strong>Viva Assessment:</strong> <em>Why must the transfer roller never be touched with bare fingers?</em> Human skin secretions leave oil deposits on the conductive sponge. In those spots, the electrical resistance increases, weakening the +600V charge transfer and leaving faded vertical patches on the printout.</p>
      </div>
    </div>

    <!-- Lab 10 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">EXP 10</span> Virtualization Host Deployment: Type-1 Hypervisor Setup &amp; Virtual Machine Provisioning</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Objective:</strong> Enable hardware virtualization extensions (Intel VT-x / AMD-V) in BIOS, configure Microsoft Hyper-V / VMware Workstation, create an external virtual switch (vSwitch), and provision a guest Linux virtual machine.</p>
        <p><strong>Procedure:</strong></p>
        <ol>
          <li>Enter UEFI firmware: enable <em>Intel Virtualization Technology (VT-x)</em> and <em>VT-d (Directed I/O)</em>. Save and boot into Windows.</li>
          <li>Enable Hyper-V platform via administrative PowerShell: `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`. Reboot system.</li>
          <li>Launch <em>Hyper-V Manager</em>: open <em>Virtual Switch Manager</em>. Create an <strong>External Virtual Switch</strong> bound to the physical gigabit NIC (enabling guest VMs to obtain real DHCP leases on the physical network).</li>
          <li>Click <em>New Virtual Machine</em>: select Generation 2 (enables UEFI firmware, SCSI controllers, and Secure Boot).</li>
          <li>Allocate resources: 2 vCPUs, 4096 MB Dynamic RAM, and 50 GB dynamically expanding VHDX storage disk.</li>
          <li>Attach Ubuntu Server ISO to the virtual DVD drive, power on VM, and verify successful boot into the guest operating system installer.</li>
        </ol>
        <p><strong>Viva Assessment:</strong> <em>What is the difference between a Type-1 and Type-2 hypervisor?</em> A Type-1 hypervisor (ESXi, Hyper-V core) runs directly on the bare-metal hardware without a host OS; a Type-2 hypervisor (VirtualBox, VMware Workstation) runs as an application process inside a host operating system.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Unit 06 Complete • Next: Unit 07 Engineering Simulators</span>
    <span>Unit 06 • Practical Manual</span>
  </div>
</article>
"""
