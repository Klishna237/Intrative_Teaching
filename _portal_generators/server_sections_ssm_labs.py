# -*- coding: utf-8 -*-
"""
Server Administration Portal - Practical Laboratory Manual
SSM Engineering Standard Gold Standard Architecture
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
      Conforming strictly to the Department of Computer Science & Engineering Server Administration syllabus, this lab manual delivers step-by-step procedures, terminal commands (PowerShell 7 and Linux Bash), expected execution outputs, and oral examination (Viva Voce) questions for ten foundational server engineering experiments.
    </p>
  </header>

  <!-- LAB 1 -->
  <div class="subj-card revealed" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 01</div>
      <div class="subj-title">Enterprise Server Operating System Installation (Windows Server 2022 / RHEL 9) in Virtualized Environment</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Provision a Type-1 virtualized server environment (Hyper-V or VMware ESXi), configure virtual hardware baseline (4 vCPUs, 16GB ECC RAM, 100GB GPT VHDX), install Windows Server 2022 Datacenter, and execute post-installation initialization.</p>
      
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">PowerShell • Initial Server Post-Installation Bootstrap</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-powershell"># 1. Rename host computer to enterprise naming convention
Rename-Computer -NewName "SRV-DC01" -Restart -Force

# 2. Configure Static IPv4 address, subnet mask, and DNS
New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress 192.168.10.10 -PrefixLength 24 -DefaultGateway 192.168.10.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.10.10", "1.1.1.1")

# 3. Enable Remote Desktop and configure firewall
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"</code></pre>
        </div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why is Windows Server Core edition preferred over Desktop Experience in enterprise datacenters?</strong><br>
          <em>Answer:</em> Server Core omits the GUI shell, reducing disk footprint by ~4GB, lowering memory overhead, eliminating ~70% of monthly security patch reboots, and drastically reducing attack surface.<br><br>
          <strong>Q2: What is the purpose of sysprep before imaging a template VM?</strong><br>
          <em>Answer:</em> <code class="code-inline">sysprep /generalize</code> removes machine-specific state (including unique machine SIDs, driver associations, and event logs) so cloned VMs do not duplicate SIDs across the Active Directory domain.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 2 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 02</div>
      <div class="subj-title">Server Firmware Management: UEFI / BIOS Hardening &amp; Out-of-Band Redfish Updates</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure secure UEFI firmware settings, enable hardware virtualization extensions (VT-x/AMD-V), configure TPM 2.0 security, and execute an out-of-band firmware flash via Redfish RESTful APIs.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">Bash / cURL • DMTF Redfish Out-of-Band Power Cycle</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># Query BMC power state via DMTF Redfish REST API
curl -k -u "root:calvin" -X GET https://192.168.100.50/redfish/v1/Systems/System.Embedded.1

# Issue remote graceful restart command to BMC
curl -k -u "root:calvin" -X POST \
    -H "Content-Type: application/json" \
    -d '{"ResetType": "GracefulRestart"}' \
    https://192.168.100.50/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset</code></pre>
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 3 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 03</div>
      <div class="subj-title">Hardware Component Diagnostics: NUMA Topologies, ECC RAM &amp; PCIe Expansion</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Inspect physical processor topology, verify multi-socket NUMA node assignments, validate ECC SECDED memory error thresholds, and inspect PCIe link negotiations.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">Linux CLI • NUMA &amp; Hardware Diagnostics</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># Inspect multi-socket NUMA node layout and core bindings
numactl --hardware

# View ECC memory errors recorded in Linux kernel EDAC
edac-util -v

# Verify PCIe 4.0/5.0 link width and transfer speed
lspci -vv -s 01:00.0 | grep -E "(LnkCap|LnkSta)"</code></pre>
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 4 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 04</div>
      <div class="subj-title">Storage Technologies: Software &amp; Hardware RAID Configuration (RAID 0, 1, 5, 10)</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Initialize 4 block devices, configure a software RAID 5 array with a hot spare using Linux <code class="code-inline">mdadm</code> or Windows Storage Spaces, simulate a disk drive failure, and observe autonomous parity rebuild.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">Linux CLI • mdadm RAID 5 Provisioning &amp; Failure Test</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># 1. Create RAID 5 array with 3 active drives and 1 hot spare
sudo mdadm --create --verbose /dev/md0 --level=5 --raid-devices=3 /dev/sdb /dev/sdc /dev/sdd --spare-devices=1 /dev/sde

# 2. Format with XFS filesystem and mount
sudo mkfs.xfs /dev/md0
sudo mkdir -p /mnt/raid5_data && sudo mount /dev/md0 /mnt/raid5_data

# 3. Simulate failure of /dev/sdb and monitor automated rebuild onto spare
sudo mdadm --manage /dev/md0 --fail /dev/sdb
cat /proc/mdstat</code></pre>
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 5 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 05</div>
      <div class="subj-title">Enterprise Network Services: Static IP, Active Directory Integrated DNS &amp; DHCP Failover</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Deploy Windows Server DHCP and DNS roles, configure a high-availability DHCP Failover relationship in Load-Sharing mode across two servers, and test lease synchronization.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">PowerShell • DHCP Failover Deployment</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-powershell"># Install DHCP server role
Install-WindowsFeature -Name DHCP -IncludeManagementTools -Restart

# Create DHCP Scope
Add-DhcpServerv4Scope -Name "StudentLabScope" -StartRange 10.0.1.100 -EndRange 10.0.1.200 -SubnetMask 255.255.255.0

# Configure 50/50 Load-Sharing Failover with secondary partner server
Add-DhcpServerv4Failover -Name "DHCP-HA-Pair" -ScopeId 10.0.1.0 `
    -PartnerServer "SRV-DHCP02.corp.local" -Mode LoadBalance -LoadPercent 50 `
    -SharedSecret "EnterpriseSecretPassword123!"</code></pre>
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 6 to 10 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 06</div>
      <div class="subj-title">Enterprise Server Roles: Active Directory Domain Services (AD DS) Forest Promotion</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Promote a standalone Windows Server 2022 to an enterprise Domain Controller, establishing a new forest root domain (<code class="code-inline">corp.contoso.com</code>) with DNS integration and global catalog services.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">PowerShell • AD DS Forest Promotion</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-powershell">Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName "corp.contoso.com" -DomainNetbiosName "CORP" `
    -InstallDns:$true -ForestMode "WinThreshold" -DomainMode "WinThreshold" `
    -SafeModeAdministratorPassword (ConvertTo-SecureString "DSRMPassword123!" -AsPlainText -Force)</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 07</div>
      <div class="subj-title">Type-1 Hypervisor Management: Hyper-V VM Provisioning, Virtual Switches &amp; VHDX</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure Hyper-V Virtual Switches (External with VLAN trunking), create Generation 2 virtual machines, and attach dynamically expanding VHDX storage disks.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">PowerShell • Hyper-V VM Creation</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-powershell">New-VMSwitch -Name "vSwitch-Production" -NetAdapterName "Ethernet0" -AllowManagementOS $true
New-VM -Name "VM-AppServer01" -Generation 2 -MemoryStartupBytes 4GB -SwitchName "vSwitch-Production"
New-VHD -Path "C:\Hyper-V\Virtual Hard Disks\AppServer01.vhdx" -SizeBytes 60GB -Dynamic
Add-VMHardDiskDrive -VMName "VM-AppServer01" -Path "C:\Hyper-V\Virtual Hard Disks\AppServer01.vhdx"</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 08</div>
      <div class="subj-title">Performance Baselines &amp; Monitoring: PerfMon, Resource Monitor &amp; Event Viewer</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Create a User-Defined Data Collector Set in Performance Monitor tracking CPU % Processor Time, Memory Available MBytes, and Disk Avg. Disk sec/Transfer to detect bottlenecks.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">CMD • Logman Performance Counter Collection</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-cmd">logman create counter ServerBaseline -s localhost -o C:\PerfLogs\baseline.blg -f bin -si 00:00:15 -c "\Processor(_Total)\% Processor Time" "\Memory\Available MBytes" "\PhysicalDisk(_Total)\Avg. Disk sec/Transfer"
logman start ServerBaseline</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 09</div>
      <div class="subj-title">Enterprise Backup &amp; Disaster Recovery: Windows Server Backup &amp; VSS Volume Snapshots</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Install Windows Server Backup, configure a scheduled system state backup using Volume Shadow Copy Service (VSS), delete a critical file, and perform an authoritative restore.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">PowerShell • Wbadmin System State Backup</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-powershell">Install-WindowsFeature -Name Windows-Server-Backup -IncludeManagementTools
wbadmin start systemstatebackup -backupTarget:E: -quiet</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 10</div>
      <div class="subj-title">Identity &amp; Access Governance: Active Directory RBAC &amp; Least Privilege Delegation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Design an Organizational Unit (OU) structure, create security groups adhering to the AGDLP principle (Accounts &rarr; Global Groups &rarr; Domain Local Groups &rarr; Permissions), and delegate password-reset privileges without granting Domain Admin access.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">PowerShell • AD User &amp; OU Delegation</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-powershell">New-ADOrganizationalUnit -Name "Staff" -Path "DC=corp,DC=contoso,DC=com"
New-ADGroup -Name "HelpDeskStaff" -GroupScope Global -Path "OU=Staff,DC=corp,DC=contoso,DC=com"
New-ADUser -Name "John Doe" -SamAccountName "jdoe" -UserPrincipalName "jdoe@corp.contoso.com" -AccountPassword (ConvertTo-SecureString "P@ssword2026!" -AsPlainText -Force) -Enabled $true</code></pre>
        </div>
      </div>
    </div>
  </div>

</article>
"""
