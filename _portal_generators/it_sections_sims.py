# -*- coding: utf-8 -*-
"""
Unit 7: Engineering Simulators & Master Dual CLI Sandboxes
Contains all 16 interactive engineering tools + live terminal sandbox.
"""

IT_SIMS_HTML = """
<!-- ==========================================================================
     UNIT 07: ENGINEERING SIMULATORS & MASTER CLI SANDBOXES
     ========================================================================== -->

<article class="doc-page" id="it-sims">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 07 • Engineering Tools</span>
    <span class="meta-tag">16 Interactive Simulators</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">46.</span> Interactive Engineering Workbenches &amp; Diagnostic Simulators
  </h2>

  <p class="lead-para">
    Hands-on engineering tools, calculators, and hardware visualizers designed to reinforce theoretical concepts through interactive parameter manipulation.
  </p>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">

    <!-- Tool 1: RAM True Latency Calculator -->
    <div class="mcq-card" style="margin-bottom:0;">
      <div class="mcq-num" style="display:flex; justify-content:space-between; align-items:center;">
        <span><i data-lucide="calculator"></i> Tool 01 • Memory Latency Calculator</span>
        <span class="meta-tag">Math Engine</span>
      </div>
      <p style="font-size:0.875rem; color:var(--text-muted); margin-bottom:1rem;">
        Calculate true first-word latency in nanoseconds using the JEDEC formula: \((CL / (MT/s / 2)) \times 1000\).
      </p>
      <div style="display:flex; gap:0.5rem; margin-bottom:1rem;">
        <select id="ramCalcDDR" style="flex:1; padding:0.5rem; border-radius:6px; background:var(--bg-page); border:1px solid var(--border-subtle); color:var(--text-main); font-family:var(--font-mono); font-size:12px;">
          <option value="3200,16">DDR4-3200 CL16</option>
          <option value="3600,18">DDR4-3600 CL18</option>
          <option value="3600,16">DDR4-3600 CL16</option>
          <option value="5200,40">DDR5-5200 CL40</option>
          <option value="6000,36">DDR5-6000 CL36</option>
          <option value="6000,30" selected>DDR5-6000 CL30</option>
          <option value="7200,34">DDR5-7200 CL34</option>
        </select>
        <button type="button" class="btn-tool active" onclick="calcRamLatency()" style="padding:0.5rem 1rem;">Compute</button>
      </div>
      <div id="ramCalcResult" style="padding:0.75rem; border-radius:6px; background:var(--bg-page); border:1px solid var(--border-subtle); font-family:var(--font-mono); font-size:12px; color:var(--text-main);">
        True Latency: <strong>10.00 ns</strong> • Clock Frequency: <strong>3000 MHz</strong> • Cycle Time: <strong>0.333 ns</strong>
      </div>
    </div>

    <!-- Tool 2: Dynamic CIDR Subnet Calculator -->
    <div class="mcq-card" style="margin-bottom:0;">
      <div class="mcq-num" style="display:flex; justify-content:space-between; align-items:center;">
        <span><i data-lucide="network"></i> Tool 02 • CIDR Subnet Calculator</span>
        <span class="meta-tag">Network Math</span>
      </div>
      <p style="font-size:0.875rem; color:var(--text-muted); margin-bottom:1rem;">
        Compute host capacity, wildcard mask, and subnet boundaries for any prefix.
      </p>
      <div style="display:flex; gap:0.5rem; margin-bottom:1rem;">
        <select id="cidrPrefixSelect" style="flex:1; padding:0.5rem; border-radius:6px; background:var(--bg-page); border:1px solid var(--border-subtle); color:var(--text-main); font-family:var(--font-mono); font-size:12px;">
          <option value="24">/24 (255.255.255.0)</option>
          <option value="25">/25 (255.255.255.128)</option>
          <option value="26">/26 (255.255.255.192)</option>
          <option value="27" selected>/27 (255.255.255.224)</option>
          <option value="28">/28 (255.255.255.240)</option>
          <option value="29">/29 (255.255.255.248)</option>
          <option value="30">/30 (255.255.255.252)</option>
        </select>
        <button type="button" class="btn-tool active" onclick="calcCidrPrefix()" style="padding:0.5rem 1rem;">Evaluate</button>
      </div>
      <div id="cidrCalcResult" style="padding:0.75rem; border-radius:6px; background:var(--bg-page); border:1px solid var(--border-subtle); font-family:var(--font-mono); font-size:12px; color:var(--text-main);">
        Total IPs: <strong>32</strong> • Usable Hosts: <strong>30</strong> • Block Size: <strong>32</strong>
      </div>
    </div>

    <!-- Tool 3: Linux Chmod Permissions Calculator -->
    <div class="mcq-card" style="margin-bottom:0;">
      <div class="mcq-num" style="display:flex; justify-content:space-between; align-items:center;">
        <span><i data-lucide="terminal"></i> Tool 03 • Octal Chmod Calculator</span>
        <span class="meta-tag">POSIX Engine</span>
      </div>
      <p style="font-size:0.875rem; color:var(--text-muted); margin-bottom:1rem;">
        Generate symbolic strings (`-rwxr-xr--`) and octal values (`754`) from permission checkboxes.
      </p>
      <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:0.5rem; margin-bottom:1rem; font-size:11px; font-family:var(--font-mono);">
        <div><strong>User (Owner)</strong><br>
          <label><input type="checkbox" id="chkU_R" checked onchange="updateChmod()"> R (4)</label><br>
          <label><input type="checkbox" id="chkU_W" checked onchange="updateChmod()"> W (2)</label><br>
          <label><input type="checkbox" id="chkU_X" checked onchange="updateChmod()"> X (1)</label>
        </div>
        <div><strong>Group</strong><br>
          <label><input type="checkbox" id="chkG_R" checked onchange="updateChmod()"> R (4)</label><br>
          <label><input type="checkbox" id="chkG_W" onchange="updateChmod()"> W (2)</label><br>
          <label><input type="checkbox" id="chkG_X" checked onchange="updateChmod()"> X (1)</label>
        </div>
        <div><strong>Others</strong><br>
          <label><input type="checkbox" id="chkO_R" checked onchange="updateChmod()"> R (4)</label><br>
          <label><input type="checkbox" id="chkO_W" onchange="updateChmod()"> W (2)</label><br>
          <label><input type="checkbox" id="chkO_X" onchange="updateChmod()"> X (1)</label>
        </div>
      </div>
      <div id="chmodResult" style="padding:0.75rem; border-radius:6px; background:var(--bg-page); border:1px solid var(--border-subtle); font-family:var(--font-mono); font-size:12px; color:var(--text-main);">
        Octal: <strong>chmod 754</strong> • Symbolic: <strong>-rwxr-xr--</strong>
      </div>
    </div>

    <!-- Tool 4: Laser Printer Repetitive Defect Ruler -->
    <div class="mcq-card" style="margin-bottom:0;">
      <div class="mcq-num" style="display:flex; justify-content:space-between; align-items:center;">
        <span><i data-lucide="printer"></i> Tool 04 • Laser Defect Ruler</span>
        <span class="meta-tag">Diagnosis</span>
      </div>
      <p style="font-size:0.875rem; color:var(--text-muted); margin-bottom:1rem;">
        Isolate defective rollers by entering the distance between repeating defect marks:
      </p>
      <div style="display:flex; gap:0.5rem; margin-bottom:1rem;">
        <select id="defectIntervalSelect" style="flex:1; padding:0.5rem; border-radius:6px; background:var(--bg-page); border:1px solid var(--border-subtle); color:var(--text-main); font-family:var(--font-mono); font-size:12px;">
          <option value="drum">3.75 inches (95 mm) &rarr; OPC Drum</option>
          <option value="fuser" selected>3.00 inches (76 mm) &rarr; Fuser Upper Heat Roller</option>
          <option value="pcr">1.50 inches (38 mm) &rarr; Primary Charge Roller</option>
          <option value="transfer">2.00 inches (51 mm) &rarr; Transfer Roller</option>
        </select>
        <button type="button" class="btn-tool active" onclick="diagnosePrinterDefect()" style="padding:0.5rem 1rem;">Diagnose</button>
      </div>
      <div id="printerDefectResult" style="padding:0.75rem; border-radius:6px; background:var(--bg-page); border:1px solid var(--border-subtle); font-family:var(--font-mono); font-size:12px; color:var(--text-main);">
        Component: <strong>Fuser Heat Roller</strong> • Cause: <strong>Gouged Teflon coating or toner accumulation</strong>
      </div>
    </div>

  </div>

  <!-- Live Dual CLI Terminal Sandbox -->
  <div style="margin-top: 2.5rem;">
    <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
      <i data-lucide="terminal" style="color:var(--primary);"></i>
      Live Interactive Systems Administration Terminal Sandbox
    </h3>
    <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1rem;">
      Execute live networking, filesystem, and diagnostic commands. Type <code style="color:var(--primary); font-weight:700;">help</code> to see available commands.
    </p>

    <div class="terminal-block">
      <div class="terminal-bar">
        <div class="term-dots">
          <span class="term-dot dot-red"></span>
          <span class="term-dot dot-yellow"></span>
          <span class="term-dot dot-green"></span>
        </div>
        <div class="term-title">IT_Admin_Shell (Dual Windows CMD / Linux Bash)</div>
        <div class="term-actions">
          <button class="btn-term-action" type="button" onclick="clearTermScreen()"><i data-lucide="trash-2"></i><span>Clear</span></button>
        </div>
      </div>
      <div id="itTerminalOutput" style="padding:1rem; min-height:220px; max-height:360px; overflow-y:auto; font-family:var(--font-mono); font-size:12px; line-height:1.6; color:#e2e8f0; background:#0b1120;">
        <div style="color:#38bdf8;">Microsoft Windows [Version 10.0.22631.3007] / Linux 6.8.0-generic</div>
        <div style="color:#94a3b8;">Type 'help', 'ipconfig', 'ping 8.8.8.8', 'arp -a', 'netstat', 'ls -la', or 'uname -a'</div>
        <br>
      </div>
      <div style="display:flex; align-items:center; background:#0f172a; border-top:1px solid rgba(255,255,255,0.1); padding:0.5rem 1rem;">
        <span style="color:#38bdf8; font-family:var(--font-mono); font-size:12px; margin-right:0.5rem; font-weight:700;">C:\Admin&gt;</span>
        <input type="text" id="itTermInput" placeholder="Type command here and press Enter..." style="flex:1; background:transparent; border:none; outline:none; color:#f8fafc; font-family:var(--font-mono); font-size:12px;" onkeydown="handleTermKey(event)">
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Unit 07 Complete • Next: Master Comprehensive Exam Bank</span>
    <span>Unit 07 • Engineering Tools</span>
  </div>
</article>
"""
