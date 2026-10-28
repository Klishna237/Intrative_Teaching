# -*- coding: utf-8 -*-
"""
IT Fundamentals Portal - Practical Laboratory Manual (Master Gold Standard)
10 Comprehensive Hands-On Experiments with Terminal Windows, Verification, and Viva Questions
Exact layout, classes, and styling matching Cloud and Server administration portals.
"""

IT_LABS_HTML = r"""
<!-- ===================================================================
     HANDS-ON LABORATORY MANUAL: 10 PRACTICAL EXPERIMENTS
     =================================================================== -->
<article class="doc-page" id="it-labs">
  <header class="doc-page-header">
    <span class="page-header-meta">Curriculum Lab Manual • Hands-On Practicals</span>
    <h2 class="section-title"><span class="sec-num">LAB.1</span> IT Fundamentals Laboratory Manual: 10 Rigorous Hands-on Practicals</h2>
    <p class="lead-para">
      This practical lab manual provides end-to-end, reproducible engineering procedures conforming to the Department of Computer Science &amp; Engineering IT Fundamentals (CSC104) syllabus. Each experiment includes exact terminal commands, hardware inspection procedures, expected execution outputs, troubleshooting scenarios, and oral examination (Viva Voce) question sets.
    </p>
  </header>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="terminal"></i> LABORATORY PREREQUISITES &amp; ENVIRONMENT SETUP</div>
    <div class="callout-body">
      Ensure you have access to a laboratory workstation running Windows 10/11 Pro (or Linux dual-boot) with administrative privileges, an ESD anti-static wrist strap, #2 Phillips screwdriver, multimeters, patch cables, SOHO wireless router, network printer, and Oracle VM VirtualBox installed.
    </div>
  </div>

  <!-- LAB 1 -->
  <div class="subj-card revealed" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 01</div>
      <div class="subj-title">Identification of Computer Hardware Components &amp; Motherboard Subsystems</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Safely inspect and identify desktop motherboard form factors (ATX, Micro-ATX, Mini-ITX), CPU sockets (LGA1700, AM5), DDR4/DDR5 DIMM slots, PCIe expansion risers, NVMe M.2 interfaces, SMPS power rails, and front-panel pinouts.</p>
      <p><strong>Apparatus &amp; Tools:</strong> ESD wrist strap, #2 Phillips non-magnetic screwdriver, modular desktop workstation, multi-meter, and component trays.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • Hardware Subsystem Discovery</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Query motherboard manufacturer, chipset product model, and firmware version</span>
Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product, SerialNumber, Version

<span class="code-comment"># 2. Inspect CPU processor architecture, physical core count, and socket designation</span>
Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, SocketDesignation, MaxClockSpeed

<span class="code-comment"># 3. Query physical RAM modules: bank label, capacity in bytes, speed (MT/s), and form factor</span>
Get-CimInstance Win32_PhysicalMemory | Select-Object DeviceLocator, Capacity, Speed, MemoryType, Manufacturer

<span class="code-comment"># 4. Enumerate disk storage devices, bus connection types (NVMe / SATA), and health</span>
Get-PhysicalDisk | Select-Object DeviceId, FriendlyName, MediaType, BusType, Size, OperationalStatus</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Terminal returns active baseboard model (e.g. <code>Z790 AORUS ELITE</code>), CPU socket designation (e.g. <code>LGA1700</code>), physical memory bank placement (e.g. <code>DIMM_A2, DIMM_B2</code> for dual-channel interleaving), and NVMe bus type reporting <code>OperationalStatus: OK</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the primary physical difference between LGA and PGA sockets?</strong><br>
          <em>Answer:</em> In LGA (Land Grid Array), delicate conductive pins reside inside the motherboard socket contacting flat gold pads on the CPU substrate. In PGA (Pin Grid Array), pins are soldered to the bottom of the CPU package and insert into socket pinholes.<br><br>
          <strong>Q2: Why are motherboard standoffs mandatory when installing a motherboard inside an ATX case?</strong><br>
          <em>Answer:</em> Standoffs physically elevate the motherboard PCB 6-10 mm above the metal chassis backplate, preventing exposed solder joints and electrical signal traces from short-circuiting against the grounded metal frame.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 2 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 02</div>
      <div class="subj-title">System Diagnostics, Hardware Auditing &amp; Performance Telemetry</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Use Windows System Information (<code>MSINFO32</code>), Device Manager, Performance Monitor (<code>perfmon</code>), and Command Prompt to analyze memory paging, CPU bottlenecks, and driver states.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows 10/11 Enterprise workstation, Performance Monitor, Sysinternals Process Explorer.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Command Prompt / PowerShell • Diagnostic Utilities</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Launch complete GUI Windows System Information tree</span>
msinfo32

<span class="code-comment"># 2. Extract operating system build, SMBIOS version, and physical memory capacity</span>
Get-ComputerInfo | Select-Object CsName, WindowsProductName, BiosFirmwareType, BiosSMBIOSBIOSVersion, TotalPhysicalMemory

<span class="code-comment"># 3. Monitor CPU load, committed memory, and disk queue length in real time</span>
Get-Counter -Counter "\Processor(_Total)\% Processor Time", "\Memory\Available MBytes", "\LogicalDisk(_Total)\Current Disk Queue Length" -SampleInterval 2 -MaxSamples 3

<span class="code-comment"># 4. Enumerate all Plug and Play hardware devices with malfunctioning drivers</span>
Get-PnpDevice | Where-Object { $_.Status -ne "OK" } | Select-Object FriendlyName, InstanceId, Class, Status</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Telemetry stream confirms processor load, memory availability (&gt; 4096 MB), and zero devices returning error state <code>Error / Degraded</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What does a high value in the `Memory\Pages/sec` performance counter indicate?</strong><br>
          <em>Answer:</em> It indicates excessive hard page faults where the operating system is constantly swapping data between physical RAM and the virtual memory pagefile (pagefile.sys) on disk due to memory exhaustion.<br><br>
          <strong>Q2: What is the architectural difference between UEFI and legacy BIOS firmware?</strong><br>
          <em>Answer:</em> UEFI supports 64-bit CPU modes, boot disks larger than 2.2 TB using GPT partitioning, Secure Boot digital signature validation, and pre-boot networking, unlike 16-bit real-mode legacy BIOS limited to 2 TB MBR disks.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 3 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 03</div>
      <div class="subj-title">BIOS/UEFI Firmware Configuration, Boot Priority &amp; Virtualization Setup</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Access UEFI firmware settings, verify hardware component recognition, configure boot device priority order, enable hardware virtualization (Intel VT-x / AMD-V), and configure Secure Boot key exchange.</p>
      <p><strong>Apparatus &amp; Tools:</strong> UEFI motherboard testbench, USB boot media, Command Prompt.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Command Prompt • Boot Configuration Data</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Force immediate system reboot directly into UEFI Firmware Settings GUI</span>
shutdown /r /fw /t 0

<span class="code-comment">:: 2. Display the active Windows Boot Configuration Data (BCD) store entries</span>
bcdedit /enum {current}

<span class="code-comment"># 3. Verify hardware virtualization capabilities supported by processor</span>
systeminfo | findstr /i "Virtualization"

<span class="code-comment"># 4. Query Secure Boot enablement status via PowerShell</span>
powershell -Command "Confirm-SecureBootUEFI"</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Command <code>Confirm-SecureBootUEFI</code> returns <code>True</code>, and <code>systeminfo</code> confirms <code>Virtualization Enabled In Firmware: Yes</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What role does Secure Boot play in protecting the operating system integrity?</strong><br>
          <em>Answer:</em> Secure Boot ensures firmware executes only bootloaders, kernels, and option ROMs that are digitally signed with cryptographic keys trusted in the UEFI DB keystore, blocking rootkits and bootkits.<br><br>
          <strong>Q2: Why must hardware virtualization (Intel VT-x / AMD-V) be enabled in BIOS before installing Type-2 hypervisors?</strong><br>
          <em>Answer:</em> It enables CPU hardware extensions (VMX/SVM) that allow hypervisors to execute guest operating system rings without costly binary translation, slashing VM context-switching overhead.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 4 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 04</div>
      <div class="subj-title">Operating System User Administration &amp; NTFS Discretionary Access Control (DACLs)</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Create local administrative and standard user accounts, enforce account password policies, create departmental directory hierarchies, and configure granular NTFS file and folder permissions using GUI and <code>icacls</code>.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows 10/11 Professional workstation, Local Users and Groups (<code>lusrmgr.msc</code>), Command Prompt.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Command Prompt • User &amp; Permission Administration</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Create a new standard local user account with non-expiring password</span>
net user dev_analyst P@ssw0rd2026! /add /comment:"Junior Developer" /passwordchg:no

<span class="code-comment">:: 2. Create an administrative engineering group and assign membership</span>
net localgroup EngineeringTeam /add
net localgroup EngineeringTeam dev_analyst /add

<span class="code-comment">:: 3. Create departmental directory structure on drive C:</span>
mkdir C:\Projects\FinTech_Core

<span class="code-comment">:: 4. Grant EngineeringTeam Read-and-Execute and restrict write access</span>
icacls "C:\Projects\FinTech_Core" /grant:r EngineeringTeam:(OI)(CI)(RX)
icacls "C:\Projects\FinTech_Core" /inheritance:r
icacls "C:\Projects\FinTech_Core" /grant:r Administrators:(OI)(CI)(F)</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Executing <code>icacls C:\Projects\FinTech_Core</code> displays <code>EngineeringTeam:(OI)(CI)(RX)</code> and <code>Administrators:(OI)(CI)(F)</code> with broken inheritance from root.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the difference between NTFS permissions and Share permissions?</strong><br>
          <em>Answer:</em> Share permissions only restrict network-based SMB access to folders, whereas NTFS permissions apply universally both over the network and locally at the disk filesystem level. The most restrictive permission takes precedence.<br><br>
          <strong>Q2: What do the `(OI)` and `(CI)` flags represent in `icacls` permission inheritance?</strong><br>
          <em>Answer:</em> `(OI)` stands for Object Inherit (child files inherit the permission), and `(CI)` stands for Container Inherit (child subdirectories inherit the permission).
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 5 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 05</div>
      <div class="subj-title">Basic Network Configuration, Static/DHCP Addressing &amp; Diagnostic Utilities</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure static and dynamic IPv4/IPv6 parameters on network interfaces, calculate CIDR subnet ranges, verify default gateway routing, test DNS resolution, and trace network latency across hops.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Network patch cable, Cat6 RJ-45 crimper, cable tester, Command Prompt / PowerShell.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Command Prompt • Network Diagnostic Stack</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Display full TCP/IP configuration, MAC addresses, and active DHCP leases</span>
ipconfig /all

<span class="code-comment">:: 2. Flush and reset the local DNS resolver cache to clear corrupted records</span>
ipconfig /flushdns

<span class="code-comment">:: 3. Test ICMP end-to-end network connectivity with 4 echo requests</span>
ping -n 4 8.8.8.8

<span class="code-comment">:: 4. Path MTU Discovery: Ping with Don't Fragment (DF) flag set to find MTU ceiling</span>
ping 8.8.8.8 -f -l 1472

<span class="code-comment">:: 5. Trace Layer 3 routing hops and latency to target destination</span>
tracert -d 8.8.8.8

<span class="code-comment">:: 6. Display local ARP cache mapping IPv4 addresses to physical MAC addresses</span>
arp -a

<span class="code-comment">:: 7. List all active listening TCP ports and associated process IDs</span>
netstat -ano | findstr "LISTENING"</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Ping to <code>8.8.8.8</code> succeeds with 0% packet loss and round-trip latency &lt; 20 ms. <code>arp -a</code> displays gateway MAC address corresponding to local router.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why does a standard Ethernet ping packet with a 1472-byte payload result in a 1500-byte frame?</strong><br>
          <em>Answer:</em> The 1472-byte ICMP data payload is encapsulated with a 20-byte IPv4 header and an 8-byte ICMP header (1472 + 20 + 8 = 1500 bytes), which is the standard Ethernet Maximum Transmission Unit (MTU).<br><br>
          <strong>Q2: What does an IPv4 address beginning with `169.254.x.x` signify?</strong><br>
          <em>Answer:</em> It indicates an Automatic Private IP Addressing (APIPA) link-local address assigned by the client when it fails to receive an answer from a DHCP server during the DORA process.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 6 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 06</div>
      <div class="subj-title">Wireless Network Architecture &amp; SOHO Router Security Hardening</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Access SOHO wireless router management portals, configure distinct SSID broadcasts for 2.4 GHz and 5 GHz bands, enforce WPA2/WPA3 Personal encryption with strong pre-shared keys, configure DHCP server address pools, and disable WPS.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Dual-band 802.11ax Wi-Fi router, Ethernet patch cable, Command Prompt.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Command Prompt • WLAN Diagnostics &amp; Auditing</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Display active wireless network interface parameters and signal quality</span>
netsh wlan show interfaces

<span class="code-comment">:: 2. Enumerate surrounding Wi-Fi networks, BSSIDs, signal strengths, and channels</span>
netsh wlan show networks mode=bssid

<span class="code-comment">:: 3. Display list of all saved Wi-Fi connection profiles on the host</span>
netsh wlan show profiles

<span class="code-comment">:: 4. Export wireless profile with cleartext pre-shared security key for audit</span>
netsh wlan show profile name="Lab-Office-5G" key=clear

<span class="code-comment">:: 5. Release and renew DHCP lease obtained from SOHO wireless router</span>
ipconfig /release
ipconfig /renew</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>netsh wlan show interfaces</code> shows State: connected, Radio type: <code>802.11ax</code>, Authentication: <code>WPA3-Personal</code>, and Cipher: <code>CCMP / GCMP-256</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why is WPA3 Personal significantly more secure than WPA2 against offline dictionary attacks?</strong><br>
          <em>Answer:</em> WPA3 replaces the WPA2 4-way handshake with Simultaneous Authentication of Equals (SAE, Dragonfly protocol), providing Forward Secrecy and preventing adversaries from capturing handshakes for offline brute-force cracking.<br><br>
          <strong>Q2: Why should Wi-Fi Protected Setup (WPS) always be disabled on enterprise and SOHO routers?</strong><br>
          <em>Answer:</em> WPS PIN authentication uses an 8-digit PIN validated in two separate halves (10,000 and 1,000 combinations), allowing tools like Reaver to brute-force the PIN in less than 4 hours.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 7 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 07</div>
      <div class="subj-title">Local &amp; Network Printer Installation, Driver Isolation &amp; Spooler Triage</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Install network printers via standard TCP/IP ports, configure RAW and LPR port protocols, manage print spooler services, purge stuck print queue jobs, and diagnose 7-stage laser printer electrophotographic defects.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Network laser printer, printer drivers, Print Management console, PowerShell.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • Print Spooler Triage &amp; Management</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Enumerate all locally installed and networked printer devices and drivers</span>
Get-Printer | Select-Object Name, DriverName, PortName, Shared, PrinterStatus

<span class="code-comment"># 2. Query active print jobs currently queued in the print spooler</span>
Get-PrintJob -PrinterName "HP-LaserJet-Lab" | Select-Object Id, DocumentName, TotalPages, SubmittedTime

<span class="code-comment"># 3. Forcibly stop the Windows Print Spooler service</span>
Stop-Service -Name Spooler -Force

<span class="code-comment"># 4. Clear all corrupt or stuck print job spool files (.SPL and .SHD)</span>
Remove-Item -Path "C:\Windows\System32\spool\PRINTERS\*" -Force

<span class="code-comment"># 5. Restart the Print Spooler service and verify running status</span>
Start-Service -Name Spooler
Get-Service -Name Spooler</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>Get-Service -Name Spooler</code> reports Status: <code>Running</code>, and the print queue displays 0 pending jobs.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What causes repetitive dark spots or voids appearing at fixed intervals down a laser-printed page?</strong><br>
          <em>Answer:</em> A damaged or gouged roller in the electrophotographic assembly. The exact distance between repeating defects corresponds directly to the circumference of the defective roller: Interval = &pi; &times; Diameter (e.g. 30 mm OPC drum &approx; 94.2 mm interval).<br><br>
          <strong>Q2: What is the function of the Fuser Assembly in an electrophotographic laser printer?</strong><br>
          <em>Answer:</em> The fuser uses high heat (180°C–205°C) and mechanical pressure to melt the resin particles in the toner powder and permanently bond them into the cellulose fibers of the paper.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 8 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 08</div>
      <div class="subj-title">Type-2 Hypervisor Virtualization &amp; Guest Linux Operating System Installation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Install Oracle VM VirtualBox or VMware Workstation, create a customized virtual machine (2 vCPUs, 4 GB RAM, 25 GB VDI dynamic disk), attach an Ubuntu Linux ISO, configure NAT / Host-Only virtual network adapters, and install guest additions.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Oracle VM VirtualBox, Ubuntu Desktop 24.04 LTS ISO, VirtualBox CLI (<code>VBoxManage</code>).</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> VirtualBox CLI • VBoxManage Automation</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Query VirtualBox hypervisor version and host system capabilities</span>
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" --version

<span class="code-comment">:: 2. Create and register a new 64-bit Linux virtual machine</span>
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" createvm --name "Ubuntu-DevLab" --ostype "Ubuntu_64" --register

<span class="code-comment">:: 3. Configure VM CPU count, memory allocation (4096 MB), and VRAM (128 MB)</span>
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "Ubuntu-DevLab" --cpus 2 --memory 4096 --vram 128

<span class="code-comment">:: 4. Attach virtual storage controller and provision 25 GB dynamic virtual disk</span>
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" storagectl "Ubuntu-DevLab" --name "SATA Controller" --add sata --controller IntelAHCI
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" createmedium disk --filename "C:\VMs\Ubuntu-DevLab\disk.vdi" --size 25600 --format VDI

<span class="code-comment">:: 5. Configure Network Adapter 1 to Network Address Translation (NAT)</span>
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" modifyvm "Ubuntu-DevLab" --nic1 nat</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>VBoxManage showvminfo Ubuntu-DevLab</code> outputs state: <code>powered off</code>, Memory size: <code>4096MB</code>, Number of CPUs: <code>2</code>, NIC 1: <code>MAC: ..., Attachment: NAT</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the key difference between Type-1 and Type-2 hypervisors?</strong><br>
          <em>Answer:</em> Type-1 (bare-metal) hypervisors like VMware ESXi or KVM run directly on server hardware with zero host OS overhead. Type-2 (hosted) hypervisors like VirtualBox run as software applications on top of an existing host OS (Windows/macOS).<br><br>
          <strong>Q2: What is the difference between NAT mode and Bridged mode in VM networking?</strong><br>
          <em>Answer:</em> In NAT mode, the VM shares the host IP via internal router translation and cannot be initiated from the external LAN. In Bridged mode, the VM connects directly to the physical network switch and receives its own independent IP from the local LAN DHCP server.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 9 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 09</div>
      <div class="subj-title">Windows Defender Security Hardening, Advanced Firewall Rules &amp; Audit Logging</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure the Windows Defender Advanced Security Firewall, create inbound port blocking rules, configure outbound application restriction policies, inspect Microsoft Defender antivirus signature status, and audit security events in Event Viewer.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows Defender Firewall with Advanced Security, Event Viewer, Command Prompt.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Command Prompt • Security Policy &amp; Firewall</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Verify Windows Defender real-time antivirus engine and signature version</span>
powershell -Command "Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureAge"

<span class="code-comment">:: 2. Enforce active firewall state across Domain, Private, and Public profiles</span>
netsh advfirewall set allprofiles state on

<span class="code-comment">:: 3. Create inbound firewall rule blocking insecure Telnet (TCP Port 23)</span>
netsh advfirewall firewall add rule name="Block-Telnet-Inbound" dir=in action=block protocol=TCP localport=23

<span class="code-comment">:: 4. Create inbound firewall rule permitting secure SSH (TCP Port 22)</span>
netsh advfirewall firewall add rule name="Allow-SSH-Inbound" dir=in action=allow protocol=TCP localport=22

<span class="code-comment">:: 5. Query the last 5 security log events recorded in Windows Event Viewer</span>
wevtutil qe Security /c:5 /rd:true /f:text</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>netsh advfirewall firewall show rule name="Block-Telnet-Inbound"</code> reports Action: <code>Block</code>, Protocol: <code>TCP</code>, LocalPort: <code>23</code>, Enabled: <code>Yes</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: In Windows Event Viewer, what do Event IDs 4624 and 4625 indicate?</strong><br>
          <em>Answer:</em> Event ID 4624 represents a successful account logon, while Event ID 4625 indicates a failed account logon attempt (critical for detecting brute-force password spraying attacks).<br><br>
          <strong>Q2: What is the difference between a stateless packet filter and a stateful firewall?</strong><br>
          <em>Answer:</em> A stateless filter inspects each packet in isolation against static rules. A stateful firewall tracks active transport connections in a state table, automatically permitting legitimate response traffic to outbound connections without requiring manual inbound rules.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 10 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">LAB 10</div>
      <div class="subj-title">System Maintenance, Storage Optimization &amp; Disaster Recovery Procedures</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Execute preventive storage maintenance, clean temporary cache artifacts, verify NTFS filesystem integrity using <code>chkdsk</code>, repair corrupted Windows Component Store packages using DISM, and create system restore points.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows 10/11 Professional workstation, DISM, SFC, Defrag utility.</p>

      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Command Prompt • Maintenance &amp; Repair Suite</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment">:: 1. Scan and verify NTFS volume integrity and report bad sector allocation</span>
chkdsk C: /f /r

<span class="code-comment">:: 2. Scan and repair corrupted Windows System Component Store using DISM</span>
dism /online /cleanup-image /restorehealth

<span class="code-comment">:: 3. Execute System File Checker (SFC) to replace corrupted protected system files</span>
sfc /scannow

<span class="code-comment">:: 4. Optimize and trim fragmented SSD and HDD volumes</span>
defrag C: /O

<span class="code-comment">:: 5. Create an immediate System Restore Point for disaster recovery</span>
powershell -Command "Checkpoint-Computer -Description 'Pre-Lab-Baseline' -RestorePointType 'MODIFY_SETTINGS'"</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>sfc /scannow</code> outputs <code>Windows Resource Protection did not find any integrity violations</code>, and DISM returns <code>The restore operation completed successfully. The operation completed successfully.</code>
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the functional difference between `sfc /scannow` and `dism /online /cleanup-image /restorehealth`?</strong><br>
          <em>Answer:</em> `sfc /scannow` checks protected OS files against the local Component Store cache (%WinDir%\WinSxS). If the WinSxS store itself is corrupted, SFC cannot repair files; DISM connects to Windows Update or a clean ISO to repair the corrupted WinSxS store first.<br><br>
          <strong>Q2: Why should hard disk defragmentation (`defrag`) never be run in traditional mode on Solid State Drives (SSDs)?</strong><br>
          <em>Answer:</em> SSDs have zero mechanical rotational latency and uniform flash access times. Traditional defragmentation causes unnecessary flash memory write cycles, wearing out NAND flash cells prematurely. SSDs instead require the TRIM command (`defrag /O`).
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Laboratory Practicum Complete • 10 Experiments Verified</span>
    <span>Practical Manual • Page 10</span>
  </div>
</article>
"""
