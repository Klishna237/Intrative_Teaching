# -*- coding: utf-8 -*-
IT_UNIT5_HTML = r"""
<!-- ==========================================================================
     UNIT 05: OS TROUBLESHOOTING AND COMMAND LINE
     ========================================================================== -->
<article class="doc-page" id="sec13">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 1</span>
          <span>Enterprise CLI Commands • Page 10</span>
        </header>

        <h2 class="section-title"><span class="sec-num">13.</span> Core Administrative CLI Commands (In-Depth)</h2>
        <p>
          Mastery of command-line administration tools is essential for Windows system administrators and IT security
          engineers. Below are comprehensive syntaxes and real-world enterprise use cases for <code>net user</code>,
          <code>net localgroup</code>, <code>icacls</code>, and <code>netsh</code>.
        </p>

        <!-- Command 1: net user -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--primary);">A. User Account
          Management (<code>net user</code>)</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span>
              <span class="term-dot dot-yellow"></span>
              <span class="term-dot dot-green"></span>
              <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Administrator
                Command Prompt — net user</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy"
                  style="width:12px;height:12px;"></i> <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="code-comment">:: List all local user accounts on the system</span>
<span class="c-kw">net user</span>

<span class="code-comment">:: View detailed security metadata, password age, and group memberships for a user</span>
<span class="c-kw">net user</span> <span class="c-var">john_doe</span>

<span class="code-comment">:: Create a new local user account with a strong initial password</span>
<span class="c-kw">net user</span> <span class="c-var">alice_dev</span> <span class="c-str">"P@ssw0rd2026!"</span> <span class="c-flg">/add</span> <span class="c-flg">/fullname:</span><span class="c-str">"Alice Developer"</span> <span class="c-flg">/comment:</span><span class="c-str">"R&amp;D Team"</span>

<span class="code-comment">:: Force user to change password on next interactive logon</span>
<span class="c-kw">net user</span> <span class="c-var">alice_dev</span> <span class="c-flg">/logonpasswordchg:yes</span>

<span class="code-comment">:: Disable a compromised or departing user account immediately</span>
<span class="c-kw">net user</span> <span class="c-var">contractor1</span> <span class="c-flg">/active:no</span>

<span class="code-comment">:: Set an expiration date for a temporary account (DD/MM/YYYY)</span>
<span class="c-kw">net user</span> <span class="c-var">intern_bob</span> <span class="c-flg">/expires:31/12/2026</span>

<span class="code-comment">:: Delete a user account permanently from the local SAM database</span>
<span class="c-kw">net user</span> <span class="c-var">temp_user</span> <span class="c-flg">/delete</span></code></pre>
          </div>
        </div>

        <!-- Command 2: net localgroup -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--accent-purple);">B. Local
          Security Group Management (<code>net localgroup</code>)</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span>
              <span class="term-dot dot-yellow"></span>
              <span class="term-dot dot-green"></span>
              <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Administrator
                Command Prompt — net localgroup</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy"
                  style="width:12px;height:12px;"></i> <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="code-comment">:: List all local security groups on the computer</span>
<span class="c-kw">net localgroup</span>

<span class="code-comment">:: Inspect members of the privileged local Administrators group</span>
<span class="c-kw">net localgroup</span> <span class="c-var">Administrators</span>

<span class="code-comment">:: Create a new custom local group for project access</span>
<span class="c-kw">net localgroup</span> <span class="c-var">"DevOps_Engineers"</span> <span class="c-flg">/add</span> <span class="c-flg">/comment:</span><span class="c-str">"CI/CD Pipeline Access"</span>

<span class="code-comment">:: Add a local user to the local Administrators group</span>
<span class="c-kw">net localgroup</span> <span class="c-var">Administrators</span> <span class="c-var">alice_dev</span> <span class="c-flg">/add</span>

<span class="code-comment">:: Remove a user from a security group</span>
<span class="c-kw">net localgroup</span> <span class="c-var">"Remote Desktop Users"</span> <span class="c-var">bob_intern</span> <span class="c-flg">/delete</span>

<span class="code-comment">:: Delete a custom local group (does not delete member user accounts)</span>
<span class="c-kw">net localgroup</span> <span class="c-var">"Old_Project_Group"</span> <span class="c-flg">/delete</span></code></pre>
          </div>
        </div>

        <!-- Command 3: icacls -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--accent-emerald);">C. NTFS File
          &amp; Folder Access Control Lists (<code>icacls</code>)</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span>
              <span class="term-dot dot-yellow"></span>
              <span class="term-dot dot-green"></span>
              <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Administrator
                Command Prompt — icacls</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy"
                  style="width:12px;height:12px;"></i> <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="code-comment">:: Display current DACL permissions on a confidential directory</span>
<span class="c-kw">icacls</span> <span class="c-str">"C:\FinanceData"</span>

<span class="code-comment">:: Grant Read &amp; Execute permission to FinanceUsers group with folder/subfolder inheritance</span>
<span class="c-kw">icacls</span> <span class="c-str">"C:\FinanceData"</span> <span class="c-flg">/grant</span> <span class="c-var">FinanceUsers</span>:(OI)(CI)RX

<span class="code-comment">:: Grant Full Control (F) to Administrator and Modify (M) to Managers</span>
<span class="c-kw">icacls</span> <span class="c-str">"C:\FinanceData"</span> <span class="c-flg">/grant:r</span> <span class="c-var">Managers</span>:(OI)(CI)M

<span class="code-comment">:: Explicitly DENY Write (W) permission to Contractors group (Deny overrides Allow!)</span>
<span class="c-kw">icacls</span> <span class="c-str">"C:\FinanceData"</span> <span class="c-flg">/deny</span> <span class="c-var">Contractors</span>:(OI)(CI)W

<span class="code-comment">:: Disable permission inheritance and copy current inherited ACEs as explicit ACEs</span>
<span class="c-kw">icacls</span> <span class="c-str">"C:\SecureVault"</span> <span class="c-flg">/inheritance:d</span>

<span class="code-comment">:: Backup ACLs of an entire directory tree into a text file</span>
<span class="c-kw">icacls</span> <span class="c-str">"C:\FinanceData"</span> <span class="c-flg">/save</span> <span class="c-str">"C:\Backup\Finance_ACLs.txt"</span> <span class="c-flg">/t</span>

<span class="code-comment">:: Restore backed-up ACL permissions</span>
<span class="c-kw">icacls</span> <span class="c-str">"C:\"</span> <span class="c-flg">/restore</span> <span class="c-str">"C:\Backup\Finance_ACLs.txt"</span></code></pre>
          </div>
        </div>

        <!-- Command 4: netsh -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--accent-rose);">D. Network Shell
          Configuration (<code>netsh</code>)</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span>
              <span class="term-dot dot-yellow"></span>
              <span class="term-dot dot-green"></span>
              <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Administrator
                Command Prompt — netsh</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy"
                  style="width:12px;height:12px;"></i> <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="code-comment">:: Display IP address configurations for all network interfaces</span>
<span class="c-kw">netsh interface ipv4 show addresses</span>

<span class="code-comment">:: Assign a Static IPv4 address, Subnet Mask, and Default Gateway</span>
<span class="c-kw">netsh interface ipv4 set address</span> <span class="c-flg">name=</span><span class="c-str">"Ethernet0"</span> <span class="c-flg">static</span> <span class="c-num">192.168.1.150</span> <span class="c-num">255.255.255.0</span> <span class="c-num">192.168.1.1</span>

<span class="code-comment">:: Configure Primary Static DNS Server (Google Public DNS)</span>
<span class="c-kw">netsh interface ipv4 set dns</span> <span class="c-flg">name=</span><span class="c-str">"Ethernet0"</span> <span class="c-flg">static</span> <span class="c-num">8.8.8.8</span>

<span class="code-comment">:: Switch interface back to dynamic DHCP for IP and DNS</span>
<span class="c-kw">netsh interface ipv4 set address</span> <span class="c-flg">name=</span><span class="c-str">"Ethernet0"</span> <span class="c-flg">dhcp</span>
<span class="c-kw">netsh interface ipv4 set dns</span> <span class="c-flg">name=</span><span class="c-str">"Ethernet0"</span> <span class="c-flg">dhcp</span>

<span class="code-comment">:: Create an inbound Windows Defender Firewall rule to allow port 8080 TCP</span>
<span class="c-kw">netsh advfirewall firewall add rule</span> <span class="c-flg">name=</span><span class="c-str">"AppServer_8080"</span> <span class="c-flg">dir=</span>in <span class="c-flg">action=</span>allow <span class="c-flg">protocol=</span>TCP <span class="c-flg">localport=</span><span class="c-num">8080</span>

<span class="code-comment">:: Export saved Wi-Fi profiles and cleartext pre-shared keys (passwords)</span>
<span class="c-kw">netsh wlan show profile</span> <span class="c-flg">name=</span><span class="c-str">"CorpWiFi"</span> <span class="c-flg">key=</span>clear</code></pre>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 01</span>
        </footer>
      </article>

<!-- Page 28: Windows OS Problem Troubleshooting -->
<article class="doc-page" id="it5-troubleshoot-win">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 05 • Page 02</span>
    <span class="meta-tag">Bloom's: Apply / Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">28.</span> Windows Problem Triage: Boot Failures, BSOD Crash Dumps &amp; Bottlenecks
  </h2>

  <p class="lead-para">
    Enterprise operating system maintenance requires structured isolation of hardware versus software fault domains. Technicians must methodically analyze UEFI/BCD boot chain corruptions, decode Blue Screen of Death (BSOD) stop errors via memory dump debugging, and resolve thread deadlock and paging performance bottlenecks.
  </p>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="alert-octagon"></i> WINDOWS BOOT ENVIRONMENT REPAIR ARCHITECTURE</div>
    <div class="callout-body">
      When Windows fails to boot, recovery procedures depend on firmware partitioning:
      <ul style="margin-top:0.4rem; margin-left:1.25rem; line-height:1.6;">
        <li><strong>UEFI / GPT Boot Chain:</strong> Firmware executes <code>\EFI\Microsoft\Boot\bootmgfw.efi</code> located on the FAT32 EFI System Partition (ESP). It loads the Boot Configuration Data (BCD) store, then executes <code>winload.efi</code> to initialize the NT kernel (<code>ntoskrnl.exe</code>).</li>
        <li><strong>Legacy BIOS / MBR Boot Chain:</strong> The BIOS loads Sector 0 (MBR), which parses partition tables to locate the active partition and executes <code>bootmgr</code>, reading the root BCD store.</li>
      </ul>
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Critical BSOD Stop Codes &amp; Kernel BugCheck Analysis
  </h3>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>BSOD Stop Error</th>
          <th>BugCheck Code</th>
          <th>Underlying Kernel Root Cause</th>
          <th>Triage &amp; Remediation Procedure</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>CRITICAL_PROCESS_DIED</strong></td>
          <td><code>0x000000EF</code></td>
          <td>A core Windows system process (e.g. <code>csrss.exe</code>, <code>wininit.exe</code>, or <code>services.exe</code>) terminated unexpectedly.</td>
          <td>Execute <code>sfc /scannow</code> and <code>dism /online /cleanup-image /restorehealth</code> from WinPE; check system drive for bad sectors.</td>
        </tr>
        <tr>
          <td><strong>IRQL_NOT_LESS_OR_EQUAL</strong></td>
          <td><code>0x0000000A</code></td>
          <td>Kernel-mode process attempted to access pageable memory at an Interrupt Request Level (IRQL) that was too high.</td>
          <td>Defective or buggy third-party kernel driver (.sys) or faulty physical RAM. Inspect minidump file via WinDbg <code>!analyze -v</code> to identify offending driver.</td>
        </tr>
        <tr>
          <td><strong>PAGE_FAULT_IN_NONPAGED_AREA</strong></td>
          <td><code>0x00000050</code></td>
          <td>Requested system memory was invalid. The kernel dereferenced a null pointer or memory page marked as non-existent.</td>
          <td>Hardware memory failure, L2/L3 CPU cache corruption, or antivirus filter driver bug. Run Windows Memory Diagnostic (<code>mdsched.exe</code>).</td>
        </tr>
        <tr>
          <td><strong>INACCESSIBLE_BOOT_DEVICE</strong></td>
          <td><code>0x0000007B</code></td>
          <td>I/O subsystem failed to initialize the boot storage device driver (SATA/NVMe controller) during Phase 1 kernel init.</td>
          <td>Storage driver mismatch after cloning or switching SATA mode (IDE &rarr; AHCI &rarr; RAID/RST). Boot into Safe Mode to force storage driver redetection.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="terminal-block full-width-module">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span>
        <span class="term-dot dot-yellow"></span>
        <span class="term-dot dot-green"></span>
        <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> WinPE / Command Prompt • Bootloader &amp; Component Store Triage</span>
      </div>
      <div class="terminal-actions">
        <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
        <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
      </div>
    </div>
    <div class="terminal-body">
      <pre class="code-pre"><code><span class="code-comment"># 1. Repair Master Boot Record and partition boot sectors</span>
bootrec /fixmbr
bootrec /fixboot

<span class="code-comment"># 2. Scan disks for Windows installations and rebuild corrupted BCD store</span>
bootrec /scanos
bootrec /rebuildbcd

<span class="code-comment"># 3. For UEFI GPT systems, reinstall fresh UEFI boot files to EFI System Partition</span>
bcdboot C:\Windows /s S: /f UEFI

<span class="code-comment"># 4. Repair Windows Component Store and protected system binaries</span>
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow</code></pre>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Windows Networking Administration &amp; Firewall</span>
    <span>Unit 05 • Page 02</span>
  </div>
</article>

<!-- Page 29: Windows Networking Administration & Firewall -->
<article class="doc-page" id="it5-windows-networking">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 05 • Page 03</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">29.</span> Windows Networking Administration, Firewall Rules &amp; Remote Access (RDP)
  </h2>

  <p class="lead-para">
    Windows enterprise administration requires fine-grained control over network adapter configurations, host-based stateful packet filtering via Windows Defender Firewall with Advanced Security, secure Server Message Block (SMB 3.1.1) file sharing, and encrypted Remote Desktop Protocol (RDP) administration.
  </p>

  <div class="callout callout-key">
    <div class="callout-label"><i data-lucide="shield-check"></i> THE THREE WINDOWS DEFENDER FIREWALL NETWORK PROFILES</div>
    <div class="callout-body">
      Windows automatically assigns one of three security profiles to each connected network interface:
      <ul style="margin-top:0.4rem; margin-left:1.25rem; line-height:1.6;">
        <li><strong>Domain Profile:</strong> Applied automatically when the client authenticates against an Active Directory Domain Controller. Most permissive profile; enables administrative RPC, WinRM, and management shares.</li>
        <li><strong>Private Profile:</strong> User-designated for trusted home or branch office networks. Enables network discovery and file/printer sharing between trusted endpoints.</li>
        <li><strong>Public Profile:</strong> Default for untrusted networks (airports, coffee shops, direct Internet). Blocks all inbound connection attempts and disables network discovery.</li>
      </ul>
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Windows Network Diagnostics &amp; Firewall Management CLI
  </h3>

  <div class="terminal-block full-width-module">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span>
        <span class="term-dot dot-yellow"></span>
        <span class="term-dot dot-green"></span>
        <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell &amp; CMD • Network Configuration &amp; Firewall Rules</span>
      </div>
      <div class="terminal-actions">
        <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
        <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
      </div>
    </div>
    <div class="terminal-body">
      <pre class="code-pre"><code><span class="code-comment"># 1. Flush DNS resolver cache and release/renew DHCP lease</span>
ipconfig /flushdns
ipconfig /release && ipconfig /renew

<span class="code-comment"># 2. Inspect active TCP connections and listening process PIDs</span>
netstat -ano | findstr :3389

<span class="code-comment"># 3. Create Windows Defender Firewall rule opening TCP Port 3389 for RDP in Domain Profile</span>
New-NetFirewallRule -DisplayName "Allow Enterprise RDP" -Direction Inbound `
    -Protocol TCP -LocalPort 3389 -Action Allow -Profile Domain

<span class="code-comment"># 4. Enable Remote Desktop and enforce Network Level Authentication (NLA) via Registry</span>
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "UserAuthentication" -Value 1</code></pre>
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    2. SMB Share Permissions vs NTFS File Permissions
  </h3>

  <p>
    When resources are accessed over the network, Windows evaluates both <strong>Share Permissions</strong> and <strong>NTFS File Permissions</strong>. The effective permission is always the <strong>Most Restrictive Rule</strong>:
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Scenario</th>
          <th>SMB Share Permission</th>
          <th>NTFS File Permission</th>
          <th>Effective Remote Network Permission</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Scenario A</td>
          <td>Full Control</td>
          <td>Read</td>
          <td><strong>Read Only</strong> (NTFS restricts write access)</td>
        </tr>
        <tr>
          <td>Scenario B</td>
          <td>Read Only</td>
          <td>Full Control</td>
          <td><strong>Read Only</strong> (Share restricts remote modifications)</td>
        </tr>
        <tr>
          <td>Scenario C</td>
          <td>Change (Read/Write)</td>
          <td>Modify (Read/Write/Delete)</td>
          <td><strong>Modify</strong> (Harmonized read/write access granted)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Linux Architecture &amp; Shell Mechanics</span>
    <span>Unit 05 • Page 03</span>
  </div>
</article>

<article class="doc-page" id="sec28-bash">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 3</span>
          <span>Linux Architecture &amp; Shell • Page 18</span>
        </header>

        <div class="doc-hero">
          <div class="doc-kicker">Unit 03 • Linux &amp; Bash Scripting Fundamentals</div>
          <h1 class="doc-main-title">Linux Operating System &amp; Bash Shell Scripting Mastery</h1>
          <p class="doc-subtitle">
            A structured, hands-on guide from foundational Unix concepts, variables, operators, and control flow to
            advanced scripting, process automation, system monitoring, and 10 production-ready practical programs.
          </p>
          <div class="meta-pills-bar">
            <span class="meta-pill"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Module: <strong>Unit
                03</strong></span>
            <span class="meta-pill"><i data-lucide="code" style="width:13px;height:13px;"></i> Shell: <strong>GNU Bash
                5.x</strong></span>
            <span class="meta-pill"><i data-lucide="check-circle" style="width:13px;height:13px;"></i> Questions:
              <strong>30 MCQs + 9 Subjective + 10 Programs</strong></span>
            <span class="meta-pill"><i data-lucide="user" style="width:13px;height:13px;"></i> Academic Engineering Publication</span>
          </div>
        </div>

        <h2 class="section-title"><span class="sec-num">28.</span> Linux OS Architecture &amp; Shell Mechanics</h2>
        <p>
          Linux is a modular, Unix-like operating system based on a <strong>Monolithic Kernel</strong> with dynamic
          loadable kernel modules (LKMs). The system is organized into concentric execution tiers:
        </p>

        <div class="diagram-container">
          <div class="diagram-caption"><i data-lucide="layers" style="width:14px;height:14px;"></i> Linux Architectural
            Hierarchy</div>
          <div class="arch-stack-visual">
            <div class="arch-chip" style="background:var(--primary-light); border-color:var(--primary-border);">
              <strong>1. User Applications &amp; Utilities:</strong> Bash scripts, Python, GCC, Vim, Apache, Nginx, GUI
              Desktop.
            </div>
            <div class="arch-chip" style="border-left:4px solid var(--accent-purple);">
              <strong>2. GNU C Library (glibc) &amp; Shell:</strong> Standard C library functions, command interpreter,
              system call wrappers.
            </div>
            <div class="arch-chip" style="border-left:4px solid var(--accent-rose);">
              <strong>3. System Call Interface (SCI):</strong> <code>sys_read()</code>, <code>sys_write()</code>,
              <code>sys_fork()</code>, <code>sys_execve()</code>.
            </div>
            <div class="arch-chip" style="border-left:4px solid var(--accent-emerald);">
              <strong>4. Linux Monolithic Kernel:</strong> Process Scheduler (CFS), Virtual File System (VFS), Memory
              Management, Network Stack.
            </div>
            <div class="arch-chip" style="background:var(--box-hood-bg); border-color:var(--border-strong);">
              <strong>5. Physical Hardware:</strong> CPU, Physical RAM, NVMe/SATA SSDs, NIC, GPU, Peripheral Buses.
            </div>
          </div>
        </div>

        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1.25rem;">The Shebang Line &amp; Execution
          Mechanics</h3>
        <p>
          A Bash script is a plain-text ASCII/UTF-8 file containing a sequence of shell commands. The first line of an
          executable script must contain the <strong>Shebang</strong> (<code>#!</code>) followed by the absolute
          interpreter path:
        </p>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Bash Shebang Options</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="code-comment"># Direct standard path</span>
<span class="c-shebang">#!/bin/bash</span>

<span class="code-comment"># Portable best practice (searches system PATH dynamically)</span>
<span class="c-shebang">#!/usr/bin/env bash</span></code></pre>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>
<article class="doc-page" id="sec29-syntax">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 3</span>
          <span>Syntax, Permissions &amp; Variables • Page 19</span>
        </header>

        <h2 class="section-title"><span class="sec-num">29.</span> Script Permissions, Comments &amp; Execution Modes
        </h2>
        <p>
          Before a script can be executed directly as a binary, it must be granted execute (<code>+x</code>) permissions
          in Linux:
        </p>

        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Linux Script Execution Workflow</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="code-comment"># Grant execute permissions to the script owner</span>
<span class="c-kw">chmod</span> <span class="c-flg">+x</span> script.sh

<span class="code-comment"># Method 1: Execute directly in a spawned subshell (requires +x permission)</span>
./script.sh

<span class="code-comment"># Method 2: Pass script as argument to bash interpreter (does NOT require +x)</span>
<span class="c-kw">bash</span> script.sh

<span class="code-comment"># Method 3: Source script into CURRENT shell environment (retains variables in current shell)</span>
<span class="c-kw">source</span> script.sh
<span class="code-comment"># or:</span> . script.sh</code></pre>
          </div>
        </div>

        <h2 class="section-title" id="sec30-vars"><span class="sec-num">30.</span> Variables, Data Types &amp; Quoting
          Rules</h2>
        <p>
          Variables in Bash are dynamically typed and treated as untyped character strings by default. There must be
          <strong>NO WHITESPACE</strong> around the assignment operator (<code>=</code>).
        </p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 25%;">Quoting Mechanism</th>
                <th style="width: 35%;">Syntax Example</th>
                <th style="width: 40%;">Behavior &amp; Variable Expansion</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Single Quotes (<code>'...'</code>)</strong></td>
                <td><code>echo 'User is $USER'</code> &rarr; <code>User is $USER</code></td>
                <td><strong>Strictly Literal:</strong> Disables all variable interpolation, command substitution, and
                  escape characters.</td>
              </tr>
              <tr>
                <td><strong>Double Quotes (<code>"..."</code>)</strong></td>
                <td><code>echo "User is $USER"</code> &rarr; <code>User is john</code></td>
                <td><strong>Weak Quoting:</strong> Expands variables (<code>$VAR</code>), command substitutions
                  (<code>$(...)</code>), and arithmetic (<code>$((...))</code>), but preserves internal whitespace.</td>
              </tr>
              <tr>
                <td><strong>Command Sub (<code>$(...)</code>)</strong></td>
                <td><code>KERNEL_VER=$(uname -r)</code></td>
                <td>Executes the inner command in a subshell and captures its standard output into the variable.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>
"""
