# -*- coding: utf-8 -*-
"""
Server Administration Portal - Interactive Engineering Simulators & Dual CLI Sandbox
SSM Engineering Standard Gold Standard Architecture
"""

SERVER_SIMS_HTML = r"""
<!-- ===================================================================
     INTERACTIVE ENGINEERING TOOLS & DUAL POWERSHELL / BASH SANDBOX
     =================================================================== -->
<article class="doc-page" id="server-simulators-tools">
  <header class="doc-page-header">
    <span class="page-header-meta">Engineering Utilities • Interactive Server Simulators</span>
    <h2 class="section-title"><span class="sec-num">SIM.1</span> Interactive Server Engineering Calculators &amp; Live Dual CLI Sandbox</h2>
    <p class="lead-para">
      Perform real-time calculations for RAID array capacity, write penalty IOPS inflation, Base-10 to Base-2 binary storage discrepancy, and execute live commands in an embedded dual Windows PowerShell and Linux Bash terminal sandbox.
    </p>
  </header>

  <!-- CALCULATOR GRID -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
    
    <!-- 1. RAID CALCULATOR -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="hard-drive"></i> Enterprise RAID Sizing &amp; Parity Calculator
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 0.75rem;">
        Calculates usable capacity, parity overhead, and fault tolerance across RAID levels:
      </p>
      <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem; flex-wrap: wrap;">
        <select id="raidLevel" style="background: var(--bg-page); border: 1px solid var(--border-subtle); color: var(--text-normal); font-family: var(--font-mono); font-size: 12px; padding: 0.4rem; border-radius: 4px;">
          <option value="5">RAID 5 (Distributed Parity)</option>
          <option value="6">RAID 6 (Dual Parity)</option>
          <option value="10">RAID 10 (Striped Mirrors)</option>
          <option value="1">RAID 1 (Mirroring)</option>
          <option value="0">RAID 0 (Striping)</option>
        </select>
        <input type="number" id="raidDrives" value="6" min="2" max="24" style="width: 70px; background: var(--bg-page); border: 1px solid var(--border-subtle); color: var(--text-normal); font-family: var(--font-mono); font-size: 12px; padding: 0.4rem; border-radius: 4px;" title="Drive Count">
        <input type="number" id="driveSize" value="4" min="1" max="30" style="width: 70px; background: var(--bg-page); border: 1px solid var(--border-subtle); color: var(--text-normal); font-family: var(--font-mono); font-size: 12px; padding: 0.4rem; border-radius: 4px;" title="Size per drive (TB)">
        <button class="btn-tool" onclick="calculateRaid()" style="background: var(--primary); color: white; padding: 0.4rem 0.8rem; font-weight: 600;">Calculate</button>
      </div>
      <div id="raidResult" style="font-family: var(--font-mono); font-size: 11px; line-height: 1.6; color: var(--text-muted); background: var(--bg-code); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-subtle);">
        • Total Raw Capacity: 24 TB<br>
        • Usable Capacity: <strong style="color:var(--primary);">20 TB</strong> (83.3% efficiency)<br>
        • Parity Protection Overhead: 4 TB (1 Drive)<br>
        • Fault Tolerance: Survives ANY 1 drive failure
      </div>
    </div>

    <!-- 2. WRITE PENALTY CALCULATOR -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="gauge"></i> RAID Write Penalty &amp; IOPS Sizer
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 0.75rem;">
        Enter required application IOPS to calculate required physical disk IOPS:
      </p>
      <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem; align-items: center;">
        <span style="font-size: 11px; color: var(--text-muted);">App IOPS:</span>
        <input type="number" id="appIops" value="1000" style="width: 90px; background: var(--bg-page); border: 1px solid var(--border-subtle); color: var(--text-normal); font-family: var(--font-mono); font-size: 12px; padding: 0.4rem; border-radius: 4px;">
        <span style="font-size: 11px; color: var(--text-muted);">% Writes:</span>
        <input type="number" id="writePct" value="30" min="0" max="100" style="width: 60px; background: var(--bg-page); border: 1px solid var(--border-subtle); color: var(--text-normal); font-family: var(--font-mono); font-size: 12px; padding: 0.4rem; border-radius: 4px;">
        <button class="btn-tool" onclick="calculateIopsPenalty()" style="background: var(--primary); color: white; padding: 0.4rem 0.8rem; font-weight: 600;">Calculate</button>
      </div>
      <div id="iopsResult" style="font-family: var(--font-mono); font-size: 11px; line-height: 1.6; color: var(--text-muted); background: var(--bg-code); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-subtle);">
        • RAID 10 (Penalty 2): <strong style="color:#60a5fa;">1,300 Disk IOPS</strong><br>
        • RAID 5 (Penalty 4): <strong style="color:var(--primary);">1,900 Disk IOPS</strong><br>
        • RAID 6 (Penalty 6): <strong style="color:#f59e0b;">2,500 Disk IOPS</strong>
      </div>
    </div>

    <!-- 3. BASE-10 TO BASE-2 CALCULATOR -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="binary"></i> Base-10 to Binary OS Discrepancy
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 0.75rem;">
        Converts drive manufacturer decimal TB into true operating system binary TiB / GiB:
      </p>
      <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">
        <input type="number" id="decimalTb" value="8" style="flex: 1; background: var(--bg-page); border: 1px solid var(--border-subtle); color: var(--text-normal); font-family: var(--font-mono); font-size: 12px; padding: 0.4rem; border-radius: 4px;">
        <span style="font-size: 12px; align-self: center; color: var(--text-muted);">TB</span>
        <button class="btn-tool" onclick="calculateBinaryStorage()" style="background: var(--primary); color: white; padding: 0.4rem 0.8rem; font-weight: 600;">Convert</button>
      </div>
      <div id="binaryResult" style="font-family: var(--font-mono); font-size: 11px; line-height: 1.6; color: var(--text-muted); background: var(--bg-code); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-subtle);">
        • Decimal Marketing Capacity: 8,000,000,000,000 bytes<br>
        • True OS Binary Capacity: <strong style="color:#34d399;">7.276 TiB</strong> (7,450.58 GiB)<br>
        • Discrepancy Delta: ~724 GB (9.05% perceived loss)
      </div>
    </div>

    <!-- 4. QUORUM CALCULATOR -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="layers"></i> Failover Cluster Quorum Majority
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 0.75rem;">
        Formula: \(\lfloor N / 2 \rfloor + 1\) votes required for cluster survivability:
      </p>
      <ul style="font-size: 11px; color: var(--text-muted); line-height: 1.8; margin-left: 1.2rem;">
        <li><strong>2 Nodes (No Witness):</strong> 2 of 2 votes required (0 node fault tolerance!)</li>
        <li><strong>2 Nodes + Witness:</strong> 2 of 3 votes required (Survives 1 node loss)</li>
        <li><strong>4 Nodes + Witness:</strong> 3 of 5 votes required (Survives 2 node loss)</li>
      </ul>
    </div>

  </div>

  <!-- DUAL TERMINAL SANDBOX -->
  <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 2.5rem; margin-bottom: 1rem;">
    <h3 style="color: var(--text-normal); font-size: 18px; display: flex; align-items: center; gap: 0.5rem; margin: 0;">
      <i data-lucide="terminal"></i> Live Interactive Dual CLI Terminal Sandbox
    </h3>
    <div style="display: flex; gap: 0.5rem;">
      <button id="btnModePs" class="btn-tool active" onclick="switchCliMode('ps')" style="background: var(--primary); color: white; padding: 0.35rem 0.75rem; font-size: 11px; font-weight: bold;">PowerShell 7.4 (Windows)</button>
      <button id="btnModeBash" class="btn-tool" onclick="switchCliMode('bash')" style="background: var(--bg-surface); border: 1px solid var(--border-subtle); color: var(--text-muted); padding: 0.35rem 0.75rem; font-size: 11px; font-weight: bold;">Bash Shell (RHEL 9)</button>
    </div>
  </div>

  <div class="terminal-block" style="border: 1px solid var(--border-strong);">
    <div class="code-header">
      <div class="code-header-left">
        <span class="terminal-dot dot-red"></span>
        <span class="terminal-dot dot-yellow"></span>
        <span class="terminal-dot dot-green"></span>
        <span class="code-title" id="terminalTitle">Windows PowerShell 7.4.1 • Administrator • SRV-DC01.corp.contoso.com</span>
      </div>
      <button class="btn-tool" onclick="clearServerCli()"><i data-lucide="trash-2"></i> Clear</button>
    </div>
    <div class="code-body" style="background: #090d16; min-height: 260px; font-family: var(--font-mono); font-size: 12px; padding: 1rem; color: #e2e8f0;">
      <div id="serverCliOutput" style="white-space: pre-wrap; line-height: 1.5; margin-bottom: 0.75rem;">
<span style="color: #60a5fa;">====================================================================================
Department of Computer Science & Engineering • SERVER ADMINISTRATION MASTER DUAL CLI EMULATOR
PowerShell 7.4.1 / Linux Bash • Type 'help' to inspect available system commands.
====================================================================================</span>
</div>
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <span id="cliPrompt" style="color: #818cf8; font-weight: bold;">PS C:\Windows\System32&gt;</span>
        <input type="text" id="serverCliInput" placeholder="Get-Service, Get-ADUser, Test-NetConnection..." style="flex: 1; background: transparent; border: none; outline: none; color: #fff; font-family: var(--font-mono); font-size: 12px;" onkeydown="handleServerCliKeyDown(event)">
      </div>
    </div>
  </div>

</article>

<script>
let activeCliMode = 'ps';

function switchCliMode(mode) {
  activeCliMode = mode;
  const btnPs = document.getElementById('btnModePs');
  const btnBash = document.getElementById('btnModeBash');
  const title = document.getElementById('terminalTitle');
  const prompt = document.getElementById('cliPrompt');
  const input = document.getElementById('serverCliInput');
  const out = document.getElementById('serverCliOutput');
  
  if (mode === 'ps') {
    btnPs.style.background = 'var(--primary)';
    btnPs.style.color = '#fff';
    btnBash.style.background = 'var(--bg-surface)';
    btnBash.style.color = 'var(--text-muted)';
    title.innerText = 'Windows PowerShell 7.4.1 • Administrator • SRV-DC01.corp.contoso.com';
    prompt.innerText = 'PS C:\\Windows\\System32>';
    prompt.style.color = '#818cf8';
    input.placeholder = 'Get-Service, Get-ADUser, Test-NetConnection...';
    out.innerHTML += '\n<span style="color:#818cf8;">Switched to Windows PowerShell 7.4 environment.</span>\n';
  } else {
    btnBash.style.background = 'var(--primary)';
    btnBash.style.color = '#fff';
    btnPs.style.background = 'var(--bg-surface)';
    btnPs.style.color = 'var(--text-muted)';
    title.innerText = 'Bash 5.1.8 • root@rhel-srv01.corp.contoso.com • /root';
    prompt.innerText = '[root@rhel-srv01 ~]#';
    prompt.style.color = '#34d399';
    input.placeholder = 'systemctl status, lsblk -f, dmesg, getenforce...';
    out.innerHTML += '\n<span style="color:#34d399;">Switched to Red Hat Enterprise Linux 9 Bash environment.</span>\n';
  }
}

function clearServerCli() {
  document.getElementById('serverCliOutput').innerHTML = '';
}

function handleServerCliKeyDown(e) {
  if (e.key === 'Enter') {
    const input = document.getElementById('serverCliInput');
    const cmd = input.value.trim();
    input.value = '';
    executeServerCmd(cmd);
  }
}

function executeServerCmd(cmd) {
  const out = document.getElementById('serverCliOutput');
  const prompt = activeCliMode === 'ps' ? 'PS C:\\Windows\\System32>' : '[root@rhel-srv01 ~]#';
  const color = activeCliMode === 'ps' ? '#818cf8' : '#34d399';
  out.innerHTML += `\n<span style="color:${color};">${prompt}</span> <span style="color:#fff;">${cmd}</span>\n`;
  
  const c = cmd.toLowerCase().trim();
  if (c === 'clear' || c === 'cls') {
    out.innerHTML = '';
    return;
  }
  
  if (c === 'help') {
    if (activeCliMode === 'ps') {
      out.innerHTML += `<span style="color:#94a3b8;">Available PowerShell Commands:
  Get-ADUser               Inspect Active Directory user accounts
  Get-Service              List status of enterprise system services
  Get-Disk                 Display connected physical block drives
  Test-NetConnection       Test TCP port connectivity to remote hosts
  w32tm /query /status     Query Active Directory time synchronization status
  Get-CauClusterRole       Inspect Cluster-Aware Updating status
  clear                    Clear terminal screen</span>\n`;
    } else {
      out.innerHTML += `<span style="color:#94a3b8;">Available Bash Commands:
  systemctl status         List running systemd daemon units
  lsblk -f                 Display block device tree with filesystems
  dmesg                    Display kernel ring buffer events
  nmcli con show           Display NetworkManager connection profiles
  getenforce               Query SELinux enforcement mode
  numactl --hardware       Inspect multi-socket NUMA node topography
  clear                    Clear terminal screen</span>\n`;
    }
    return;
  }
  
  if (activeCliMode === 'ps') {
    if (c.includes('get-aduser')) {
      out.innerHTML += `<span style="color:#a78bfa;">DistinguishedName : CN=Alice Smith,OU=Finance,DC=corp,DC=contoso,DC=com
Enabled           : True
GivenName         : Alice
Name              : Alice Smith
SamAccountName    : asmith
UserPrincipalName : asmith@corp.contoso.com</span>\n`;
    } else if (c.includes('get-service')) {
      out.innerHTML += `<span style="color:#60a5fa;">Status   Name               DisplayName
------   ----               -----------
Running  NTDS               Active Directory Domain Services
Running  DNS                DNS Server
Running  W32Time            Windows Time
Running  W3SVC              World Wide Web Publishing Service
Stopped  Spooler            Print Spooler</span>\n`;
    } else if (c.includes('get-disk')) {
      out.innerHTML += `<span style="color:#f59e0b;">Number Friendly Name Serial Number                    HealthStatus OperationalStatus Total Size Partition Style
------ ------------- -------------                    ------------ ----------------- ---------- ---------------
0      PERC H750     00c7a8450f329910                 Healthy      Online                100 GB GPT            
1      PERC H750     00c7a8450f329911                 Healthy      Online                1.8 TB GPT            </span>\n`;
    } else if (c.includes('test-netconnection')) {
      out.innerHTML += `<span style="color:#34d399;">ComputerName     : fs01.corp.contoso.com
RemoteAddress    : 192.168.10.25
RemotePort       : 445
InterfaceAlias   : Ethernet0
SourceAddress    : 192.168.10.10
TcpTestSucceeded : True</span>\n`;
    } else if (c.includes('w32tm')) {
      out.innerHTML += `<span style="color:#38bdf8;">Leap Indicator: 0(no warning)
Stratum: 2 (secondary reference - syncd by (S)NTP)
Precision: -23 (119.209ns per tick)
Root Delay: 0.0152410s
Root Dispersion: 0.0284102s
ReferenceId: 0x82D01402 (Source IP:  130.208.20.2)
Last Successful Sync Time: 10/27/2026 15:40:12
Source: pool.ntp.org,0x1
Poll Interval: 10 (1024s)</span>\n`;
    } else {
      out.innerHTML += `<span style="color:#ef4444;">The term '${cmd}' is not recognized as a cmdlet, function, or operable program. Type 'help'.</span>\n`;
    }
  } else {
    // Bash Mode
    if (c.includes('systemctl status')) {
      out.innerHTML += `<span style="color:#34d399;">● named.service - Berkeley Internet Name Domain (DNS)
     Loaded: loaded (/usr/lib/systemd/system/named.service; enabled)
     Active: active (running) since Tue 2026-10-27 08:15:22 IST; 7h ago
   Main PID: 1422 (named)
     CGroup: /system.slice/named.service
             └─1422 /usr/sbin/named -u named -c /etc/named.conf</span>\n`;
    } else if (c.includes('lsblk')) {
      out.innerHTML += `<span style="color:#f59e0b;">NAME        FSTYPE FSVER LABEL UUID                                 MOUNTPOINTS
nvme0n1                                                              
├─nvme0n1p1 vfat   FAT32       E3A1-7B92                            /boot/efi
├─nvme0n1p2 xfs                a1b2c3d4-e5f6-7890-1234-56789abcdef0 /boot
└─nvme0n1p3 LVM2_m LVM2        Bq8z34-pKm1-7Rt4-uU8w-99L2-VwXy-1a2b 
  ├─rhel-root xfs              99aa88bb-77cc-66dd-55ee-44ff33aa22bb /
  └─rhel-swap swap   1         11223344-5566-7788-9900-aabbccddeeff [SWAP]</span>\n`;
    } else if (c.includes('getenforce')) {
      out.innerHTML += `<span style="color:#34d399;">Enforcing</span>\n`;
    } else if (c.includes('dmesg')) {
      out.innerHTML += `<span style="color:#94a3b8;">[    0.000000] Linux version 5.14.0-362.8.1.el9_3.x86_64 (mockbuild@x86-vm-07.build.eng.bos.redhat.com)
[    0.000000] Command line: BOOT_IMAGE=(hd0,gpt2)/vmlinuz root=/dev/mapper/rhel-root ro crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M
[    0.412850] smp: Brought up 2 nodes, 56 CPUs
[    1.120400] EDAC MC0: Giving out device to module i10nm_edac controller TopLevel: DEV 0000:00:00.0 (INTERRUPT)</span>\n`;
    } else if (c.includes('numactl')) {
      out.innerHTML += `<span style="color:#a78bfa;">available: 2 nodes (0-1)
node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 28 29 30 31 32 33 34 35 36 37 38 39 40 41
node 0 size: 128542 MB
node 0 free: 89410 MB
node 1 cpus: 14 15 16 17 18 19 20 21 22 23 24 25 26 27 42 43 44 45 46 47 48 49 50 51 52 53 54 55
node 1 size: 128912 MB
node 1 free: 91240 MB
node distances:
node   0   1 
  0:  10  21 
  1:  21  10 </span>\n`;
    } else {
      out.innerHTML += `<span style="color:#ef4444;">bash: ${cmd}: command not found. Type 'help' for available commands.</span>\n`;
    }
  }
}

// Calculators
function calculateRaid() {
  const lvl = document.getElementById('raidLevel').value;
  const n = parseInt(document.getElementById('raidDrives').value);
  const sz = parseFloat(document.getElementById('driveSize').value);
  const out = document.getElementById('raidResult');
  
  if (lvl === '5' && n < 3) {
    out.innerHTML = '<span style="color:#ef4444;">RAID 5 requires at least 3 drives!</span>';
    return;
  }
  if (lvl === '6' && n < 4) {
    out.innerHTML = '<span style="color:#ef4444;">RAID 6 requires at least 4 drives!</span>';
    return;
  }
  if (lvl === '10' && (n < 4 || n % 2 !== 0)) {
    out.innerHTML = '<span style="color:#ef4444;">RAID 10 requires an even number of drives (min 4)!</span>';
    return;
  }
  
  let usable = 0, parity = 0, tol = "";
  if (lvl === '0') {
    usable = n * sz;
    parity = 0;
    tol = "Zero (1 drive loss fails entire array)";
  } else if (lvl === '1') {
    usable = sz;
    parity = (n - 1) * sz;
    tol = "Survives " + (n - 1) + " drive failures";
  } else if (lvl === '5') {
    usable = (n - 1) * sz;
    parity = sz;
    tol = "Survives ANY 1 drive failure";
  } else if (lvl === '6') {
    usable = (n - 2) * sz;
    parity = 2 * sz;
    tol = "Survives ANY 2 simultaneous drive failures";
  } else if (lvl === '10') {
    usable = (n / 2) * sz;
    parity = (n / 2) * sz;
    tol = "Survives up to " + (n / 2) + " drive failures (1 per mirrored pair)";
  }
  
  const raw = n * sz;
  const eff = ((usable / raw) * 100).toFixed(1);
  out.innerHTML = `• Total Raw Capacity: ${raw} TB<br>` +
                  `• Usable Storage: <strong style="color:var(--primary);">${usable} TB</strong> (${eff}% efficiency)<br>` +
                  `• Parity / Mirror Overhead: ${parity} TB<br>` +
                  `• Fault Tolerance: ${tol}`;
}

function calculateIopsPenalty() {
  const iops = parseFloat(document.getElementById('appIops').value);
  const wPct = parseFloat(document.getElementById('writePct').value) / 100;
  const rPct = 1 - wPct;
  const reads = iops * rPct;
  const writes = iops * wPct;
  
  const r10 = reads + (2 * writes);
  const r5 = reads + (4 * writes);
  const r6 = reads + (6 * writes);
  
  document.getElementById('iopsResult').innerHTML = 
    `• RAID 10 (Penalty 2): <strong style="color:#60a5fa;">${r10.toLocaleString()} Disk IOPS</strong><br>` +
    `• RAID 5 (Penalty 4): <strong style="color:var(--primary);">${r5.toLocaleString()} Disk IOPS</strong><br>` +
    `• RAID 6 (Penalty 6): <strong style="color:#f59e0b;">${r6.toLocaleString()} Disk IOPS</strong>`;
}

function calculateBinaryStorage() {
  const decTb = parseFloat(document.getElementById('decimalTb').value);
  const bytes = decTb * 1e12;
  const tib = (bytes / Math.pow(2, 40)).toFixed(3);
  const gib = (bytes / Math.pow(2, 30)).toFixed(2);
  const lossGb = ((decTb * 1000) - (bytes / 1e9 * (tib / decTb))).toFixed(1);
  
  document.getElementById('binaryResult').innerHTML = 
    `• Marketing Decimal: ${bytes.toLocaleString()} bytes (${decTb} TB)<br>` +
    `• True Operating System Capacity: <strong style="color:#34d399;">${tib} TiB</strong> (${gib} GiB)<br>` +
    `• Discrepancy: ${lossGb} GB lower than decimal label purely due to Base-2 conversion`;
}
</script>
"""
