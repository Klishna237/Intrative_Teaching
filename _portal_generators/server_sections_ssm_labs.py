# -*- coding: utf-8 -*-
"""
Server Administration Portal - Practical Laboratory Manual (Master Gold Standard)
10 Comprehensive Hands-On Server Practicals with Terminal CLI, Verification, and Viva Questions
Exact layout, classes, and styling matching IT Fundamentals and Cloud Administration portals.
"""

SERVER_LABS_HTML = r"""
<!-- ===================================================================
     HANDS-ON LABORATORY MANUAL: 10 ENTERPRISE SERVER PRACTICALS
     =================================================================== -->
<article class="doc-page" id="server-labs-manual">
  <header class="doc-page-header">
    <span class="page-header-meta">Curriculum Lab Manual • Hands-On Enterprise Practicals</span>
    <h2 class="section-title"><span class="sec-num">LAB.1</span> Enterprise Server Administration Laboratory Manual: 10 Rigorous Practicals</h2>
    <p class="lead-para">
      Conforming strictly to the Department of Computer Science &amp; Engineering Server Administration syllabus, this lab manual delivers step-by-step procedures, hardware inspection, terminal commands (PowerShell 7 and Linux Bash), expected execution outputs, and oral examination (Viva Voce) questions for ten foundational server engineering experiments.
    </p>
  </header>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="terminal"></i> LABORATORY PREREQUISITES &amp; ENVIRONMENT SETUP</div>
    <div class="callout-body">
      Ensure you have access to a hypervisor host (Hyper-V Server 2022 or VMware ESXi 8.0) with a minimum of 32 GB RAM, ISO media for Windows Server 2022 Datacenter and RHEL 9, PowerShell 7.4+ installed, and administrator credentials for the test forest domain.
    </div>
  </div>

  <!-- LAB 1 -->
  <div class="subj-card revealed" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 01</div>
      <div class="subj-title">Enterprise Server Operating System Installation (Windows Server 2022 / RHEL 9) in Virtualized Environment</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Provision a Type-1 virtualized server environment (Hyper-V or VMware ESXi), configure virtual hardware baseline (4 vCPUs, 16GB ECC RAM, 100GB GPT VHDX), install Windows Server 2022 Datacenter, and execute post-installation initialization.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Type-1 Hypervisor workstation, Windows Server 2022 Datacenter ISO, PowerShell 7 administrative console, and virtual switch configuration sheet.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • Initial Server Post-Installation Bootstrap</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Rename host computer to enterprise naming convention</span>
Rename-Computer -NewName "SRV-DC01" -Restart -Force

<span class="code-comment"># 2. Configure Static IPv4 address, subnet mask, and DNS</span>
New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress 192.168.10.10 -PrefixLength 24 -DefaultGateway 192.168.10.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.10.10", "1.1.1.1")

<span class="code-comment"># 3. Enable Remote Desktop and configure firewall</span>
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Executing <code>Get-ComputerInfo | Select-Object WindowsProductName, CsDNSHostName, OsArchitecture</code> displays <code>Windows Server 2022 Datacenter</code>, hostname <code>SRV-DC01</code>, and <code>Test-NetConnection -Port 3389 -ComputerName localhost</code> returns <code>TcpTestSucceeded: True</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why is Windows Server Core edition preferred over Desktop Experience in enterprise datacenters?</strong><br>
          <em>Answer:</em> Server Core omits the GUI shell, reducing disk footprint by ~4GB, lowering memory overhead, eliminating ~70% of monthly security patch reboots, and drastically reducing attack surface.<br><br>
          <strong>Q2: What is the purpose of sysprep before imaging a template VM?</strong><br>
          <em>Answer:</em> <code>sysprep /generalize</code> removes machine-specific state (including unique machine SIDs, driver associations, and event logs) so cloned VMs do not duplicate SIDs across the Active Directory domain.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 2 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 02</div>
      <div class="subj-title">Server Firmware Management: UEFI / BIOS Hardening &amp; Out-of-Band Redfish Updates</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure secure UEFI firmware settings, enable hardware virtualization extensions (VT-x/AMD-V), configure TPM 2.0 security, and execute an out-of-band firmware flash via Redfish RESTful APIs.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Enterprise server with Baseboard Management Controller (iDRAC9 / iLO 5), out-of-band dedicated management network, and cURL / REST client.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Bash / cURL • DMTF Redfish Out-of-Band Power Cycle</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Query BMC power state via DMTF Redfish REST API</span>
curl -k -u "root:calvin" -X GET https://192.168.100.50/redfish/v1/Systems/System.Embedded.1

<span class="code-comment"># 2. Query TPM and SecureBoot status from firmware schema</span>
curl -k -u "root:calvin" -X GET https://192.168.100.50/redfish/v1/Systems/System.Embedded.1/SecureBoot

<span class="code-comment"># 3. Issue remote graceful restart command to BMC</span>
curl -k -u "root:calvin" -X POST \
    -H "Content-Type: application/json" \
    -d '{"ResetType": "GracefulRestart"}' \
    https://192.168.100.50/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          The Redfish endpoint responds with HTTP <code>204 No Content</code> or <code>200 OK</code> with JSON attribute <code>"PowerState": "On"</code> and <code>"SecureBootEnable": true</code>, confirming remote out-of-band administration without requiring in-band OS connectivity.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the DMTF Redfish standard and why does it supersede IPMI?</strong><br>
          <em>Answer:</em> Redfish is an open industry standard utilizing modern RESTful HTTPS interfaces and JSON payloads. It replaces legacy IPMI 2.0, which suffers from severe protocol vulnerabilities (cipher 0 flaws), lack of granular encryption, and complex binary formats.<br><br>
          <strong>Q2: Why must BMC management traffic reside on a dedicated out-of-band (OOB) VLAN?</strong><br>
          <em>Answer:</em> BMCs possess raw, direct hardware access (including remote virtual media and physical power controls). Segregating OOB ports prevents unauthorized tenants or attackers on data networks from compromising bare-metal server firmware.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 3 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 03</div>
      <div class="subj-title">Hardware Component Diagnostics: NUMA Topologies, ECC RAM &amp; PCIe Expansion</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Inspect physical processor topology, verify multi-socket NUMA node assignments, validate ECC SECDED memory error thresholds, and inspect PCIe link negotiations.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Dual-socket server running Enterprise Linux (RHEL 9 / Rocky Linux), <code>numactl</code>, <code>edac-util</code>, <code>pciutils</code>, and IPMI system event logs.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Linux CLI • NUMA &amp; Hardware Diagnostics</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Inspect multi-socket NUMA node layout and core bindings</span>
numactl --hardware

<span class="code-comment"># 2. View ECC memory errors recorded in Linux kernel EDAC subsystem</span>
edac-util -v

<span class="code-comment"># 3. Verify PCIe 4.0/5.0 link width (x16) and transfer speed (16.0 GT/s)</span>
lspci -vv -s 01:00.0 | grep -E "(LnkCap|LnkSta)"</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>numactl</code> outputs <code>available: 2 nodes (0-1)</code> with equal RAM allocated per node and low cross-node latency distance (10 local, 21 remote). <code>edac-util</code> confirms zero Uncorrected Errors (UE) across all DIMM channels.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is NUMA and why does cross-node memory access impact database performance?</strong><br>
          <em>Answer:</em> In Non-Uniform Memory Access, each physical CPU socket owns local memory channels. Accessing memory wired to another socket traverses high-speed inter-socket interconnects (UPI/Infinity Fabric), incurring higher latency (typically 2x to 3x) and reducing transaction throughput.<br><br>
          <strong>Q2: How does ECC SECDED protect against silent data corruption?</strong><br>
          <em>Answer:</em> Single Error Correction, Double Error Detection uses 8 extra Hamming parity bits per 64-bit word. It autonomously detects and corrects single-bit flips on-the-fly, while halting the kernel upon double-bit flips to prevent corrupted data from writing to disk.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 4 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 04</div>
      <div class="subj-title">Storage Technologies: Software &amp; Hardware RAID Configuration (RAID 0, 1, 5, 10)</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Initialize 4 block devices, configure a software RAID 5 array with a hot spare using Linux <code>mdadm</code> or Windows Storage Spaces, simulate a disk drive failure, and observe autonomous parity rebuild.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Linux test workstation with 4 raw SATA/NVMe disks (<code>sdb</code>, <code>sdc</code>, <code>sdd</code>, <code>sde</code>), <code>mdadm</code> utility, and XFS filesystem tools.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Linux CLI • mdadm RAID 5 Provisioning &amp; Failure Test</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create RAID 5 array with 3 active drives and 1 hot spare</span>
sudo mdadm --create --verbose /dev/md0 --level=5 --raid-devices=3 /dev/sdb /dev/sdc /dev/sdd --spare-devices=1 /dev/sde

<span class="code-comment"># 2. Format with XFS filesystem and mount to data directory</span>
sudo mkfs.xfs /dev/md0
sudo mkdir -p /mnt/raid5_data && sudo mount /dev/md0 /mnt/raid5_data

<span class="code-comment"># 3. Simulate hardware failure of disk /dev/sdb and monitor rebuild</span>
sudo mdadm --manage /dev/md0 --fail /dev/sdb
cat /proc/mdstat</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>cat /proc/mdstat</code> indicates <code>/dev/sdb[0](F)</code> is marked faulty, while hot spare <code>/dev/sde[3]</code> immediately transitions to <code>recovery = xx% (speed=xxxxK/sec)</code>. The mounted filesystem remains fully online and accessible throughout rebuild.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why does RAID 5 suffer from the "Write Hole" problem during power outages?</strong><br>
          <em>Answer:</em> RAID 5 updates data and parity in two separate I/O operations. A power loss between the data write and parity update produces a desynchronization called the write hole, corrupting parity calculations upon reboot unless protected by battery-backed write cache (BBWC).<br><br>
          <strong>Q2: What is the minimum number of disks required for RAID 5, RAID 6, and RAID 10?</strong><br>
          <em>Answer:</em> RAID 5 requires a minimum of 3 disks (1 parity tolerance); RAID 6 requires a minimum of 4 disks (dual parity tolerance); RAID 10 requires a minimum of 4 disks (mirrored stripes).
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 5 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 05</div>
      <div class="subj-title">Enterprise Network Services: Static IP, Active Directory Integrated DNS &amp; DHCP Failover</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Deploy Windows Server DHCP and DNS roles, configure a high-availability DHCP Failover relationship in Load-Sharing mode across two servers, and test lease synchronization.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Two Windows Server 2022 VMs (<code>SRV-DHCP01</code> and <code>SRV-DHCP02</code>) joined to an Active Directory domain, PowerShell administrative shell.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • DHCP Failover Deployment</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Install DHCP server role and management tools</span>
Install-WindowsFeature -Name DHCP -IncludeManagementTools -Restart

<span class="code-comment"># 2. Create enterprise DHCP Scope</span>
Add-DhcpServerv4Scope -Name "StudentLabScope" -StartRange 10.0.1.100 -EndRange 10.0.1.200 -SubnetMask 255.255.255.0

<span class="code-comment"># 3. Configure 50/50 Load-Sharing Failover with secondary partner server</span>
Add-DhcpServerv4Failover -Name "DHCP-HA-Pair" -ScopeId 10.0.1.0 `
    -PartnerServer "SRV-DHCP02.corp.local" -Mode LoadBalance -LoadPercent 50 `
    -SharedSecret "EnterpriseSecretPassword123!"</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Executing <code>Get-DhcpServerv4Failover -Name "DHCP-HA-Pair"</code> returns <code>State: Normal</code>, <code>Mode: LoadBalance</code>, and leasing a test client registers active IP assignments synchronously in both DHCP consoles.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What are the two modes of Windows Server DHCP Failover?</strong><br>
          <em>Answer:</em> 1. <strong>Load Balance mode</strong> (active-active) distributes lease requests according to a percentage ratio (e.g. 50/50). 2. <strong>Hot Standby mode</strong> (active-passive) routes 100% of leases through the primary server until a failure occurs.<br><br>
          <strong>Q2: Why must a DHCP Server be authorized in Active Directory before issuing leases?</strong><br>
          <em>Answer:</em> Active Directory authorization prevents rogue DHCP servers from introducing IP address conflicts or delivering malicious default gateway settings (Man-in-the-Middle attacks) to domain clients.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 6 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 06</div>
      <div class="subj-title">Enterprise Server Roles: Active Directory Domain Services (AD DS) Forest Promotion</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Promote a standalone Windows Server 2022 to an enterprise Domain Controller, establishing a new forest root domain (<code>corp.contoso.com</code>) with DNS integration and global catalog services.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Clean Windows Server 2022 instance, static IP network configuration, AD DS role installer, and DSRM restore credentials.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • AD DS Forest Promotion</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Install AD DS server feature and management consoles</span>
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

<span class="code-comment"># 2. Promote server to root Domain Controller of new Active Directory Forest</span>
Install-ADDSForest -DomainName "corp.contoso.com" -DomainNetbiosName "CORP" `
    -InstallDns:$true -ForestMode "WinThreshold" -DomainMode "WinThreshold" `
    -SafeModeAdministratorPassword (ConvertTo-SecureString "DSRMPassword123!" -AsPlainText -Force)</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          After autonomous reboot, run <code>dcdiag /test:DNS /v</code> and <code>Get-ADDomainController</code>. Tests verify that AD DS partition databases (<code>NTDS.dit</code>) and the SYSVOL share are advertising properly across the network.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What are the 5 FSMO roles in an Active Directory forest?</strong><br>
          <em>Answer:</em> Forest-wide: Schema Master, Domain Naming Master. Domain-wide: RID Master, PDC Emulator, Infrastructure Master.<br><br>
          <strong>Q2: What is the function of the SYSVOL directory?</strong><br>
          <em>Answer:</em> SYSVOL is a shared folder replicated to all Domain Controllers via Distributed File System Replication (DFSR) storing Group Policy Objects (GPOs), login scripts, and domain security policies.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 7 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 07</div>
      <div class="subj-title">Type-1 Hypervisor Management: Hyper-V VM Provisioning, Virtual Switches &amp; VHDX</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure Hyper-V Virtual Switches (External with VLAN trunking), create Generation 2 virtual machines, and attach dynamically expanding VHDX storage disks.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows Server 2022 with Hyper-V role, physical NIC adapter, PowerShell Hyper-V module.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • Hyper-V VM Creation</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create External Virtual Switch connected to physical NIC</span>
New-VMSwitch -Name "vSwitch-Production" -NetAdapterName "Ethernet0" -AllowManagementOS $true

<span class="code-comment"># 2. Provision Generation 2 VM with 4GB startup memory</span>
New-VM -Name "VM-AppServer01" -Generation 2 -MemoryStartupBytes 4GB -SwitchName "vSwitch-Production"

<span class="code-comment"># 3. Create dynamic VHDX and attach to SCSI controller</span>
New-VHD -Path "C:\Hyper-V\Virtual Hard Disks\AppServer01.vhdx" -SizeBytes 60GB -Dynamic
Add-VMHardDiskDrive -VMName "VM-AppServer01" -Path "C:\Hyper-V\Virtual Hard Disks\AppServer01.vhdx"</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Running <code>Get-VM -Name "VM-AppServer01" | Select-Object State, Generation, MemoryAssigned</code> outputs state <code>Running</code>, Generation <code>2</code> (UEFI), and confirms virtual switch bindings.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why are Generation 2 VMs superior to Generation 1 VMs in Hyper-V?</strong><br>
          <em>Answer:</em> Generation 2 VMs drop legacy emulated hardware (IDE controllers, legacy NICs, floppy controllers) in favor of synthetic VMBus devices, support UEFI Secure Boot, PXE boot via standard synthetic NICs, and boot faster.<br><br>
          <strong>Q2: What is the maximum capacity of a VHDX file versus legacy VHD?</strong><br>
          <em>Answer:</em> VHDX supports up to 64 TB (compared to 2 TB for legacy VHD) and includes power failure resiliency protection via internal logging mechanisms.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 8 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 08</div>
      <div class="subj-title">Performance Baselines &amp; Monitoring: PerfMon, Resource Monitor &amp; Event Viewer</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Create a User-Defined Data Collector Set in Performance Monitor tracking CPU % Processor Time, Memory Available MBytes, and Disk Avg. Disk sec/Transfer to detect bottlenecks.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows Server workstation, Performance Monitor (<code>perfmon.msc</code>), <code>logman</code> command line, and Sysinternals Suite.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> CMD • Logman Performance Counter Collection</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create Data Collector Set recording baseline hardware metrics every 15 seconds</span>
logman create counter ServerBaseline -s localhost -o C:\PerfLogs\baseline.blg -f bin -si 00:00:15 -c "\Processor(_Total)\% Processor Time" "\Memory\Available MBytes" "\PhysicalDisk(_Total)\Avg. Disk sec/Transfer"

<span class="code-comment"># 2. Start the Data Collector Set</span>
logman start ServerBaseline

<span class="code-comment"># 3. Query collection status</span>
logman query ServerBaseline</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          The binary log file <code>C:\PerfLogs\baseline.blg</code> generates continuously. Opening this log file in <code>perfmon</code> produces graphical waveforms illustrating CPU demand, memory commitments, and disk latency over the collection interval.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What threshold indicates a severe physical disk latency bottleneck in PerfMon?</strong><br>
          <em>Answer:</em> <code>\PhysicalDisk(_Total)\Avg. Disk sec/Transfer</code> sustained above 0.020 seconds (20 milliseconds) indicates noticeable latency, while sustained values exceeding 50 ms indicate a critical storage bottleneck.<br><br>
          <strong>Q2: What is the significance of the "Pages/sec" memory counter?</strong><br>
          <em>Answer:</em> <code>\Memory\Pages/sec</code> measures the rate at which pages are read from or written to disk to resolve hard page faults. Sustained high rates combined with low Available MBytes signify physical RAM starvation.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 9 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 09</div>
      <div class="subj-title">Enterprise Backup &amp; Disaster Recovery: Windows Server Backup &amp; VSS Volume Snapshots</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Install Windows Server Backup, configure a scheduled system state backup using Volume Shadow Copy Service (VSS), delete a critical file, and perform an authoritative restore.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows Server 2022 instance, dedicated secondary backup target volume (<code>E:</code>), <code>wbadmin</code> CLI utility.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • Wbadmin System State Backup</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Install Windows Server Backup feature</span>
Install-WindowsFeature -Name Windows-Server-Backup -IncludeManagementTools

<span class="code-comment"># 2. Initiate non-interactive system state backup to dedicated volume</span>
wbadmin start systemstatebackup -backupTarget:E: -quiet

<span class="code-comment"># 3. Query backup catalog to verify backup snapshot integrity</span>
wbadmin get versions -backupTarget:E:</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          <code>wbadmin get versions</code> displays the backup timestamp, version identifier, and confirms <code>Can recover: Volume(s), File(s), System State</code> with status <code>The backup operation successfully completed</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What components comprise the Windows Server "System State"?</strong><br>
          <em>Answer:</em> Active Directory database (<code>ntds.dit</code>), SYSVOL share, Registry hives, system boot files, COM+ class registration database, and Certificate Services database (if installed).<br><br>
          <strong>Q2: What is the core difference between Authoritative and Non-Authoritative AD restore?</strong><br>
          <em>Answer:</em> In Non-Authoritative restore, the restored Domain Controller synchronizes newer data from replication partners. In Authoritative restore, the admin increments USN version numbers on specific restored objects so they replicate outwards, overwriting changes on all other DCs.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 10 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">LAB 10</div>
      <div class="subj-title">Identity &amp; Access Governance: Active Directory RBAC &amp; Least Privilege Delegation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Design an Organizational Unit (OU) structure, create security groups adhering to the AGDLP principle (Accounts &rarr; Global Groups &rarr; Domain Local Groups &rarr; Permissions), and delegate password-reset privileges without granting Domain Admin access.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Windows Server 2022 Domain Controller, Active Directory Administrative Center, PowerShell Active Directory module.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; Terminal Execution Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> PowerShell • AD User &amp; OU Delegation</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create Organizational Unit (OU) structure</span>
New-ADOrganizationalUnit -Name "Staff" -Path "DC=corp,DC=contoso,DC=com"

<span class="code-comment"># 2. Create Global Security Group for role-based access</span>
New-ADGroup -Name "HelpDeskStaff" -GroupScope Global -Path "OU=Staff,DC=corp,DC=contoso,DC=com"

<span class="code-comment"># 3. Create new user account with secure password</span>
New-ADUser -Name "John Doe" -SamAccountName "jdoe" -UserPrincipalName "jdoe@corp.contoso.com" `
    -AccountPassword (ConvertTo-SecureString "P@ssword2026!" -AsPlainText -Force) -Enabled $true

<span class="code-comment"># 4. Delegate password reset permissions on Staff OU to HelpDeskStaff</span>
$OU = [ADSI]"LDAP://OU=Staff,DC=corp,DC=contoso,DC=com"
$Group = [System.Security.Principal.NTAccount]"CORP\HelpDeskStaff"
$Sid = $Group.Translate([System.Security.Principal.SecurityIdentifier])
$Acl = $OU.ObjectSecurity
$Right = [System.DirectoryServices.ActiveDirectoryRights]::ExtendedRight
$Type = [System.Security.AccessControl.AccessControlType]::Allow
$Guid = [Guid]"00299570-246d-11d0-a768-00aa006e0529"
$Rule = New-Object System.DirectoryServices.ActiveDirectoryAccessRule ($Sid, $Right, $Type, $Guid)
$Acl.AddAccessRule($Rule)
$OU.CommitChanges()</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Testing with user <code>jdoe</code> confirms successful password modification for accounts inside <code>OU=Staff</code>. Attempting to modify accounts in <code>OU=Domain Controllers</code> or <code>CN=Users</code> throws Access Denied, validating Least Privilege boundaries.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What does the AGDLP principle stand for and why is it recommended?</strong><br>
          <em>Answer:</em> <strong>A</strong>ccounts go into <strong>G</strong>lobal groups (representing user business roles), which go into <strong>D</strong>omain <strong>L</strong>ocal groups (representing resource access permissions), to which <strong>P</strong>ermissions are assigned. It prevents permission sprawl and simplifies auditing across multi-domain forests.<br><br>
          <strong>Q2: What is the danger of granting full Domain Admin membership for desktop helpdesk staff?</strong><br>
          <em>Answer:</em> Domain Admins can access and control all Domain Controllers, modify Active Directory schemas, decrypt Kerberos ticket-granting accounts (KRBTGT), and access sensitive enterprise records. Delegating specific OU rights follows Least Privilege and prevents catastrophic lateral credential compromise.
        </div>
      </div>
    </div>
  </div>

</article>
"""
