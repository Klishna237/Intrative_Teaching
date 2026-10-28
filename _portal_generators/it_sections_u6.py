# -*- coding: utf-8 -*-
IT_UNIT6_HTML = r"""
<!-- ==========================================================================
     UNIT 06: SCRIPTING, REMOTE SUPPORT, AND SAFETY
     ========================================================================== -->

<!-- Page 32: Mobile OS Security, Biometrics & MDM Remote Wipe -->
<article class="doc-page" id="it6-mobile-security">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 06 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">32.</span> Mobile Operating System Security: Biometrics, MDM Remote Wipe &amp; Sandboxing
  </h2>

  <p class="lead-para">
    Smartphones and tablets handling enterprise communications require stringent hardware-backed encryption, cryptographic separation between personal and corporate data, granular application permission architectures, and Mobile Device Management (MDM) enrollment for remote fleet governance.
  </p>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="smartphone"></i> HARDWARE-BACKED CRYPTOGRAPHIC ENCLAVES</div>
    <div class="callout-body">
      Modern mobile silicon (Apple Secure Enclave, Android Titan M2 / TrustZone) isolates cryptographic keys from the main application processor. Biometric sensor data (fingerprint minutiae points, facial 3D depth maps) is processed entirely within the isolated enclave. The main OS kernel receives only a cryptographic boolean confirmation (Match / No Match), ensuring that even a completely compromised OS kernel cannot extract user biometric templates.
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Mobile Security Features &amp; Enterprise Governance Protocols
  </h3>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Security Mechanism</th>
          <th>Operating Principle</th>
          <th>Attack Vector Mitigated</th>
          <th>Enterprise Best Practice</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Passcode Lockout Policy</strong></td>
          <td>Imposes escalating exponential time delays after failed attempts; initiates cryptographic erase after 10 failed entries.</td>
          <td>Hardware automated brute-force attacks via USB lightning/type-C automated keypress rigs.</td>
          <td>Enforce 6-digit minimum alphanumeric PIN via MDM policy.</td>
        </tr>
        <tr>
          <td><strong>Full Device Remote Wipe</strong></td>
          <td>MDM pushes cryptographic key destruction command; the device securely discards the hardware master storage encryption key (FileVault / FBE).</td>
          <td>Data theft from physically lost or stolen mobile endpoints.</td>
          <td>Deploy immediately upon employee separation or reported loss of personal/corporate phone.</td>
        </tr>
        <tr>
          <td><strong>Selective / Enterprise Wipe</strong></td>
          <td>Removes only corporate email accounts, managed apps, and VPN profiles, preserving employee personal photos and personal apps.</td>
          <td>Legal liability and privacy violations in Bring-Your-Own-Device (BYOD) environments.</td>
          <td>Mandatory for BYOD mobile fleet offboarding.</td>
        </tr>
        <tr>
          <td><strong>Application Sandboxing</strong></td>
          <td>Each app runs in an isolated user account (UID) with unique virtual filesystem namespaces; inter-process access blocked.</td>
          <td>Malicious third-party apps scraping banking tokens, SMS 2FA codes, or contacts from other apps.</td>
          <td>Disable Android sideloading ("Unknown Sources") and restrict iOS to Apple App Store / MDM Catalog.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Multi-Language Scripting Fundamentals</span>
    <span>Unit 06 • Page 01</span>
  </div>
</article>




<!-- Page 33: Multi-Language Scripting Basics: Batch, PowerShell & Python -->
<article class="doc-page" id="it6-scripting-languages">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 06 • Page 02</span>
    <span class="meta-tag">Bloom's: Understand / Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">33.</span> Multi-Language Scripting Fundamentals: Windows Batch, PowerShell &amp; Python 3
  </h2>

  <p class="lead-para">
    Enterprise system administrators leverage multiple scripting environments to automate repetitive operational tasks, audit system configurations, orchestrate scheduled backups, and enforce fleet-wide configuration baselines. Understanding language paradigms, execution contexts, and security execution policies is vital for modern IT infrastructure support.
  </p>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="terminal"></i> SCRIPTING ARCHITECTURES COMPARED</div>
    <div class="callout-body">
      Traditional text-stream shells (Batch, Bash) process input and output as raw streams of ASCII/UTF-8 character lines requiring text parsers (<code>sed</code>, <code>awk</code>, <code>findstr</code>). In contrast, <strong>PowerShell</strong> is an object-oriented shell where cmdlets pass rich .NET objects containing structured properties and methods through the pipeline, eliminating string parsing errors entirely. <strong>Python</strong> provides platform-independent, object-oriented enterprise automation with vast standard library capabilities.
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Administrative Scripting Language Matrix
  </h3>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Language</th>
          <th>File Extension</th>
          <th>Execution Engine</th>
          <th>Data Pipeline Model</th>
          <th>Primary IT Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Windows Batch</strong></td>
          <td><code>.bat</code> / <code>.cmd</code></td>
          <td><code>cmd.exe</code></td>
          <td>Raw ASCII text stream</td>
          <td>Legacy system logon scripts, simple file copies, basic registry imports.</td>
        </tr>
        <tr>
          <td><strong>PowerShell</strong></td>
          <td><code>.ps1</code></td>
          <td><code>powershell.exe</code> / <code>pwsh</code></td>
          <td>Structured .NET CLI Objects</td>
          <td>Active Directory administration, Windows Server management, cloud provisioning (Azure/M365), hypervisor automation.</td>
        </tr>
        <tr>
          <td><strong>Python 3</strong></td>
          <td><code>.py</code></td>
          <td><code>python.exe</code> (CPython)</td>
          <td>Python Objects &amp; Dictionaries</td>
          <td>Cross-platform automation, network switch configuration, REST API integrations, system telemetry parsing.</td>
        </tr>
        <tr>
          <td><strong>Linux Bash</strong></td>
          <td><code>.sh</code></td>
          <td><code>/bin/bash</code></td>
          <td>POSIX text byte stream</td>
          <td>Linux server provisioning, cron jobs, container orchestration, log file processing.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    2. Windows Batch Scripting (.bat / .cmd)
  </h3>
  <p>
    Batch scripts execute sequentially line-by-line within the Windows Command Prompt interpreter. Key constructs include suppressing command echoing (<code>@echo off</code>), variable assignment (<code>set VAR=val</code>), string interpolation (<code>%VAR%</code>), conditional branch checking (<code>if exist</code>, <code>if errorlevel</code>), and looping (<code>for %%i in (...) do ...</code>).
  </p>

  <div class="terminal-block comments-hidden full-width-module">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span class="term-dot dot-green"></span>
        <span class="terminal-title">Windows Batch Script: Automated Log Archiver (archive_logs.bat)</span>
      </div>
      <div class="terminal-actions">
        <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
        <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
      </div>
    </div>
    <div class="terminal-body">
      <pre class="code-pre"><code><span class="code-comment">@echo off</span>
<span class="code-comment">:: Automated Diagnostic Log Archival Script</span>
<span class="c-kw">setlocal</span> enabledelayedexpansion

<span class="c-kw">set</span> <span class="c-var">SRC_DIR</span>=C:\AppLogs
<span class="c-kw">set</span> <span class="c-var">DEST_DIR</span>=D:\ArchiveLogs\%date:~10,4%-%date:~4,2%-%date:~7,2%

<span class="c-fn">echo</span> [INFO] Initializing Daily Log Archive Process...
<span class="c-kw">if not exist</span> <span class="c-str">"%DEST_DIR%"</span> (
    <span class="c-fn">mkdir</span> <span class="c-str">"%DEST_DIR%"</span>
    <span class="c-fn">echo</span> [INFO] Created backup destination directory: %DEST_DIR%
)

<span class="c-fn">robocopy</span> <span class="c-str">"%SRC_DIR%"</span> <span class="c-str">"%DEST_DIR%"</span> *.log /mov /minage:7 /r:3 /w:5
<span class="c-kw">if</span> %errorlevel% <span class="c-kw">geq</span> 8 (
    <span class="c-fn">echo</span> [ERROR] Robocopy encountered critical errors during file transfer!
    <span class="c-kw">exit</span> /b 1
) <span class="c-kw">else</span> (
    <span class="c-fn">echo</span> [SUCCESS] Stale logs successfully archived and purged from production.
    <span class="c-kw">exit</span> /b 0
)</code></pre>
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    3. PowerShell Automation &amp; Execution Policies (.ps1)
  </h3>
  <p>
    PowerShell cmdlets use a standardized <code>Verb-Noun</code> naming convention (e.g. <code>Get-Service</code>, <code>Restart-Computer</code>). Execution policies in Windows safeguard against unintended script execution:
  </p>
  <ul style="margin-left: 1.25rem; line-height: 1.6; color: var(--text-muted); font-size: 0.9rem;">
    <li><code>Restricted</code>: Default on Windows clients; no scripts can run; interactive commands only.</li>
    <li><code>RemoteSigned</code>: Local scripts run without signature; downloaded scripts must be signed by a trusted publisher. Default on Windows Server.</li>
    <li><code>AllSigned</code>: All scripts (local and remote) require a digital cryptographic signature.</li>
    <li><code>Unrestricted</code> / <code>Bypass</code>: All scripts execute without warnings or security prompts.</li>
  </ul>

  <div class="terminal-block comments-hidden full-width-module" style="margin-top: 1rem;">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span class="term-dot dot-green"></span>
        <span class="terminal-title">PowerShell Script: Service Health Watchdog &amp; Restarter (Watchdog.ps1)</span>
      </div>
      <div class="terminal-actions">
        <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
        <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
      </div>
    </div>
    <div class="terminal-body">
      <pre class="code-pre"><code><span class="code-comment"># Enforce execution policy for current process: Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned</span>
<span class="c-var">$TargetServices</span> = @(<span class="c-str">"Spooler"</span>, <span class="c-str">"W32Time"</span>, <span class="c-str">"LanmanServer"</span>)

<span class="c-kw">foreach</span> (<span class="c-var">$svcName</span> <span class="c-kw">in</span> <span class="c-var">$TargetServices</span>) {
    <span class="c-var">$service</span> = <span class="c-fn">Get-Service</span> -Name <span class="c-var">$svcName</span> -ErrorAction SilentlyContinue
    
    <span class="c-kw">if</span> (<span class="c-var">$null</span> -eq <span class="c-var">$service</span>) {
        <span class="c-fn">Write-Warning</span> <span class="c-str">"Service '$svcName' is not registered on this host."</span>
        <span class="c-kw">continue</span>
    }

    <span class="c-kw">if</span> (<span class="c-var">$service</span>.Status -ne <span class="c-str">'Running'</span>) {
        <span class="c-fn">Write-Host</span> <span class="c-str">"[ALERT] Service '$($service.DisplayName)' is stopped! Attempting restart..."</span> -ForegroundColor Yellow
        <span class="c-fn">Start-Service</span> -Name <span class="c-var">$svcName</span>
        <span class="c-fn">Start-Sleep</span> -Seconds 2
        <span class="c-var">$refreshed</span> = <span class="c-fn">Get-Service</span> -Name <span class="c-var">$svcName</span>
        <span class="c-fn">Write-Host</span> <span class="c-str">"[STATUS] Service '$svcName' post-recovery status: $($refreshed.Status)"</span> -ForegroundColor Green
    } <span class="c-kw">else</span> {
        <span class="c-fn">Write-Host</span> <span class="c-str">"[OK] Service '$($service.DisplayName)' is healthy and running."</span> -ForegroundColor Cyan
    }
}</code></pre>
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    4. Python 3 System Automation (.py)
  </h3>
  <p>
    Python is the standard language for multi-platform infrastructure orchestration. Python scripts leverage native modules such as <code>os</code> (environment &amp; paths), <code>sys</code> (interpreter arguments), <code>subprocess</code> (external process invocation), and <code>socket</code> (network port probing):
  </p>

  <div class="terminal-block comments-hidden full-width-module" style="margin-top: 1rem;">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span class="term-dot dot-green"></span>
        <span class="terminal-title">Python 3 Script: Multi-Host Socket Port Probe (port_probe.py)</span>
      </div>
      <div class="terminal-actions">
        <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
        <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
      </div>
    </div>
    <div class="terminal-body">
      <pre class="code-pre"><code><span class="code-comment">#!/usr/bin/env python3</span>
<span class="c-kw">import</span> socket
<span class="c-kw">import</span> sys

<span class="c-var">INFRA_TARGETS</span> = [
    (<span class="c-str">"192.168.1.1"</span>, <span class="c-num">80</span>, <span class="c-str">"Gateway HTTP"</span>),
    (<span class="c-str">"192.168.1.10"</span>, <span class="c-num">445</span>, <span class="c-str">"File Server SMB"</span>),
    (<span class="c-str">"192.168.1.20"</span>, <span class="c-num">3389</span>, <span class="c-str">"Management Jumpbox RDP"</span>),
    (<span class="c-str">"8.8.8.8"</span>, <span class="c-num">53</span>, <span class="c-str">"External DNS"</span>)
]

<span class="c-kw">def</span> <span class="c-fn">check_port</span>(host, port, timeout=1.5):
    <span class="c-kw">with</span> socket.socket(socket.AF_INET, socket.SOCK_STREAM) <span class="c-kw">as</span> sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        <span class="c-kw">return</span> result == 0

<span class="c-fn">print</span>(<span class="c-str">"=" * 60</span>)
<span class="c-fn">print</span>(<span class="c-str">"INFRASTRUCTURE TCP PORT CONNECTIVITY AUDIT"</span>)
<span class="c-fn">print</span>(<span class="c-str">"=" * 60</span>)

<span class="c-kw">for</span> host, port, desc <span class="c-kw">in</span> INFRA_TARGETS:
    is_open = check_port(host, port)
    status = <span class="c-str">"[PASS] ONLINE"</span> <span class="c-kw">if</span> is_open <span class="c-kw">else</span> <span class="c-str">"[FAIL] UNREACHABLE"</span>
    <span class="c-fn">print</span>(f<span class="c-str">"{desc:&lt;26} {host}:{port:&lt;5} -&gt; {status}"</span>)
</code></pre>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Bash Shell Scripting &amp; 10 Production Scripts</span>
    <span>Unit 06 • Page 02</span>
  </div>
</article>

<article class="doc-page" id="sec31-arith">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 06</span>
          <span>Arithmetic, Input &amp; Arrays • Page 20</span>
        </header>

        <h2 class="section-title"><span class="sec-num">31.</span> Arithmetic Operators &amp; Calculations</h2>
        <p>
          Bash natively supports <strong>integer-only arithmetic</strong> via the <code>$(( ... ))</code> syntax.
          Floating-point arithmetic requires piping into the external arbitrary-precision calculator <code>bc</code>:
        </p>

        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Bash Arithmetic Examples</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="code-comment"># Native 64-bit integer arithmetic</span>
<span class="c-var">A</span>=<span class="c-num">25</span>
<span class="c-var">B</span>=<span class="c-num">4</span>
<span class="c-var">SUM</span>=$((A + B))          <span class="code-comment"># 29</span>
<span class="c-var">MOD</span>=$((A % B))          <span class="code-comment"># 1</span>
<span class="c-var">EXP</span>=$((A ** 2))         <span class="code-comment"># 625</span>

<span class="code-comment"># Floating-point arithmetic via bc (scale sets decimal places)</span>
<span class="c-var">DIV_FLOAT</span>=$(<span class="c-fn">echo</span> <span class="c-str">"scale=4; $A / $B"</span> | <span class="c-kw">bc</span>)  <span class="code-comment"># 6.2500</span></code></pre>
          </div>
        </div>

        <h2 class="section-title" id="sec32-input"><span class="sec-num">32.</span> User Input &amp; Special Positional
          Variables</h2>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 20%;">Variable / Flag</th>
                <th style="width: 35%;">Syntax Example</th>
                <th style="width: 45%;">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>read -p</code></td>
                <td><code>read -p "Enter name: " name</code></td>
                <td>Displays an inline prompt string and stores input into variable.</td>
              </tr>
              <tr>
                <td><code>read -s</code></td>
                <td><code>read -s -p "Password: " pass</code></td>
                <td>Silent mode: suppresses terminal echo (ideal for passwords).</td>
              </tr>
              <tr>
                <td><code>$0</code></td>
                <td><code>echo "Running $0"</code></td>
                <td>The name or path of the running script itself.</td>
              </tr>
              <tr>
                <td><code>$1 ... $9</code></td>
                <td><code>echo "Arg 1: $1"</code></td>
                <td>Positional arguments passed to the script or function. (Use <code>${10}</code> for arg 10+).</td>
              </tr>
              <tr>
                <td><code>$#</code></td>
                <td><code>if [ $# -lt 2 ]; then ...</code></td>
                <td>Total count of positional arguments passed.</td>
              </tr>
              <tr>
                <td><code>$@</code></td>
                <td><code>for arg in "$@"; do ...</code></td>
                <td>All arguments as individually quoted strings (<code>"$1" "$2" ...</code>).</td>
              </tr>
              <tr>
                <td><code>$?</code></td>
                <td><code>echo "Exit code: $?"</code></td>
                <td>Exit status of the most recently executed command (0 = Success, &gt;0 = Error).</td>
              </tr>
              <tr>
                <td><code>$$</code></td>
                <td><code>echo "My PID is $$"</code></td>
                <td>Process ID (PID) of the currently running script subshell.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="section-title" id="sec33-arrays"><span class="sec-num">33.</span> Indexed &amp; Associative Arrays
        </h2>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Bash Array Manipulation</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="code-comment"># Indexed Array declaration and access</span>
<span class="c-var">servers</span>=(<span class="c-str">"web01"</span> <span class="c-str">"db01"</span> <span class="c-str">"cache01"</span>)
<span class="c-fn">echo</span> <span class="c-str">"First server: ${servers[0]}"</span>
<span class="c-fn">echo</span> <span class="c-str">"All servers:  ${servers[@]}"</span>
<span class="c-fn">echo</span> <span class="c-str">"Array count:  ${#servers[@]}"</span>

<span class="code-comment"># Associative Array (Dictionary / Key-Value Map)</span>
<span class="c-kw">declare -A</span> <span class="c-var">user_roles</span>
<span class="c-var">user_roles</span>[<span class="c-str">"alice"</span>]=<span class="c-str">"Admin"</span>
<span class="c-var">user_roles</span>[<span class="c-str">"bob"</span>]=<span class="c-str">"Developer"</span>
<span class="c-fn">echo</span> <span class="c-str">"Alice role: ${user_roles["alice"]}"</span></code></pre>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>
<article class="doc-page" id="sec34-cond">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 06</span>
          <span>Conditions, Case &amp; Loops • Page 21</span>
        </header>

        <h2 class="section-title"><span class="sec-num">34.</span> Conditional Testing (`if-elif-else`) &amp; Test
          Operators</h2>
        <p>
          Bash provides two test constructs: legacy POSIX single-bracket <code>[ ... ]</code> (aliased to
          <code>test</code>) and modern extended double-bracket <code>[[ ... ]]</code> which supports regular
          expressions (<code>=~</code>) and native logical operators (<code>&amp;&amp;</code>, <code>||</code>).
        </p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 25%;">Test Operator</th>
                <th style="width: 40%;">Meaning / Condition</th>
                <th style="width: 35%;">Syntax Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>-f &lt;path&gt;</code></td>
                <td>True if file exists and is a regular file.</td>
                <td><code>[[ -f /etc/passwd ]]</code></td>
              </tr>
              <tr>
                <td><code>-d &lt;path&gt;</code></td>
                <td>True if directory exists.</td>
                <td><code>[[ -d /var/log ]]</code></td>
              </tr>
              <tr>
                <td><code>-z &lt;str&gt;</code></td>
                <td>True if string length is ZERO (empty).</td>
                <td><code>[[ -z "$input" ]]</code></td>
              </tr>
              <tr>
                <td><code>-n &lt;str&gt;</code></td>
                <td>True if string length is NON-ZERO.</td>
                <td><code>[[ -n "$user" ]]</code></td>
              </tr>
              <tr>
                <td><code>-eq, -ne, -lt, -gt</code></td>
                <td>Integer equality, inequality, less-than, greater-than.</td>
                <td><code>[[ $count -gt 10 ]]</code></td>
              </tr>
              <tr>
                <td><code>=~</code></td>
                <td>Matches string against a Regular Expression pattern.</td>
                <td><code>[[ $email =~ ^[A-Za-z0-9._%+-]+@ ]]</code></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="section-title" id="sec35-case"><span class="sec-num">35.</span> Multi-Branch Selection (`case ...
          esac`)</h2>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Case Statement Syntax</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="c-kw">case</span> <span class="c-str">"$1"</span> <span class="c-kw">in</span>
  <span class="c-str">"start"</span>)
    <span class="c-fn">echo</span> <span class="c-str">"Starting service daemon..."</span>
    ;;
  <span class="c-str">"stop"</span>)
    <span class="c-fn">echo</span> <span class="c-str">"Stopping service daemon..."</span>
    ;;
  <span class="c-str">"restart"</span>|<span class="c-str">"reload"</span>)
    <span class="c-fn">echo</span> <span class="c-str">"Restarting service daemon..."</span>
    ;;
  *)
    <span class="c-fn">echo</span> <span class="c-str">"Usage: $0 {start|stop|restart}"</span>
    <span class="c-kw">exit</span> <span class="c-num">1</span>
    ;;
<span class="c-kw">esac</span></code></pre>
          </div>
        </div>

        <h2 class="section-title" id="sec36-loops"><span class="sec-num">36.</span> Looping Constructs (`for`, `while`,
          `until`)</h2>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Looping Architectures</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="code-comment"># 1. For Loop over a range or array</span>
<span class="c-kw">for</span> i <span class="c-kw">in</span> {<span class="c-num">1..5</span>}; <span class="c-kw">do</span>
  <span class="c-fn">echo</span> <span class="c-str">"Iteration: $i"</span>
<span class="c-kw">done</span>

<span class="code-comment"># 2. C-Style For Loop</span>
<span class="c-kw">for</span> ((j=0; j&lt;3; j++)); <span class="c-kw">do</span>
  <span class="c-fn">echo</span> <span class="c-str">"Index: $j"</span>
<span class="c-kw">done</span>

<span class="code-comment"># 3. Robust Line-by-Line File Reading Loop (Preserves Leading Whitespace)</span>
<span class="c-kw">while</span> <span class="c-var">IFS</span>= <span class="c-kw">read -r</span> line; <span class="c-kw">do</span>
  <span class="c-fn">echo</span> <span class="c-str">"Processing: $line"</span>
<span class="c-kw">done</span> &lt; <span class="c-str">"/var/log/syslog"</span></code></pre>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>
<article class="doc-page" id="sec37-func">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 06</span>
          <span>Functions, Traps &amp; Hardening • Page 22</span>
        </header>

        <h2 class="section-title"><span class="sec-num">37.</span> Functions, Local Scope &amp; Return Codes</h2>
        <p>
          Functions in Bash provide code modularity. Inside functions, variables should always be scoped with the
          <code>local</code> keyword to prevent global namespace pollution:
        </p>

        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Modular Bash Function Structure</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="c-fn">calculate_disk_usage()</span> {
  <span class="c-kw">local</span> <span class="c-var">target_dir</span>=<span class="c-str">"$1"</span>
  <span class="c-kw">if</span> [[ ! -d <span class="c-str">"$target_dir"</span> ]]; <span class="c-kw">then</span>
    <span class="c-fn">echo</span> <span class="c-str">"Error: Directory $target_dir does not exist."</span> &gt;&amp;2
    <span class="c-kw">return</span> <span class="c-num">1</span>
  <span class="c-kw">fi</span>

  <span class="c-kw">local</span> <span class="c-var">usage</span>
  <span class="c-var">usage</span>=$(<span class="c-kw">du -sh</span> <span class="c-str">"$target_dir"</span> | <span class="c-kw">awk</span> <span class="c-str">'{print $1}'</span>)
  <span class="c-fn">echo</span> <span class="c-str">"$usage"</span>
  <span class="c-kw">return</span> <span class="c-num">0</span>
}

<span class="code-comment"># Function invocation and output capture</span>
<span class="c-var">DIR_SIZE</span>=$(<span class="c-fn">calculate_disk_usage</span> <span class="c-str">"/var/log"</span>)</code></pre>
          </div>
        </div>

        <h2 class="section-title" id="sec38-hard"><span class="sec-num">38.</span> Enterprise Script Hardening &amp;
          Signal Traps</h2>
        <p>
          Production scripts must be resilient against silent failures, uninitialized variables, and abrupt SIGINT
          interrupts. Use the <strong>Unofficial Bash Strict Mode</strong>:
        </p>

        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">Strict Mode &amp; Cleanup Traps</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="c-kw">set -euo pipefail</span>  <span class="code-comment"># -e (exit on error), -u (error on unset var), -o pipefail (catch pipe errors)</span>

<span class="c-var">TMP_FILE</span>=$(<span class="c-kw">mktemp</span> /tmp/backup_XXXXXX.tar.gz)

<span class="code-comment"># Cleanup function executed on normal EXIT or termination signals</span>
<span class="c-fn">cleanup()</span> {
  <span class="c-fn">echo</span> <span class="c-str">"Cleaning up temporary file $TMP_FILE..."</span>
  <span class="c-kw">rm -f</span> <span class="c-str">"$TMP_FILE"</span>
}
<span class="c-kw">trap</span> cleanup EXIT INT TERM</code></pre>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>
<article class="doc-page" id="sec40-progs">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 06</span>
          <span>10 Practical Problem Programs (Part 1) • Page 23</span>
        </header>

        <h2 class="section-title"><span class="sec-num">40.</span> 10 Practical Problem Programs (From Scratch to
          Advanced)</h2>
        <p>
          Below are 10 production-ready Bash shell scripts solving common enterprise systems, security, and
          administrative tasks. Every terminal includes full-width layout, comments toggle, and smart copy button.
        </p>

        <!-- Program 1 -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--primary);">Program 01: System
          Information &amp; Uptime Audit Reporter</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">sys_audit.sh</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="code-comment"># Program 1: Collects hostname, kernel, uptime, CPU cores, and RAM usage</span>
<span class="c-kw">set -euo pipefail</span>

<span class="c-fn">echo</span> <span class="c-str">"=================================================="</span>
<span class="c-fn">echo</span> <span class="c-str">"          SYSTEM HEALTH &amp; AUDIT REPORT           "</span>
<span class="c-fn">echo</span> <span class="c-str">"=================================================="</span>
<span class="c-fn">echo</span> <span class="c-str">"Hostname:       $(hostname)"</span>
<span class="c-fn">echo</span> <span class="c-str">"Kernel Version: $(uname -r)"</span>
<span class="c-fn">echo</span> <span class="c-str">"System Uptime:  $(uptime -p)"</span>
<span class="c-fn">echo</span> <span class="c-str">"CPU Cores:      $(nproc)"</span>
<span class="c-fn">echo</span> <span class="c-str">"Memory Usage:   $(free -h | awk '/^Mem:/ {print $3 "/" $2}')"</span>
<span class="c-fn">echo</span> <span class="c-str">"Root Disk Free: $(df -h / | awk 'NR==2 {print $4 " available (" $5 " used)"}')"</span>
<span class="c-fn">echo</span> <span class="c-str">"Generated on:   $(date '+%Y-%m-%d %H:%M:%S')"</span>
<span class="c-fn">echo</span> <span class="c-str">"=================================================="</span></code></pre>
          </div>
        </div>

        <!-- Program 2 -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--accent-purple);">Program 02:
          Arithmetic Calculator with Floating-Point Support</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">calc.sh</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="code-comment"># Program 2: Interactive calculator supporting +, -, *, /, and ^ with decimal precision</span>
<span class="c-kw">set -euo pipefail</span>

<span class="c-kw">read -p</span> <span class="c-str">"Enter First Number:  "</span> num1
<span class="c-kw">read -p</span> <span class="c-str">"Enter Operator (+ - * / ^): "</span> op
<span class="c-kw">read -p</span> <span class="c-str">"Enter Second Number: "</span> num2

<span class="c-kw">case</span> <span class="c-str">"$op"</span> <span class="c-kw">in</span>
  <span class="c-str">"+"</span>|<span class="c-str">"-"</span>|<span class="c-str">"*"</span>|<span class="c-str">"/"</span>|<span class="c-str">"^"</span>)
    <span class="c-var">result</span>=$(<span class="c-fn">echo</span> <span class="c-str">"scale=4; $num1 $op $num2"</span> | <span class="c-kw">bc -l</span>)
    <span class="c-fn">echo</span> <span class="c-str">"Result: $num1 $op $num2 = $result"</span>
    ;;
  *)
    <span class="c-fn">echo</span> <span class="c-str">"Error: Invalid operator '$op' provided."</span> &gt;&amp;2
    <span class="c-kw">exit</span> <span class="c-num">1</span>
    ;;
<span class="c-kw">esac</span></code></pre>
          </div>
        </div>

        <!-- Program 3 -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--accent-emerald);">Program 03:
          Password Policy &amp; Complexity Validator</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">check_password.sh</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="code-comment"># Program 3: Validates password length >= 8, uppercase, lowercase, digit, and special char</span>
<span class="c-kw">set -euo pipefail</span>

<span class="c-kw">read -s -p</span> <span class="c-str">"Enter password to evaluate: "</span> password
<span class="c-fn">echo</span> <span class="c-str">""</span>

<span class="c-kw">if</span> [[ ${#password} -lt 8 ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"FAIL: Password must be at least 8 characters long."</span>; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>
<span class="c-kw">if</span> ! [[ <span class="c-str">"$password"</span> =~ [A-Z] ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"FAIL: Missing at least one uppercase letter (A-Z)."</span>; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>
<span class="c-kw">if</span> ! [[ <span class="c-str">"$password"</span> =~ [a-z] ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"FAIL: Missing at least one lowercase letter (a-z)."</span>; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>
<span class="c-kw">if</span> ! [[ <span class="c-str">"$password"</span> =~ [0-9] ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"FAIL: Missing at least one numeric digit (0-9)."</span>; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>
<span class="c-kw">if</span> ! [[ <span class="c-str">"$password"</span> =~ ['!@#$%^&amp;*()_+'] ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"FAIL: Missing at least one special character (!@#$%^&amp;*)."</span>; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>

<span class="c-fn">echo</span> <span class="c-str">"SUCCESS: Password satisfies all enterprise complexity requirements."</span></code></pre>
          </div>
        </div>

        <!-- Program 4 -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--accent-amber);">Program 04: File
          Existence, Type &amp; Permission Inspector</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">file_inspector.sh</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="code-comment"># Program 4: Validates file existence, classification, size, and current permissions</span>
<span class="c-kw">set -euo pipefail</span>

<span class="c-var">target</span>=<span class="c-str">"${1:-}"</span>
<span class="c-kw">if</span> [[ -z <span class="c-str">"$target"</span> ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"Usage: $0 &lt;file_or_directory_path&gt;"</span>; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>

<span class="c-kw">if</span> [[ ! -e <span class="c-str">"$target"</span> ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"Error: Target path '$target' does not exist."</span>; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>

<span class="c-fn">echo</span> <span class="c-str">"Path:        $target"</span>
<span class="c-fn">echo</span> <span class="c-str">"Type:        $(file -b "$target")"</span>
<span class="c-fn">echo</span> <span class="c-str">"Size:        $(du -sh "$target" | awk '{print $1}')"</span>
<span class="c-fn">echo</span> <span class="c-str">"Permissions: $(stat -c '%A (%a)' "$target")"</span>
<span class="c-fn">echo</span> <span class="c-str">"Owner/Group: $(stat -c '%U:%G' "$target")"</span>
<span class="c-fn">echo</span> <span class="c-str">"Readable:    $([[ -r "$target" ]] &amp;&amp; echo "YES" || echo "NO")"</span>
<span class="c-fn">echo</span> <span class="c-str">"Writable:    $([[ -w "$target" ]] &amp;&amp; echo "YES" || echo "NO")"</span>
<span class="c-fn">echo</span> <span class="c-str">"Executable:  $([[ -x "$target" ]] &amp;&amp; echo "YES" || echo "NO")"</span></code></pre>
          </div>
        </div>

        <!-- Program 5 -->
        <h3 style="font-size: 0.95rem; font-weight: 700; margin-top: 1rem; color: var(--accent-rose);">Program 05:
          Automated Directory Backup &amp; Timestamped Tarball</h3>
        <div class="terminal-block comments-hidden full-width-module">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                class="term-dot dot-green"></span>
              <span class="terminal-title">backup_dir.sh</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                  style="width:12px;height:12px;"></i> <span>Comments</span></button>
              <button class="btn-term-action btn-copy-code"><i data-lucide="copy" style="width:12px;height:12px;"></i>
                <span>Copy</span></button>
            </div>
          </div>
          <div class="terminal-body">
            <pre
              class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="code-comment"># Program 5: Creates gzip-compressed timestamped backup and removes archives > 30 days old</span>
<span class="c-kw">set -euo pipefail</span>

<span class="c-var">SRC_DIR</span>=<span class="c-str">"${1:-/etc}"</span>
<span class="c-var">DEST_DIR</span>=<span class="c-str">"${2:-/var/backups}"</span>
<span class="c-var">TIMESTAMP</span>=$(<span class="c-kw">date</span> <span class="c-str">'+%Y%m%d_%H%M%S'</span>)
<span class="c-var">ARCHIVE_NAME</span>=<span class="c-str">"backup_$(basename "$SRC_DIR")_${TIMESTAMP}.tar.gz"</span>

<span class="c-kw">mkdir -p</span> <span class="c-str">"$DEST_DIR"</span>
<span class="c-fn">echo</span> <span class="c-str">"Creating archive $DEST_DIR/$ARCHIVE_NAME from $SRC_DIR..."</span>
<span class="c-kw">tar -czf</span> <span class="c-str">"$DEST_DIR/$ARCHIVE_NAME"</span> <span class="c-str">"$SRC_DIR"</span>

<span class="c-fn">echo</span> <span class="c-str">"Archive created successfully ($(du -sh "$DEST_DIR/$ARCHIVE_NAME" | awk '{print $1}'))."</span>
<span class="code-comment"># Delete archives older than 30 days</span>
<span class="c-kw">find</span> <span class="c-str">"$DEST_DIR"</span> <span class="c-flg">-type</span> f <span class="c-flg">-name</span> <span class="c-str">"backup_*.tar.gz"</span> <span class="c-flg">-mtime</span> <span class="c-num">+30</span> <span class="c-flg">-delete</span></code></pre>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>

<!-- Page 35: Remote Access Tools & Professional IT Communication -->
<article class="doc-page" id="it6-remote-support-communication">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 06 • Page 05</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">35.</span> Remote Access Tools &amp; Professional IT Communication Standards
  </h2>

  <p class="lead-para">
    Modern technical support requires administering remote systems securely across distributed corporate networks while upholding rigorous professional communication, active listening, customer empathy, and ethical data privacy standards.
  </p>

  <div class="callout callout-key">
    <div class="callout-label"><i data-lucide="radio"></i> REMOTE ACCESS PROTOCOL SPECIFICATIONS</div>
    <div class="callout-body">
      Remote desktop protocols vary by underlying transport layer, encryption strength, and network traversal capabilities. Technicians must select the appropriate tool according to security boundaries (intranet vs public internet) and target operating systems.
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Remote Support Technologies Comparison Matrix
  </h3>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Technology</th>
          <th>Default Port</th>
          <th>Transport Protocol</th>
          <th>Encryption &amp; Security Model</th>
          <th>Typical Support Scenario</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Microsoft RDP</strong></td>
          <td><code>TCP/UDP 3389</code></td>
          <td>RDP / T.128</td>
          <td>TLS with Network Level Authentication (NLA); enforces Windows Credential Security Support Provider (CredSSP).</td>
          <td>Corporate intranet server and workstation administration (<code>mstsc.exe</code>).</td>
        </tr>
        <tr>
          <td><strong>Microsoft Quick Assist</strong></td>
          <td><code>HTTPS 443</code></td>
          <td>WebRTC / Azure Cloud Relay</td>
          <td>TLS 1.3 end-to-end; requires one-time 6-digit cryptographic security code generated by technician.</td>
          <td>Ad-hoc remote assistance for remote Windows users without opening inbound firewall ports.</td>
        </tr>
        <tr>
          <td><strong>Third-Party Cloud (TeamViewer / AnyDesk)</strong></td>
          <td><code>TCP 443 / 5938</code></td>
          <td>Proprietary broker relay</td>
          <td>RSA 2048/4096 public/private key exchange + AES-256 session encryption. Traverses NAT/firewalls via outbound broker connections.</td>
          <td>Cross-platform remote client support across public internet firewalls.</td>
        </tr>
        <tr>
          <td><strong>Secure Shell (SSH)</strong></td>
          <td><code>TCP 22</code></td>
          <td>SSH-2</td>
          <td>Asymmetric public-key cryptography (Ed25519 / RSA-4096) with Diffie-Hellman ephemeral key exchange; eliminates cleartext credentials.</td>
          <td>Linux/UNIX server administration, network switch CLI configuration, and secure file transfer (SFTP/SCP).</td>
        </tr>
        <tr>
          <td><strong>Virtual Network Computing (VNC)</strong></td>
          <td><code>TCP 5900</code></td>
          <td>Remote Frame Buffer (RFB)</td>
          <td>Historically unencrypted cleartext; modern deployments require tunneling through an SSH tunnel or TLS wrapper.</td>
          <td>Cross-platform screen mirroring (Linux, macOS, legacy embedded appliances).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    2. Professional IT Communication &amp; Incident De-Escalation
  </h3>

  <p>
    Technical expertise is ineffective without professional communication. IT professionals serve as the human bridge between complex technology and organizational productivity.
  </p>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1rem 0;">
    <div style="padding: 1rem; border-radius: 8px; background: var(--bg-surface); border: 1px solid var(--border-subtle);">
      <h4 style="color: var(--primary); font-size: 0.95rem; margin-bottom: 0.5rem;"><i data-lucide="ear"></i> Active Listening &amp; Jargon Translation</h4>
      <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
        Allow the end user to describe the issue completely without interrupting. Paraphrase their statements to confirm mutual understanding: <em>"So if I understand correctly, the financial spreadsheet freezes whenever you click 'Generate Report', is that right?"</em> Avoid alienating acronyms (e.g. explain <em>"We are verifying your connection to the company storage"</em> instead of <em>"Checking CIFS/SMB port 445 packet loss on the default gateway"</em>).
      </p>
    </div>

    <div style="padding: 1rem; border-radius: 8px; background: var(--bg-surface); border: 1px solid var(--border-subtle);">
      <h4 style="color: var(--primary); font-size: 0.95rem; margin-bottom: 0.5rem;"><i data-lucide="shield-check"></i> Conflict De-Escalation &amp; Empathy</h4>
      <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
        Acknowledge user frustration objectively without becoming defensive or blaming the user: <em>"I understand how critical this payroll submission is, and I am making this my top priority until it is working."</em> Never make promises outside technical control; provide transparent, realistic estimated timeframes for resolution.
      </p>
    </div>

    <div style="padding: 1rem; border-radius: 8px; background: var(--bg-surface); border: 1px solid var(--border-subtle);">
      <h4 style="color: var(--primary); font-size: 0.95rem; margin-bottom: 0.5rem;"><i data-lucide="lock"></i> Ethical Data Privacy &amp; Confidentiality</h4>
      <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
        Technicians frequently possess administrative privileges granting access to sensitive HR records, intellectual property, and personal files. Professional ethics and legal regulations (GDPR, HIPAA) strictly forbid browsing user documents or disclosing confidential corporate information discovered during maintenance.
      </p>
    </div>

    <div style="padding: 1rem; border-radius: 8px; background: var(--bg-surface); border: 1px solid var(--border-subtle);">
      <h4 style="color: var(--primary); font-size: 0.95rem; margin-bottom: 0.5rem;"><i data-lucide="git-commit"></i> Digital Forensics &amp; Chain of Custody</h4>
      <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
        When handling equipment involved in security breaches or policy violations, preserve a strict <strong>Chain of Custody</strong> log detailing: exact timestamp of receipt, serial numbers, cryptographic hash of disk images (SHA-256), physical storage locker location, and signatures of every individual who accessed the evidence.
      </p>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Safety Protocols, ESD Mitigation &amp; Operational Procedures</span>
    <span>Unit 06 • Page 05</span>
  </div>
</article>

<!-- Page 38: Safety Protocols, ESD & Operational Procedures -->
<article class="doc-page" id="it6-safety-operational">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 06 • Page 06</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">38.</span> Physical Safety, ESD Mitigation, Environmental Controls &amp; Operational Documentation
  </h2>

  <p class="lead-para">
    IT technicians must prioritize human life safety, prevent invisible electrostatic discharge (ESD) degradation of sensitive semiconductor circuits, enforce datacenter HVAC environmental tolerances, and maintain professional incident documentation standards conforming to ITIL change management.
  </p>

  <div class="callout callout-key">
    <div class="callout-label"><i data-lucide="shield-alert"></i> ELECTROSTATIC DISCHARGE (ESD) PHYSICS &amp; PREVENTION</div>
    <div class="callout-body">
      A human cannot feel an electrostatic shock below <strong>3,000 Volts</strong>, and a visible spark requires &ge;<strong>10,000 Volts</strong>. However, microscopic silicon gate oxides in modern CPUs and NVMe SSDs are irreversibly punctured by static discharges as low as <strong>100 Volts</strong>!
      <ul style="margin-top:0.4rem; margin-left:1.25rem; line-height:1.6;">
        <li><strong>Antistatic Wrist Strap:</strong> Contains a 1 Megaohm current-limiting resistor to protect the technician from accidental electrocution if touching a live AC mains wire, while continuously bleeding static charges to chassis ground.</li>
        <li><strong>High-Voltage Safety Exclusion:</strong> <em>NEVER wear an ESD wrist strap when servicing Power Supply Units (SMPS) or CRT monitors!</em> Large internal electrolytic capacitors store lethal charges (400V+) long after the AC cord is unplugged.</li>
      </ul>
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Datacenter Environmental Controls &amp; Fire Suppression
  </h3>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Parameter / System</th>
          <th>ASHRAE / Enterprise Standard</th>
          <th>Consequence of Deviation</th>
          <th>Engineering Control Measure</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Ambient Temperature</strong></td>
          <td>18&deg;C–27&deg;C (64.4&deg;F–80.6&deg;F)</td>
          <td>Thermal throttling, premature capacitor failure, fan power consumption spikes.</td>
          <td>Hot Aisle / Cold Aisle containment layout with CRAC units.</td>
        </tr>
        <tr>
          <td><strong>Relative Humidity (RH)</strong></td>
          <td>40% to 60% non-condensing</td>
          <td>RH &lt; 30% creates extreme ESD hazard; RH &gt; 70% causes condensation and copper corrosion.</td>
          <td>Precision ultrasonic humidifiers and dehumidifiers monitored via BMS telemetry.</td>
        </tr>
        <tr>
          <td><strong>Fire Suppression</strong></td>
          <td>Class C (Electrical Fires) / Clean Agent (FM-200 / Inergen)</td>
          <td>Water sprinklers cause catastrophic electrical shorting and equipment destruction.</td>
          <td>Total flooding gaseous suppression that displaces oxygen without damaging electronics or leaving chemical residue.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    2. The 3-2-1 Enterprise Backup Rule &amp; Incident Documentation
  </h3>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1rem 0;">
    <div style="padding: 1rem; border-radius: 8px; background: var(--bg-surface); border: 1px solid var(--border-subtle);">
      <h4 style="color: var(--primary); font-size: 0.95rem; margin-bottom: 0.5rem;"><i data-lucide="database"></i> The 3-2-1 Backup Strategy</h4>
      <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
        Maintain at least <strong>3 copies</strong> of critical business data (1 primary production copy + 2 backup copies), across <strong>2 different media types</strong> (e.g. NVMe SAN and LTO Tape or Optical), with at least <strong>1 copy stored offsite / immutable cloud storage</strong> to guarantee recovery from physical disaster and ransomware encryption.
      </p>
    </div>

    <div style="padding: 1rem; border-radius: 8px; background: var(--bg-surface); border: 1px solid var(--border-subtle);">
      <h4 style="color: var(--primary); font-size: 0.95rem; margin-bottom: 0.5rem;"><i data-lucide="file-text"></i> Standard Operational Documentation (SOP)</h4>
      <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
        Every support incident must be documented in the enterprise ticketing system detailing: <strong>Initial User Problem Description</strong>, <strong>Root Cause Analysis (RCA)</strong>, <strong>Steps Taken to Resolve</strong>, <strong>Preventive Action Implemented</strong>, and <strong>User Acceptance Verification</strong>. Creates a searchable institutional knowledge base reducing Mean Time to Resolution (MTTR).
      </p>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 06 Practice Examination Bank</span>
    <span>Unit 06 • Page 06</span>
  </div>
</article>
<article class="doc-page" id="practice-mcq-u6">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 06</span>
          <span>Unit 3 Test Bank • 30 MCQs</span>
        </header>

        <div class="practice-sec-header" style="background: var(--accent-emerald);">
          <div>
            <h2>Unit 06 Self-Testing Bank: 30 Multiple Choice Questions</h2>
            <p>Comprehensive evaluation covering Linux architecture, Bash scripting syntax, operators, control flow,
              functions, traps, and automation.</p>
          </div>
          <div class="score-badge" id="mcqScoreU3">Score: 0 / 30</div>
        </div>

        <div class="mcq-grid">
          <!-- U3-Q01 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q01</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">What is the standard Shebang character sequence on the first line of an executable Bash
              script?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> //bin/bash</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> #!/bin/bash</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> $!/bin/bash</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> &lt;!-- #/bin/bash --&gt;</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> The Shebang is <code>#!</code> followed by the absolute interpreter path
              (e.g. <code>#!/bin/bash</code>).
            </div>
          </div>

          <!-- U3-Q02 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q02</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">Which Linux command grants execute permissions to a script named 'deploy.sh'?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> chmod +x deploy.sh</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> chown +e deploy.sh</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> setfacl --run deploy.sh</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> exec deploy.sh</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> <code>chmod +x</code> (or <code>chmod 755</code>) adds execute permissions to
              the file mode bits.
            </div>
          </div>

          <!-- U3-Q03 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="C">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q03</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">Which character begins a single-line comment in a Bash script?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> //</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> --</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> #</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> %</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: C.</strong> The hash symbol (<code>#</code>) marks the start of a comment in Bash.
            </div>
          </div>

          <!-- U3-Q04 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="D">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q04</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">What is the special variable that holds the exit status of the most recently executed
              command in Bash?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> $$</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> $#</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> $@</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> $?</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: D.</strong> <code>$?</code> returns the exit code of the last command (0 indicates
              success).
            </div>
          </div>

          <!-- U3-Q05 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q05</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">How do you declare and assign an integer variable 'PORT' with the value 8080 without
              syntax errors in Bash?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> PORT = 8080</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> PORT=8080</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> int PORT = 8080</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> set PORT: 8080</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> Bash assignments must have <strong>no spaces</strong> around the equals sign:
              <code>PORT=8080</code>.
            </div>
          </div>

          <!-- U3-Q06 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q06</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">What is the output of: `echo 'Hello $USER'`?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Hello $USER (Single quotes treat
                content literally)</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Hello root</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Hello john</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Syntax error</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> Single quotes preserve the literal value of all characters and prevent
              variable interpolation.
            </div>
          </div>

          <!-- U3-Q07 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="C">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q07</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">Which syntax is used for native integer arithmetic evaluation in modern Bash?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> $([ 10 + 5 ])</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> {10 + 5}</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> $(( 10 + 5 ))</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> #calc(10 + 5)</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: C.</strong> <code>$(( ... ))</code> performs arithmetic expansion.
            </div>
          </div>

          <!-- U3-Q08 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q08</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">Which test flag checks if a given directory path exists on disk?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> -f</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> -d</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> -z</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> -x</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> <code>-d &lt;path&gt;</code> evaluates to true if the path exists and is a
              directory.
            </div>
          </div>

          <!-- U3-Q09 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="D">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q09</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">What keyword terminates an 'if' conditional statement in Bash?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> end</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> endif</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> done</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> fi</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: D.</strong> An <code>if</code> block is closed with <code>fi</code> (if spelled
              backwards).
            </div>
          </div>

          <!-- U3-Q10 (Easy) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q10</span>
              <span class="diff-badge diff-easy">[Easy]</span>
            </div>
            <div class="mcq-q">Which read command option suppresses terminal echoing for sensitive password input?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> read -s</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> read -p</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> read -t</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> read -e</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> <code>read -s</code> enables silent mode, preventing typed characters from
              appearing on screen.
            </div>
          </div>

          <!-- U3-Q11 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="C">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q11</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">What is the difference between executing './script.sh' and 'source script.sh'?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 'source' executes the script in
                Ring 0; './script.sh' in Ring 3</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> There is no difference</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> './script.sh' spawns a separate
                child subshell; 'source' runs commands in the CURRENT shell, preserving exported variables</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 'source' only works in Python
                scripts</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: C.</strong> <code>source</code> (or <code>.</code>) executes commands directly in the
              calling shell environment, modifying current variables.
            </div>
          </div>

          <!-- U3-Q12 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q12</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">Which test operator checks if a string variable is EMPTY (length 0)?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> -n</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> -z</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> -e</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> -eq</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> <code>-z "$var"</code> returns true if string length is zero (empty).
            </div>
          </div>

          <!-- U3-Q13 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="D">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q13</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">How do you declare an Associative Array (key-value dictionary) in Bash 4+?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> array dict[]</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> map dict = {}</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> declare -a dict</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> declare -A dict</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: D.</strong> <code>declare -A</code> creates an associative array (uppercase A), whereas
              <code>declare -a</code> creates an indexed array.
            </div>
          </div>

          <!-- U3-Q14 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q14</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">What is the difference between '$@' and '$*' when enclosed in double quotes?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> "$@" preserves individual
                positional arguments as separate quoted words ("$1" "$2"); "$*" merges all arguments into a single
                string ("$1 $2")</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> "$@" is only for numbers; "$*" is
                for strings</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> "$*" is faster than "$@"</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> "$@" is deprecated in modern Bash
              </div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> <code>"$@"</code> expands each argument as a separate word, which is critical
              when iterating over parameters containing spaces.
            </div>
          </div>

          <!-- U3-Q15 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="C">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q15</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">Which command calculates floating-point division '10 / 3' to 3 decimal places?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> $(( 10 / 3.000 ))</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> expr 10 / 3 --float</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> echo "scale=3; 10 / 3" | bc</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> math.div(10, 3, 3)</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: C.</strong> <code>echo "scale=3; 10 / 3" | bc</code> invokes the GNU <code>bc</code>
              calculator with 3 decimal places of precision.
            </div>
          </div>

          <!-- U3-Q16 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q16</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">What is the purpose of 'set -e' in a Bash script?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Enables full debugging trace logs
              </div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Causes the script to terminate
                immediately if any command exits with a non-zero (error) status</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Exports all local variables to
                global environment</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Ignores all permission errors</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> <code>set -e</code> (errexit) halts script execution upon encountering any
              unhandled error.
            </div>
          </div>

          <!-- U3-Q17 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="D">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q17</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">How do you define a variable that is strictly LOCAL to a function?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> private var=10</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> let var=10</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> static var=10</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> local var=10</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: D.</strong> The <code>local</code> keyword confines variable scope to the executing
              function.
            </div>
          </div>

          <!-- U3-Q18 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q18</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">Which statement safely registers a cleanup function to execute when a script exits or
              receives SIGINT/SIGTERM?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> trap cleanup EXIT INT TERM</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> catch (cleanup)</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> on_exit cleanup</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> set --cleanup-on-kill</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> <code>trap &lt;function&gt; &lt;signals&gt;</code> intercepts OS signals and
              runs the handler routine.
            </div>
          </div>

          <!-- U3-Q19 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="C">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q19</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">Which command is used to read a text file line-by-line in Bash while safely preserving
              leading/trailing whitespace?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> for line in $(cat file.txt); do ...
                done</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> foreach line in file.txt do ...
                done</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> while IFS= read -r line; do ...
                done &lt; file.txt</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> loop file.txt &gt; line</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: C.</strong> Setting <code>IFS=</code> (empty delimiter) and <code>read -r</code> (disable
              backslash escapes) reads raw lines perfectly without truncation.
            </div>
          </div>

          <!-- U3-Q20 (Medium) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q20</span>
              <span class="diff-badge diff-med">[Medium]</span>
            </div>
            <div class="mcq-q">What does 'set -o pipefail' ensure in a chained pipeline (e.g. cmd1 | cmd2 | cmd3)?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Increases pipeline buffer size to
                64 MB</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The return code of the pipeline is
                the status of the last command to exit with a non-zero status (catches errors in earlier pipeline
                stages)</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Encrypts data flowing between
                stdout and stdin</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Restricts pipes to root users only
              </div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> By default, a pipe's exit code is only that of the last command.
              <code>pipefail</code> ensures failures in upstream stages (e.g. <code>cmd1</code>) fail the entire
              pipeline.
            </div>
          </div>

          <!-- U3-Q21 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q21</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">What parameter expansion syntax extracts a substring of length 4 starting at index 2 from
              variable 'STR="ABCDEFG"'?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ${STR:2:4}</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ${STR[2..4]}</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> ${STR#2#4}</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> ${STR(2,4)}</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> <code>${VAR:offset:length}</code> performs substring slicing (yielding
              <code>CDEF</code>).
            </div>
          </div>

          <!-- U3-Q22 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="C">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q22</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">How does the parameter expansion '${FILE%.tar.gz}' modify the string 'archive.tar.gz'?
            </div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Replaces '.tar.gz' with '.zip'
              </div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Deletes everything before '.tar.gz'
              </div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Strips the trailing suffix
                '.tar.gz', returning 'archive'</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Triggers an unhandled syntax error
              </div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: C.</strong> <code>${VAR%pattern}</code> removes the shortest matching pattern from the
              end of the variable.
            </div>
          </div>

          <!-- U3-Q23 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q23</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">What is the consequence of setting 'set -u' in a script that references an unassigned
              variable '$UNDEF_VAR'?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It assigns the variable a default
                value of 0</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Bash treats unset variables as an
                error, prints a diagnostic to stderr, and immediately terminates the script</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It prompts the user via stdin for a
                replacement value</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It automatically initializes it as
                a global array</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> <code>set -u</code> (nounset) prevents catastrophic bugs (such as
              <code>rm -rf /$UNSET_VAR</code>) by exiting on undefined variables.
            </div>
          </div>

          <!-- U3-Q24 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="D">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q24</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">Which syntax tests if variable '$EMAIL' matches a regular expression pattern inside
              double brackets '[[ ... ]]'?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> [[ $EMAIL == regex(...) ]]</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> [[ $EMAIL match pattern ]]</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> [[ $EMAIL ?= /pattern/ ]]</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> [[ $EMAIL =~
                ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$ ]]</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: D.</strong> The <code>=~</code> operator performs regex pattern matching inside
              <code>[[ ... ]]</code>.
            </div>
          </div>

          <!-- U3-Q25 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q25</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">In a subshell expression '( cd /tmp &amp;&amp; rm -f *.log )', what happens to the
              working directory of the PARENT shell after execution?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The parent shell remains in its
                original working directory (parent environment is unaffected by subshell changes)</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The parent shell changes to /tmp
              </div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The parent shell terminates
                immediately</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The parent shell switches to root
                user</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> Commands enclosed in parentheses <code>( ... )</code> execute in a forked
              child subshell; directory and variable modifications do not propagate back to the parent.
            </div>
          </div>

          <!-- U3-Q26 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="C">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q26</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">What is the default numeric value returned by a function that reaches its end without an
              explicit 'return' statement?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 1</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 255</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The exit status of the LAST command
                executed inside that function</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Undefined / Random integer</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: C.</strong> If no <code>return</code> is specified, a function's exit status is
              automatically the exit code of its final executed command.
            </div>
          </div>

          <!-- U3-Q27 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q27</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">What command creates a cryptographically secure temporary file in '/tmp' with random
              suffix characters?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> touch /tmp/random.txt</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> mktemp /tmp/temp_XXXXXX</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> tempfile --force</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> new /tmp/file</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> <code>mktemp /tmp/temp_XXXXXX</code> atomically creates a unique temporary
              file with restricted permissions (0600), preventing symlink race conditions.
            </div>
          </div>

          <!-- U3-Q28 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="D">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q28</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">Which parameter expansion assigns a default value 'dev' to variable 'ENV' ONLY IF 'ENV'
              is unset or null?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ${ENV=dev}</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ${ENV:-dev}</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> ${ENV?dev}</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> ${ENV:=dev}</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: D.</strong> <code>${VAR:=default}</code> assigns the default value to <code>VAR</code>
              in-place if it is unset/null, while <code>${VAR:-default}</code> only substitutes the value without
              modifying the variable.
            </div>
          </div>

          <!-- U3-Q29 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="A">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q29</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">How does a Bash script redirect BOTH standard output (stdout) and standard error (stderr)
              to a single log file '/var/log/audit.log'?</div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> &gt; /var/log/audit.log 2&gt;&amp;1
                (or &amp;&gt; /var/log/audit.log)</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 2&gt;1 /var/log/audit.log</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> &gt;&gt; /var/log/audit.log +err
              </div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> | tee --all /var/log/audit.log
              </div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: A.</strong> <code>&gt; file 2&gt;&amp;1</code> redirects file descriptor 2 (stderr) to
              descriptor 1 (stdout), sending all stream output into the target file.
            </div>
          </div>

          <!-- U3-Q30 (Hard) -->
          <div class="mcq-card" data-unit="3" data-correct="B">
            <div class="mcq-header-meta">
              <span class="mcq-num">Q30</span>
              <span class="diff-badge diff-hard">[Hard]</span>
            </div>
            <div class="mcq-q">What is the purpose of the 'IFS' (Internal Field Separator) special variable in Bash?
            </div>
            <div class="mcq-options">
              <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It configures the default IP
                firewall socket timeout</div>
              <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It defines the delimiter characters
                (by default space, tab, newline) used by the shell to split words during word splitting and the 'read'
                command</div>
              <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It sets the maximum file size for
                disk writes</div>
              <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It specifies the default
                cryptographic hash function</div>
            </div>
            <div class="mcq-explanation">
              <strong>Correct: B.</strong> <code>IFS</code> determines how Bash splits strings into words during
              expansions and line parsing.
            </div>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>
<article class="doc-page" id="practice-subj-short-u6">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 06</span>
          <span>Subjective Conceptual Q&amp;A • Short</span>
        </header>

        <h2 class="section-title"><span class="sec-num">Q&amp;A.</span> Unit 6 Short Conceptual Questions (5 Sets)</h2>

        <!-- SQ 1 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">SQ1</span> Explain why 'set -euo pipefail' is considered
              best practice for production Bash scripts.</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Answer:</strong></p>
            <ul style="padding-left:1.5rem; line-height:1.6;">
              <li><code>set -e</code> (errexit): Halts the script immediately if any simple command returns a non-zero
                exit status, preventing cascading failures.</li>
              <li><code>set -u</code> (nounset): Treats uninitialized or undefined variables as fatal errors, preventing
                accidental deletion of files (e.g. <code>rm -rf "$UNSET_VAR/*"</code> becoming
                <code>rm -rf "/*"</code>).</li>
              <li><code>set -o pipefail</code>: Ensures that a pipeline (e.g. <code>cmd1 | cmd2 | cmd3</code>) returns
                the exit code of the last command that failed, rather than always masking errors if <code>cmd3</code>
                succeeds.</li>
            </ul>
          </div>
        </div>

        <!-- SQ 2 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">SQ2</span> Differentiate between single quotes ('...'),
              double quotes ("..."), and command substitution ($( ... )) in Bash.</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Answer:</strong></p>
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Construct</th>
                    <th>Evaluation Behavior</th>
                    <th>Example Output for VAR=10</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Single Quotes (<code>'...'</code>)</strong></td>
                    <td>Strictly literal. No variable expansion, escape characters, or subshells are evaluated.</td>
                    <td><code>echo '$VAR'</code> &rarr; <code>$VAR</code></td>
                  </tr>
                  <tr>
                    <td><strong>Double Quotes (<code>"..."</code>)</strong></td>
                    <td>Weak quoting. Preserves whitespace but expands variables, arithmetic, and command substitutions.
                    </td>
                    <td><code>echo "$VAR"</code> &rarr; <code>10</code></td>
                  </tr>
                  <tr>
                    <td><strong>Command Sub (<code>$(...)</code>)</strong></td>
                    <td>Executes command inside a subshell and returns standard output.</td>
                    <td><code>echo "$(date)"</code> &rarr; <code>Thu Sep 24 15:00:00 UTC 2026</code></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- SQ 3 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">SQ3</span> Why is 'while IFS= read -r line' preferred
              over 'for line in $(cat file)' when reading files?</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Answer:</strong></p>
            <p>
              The construct <code>for line in $(cat file)</code> suffers from severe flaws:
            </p>
            <ul style="padding-left:1.5rem; line-height:1.6;">
              <li>It loads the entire file into memory at once, failing on large multi-gigabyte logs.</li>
              <li>Word splitting splits on spaces and tabs rather than newlines, breaking lines containing spaces into
                multiple iterations.</li>
              <li>Globbing will expand wildcard characters (like <code>*</code>) into matching filenames.</li>
            </ul>
            <p style="margin-top:0.4rem;">
              Conversely, <code>while IFS= read -r line; do ... done &lt; file</code> streams lines one by one, disables
              backslash escaping (<code>-r</code>), and preserves exact line formatting without loading the entire file
              into RAM.
            </p>
          </div>
        </div>

        <!-- SQ 4 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">SQ4</span> How does the 'trap' command function in
              handling graceful termination and temporary file cleanup?</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Answer:</strong></p>
            <p>
              The <code>trap</code> command registers a handler callback function that the shell invokes upon receiving
              specific operating system signals:
            </p>
            <ul style="padding-left:1.5rem; line-height:1.6;">
              <li><code>EXIT</code> (Pseudo-signal 0): Fires when the script terminates naturally or exits via
                <code>exit</code>.</li>
              <li><code>INT</code> (SIGINT / Ctrl+C) and <code>TERM</code> (SIGTERM): Fires when the process is
                interrupted or terminated by the OS/user.</li>
              <li>By binding <code>trap cleanup EXIT INT TERM</code>, temporary lockfiles and scratch directories
                created via <code>mktemp</code> are guaranteed to be purged even during abnormal interruptions.</li>
            </ul>
          </div>
        </div>

        <!-- SQ 5 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">SQ5</span> Write a one-line Bash command to find and
              delete all '.tmp' files in '/var/log' older than 7 days.</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Answer:</strong></p>
            <div class="terminal-block comments-hidden full-width-module">
              <div class="terminal-header">
                <div class="terminal-header-left">
                  <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                    class="term-dot dot-green"></span>
                  <span class="terminal-title">Bash One-Liner</span>
                </div>
                <div class="terminal-actions">
                  <button class="btn-term-action btn-copy-code"><i data-lucide="copy"
                      style="width:12px;height:12px;"></i> <span>Copy</span></button>
                </div>
              </div>
              <div class="terminal-body">
                <pre
                  class="code-pre"><code><span class="c-kw">find</span> /var/log <span class="c-flg">-type</span> f <span class="c-flg">-name</span> <span class="c-str">"*.tmp"</span> <span class="c-flg">-mtime</span> <span class="c-num">+7</span> <span class="c-flg">-delete</span></code></pre>
              </div>
            </div>
          </div>
        </div>

        <footer class="page-footer-meta">
          <span>Course Engineering & Knowledge Reference Suite</span>
          <span>CSC104 Study Notes • Unit 03</span>
        </footer>
      </article>
<article class="doc-page" id="practice-subj-long-u6">
        <header class="page-header-meta">
          <span>CSC104: IT Fundamentals • Unit 06</span>
          <span>Analytical Problems &amp; Answer Key</span>
        </header>

        <h2 class="section-title"><span class="sec-num">DEEP.</span> Unit 6 Analytical &amp; Scenario Problems (4 Sets)
        </h2>

        <!-- LQ 1 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">LQ1</span> Enterprise Shell Engineering: Write a complete
              automated log rotation and compression script with locking, retention thresholds, and error alerting.
            </div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Comprehensive Solution:</strong></p>
            <div class="terminal-block comments-hidden full-width-module">
              <div class="terminal-header">
                <div class="terminal-header-left">
                  <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                    class="term-dot dot-green"></span>
                  <span class="terminal-title">log_rotate_enterprise.sh</span>
                </div>
                <div class="terminal-actions">
                  <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                      style="width:12px;height:12px;"></i> <span>Comments</span></button>
                  <button class="btn-term-action btn-copy-code"><i data-lucide="copy"
                      style="width:12px;height:12px;"></i> <span>Copy</span></button>
                </div>
              </div>
              <div class="terminal-body">
                <pre class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="c-kw">set -euo pipefail</span>

<span class="c-var">LOG_DIR</span>=<span class="c-str">"/var/log/app"</span>
<span class="c-var">MAX_SIZE_MB</span>=<span class="c-num">50</span>
<span class="c-var">RETENTION_DAYS</span>=<span class="c-num">14</span>
<span class="c-var">LOCK_FILE</span>=<span class="c-str">"/tmp/log_rotate.lock"</span>

<span class="code-comment"># Ensure single instance execution via lockfile</span>
<span class="c-kw">exec</span> <span class="c-num">200</span>&gt;<span class="c-str">"$LOCK_FILE"</span>
<span class="c-kw">flock -n 200</span> || { <span class="c-fn">echo</span> <span class="c-str">"Another rotation job is already running."</span> &gt;&amp;2; <span class="c-kw">exit</span> <span class="c-num">1</span>; }

<span class="c-fn">echo</span> <span class="c-str">"[$(date '+%Y-%m-%d %H:%M:%S')] Starting log rotation audit on $LOG_DIR..."</span>

<span class="c-kw">for</span> logfile <span class="c-kw">in</span> <span class="c-str">"$LOG_DIR"</span>/*.log; <span class="c-kw">do</span>
  [[ -f <span class="c-str">"$logfile"</span> ]] || <span class="c-kw">continue</span>

  <span class="c-var">size_bytes</span>=$(<span class="c-kw">stat -c</span> <span class="c-str">'%s'</span> <span class="c-str">"$logfile"</span>)
  <span class="c-var">size_mb</span>=$((size_bytes / 1024 / 1024))

  <span class="c-kw">if</span> [[ $size_mb -ge $MAX_SIZE_MB ]]; <span class="c-kw">then</span>
    <span class="c-var">timestamp</span>=$(<span class="c-kw">date</span> <span class="c-str">'+%Y%m%d_%H%M%S'</span>)
    <span class="c-var">rotated_file</span>=<span class="c-str">"${logfile}.${timestamp}"</span>

    <span class="c-fn">echo</span> <span class="c-str">"Rotating $logfile ($size_mb MB) -&gt; $rotated_file.gz"</span>
    <span class="c-kw">mv</span> <span class="c-str">"$logfile"</span> <span class="c-str">"$rotated_file"</span>
    <span class="c-kw">touch</span> <span class="c-str">"$logfile"</span>
    <span class="c-kw">chmod 644</span> <span class="c-str">"$logfile"</span>
    <span class="c-kw">gzip</span> <span class="c-str">"$rotated_file"</span>
  <span class="c-kw">fi</span>
<span class="c-kw">done</span>

<span class="code-comment"># Purge compressed archives older than retention threshold</span>
<span class="c-kw">find</span> <span class="c-str">"$LOG_DIR"</span> <span class="c-flg">-type</span> f <span class="c-flg">-name</span> <span class="c-str">"*.log.*.gz"</span> <span class="c-flg">-mtime</span> <span class="c-str">"+$RETENTION_DAYS"</span> <span class="c-flg">-delete</span>
<span class="c-fn">echo</span> <span class="c-str">"Rotation job completed successfully."</span></code></pre>
              </div>
            </div>
          </div>
        </div>

        <!-- LQ 2 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">LQ2</span> String Processing &amp; Parameter Expansion:
              Explain and demonstrate 5 advanced expansion techniques without external binaries.</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Comprehensive Solution:</strong></p>
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Expansion Form</th>
                    <th>Operational Behavior</th>
                    <th>Pure Bash Example</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Default Value (<code>${VAR:-default}</code>)</strong></td>
                    <td>Returns <code>default</code> if <code>VAR</code> is unset or empty, but leaves <code>VAR</code>
                      unchanged.</td>
                    <td><code>PORT=${1:-8080}</code> (Assigns 8080 if arg 1 missing).</td>
                  </tr>
                  <tr>
                    <td><strong>Assign Default (<code>${VAR:=default}</code>)</strong></td>
                    <td>Assigns <code>default</code> directly to <code>VAR</code> in-place if unset.</td>
                    <td><code>${DEBUG:=0}</code> (Sets DEBUG=0 if undefined).</td>
                  </tr>
                  <tr>
                    <td><strong>Strip Suffix (<code>${VAR%pattern}</code>)</strong></td>
                    <td>Strips shortest matching pattern from the end of the string.</td>
                    <td><code>FILE="report.tar.gz"; echo "${FILE%.*}"</code> &rarr; <code>report.tar</code></td>
                  </tr>
                  <tr>
                    <td><strong>Strip Prefix (<code>${VAR#pattern}</code>)</strong></td>
                    <td>Strips shortest matching pattern from the beginning of the string.</td>
                    <td><code>PATH="/var/log/syslog"; echo "${PATH##*/}"</code> &rarr; <code>syslog</code></td>
                  </tr>
                  <tr>
                    <td><strong>Pattern Replace (<code>${VAR//old/new}</code>)</strong></td>
                    <td>Replaces ALL occurrences of <code>old</code> with <code>new</code>.</td>
                    <td><code>IP="192.168.1.1"; echo "${IP//./_}"</code> &rarr; <code>192_168_1_1</code></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- LQ 3 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">LQ3</span> Process Management &amp; Concurrency: Write a
              multi-threaded parallel ping scanner using background jobs (&) and the 'wait' command.</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Comprehensive Solution:</strong></p>
            <div class="terminal-block comments-hidden full-width-module">
              <div class="terminal-header">
                <div class="terminal-header-left">
                  <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                    class="term-dot dot-green"></span>
                  <span class="terminal-title">parallel_subnet_scanner.sh</span>
                </div>
                <div class="terminal-actions">
                  <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                      style="width:12px;height:12px;"></i> <span>Comments</span></button>
                  <button class="btn-term-action btn-copy-code"><i data-lucide="copy"
                      style="width:12px;height:12px;"></i> <span>Copy</span></button>
                </div>
              </div>
              <div class="terminal-body">
                <pre class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="c-kw">set -euo pipefail</span>

<span class="c-var">SUBNET</span>=<span class="c-str">"${1:-192.168.1}"</span>

<span class="c-fn">ping_host()</span> {
  <span class="c-kw">local</span> <span class="c-var">ip</span>=<span class="c-str">"$1"</span>
  <span class="c-kw">if</span> <span class="c-kw">ping -c 1 -W 1</span> <span class="c-str">"$ip"</span> &gt; /dev/null <span class="c-num">2</span>&gt;&amp;<span class="c-num">1</span>; <span class="c-kw">then</span>
    <span class="c-fn">echo</span> <span class="c-str">"[ACTIVE] $ip is responding."</span>
  <span class="c-kw">fi</span>
}

<span class="c-fn">echo</span> <span class="c-str">"Scanning subnet $SUBNET.0/24 in parallel..."</span>

<span class="c-kw">for</span> host <span class="c-kw">in</span> {<span class="c-num">1..254</span>}; <span class="c-kw">do</span>
  <span class="c-fn">ping_host</span> <span class="c-str">"${SUBNET}.${host}"</span> &amp;  <span class="code-comment"># Spawn in background</span>
<span class="c-kw">done</span>

<span class="code-comment"># Wait for all background subshell jobs to finish</span>
<span class="c-kw">wait</span>
<span class="c-fn">echo</span> <span class="c-str">"Subnet scan completed."</span></code></pre>
              </div>
            </div>
          </div>
        </div>

        <!-- LQ 4 -->
        <div class="subj-card">
          <div class="subj-header">
            <div class="subj-q-title"><span class="subj-q-num">LQ4</span> Enterprise Automation Scenario: Write a robust
              provisioning script that validates root privileges, parses flags (-u, -g, -p), and logs operations.</div>
            <i data-lucide="chevron-down" class="subj-chevron"></i>
          </div>
          <div class="subj-body">
            <p><strong>Comprehensive Solution:</strong></p>
            <div class="terminal-block comments-hidden full-width-module">
              <div class="terminal-header">
                <div class="terminal-header-left">
                  <span class="term-dot dot-red"></span><span class="term-dot dot-yellow"></span><span
                    class="term-dot dot-green"></span>
                  <span class="terminal-title">provision_admin.sh</span>
                </div>
                <div class="terminal-actions">
                  <button class="btn-term-action btn-toggle-comments"><i data-lucide="eye"
                      style="width:12px;height:12px;"></i> <span>Comments</span></button>
                  <button class="btn-term-action btn-copy-code"><i data-lucide="copy"
                      style="width:12px;height:12px;"></i> <span>Copy</span></button>
                </div>
              </div>
              <div class="terminal-body">
                <pre class="code-pre"><code><span class="c-shebang">#!/usr/bin/env bash</span>
<span class="c-kw">set -euo pipefail</span>

<span class="code-comment"># 1. Enforce root execution requirement</span>
<span class="c-kw">if</span> [[ $(id -u) -ne 0 ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"Error: This script must be executed as root (UID 0)."</span> &gt;&amp;2
  <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>

<span class="c-var">USERNAME</span>=<span class="c-str">""</span>; <span class="c-var">GROUPNAME</span>=<span class="c-str">"developers"</span>; <span class="c-var">PASSWORD</span>=<span class="c-str">""</span>

<span class="code-comment"># 2. Parse command-line options via getopts</span>
<span class="c-kw">while</span> <span class="c-kw">getopts</span> <span class="c-str">"u:g:p:h"</span> opt; <span class="c-kw">do</span>
  <span class="c-kw">case</span> <span class="c-str">"$opt"</span> <span class="c-kw">in</span>
    u) <span class="c-var">USERNAME</span>=<span class="c-str">"$OPTARG"</span> ;;
    g) <span class="c-var">GROUPNAME</span>=<span class="c-str">"$OPTARG"</span> ;;
    p) <span class="c-var">PASSWORD</span>=<span class="c-str">"$OPTARG"</span> ;;
    h) <span class="c-fn">echo</span> <span class="c-str">"Usage: $0 -u &lt;user&gt; [-g &lt;group&gt;] -p &lt;pass&gt;"</span>; <span class="c-kw">exit</span> <span class="c-num">0</span> ;;
    *) <span class="c-fn">echo</span> <span class="c-str">"Invalid argument"</span> &gt;&amp;2; <span class="c-kw">exit</span> <span class="c-num">1</span> ;;
  <span class="c-kw">esac</span>
<span class="c-kw">done</span>

<span class="c-kw">if</span> [[ -z <span class="c-str">"$USERNAME"</span> || -z <span class="c-str">"$PASSWORD"</span> ]]; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"Error: -u &lt;user&gt; and -p &lt;pass&gt; are required parameters."</span> &gt;&amp;2; <span class="c-kw">exit</span> <span class="c-num">1</span>
<span class="c-kw">fi</span>

<span class="code-comment"># 3. Create group if non-existent</span>
<span class="c-kw">getent group</span> <span class="c-str">"$GROUPNAME"</span> &gt; /dev/null || <span class="c-kw">groupadd</span> <span class="c-str">"$GROUPNAME"</span>

<span class="code-comment"># 4. Create user and set encrypted password</span>
<span class="c-kw">if</span> <span class="c-kw">id -u</span> <span class="c-str">"$USERNAME"</span> &gt; /dev/null <span class="c-num">2</span>&gt;&amp;<span class="c-num">1</span>; <span class="c-kw">then</span>
  <span class="c-fn">echo</span> <span class="c-str">"User $USERNAME already exists."</span>
<span class="c-kw">else</span>
  <span class="c-kw">useradd -m -g</span> <span class="c-str">"$GROUPNAME"</span> <span class="c-flg">-s</span> /bin/bash <span class="c-str">"$USERNAME"</span>
  <span class="c-fn">echo</span> <span class="c-str">"${USERNAME}:${PASSWORD}"</span> | <span class="c-kw">chpasswd</span>
  <span class="c-fn">echo</span> <span class="c-str">"Successfully provisioned user '$USERNAME' into group '$GROUPNAME'."</span>
<span class="c-kw">fi</span></code></pre>
              </div>
            </div>
          </div>
        </div>

        <!-- MASTER ANSWER KEY TABLE -->
        <h2 class="section-title" id="mcq-answer-key-u3" style="margin-top: 2rem;"><span class="sec-num">KEY.</span>
          Master 30-MCQ Answer Key Table (Unit 06)</h2>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 8%;">Q#</th>
                <th style="width: 27%;">Topic Tested</th>
                <th style="width: 15%;">Difficulty</th>
                <th style="width: 12%;">Correct Answer</th>
                <th style="width: 38%;">Core Architectural Concept</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Q01</td>
                <td>Shebang Sequence</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>B</strong></td>
                <td><code>#!/bin/bash</code> declares the script interpreter.</td>
              </tr>
              <tr>
                <td>Q02</td>
                <td>chmod Execution Flag</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>A</strong></td>
                <td><code>chmod +x</code> grants execute permissions.</td>
              </tr>
              <tr>
                <td>Q03</td>
                <td>Single-Line Comments</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>C</strong></td>
                <td>The <code>#</code> symbol starts a comment line in Bash.</td>
              </tr>
              <tr>
                <td>Q04</td>
                <td>Exit Status Variable</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>D</strong></td>
                <td><code>$?</code> stores the return status of the last command.</td>
              </tr>
              <tr>
                <td>Q05</td>
                <td>Variable Assignment</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>B</strong></td>
                <td>Variable assignment requires no spaces around <code>=</code>.</td>
              </tr>
              <tr>
                <td>Q06</td>
                <td>Single Quote Literal</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>A</strong></td>
                <td>Single quotes disable all variable interpolation.</td>
              </tr>
              <tr>
                <td>Q07</td>
                <td>Arithmetic Expansion</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>C</strong></td>
                <td><code>$(( ... ))</code> performs native integer arithmetic.</td>
              </tr>
              <tr>
                <td>Q08</td>
                <td>Directory Test Operator</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>B</strong></td>
                <td><code>-d</code> checks if a path exists and is a directory.</td>
              </tr>
              <tr>
                <td>Q09</td>
                <td>If Block Termination</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>D</strong></td>
                <td><code>fi</code> closes an <code>if</code> conditional statement.</td>
              </tr>
              <tr>
                <td>Q10</td>
                <td>Silent Password Read</td>
                <td><span class="diff-badge diff-easy">Easy</span></td>
                <td><strong>A</strong></td>
                <td><code>read -s</code> suppresses terminal character echoing.</td>
              </tr>
              <tr>
                <td>Q11</td>
                <td>Subshell vs Sourcing</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>C</strong></td>
                <td><code>source</code> executes in current shell; <code>./</code> forks a subshell.</td>
              </tr>
              <tr>
                <td>Q12</td>
                <td>Empty String Test</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>B</strong></td>
                <td><code>-z</code> returns true if string length is zero.</td>
              </tr>
              <tr>
                <td>Q13</td>
                <td>Associative Array Dec</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>D</strong></td>
                <td><code>declare -A</code> creates key-value associative arrays.</td>
              </tr>
              <tr>
                <td>Q14</td>
                <td>$@ vs $* Quoting</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>A</strong></td>
                <td><code>"$@"</code> preserves separate arguments as distinct words.</td>
              </tr>
              <tr>
                <td>Q15</td>
                <td>bc Floating Point</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>C</strong></td>
                <td><code>bc</code> provides floating-point calculation with <code>scale</code>.</td>
              </tr>
              <tr>
                <td>Q16</td>
                <td>set -e (errexit)</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>B</strong></td>
                <td><code>set -e</code> aborts script execution on any unhandled error.</td>
              </tr>
              <tr>
                <td>Q17</td>
                <td>Function Local Scope</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>D</strong></td>
                <td>The <code>local</code> keyword confines variable scope to functions.</td>
              </tr>
              <tr>
                <td>Q18</td>
                <td>Signal Trapping</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>A</strong></td>
                <td><code>trap cleanup EXIT INT TERM</code> registers cleanup handlers.</td>
              </tr>
              <tr>
                <td>Q19</td>
                <td>IFS File Reading</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>C</strong></td>
                <td><code>while IFS= read -r</code> streams lines safely without truncation.</td>
              </tr>
              <tr>
                <td>Q20</td>
                <td>pipefail Setting</td>
                <td><span class="diff-badge diff-med">Medium</span></td>
                <td><strong>B</strong></td>
                <td><code>set -o pipefail</code> propagates errors across piped stages.</td>
              </tr>
              <tr>
                <td>Q21</td>
                <td>Substring Slice</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>A</strong></td>
                <td><code>${VAR:offset:len}</code> extracts substrings in pure Bash.</td>
              </tr>
              <tr>
                <td>Q22</td>
                <td>Suffix Stripping (%)</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>C</strong></td>
                <td><code>${VAR%pattern}</code> strips trailing matches.</td>
              </tr>
              <tr>
                <td>Q23</td>
                <td>set -u (nounset)</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>B</strong></td>
                <td><code>set -u</code> triggers fatal errors on uninitialized variables.</td>
              </tr>
              <tr>
                <td>Q24</td>
                <td>Regex Matching (=~)</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>D</strong></td>
                <td><code>[[ $val =~ regex ]]</code> executes regex comparisons.</td>
              </tr>
              <tr>
                <td>Q25</td>
                <td>Parentheses Subshell</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>A</strong></td>
                <td><code>( ... )</code> runs in a subshell without altering parent state.</td>
              </tr>
              <tr>
                <td>Q26</td>
                <td>Function Default Exit</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>C</strong></td>
                <td>Default return code is the exit status of the final command.</td>
              </tr>
              <tr>
                <td>Q27</td>
                <td>mktemp Secure Temp</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>B</strong></td>
                <td><code>mktemp</code> creates unique temp files with 0600 permissions.</td>
              </tr>
              <tr>
                <td>Q28</td>
                <td>Assign Default (:=)</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>D</strong></td>
                <td><code>${VAR:=val}</code> assigns default value in-place if unset.</td>
              </tr>
              <tr>
                <td>Q29</td>
                <td>2>&amp;1 Stream Merge</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>A</strong></td>
                <td><code>&gt; log 2&gt;&amp;1</code> merges stderr into stdout file stream.</td>
              </tr>
              <tr>
                <td>Q30</td>
                <td>IFS Field Separator</td>
                <td><span class="diff-badge diff-hard">Hard</span></td>
                <td><strong>B</strong></td>
                <td><code>IFS</code> defines word splitting and delimiter tokens.</td>
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
