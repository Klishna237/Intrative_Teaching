# -*- coding: utf-8 -*-
"""
Server Administration Portal - Unit 6: Networking, Disaster Recovery & Troubleshooting
SSM Engineering Standard Gold Standard Architecture
"""

SERVER_UNIT6_HTML = r"""
<!-- ===================================================================
     UNIT 06: NETWORKING, DISASTER RECOVERY & TROUBLESHOOTING
     =================================================================== -->

<!-- ARTICLE 26: SERVER NETWORKING & NIC TEAMING -->
<article class="doc-page" id="s6-networking">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Networking &amp; Troubleshooting • Article 26</span>
    <h2 class="section-title"><span class="sec-num">26</span> Enterprise Server Networking, NIC Teaming &amp; Cabling Fabrics</h2>
    <p class="lead-para">
      Enterprise servers rely on redundant physical network interfaces aggregated via NIC Teaming (Load Balancing and Failover - LBFO) to eliminate single points of network failure and deliver aggregated multi-gigabit throughput across switches.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. NIC Teaming Architecture Modes</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Teaming Mode</th>
          <th>Switch Dependency</th>
          <th>Physical Switch Topology</th>
          <th>Traffic Distribution &amp; Failover</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Switch Independent</strong></td>
          <td>None; switches require zero configuration</td>
          <td>Physical NICs connect to two completely separate, non-stacked Top-of-Rack (ToR) switches</td>
          <td>Maximum fault tolerance; protects against complete switch failure. Uses Active/Standby or Dynamic load distribution.</td>
        </tr>
        <tr>
          <td><strong>Static Teaming (IEEE 802.3ad draft v1)</strong></td>
          <td>Requires switch configuration</td>
          <td>Ports must terminate on the same physical switch or multi-chassis LAG (MLAG)</td>
          <td>Manual configuration of trunk groups; does not detect disconnected cables dynamically.</td>
        </tr>
        <tr>
          <td><strong>LACP (IEEE 802.1ax / 802.3ad)</strong></td>
          <td>Dynamic negotiation with switch</td>
          <td>Ports terminate on LACP-enabled switch stack or Cisco vPC / Arista MLAG</td>
          <td>Exchanges Link Aggregation Control Protocol (LACP) PDUs every 1s/30s; automatically disables failing links.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">2. Enterprise Structured Cabling Comparison</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Cable Standard</th>
          <th>Physical Medium</th>
          <th>Max Data Rate</th>
          <th>Max Operating Reach</th>
          <th>Datacenter Application</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cat 6a</strong></td>
          <td>Shielded Twisted Pair (STP) Copper</td>
          <td>10 Gbps (10GBASE-T)</td>
          <td>100 meters (328 ft)</td>
          <td>Standard datacenter rack patch panels, management networks</td>
        </tr>
        <tr>
          <td><strong>Cat 8</strong></td>
          <td>Fully Shielded Twisted Pair (S/FTP)</td>
          <td>25 Gbps / 40 Gbps</td>
          <td>30 meters (98 ft)</td>
          <td>Short Top-of-Rack (ToR) switch-to-server interconnects</td>
        </tr>
        <tr>
          <td><strong>OM4 / OM5 Multimode Fiber</strong></td>
          <td>50/125 &mu;m optical core (850nm / 953nm VCSEL laser)</td>
          <td>40 Gbps / 100 Gbps (SR4)</td>
          <td>100m – 150m</td>
          <td>Intra-datacenter row aggregation, SAN Fibre Channel 32G/64G fabrics</td>
        </tr>
        <tr>
          <td><strong>OS2 Singlemode Fiber</strong></td>
          <td>9/125 &mu;m optical core (1310nm / 1550nm laser)</td>
          <td>100 Gbps / 400 Gbps (LR4)</td>
          <td>10 km – 40 km</td>
          <td>Inter-datacenter campus backbones, dark fiber metro links</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 27: PROTOCOLS & ENTERPRISE PORT MATRIX -->
<article class="doc-page" id="s6-ports">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Networking &amp; Troubleshooting • Article 27</span>
    <h2 class="section-title"><span class="sec-num">27</span> Enterprise Server Protocols &amp; Master Well-Known Port Matrix</h2>
    <p class="lead-para">
      Network administrators must memorize critical communication ports to design firewall access control lists (ACLs) and diagnose socket connection dropouts across enterprise boundaries.
    </p>
  </header>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Port #</th>
          <th>Transport Protocol</th>
          <th>Service / Daemon</th>
          <th>Operational Function in Enterprise Systems</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>53</strong></td><td>TCP / UDP</td><td>DNS (Domain Name System)</td><td>UDP for standard name queries; TCP for zone transfers and responses &gt;512 bytes</td></tr>
        <tr><td><strong>67 / 68</strong></td><td>UDP</td><td>DHCP (Dynamic Host Config)</td><td>Port 67 for Server/Relay listening; Port 68 for Client broadcast communication</td></tr>
        <tr><td><strong>88</strong></td><td>TCP / UDP</td><td>Kerberos v5 KDC</td><td>Authentication ticket requests (AS-REQ) and service ticket grants (TGS-REQ)</td></tr>
        <tr><td><strong>123</strong></td><td>UDP</td><td>NTP (Network Time Protocol)</td><td>System clock synchronization; required for Kerberos &le;5-minute skew tolerance</td></tr>
        <tr><td><strong>161 / 162</strong></td><td>UDP</td><td>SNMP (Simple Network Mgmt)</td><td>Port 161 for polling queries; Port 162 for asynchronous alert SNMP Traps</td></tr>
        <tr><td><strong>389</strong></td><td>TCP / UDP</td><td>LDAP (Lightweight Directory)</td><td>Unencrypted directory queries and Active Directory binding</td></tr>
        <tr><td><strong>443</strong></td><td>TCP</td><td>HTTPS / TLS</td><td>Encrypted web application traffic, WSUS SSL synchronization, RESTful APIs</td></tr>
        <tr><td><strong>445</strong></td><td>TCP</td><td>SMB (Server Message Block)</td><td>Windows file sharing, named pipes, RPC communication, DFS replication</td></tr>
        <tr><td><strong>636</strong></td><td>TCP</td><td>LDAPS (LDAP over TLS)</td><td>Secure directory binding and encrypted user authentication queries</td></tr>
        <tr><td><strong>3260</strong></td><td>TCP</td><td>iSCSI Target Portal</td><td>Block storage discovery, SCSI encapsulation, and LUN volume attachment</td></tr>
        <tr><td><strong>3268 / 3269</strong></td><td>TCP</td><td>Active Directory Global Catalog</td><td>Port 3268 (LDAP GC); Port 3269 (LDAPS GC) for forest-wide search queries</td></tr>
        <tr><td><strong>3389</strong></td><td>TCP / UDP</td><td>RDP (Remote Desktop Protocol)</td><td>Graphical remote administrative console access</td></tr>
        <tr><td><strong>5985 / 5986</strong></td><td>TCP</td><td>WinRM (Windows Remote Mgmt)</td><td>PowerShell Remoting; Port 5985 (HTTP plaintext); Port 5986 (HTTPS encrypted)</td></tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 28: DISASTER RECOVERY & SITE TOPOLOGIES -->
<article class="doc-page" id="s6-dr">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Networking &amp; Troubleshooting • Article 28</span>
    <h2 class="section-title"><span class="sec-num">28</span> Disaster Recovery Principles, Site Topologies &amp; Storage Replication</h2>
    <p class="lead-para">
      Disaster Recovery (DR) guarantees continuity of operations when a catastrophic physical event (earthquake, flood, regional blackout) destroys the primary datacenter. Choosing between Hot, Warm, Cold, and Mobile recovery sites balances financial expenditure against Recovery Time Objectives.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Disaster Recovery Site Topologies</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Recovery Site Type</th>
          <th>Hardware &amp; Infrastructure State</th>
          <th>Data Synchronization State</th>
          <th>Recovery Time (RTO)</th>
          <th>Capital &amp; Operational Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Hot Site</strong></td>
          <td>Fully equipped, fully powered, mirrored hardware running 24/7 in secondary facility</td>
          <td>Continuous near-real-time synchronous or asynchronous storage replication</td>
          <td><strong>Minutes to Hours (near-zero RTO)</strong></td>
          <td>Extremely High (100% duplicate infrastructure costs)</td>
        </tr>
        <tr>
          <td><strong>Warm Site</strong></td>
          <td>Power, cooling, and server hardware pre-installed, but servers are idle/unconfigured</td>
          <td>Periodic asynchronous delta backups restored on a scheduled basis (daily/weekly)</td>
          <td><strong>Hours to Days (e.g. 12–48 hours)</strong></td>
          <td>Moderate</td>
        </tr>
        <tr>
          <td><strong>Cold Site</strong></td>
          <td>Physical real estate, power outlets, and HVAC present; zero server hardware</td>
          <td>No data present; administrator must procure hardware, install OS, and restore tapes</td>
          <td><strong>Weeks to Months</strong></td>
          <td>Lowest (leased commercial warehouse space)</td>
        </tr>
        <tr>
          <td><strong>Mobile Site</strong></td>
          <td>Self-contained trailer or shipping container equipped with mobile generator, racks, and satellite uplinks</td>
          <td>Restored from off-site cloud backups or transported hard drives</td>
          <td><strong>Days to Weeks</strong></td>
          <td>High specialized mobilization cost</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 29: BACKUP METHODOLOGIES & RPO/RTO MATHEMATICS -->
<article class="doc-page" id="s6-backups">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Networking &amp; Troubleshooting • Article 29</span>
    <h2 class="section-title"><span class="sec-num">29</span> Enterprise Backup Methodologies &amp; RPO / RTO SLA Mathematics</h2>
    <p class="lead-para">
      Backups represent the final line of defense against catastrophic ransomware, physical media degradation, and database corruption. Establishing compliant backup policies mandates mathematical optimization of Recovery Point Objectives (RPO), Recovery Time Objectives (RTO), and the modern 3-2-1-1-0 architecture.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Full vs Differential vs Incremental Backup Comparison</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Backup Type</th>
          <th>Blocks Backed Up</th>
          <th>Archive Bit Handling</th>
          <th>Backup Execution Speed</th>
          <th>Restore Complexity &amp; Speed</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Full Backup</strong></td>
          <td>All selected files and blocks on disk (100% data)</td>
          <td><strong>Clears</strong> archive bit (sets to 0)</td>
          <td>Slowest (hours to days); highest storage consumption</td>
          <td><strong>Fastest &amp; Simplest:</strong> Requires only 1 tape/image to restore full state.</td>
        </tr>
        <tr>
          <td><strong>Differential Backup</strong></td>
          <td>All files modified <em>since the last FULL backup</em></td>
          <td>Does <strong>NOT</strong> clear archive bit (remains 1)</td>
          <td>Moderate; backup size grows larger each subsequent day</td>
          <td><strong>Fast:</strong> Requires exactly 2 backup sets (Full + Latest Differential).</td>
        </tr>
        <tr>
          <td><strong>Incremental Backup</strong></td>
          <td>All files modified <em>since the last backup of ANY type</em> (Full or Incremental)</td>
          <td><strong>Clears</strong> archive bit (sets to 0)</td>
          <td><strong>Fastest:</strong> Backs up only tiny daily change deltas</td>
          <td><strong>Slowest &amp; Most Fragile:</strong> Requires Full + ALL sequential incrementals. If 1 incremental tape is corrupted, restore fails!</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="shield-check"></i> THE GOLD STANDARD: 3-2-1-1-0 BACKUP RULE</div>
    <div class="callout-body">
      To guarantee survival against modern ransomware and natural disasters:
      <ul style="margin-left: 1.2rem; margin-top: 0.5rem; line-height: 1.8;">
        <li><strong>3 Copies of Data:</strong> 1 primary production copy + at least 2 distinct backup copies.</li>
        <li><strong>2 Different Media Formats:</strong> E.g., fast local NVMe/SSD deduplication appliance + magnetic tape (LTO-9) or optical media.</li>
        <li><strong>1 Off-Site Copy:</strong> Replicated to a remote datacenter or cloud object storage repository.</li>
        <li><strong>1 Offline / Immutable Copy:</strong> Air-gapped magnetic tape or S3 Object Lock (WORM) storage that cannot be deleted even with root admin credentials.</li>
        <li><strong>0 Errors During Automated Recovery Testing:</strong> Daily automated boot verification (e.g., Veeam SureBackup) confirming zero database corruptions.</li>
      </ul>
    </div>
  </div>
</article>

<!-- ARTICLE 30: DIAGNOSTIC TRIAGE & BSOD KERNEL ANALYSIS -->
<article class="doc-page" id="s6-triage">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Networking &amp; Troubleshooting • Article 30</span>
    <h2 class="section-title"><span class="sec-num">30</span> Enterprise Diagnostic Triage &amp; Blue Screen (BSOD) Crash Analysis</h2>
    <p class="lead-para">
      When a production server crashes, an administrator must resist guess-and-check methodologies. Following the standardized CompTIA 7-Step Troubleshooting Model and analyzing Windows Blue Screen of Death (BSOD) kernel memory dumps (<code class="code-inline">MEMORY.DMP</code>) with WinDbg pinpoints hardware and driver faults with surgical precision.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. The CompTIA 7-Step Diagnostic Framework</h3>
  <ol style="margin-left: 1.5rem; line-height: 1.8; margin-bottom: 1.5rem;">
    <li><strong>Step 1: Identify the problem.</strong> Gather symptoms, question users, inspect error codes and system event logs, determine if anything changed recently.</li>
    <li><strong>Step 2: Establish a theory of probable cause.</strong> Brainstorm causes based on architectural knowledge; question the obvious.</li>
    <li><strong>Step 3: Test the theory to determine cause.</strong> Execute targeted diagnostic tests. If confirmed, proceed; if disproven, establish a new theory.</li>
    <li><strong>Step 4: Establish a plan of action and implement the solution.</strong> Document the change, identify potential impacts, test in a lab environment.</li>
    <li><strong>Step 5: Verify full system functionality.</strong> Test with the user; implement preventive measures to prevent recurrence.</li>
    <li><strong>Step 6: Document findings, actions, and outcomes.</strong> Record root cause, change logs, and resolutions in the enterprise ticketing knowledge base.</li>
  </ol>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">2. Windows Blue Screen Stop Code Reference &amp; WinDbg</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Bug Check / Stop Code</th>
          <th>Hex Value</th>
          <th>Root Cause Mechanism</th>
          <th>Common Trigger / Failing Component</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code class="code-inline">IRQL_NOT_LESS_OR_EQUAL</code></td>
          <td><code class="code-inline">0x0000000A</code></td>
          <td>A kernel process attempted to access pageable memory at an elevated Interrupt Request Level (IRQL).</td>
          <td>Buggy third-party kernel device driver (NIC, RAID, antivirus filter driver) accessing invalid pointer.</td>
        </tr>
        <tr>
          <td><code class="code-inline">PAGE_FAULT_IN_NONPAGED_AREA</code></td>
          <td><code class="code-inline">0x00000050</code></td>
          <td>Requested memory address was not in physical RAM and cannot be paged in from disk.</td>
          <td>Defective physical ECC RAM module, failing L3 CPU cache, or corrupted NTFS filesystem metadata.</td>
        </tr>
        <tr>
          <td><code class="code-inline">CRITICAL_PROCESS_DIED</code></td>
          <td><code class="code-inline">0x000000EF</code></td>
          <td>A critical system process essential to OS integrity (e.g. <code class="code-inline">csrss.exe</code>, <code class="code-inline">services.exe</code>) terminated unexpectedly.</td>
          <td>Corrupted system binary, malware termination attempt, or failing boot SSD storage drive.</td>
        </tr>
        <tr>
          <td><code class="code-inline">INACCESSIBLE_BOOT_DEVICE</code></td>
          <td><code class="code-inline">0x0000007B</code></td>
          <td>Windows kernel initialization failed to find or read the system partition during boot.</td>
          <td>Missing or corrupted storage controller driver (SAS/NVMe), changed UEFI SATA mode (AHCI to RAID), or corrupted BCD.</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- UNIT 6 PRACTICE BANK: 30 MCQS -->
<article class="doc-page" id="practice-mcq-s6">
  <div class="page-header-meta">
    <span class="meta-tag">Server Administration • Unit 06</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreS6">Score: 0 / 30</span>
  </div>
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Assessment • Practice Bank</span>
    <h2 class="section-title"><span class="sec-num">Q1</span> Unit 6 Practice Bank: 30 Interactive Examination MCQs</h2>
    <p class="lead-para">
      Comprehensive assessment questions matching CompTIA Server+, CompTIA Network+, and Microsoft IT Infrastructure certification standards.
    </p>
  </header>

  <div class="callout callout-deep" style="margin-bottom: 2rem;">
    <div class="callout-label"><i data-lucide="award"></i> REAL-TIME SCORE ENGINE</div>
    <div class="callout-body">
      Select your answer for each question. Instant feedback will highlight correct answers in green and explanations will appear automatically.
    </div>
  </div>

  <!-- MCQ 1 -->
  <div class="mcq-card" data-unit="s6" data-correct="C">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q1</span>
      <div class="mcq-question-text">An administrator performs a Full backup on Sunday night, followed by Incremental backups Monday through Thursday. On Friday morning, a storage array fails. What is the minimum set of backup media required to restore the server to its Thursday night state?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Only the Thursday incremental backup.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Sunday Full backup + Thursday incremental backup only.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Sunday Full backup + Monday, Tuesday, Wednesday, and Thursday incremental backups sequentially.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Any two random incremental tapes.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: C.</strong> Incremental backups record only the files modified since the preceding backup. Restoring requires the original Full backup plus EVERY sequential incremental backup in chronological order.
    </div>
  </div>

  <!-- MCQ 2 -->
  <div class="mcq-card" data-unit="s6" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q2</span>
      <div class="mcq-question-text">What diagnostic command in the Windows Debugger (WinDbg) automatically parses a memory crash dump (MEMORY.DMP) to determine the failing device driver and bug check stop code?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> !fixsystem</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> !analyze -v</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> chkdsk /r</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> sfc /scannow</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B (!analyze -v).</strong> In WinDbg, the extension command <code class="code-inline">!analyze -v</code> displays detailed bug check parameters, exception addresses, stack backtraces, and the specific driver module that triggered the crash.
    </div>
  </div>

  <!-- MCQ 3 -->
  <div class="mcq-card" data-unit="s6" data-correct="D">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q3</span>
      <div class="mcq-question-text">Which disaster recovery site model features pre-installed server hardware, power, cooling, and active data replication, providing recovery within minutes to hours at the highest financial cost?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Cold Site</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Warm Site</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Mobile Trailer Site</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Hot Site</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: D (Hot Site).</strong> A Hot Site is a fully operational mirrored datacenter with continuous replication, capable of absorbing production workloads with near-zero downtime.
    </div>
  </div>

  <!-- MCQ 4 -->
  <div class="mcq-card" data-unit="s6" data-correct="A">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q4</span>
      <div class="mcq-question-text">What is the IEEE standard for dynamic Link Aggregation Control Protocol (LACP) used in enterprise server NIC teaming?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> IEEE 802.1ax / IEEE 802.3ad</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> IEEE 802.11ac</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> IEEE 802.1D Spanning Tree</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> IEEE 802.3af PoE</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: A.</strong> IEEE 802.1ax (formerly 802.3ad) governs LACP, allowing servers and switches to dynamically bundle multiple physical Ethernet ports into a single logical channel.
    </div>
  </div>

  <!-- MCQ 5 -->
  <div class="mcq-card" data-unit="s6" data-correct="C">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q5</span>
      <div class="mcq-question-text">An enterprise SLA mandates that in the event of an outage, financial transaction systems must lose NO MORE than 15 minutes of transactional data. What disaster recovery metric does this represent?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Recovery Time Objective (RTO)</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Mean Time Between Failures (MTBF)</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Recovery Point Objective (RPO)</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Work Recovery Time (WRT)</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: C (RPO).</strong> Recovery Point Objective (RPO) dictates the maximum acceptable age of data that can be lost in an outage, measured in units of time (e.g. 15 minutes).
    </div>
  </div>

  <!-- MCQs 6 to 30 concise cards -->
  <div class="mcq-card" data-unit="s6" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q6</span><div class="mcq-question-text">What port is utilized by Windows Remote Management (WinRM) for secure, encrypted PowerShell Remoting sessions over HTTPS?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> TCP 5985</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> TCP 5986</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> TCP 3389</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> TCP 22</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> WinRM uses port 5985 for unencrypted HTTP, and port 5986 for TLS-encrypted HTTPS communication.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q7</span><div class="mcq-question-text">Which fiber optic cable type utilizes a microscopic 9-micron core, enabling 100Gbps transmission over distances up to 40 kilometers using laser diodes?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> OM1 Multimode (62.5 &mu;m)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> OM3 Multimode (50 &mu;m)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> OM4 Multimode (50 &mu;m)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> OS2 Singlemode (9 &mu;m)</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> OS2 Singlemode fiber's tiny core eliminates modal dispersion, allowing light signals to travel tens of kilometers without repeaters.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q8</span><div class="mcq-question-text">What is the first step in the standardized CompTIA 7-Step Troubleshooting Methodology?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Identify the problem</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Establish a theory of probable cause</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Document findings</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Implement the solution</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Step 1 requires identifying the problem by gathering symptoms, questioning users, reviewing system logs, and noting recent changes.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q9</span><div class="mcq-question-text">What occurs when a Windows Blue Screen of Death stop code displays `INACCESSIBLE_BOOT_DEVICE` (0x7B)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The monitor cable is unplugged.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The CPU is overheating.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The operating system kernel failed to locate or read the boot partition due to a missing storage controller driver, corrupted BCD, or modified UEFI SATA mode.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The user entered an invalid password.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Stop code 0x7B indicates that during the transition from real-mode bootloader to kernel mode, the storage controller driver failed to initialize the system disk.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q10</span><div class="mcq-question-text">In enterprise backup architecture, what is a "Synthetic Full Backup"?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A backup generated by artificial intelligence.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> An operation where the backup server synthesizes a brand-new Full backup by merging the previous Full backup with subsequent Incremental deltas directly on the backup storage repository, without reading data from the production server.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> A fake backup used to test employee reactions.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Backing up data to social media.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Synthetic full backups eliminate production server I/O and network overhead by rolling incremental deltas into the full backup image directly on the storage target.</div></div>

  <!-- MCQs 11 to 30 -->
  <div class="mcq-card" data-unit="s6" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q11</span><div class="mcq-question-text">Which port does an enterprise domain controller use to listen for secure, encrypted LDAPS queries over SSL/TLS?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> TCP 80</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> TCP 389</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> TCP 443</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> TCP 636</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Standard plaintext LDAP operates on TCP 389; encrypted LDAPS operates on TCP 636.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q12</span><div class="mcq-question-text">What is the function of the Volume Shadow Copy Service (VSS) on Windows Server?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Coordinates between applications (VSS Writers), the OS (VSS Coordinator), and storage (VSS Providers) to capture application-consistent point-in-time volume snapshots while databases are actively running.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Adjusts monitor brightness based on room lighting.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Deletes unused user accounts.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Regulates cooling fan voltages.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> VSS freezes database I/O for seconds, flushes buffers, and creates an instant snapshot, enabling backups of active SQL and Exchange databases without stopping services.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q13</span><div class="mcq-question-text">An enterprise SLA mandates that after an unexpected server room flood, all core web portals must be fully restored and online within 2 hours. What metric does this represent?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Recovery Point Objective (RPO)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Mean Time to Detect (MTTD)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Recovery Time Objective (RTO)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Power Usage Effectiveness (PUE)</div></div><div class="mcq-explanation"><strong>Correct Answer: C (RTO).</strong> Recovery Time Objective (RTO) is the maximum acceptable duration of clock time allowed to restore a business process following a disaster.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q14</span><div class="mcq-question-text">What network diagnostic command in Windows displays all active TCP listening sockets, foreign addresses, connection states, and the process ID (PID) owning each socket?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ping -t</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> netstat -ano</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> ipconfig /all</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> traceroute</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> <code class="code-inline">netstat -ano</code> lists all active connections numerically (-n) with protocol and listening state (-a), showing the owning process PID (-o).</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q15</span><div class="mcq-question-text">What is the fundamental difference between Synchronous and Asynchronous storage replication across disaster recovery sites?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Synchronous replication only runs over Wi-Fi.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Asynchronous replication requires liquid cooling.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Synchronous is free, while Asynchronous requires a license.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Synchronous commits writes to BOTH primary and remote sites before acknowledging the host (zero RPO, constrained by distance/latency &lt;100km); Asynchronous acknowledges primary write immediately and replicates in background (survives unlimited distance, small non-zero RPO).</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Synchronous replication guarantees zero data loss (RPO = 0) but latency restricts distance to &lt;100km. Asynchronous replication operates over thousands of kilometers with a slight recovery delta.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q16</span><div class="mcq-question-text">What is the function of the "Archive Bit" in traditional file systems during backup operations?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A 1-bit file attribute set to 1 whenever a file is created or modified, signaling to backup software that the file needs to be backed up.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Compresses files using ZIP.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Encrypts files with RSA.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Prevents files from being deleted.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Full and Incremental backups clear the archive bit (set to 0). When a user modifies the file, the filesystem sets it back to 1. Differential backups inspect the bit but do not clear it.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q17</span><div class="mcq-question-text">Which Linux tool captures and logs kernel crash dumps following a fatal kernel panic?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> grep</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> top</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> kdump / kexec</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> sed</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> <code class="code-inline">kdump</code> uses <code class="code-inline">kexec</code> to boot a lightweight capture kernel inside reserved RAM without executing BIOS POST, dumping physical memory to <code class="code-inline">/var/crash/</code> for analysis.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q18</span><div class="mcq-question-text">In Windows NIC Teaming, which load balancing mode calculates an outbound hash based on IP addresses and TCP ports to distribute traffic across team members?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Hyper-V Port Mode</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Address Hash Mode</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Static Mode</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Broadcast Mode</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Address Hash calculates a 4-tuple or 2-tuple hash of IP and port numbers to balance parallel TCP streams across NIC team members.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q19</span><div class="mcq-question-text">What diagnostic hardware tool is plugged into a motherboard PCIe slot or diagnostic header to display 2-digit hexadecimal POST codes during boot failure?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Loopback adapter</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Multimeter</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Cable tester</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> POST Card (Power-On Self-Test Diagnostic Card)</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> POST cards monitor port 80h/84h on the bus, displaying hex codes indicating exactly which component (RAM, CPU, PCIe) failed pre-boot initialization.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q20</span><div class="mcq-question-text">What is the consequence of configuring an MTU mismatch where a server NIC has Jumbo Frames (9000 bytes) enabled, but an intermediate switch port is configured with standard 1500 MTU?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Packets larger than 1500 bytes with the "Don't Fragment" (DF) bit set will be silently dropped, causing connections to establish TCP handshakes but stall indefinitely during data transfer ("black hole router").</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The switch will explode.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The server will automatically downclock its CPU.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The server will delete all stored passwords.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> MTU mismatches drop large frames. Small SYN/ACK packets pass, but large storage/web payloads exceed the 1500 limit and drop without ICMP notification, causing infinite timeouts.</div></div>

  <!-- MCQs 21 to 30 -->
  <div class="mcq-card" data-unit="s6" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q21</span><div class="mcq-question-text">What is the purpose of an "Optical Time-Domain Reflectometer" (OTDR) in enterprise datacenter fiber cabling maintenance?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Measures server fan speed.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Formats SAS hard drives.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Injects light pulses down optical fiber strands to measure signal attenuation, splice loss, and identify the exact physical distance to a fiber break.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Scans for computer viruses.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> OTDRs analyze backscattered light along fiber runs, pinpointing micro-bends, bad splices, and fiber cable cuts down to the meter.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q22</span><div class="mcq-question-text">What is the final step in the CompTIA 7-Step Troubleshooting Methodology?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Test the theory</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Document findings, actions, and outcomes</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Identify the problem</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Establish a plan of action</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Step 7 mandates documenting all findings, root causes, actions taken, and final outcomes in the ticketing system to build institutional knowledge.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q23</span><div class="mcq-question-text">What is the function of a "Crash Dump Filter Driver" during a Windows Blue Screen of Death event?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Plays an error sound over speakers.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Emails Microsoft customer support.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Disables the computer's graphics card.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Bypasses standard I/O stacks to write physical RAM memory contents directly into the pagefile on the system disk using dedicated, isolated storage drivers.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> When Windows crashes, standard drivers cannot be trusted. The crash dump subsystem (<code class="code-inline">dump_diskdump.sys</code>) uses a lightweight, self-contained driver to dump RAM directly to disk.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q24</span><div class="mcq-question-text">Which port does an Active Directory Domain Controller use for Global Catalog LDAP queries across the forest?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> TCP 3268</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> TCP 389</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> TCP 88</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> TCP 445</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Port 3268 is used for Global Catalog queries; port 389 is used for local domain LDAP queries.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q25</span><div class="mcq-question-text">What is "Split-Brain" in high-availability server clustering?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A server running two operating systems on two screens.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> When a CPU core splits into two virtual threads.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> A catastrophic condition where cluster nodes lose communication with each other and simultaneously attempt to claim exclusive ownership of shared storage and IP resources, causing data corruption.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> A memory error on dual-channel RAM.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Split-brain occurs when an isolated cluster partition believes its partner is dead and mounts shared volumes concurrently, causing catastrophic disk overwrites.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q26</span><div class="mcq-question-text">In Windows Server NIC Teaming, which load balancing mode is recommended for virtualized Hyper-V hosts to pin specific VM vNICs to specific physical team members?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Round Robin</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Hyper-V Port Mode</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Broadcast</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Priority Only</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Hyper-V Port mode binds each virtual machine's virtual network interface to a dedicated physical NIC in the team, guaranteeing consistent MAC address routing on external switches.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q27</span><div class="mcq-question-text">What diagnostic command on an enterprise Linux server displays kernel ring buffer messages, hardware peripheral detection, and driver error events?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ls</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> pwd</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> ifconfig</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> dmesg -T</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> <code class="code-inline">dmesg -T</code> outputs the kernel log buffer with human-readable timestamps, showing PCIe link negotiations, storage driver events, and memory errors.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q28</span><div class="mcq-question-text">What is the benefit of a Differential backup over an Incremental backup during a full disaster recovery restore?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Restoration requires only two backup sets (the Full backup + the latest Differential backup), making restores much faster and less prone to tape failure.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Differential backups take up zero disk space.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Differential backups can only be read on Sundays.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Differential backups do not require passwords.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Differential backups consolidate all changes since the full backup into a single image, eliminating the need to restore multiple incremental delta tapes.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q29</span><div class="mcq-question-text">What is the function of a "Time-Domain Reflectometer" (TDR) for copper twisted-pair Ethernet cables?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Overclocks the network cable to 100Gbps.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Changes the color of the cable jacket.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Sends electrical pulses down copper pairs and measures reflected energy to pinpoint cable shorts, opens, and the exact distance to a severed wire.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Backs up data over copper.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> TDR instruments measure impedance reflections, accurately identifying split pairs, crimp defects, and the exact footage to a wire break.</div></div>

  <div class="mcq-card" data-unit="s6" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q30</span><div class="mcq-question-text">What Windows PowerShell command captures a complete system configuration report including hotfixes, BIOS version, memory channels, and network adaptors?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Get-Process</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> systeminfo / get-computerinfo</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> clear-host</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> restart-computer</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> <code class="code-inline">Get-ComputerInfo</code> or <code class="code-inline">systeminfo</code> dumps OS build versions, processor architecture, physical memory, hotfix IDs, and network configuration.</div></div>

</article>

<!-- UNIT 6 SUBJECTIVE SHORT CONCEPTUAL Q&A (5M) -->
<article class="doc-page" id="practice-subj-short-s6">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Assessment • Conceptual Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q2</span> Conceptual Review Questions (5 Marks Each)</h2>
    <p class="lead-para">
      Five focused technical problems analyzing NIC teaming modes, disaster recovery site topologies, backup methodologies, RPO/RTO SLA calculations, and BSOD bug checks.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q1: Contrast Switch Independent NIC Teaming with LACP (802.1ax) across switch requirements and fault tolerance.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Switch Independent Teaming:</strong> Requires zero configuration on the physical switches. The server's physical network adapters connect to two completely separate, independent Top-of-Rack (ToR) switches. This provides the highest possible level of hardware redundancy: even if Switch A suffers a complete power outage or supervisor crash, Switch B continues routing traffic seamlessly. Inbound traffic is handled by Active/Standby or Dynamic load distribution.</li>
        <li><strong>LACP (802.1ax / 802.3ad) Teaming:</strong> Requires dynamic protocol coordination with the switch stack. All physical ports must terminate on the same logical switch entity (either a stacked switch, Cisco vPC, or Arista MLAG). LACP exchanges periodic Link Aggregation Control Protocol PDUs (every 1s or 30s) to detect cable faults and balance bidirectional traffic across links. It delivers aggregated bandwidth for multiple concurrent TCP streams, but cannot span independent, unstacked switches.</li>
      </ul>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q2: Differentiate Hot, Warm, and Cold Disaster Recovery sites across equipment readiness, replication, and RTO.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Hot Site:</strong> Fully equipped, fully powered, mirrored hardware running 24/7 in an alternate datacenter. Storage is replicated continuously in real-time (synchronous or asynchronous). Recovery Time Objective (RTO) is near-zero (minutes to an hour). Most expensive disaster recovery model.</li>
        <li><strong>Warm Site:</strong> Infrastructure (HVAC, rack cabinets, power) and server hardware are pre-installed, but servers are not actively running production workloads. Data is restored from periodic delta backups (e.g., daily or weekly). RTO ranges from hours to a couple of days. Balances cost and recovery speed.</li>
        <li><strong>Cold Site:</strong> Physical building space with electrical power, cooling, and network jacks, but ZERO server hardware pre-installed. In a disaster, administrators must procure replacement servers, mount hardware, install operating systems, and restore from off-site backup tapes. RTO ranges from weeks to months. Lowest capital cost.</li>
      </ul>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q3: Contrast Differential vs Incremental backup strategies in terms of backup window duration and restoration speed.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Differential Backup:</strong> Backs up all files modified since the last FULL backup. It does not clear the archive bit. <em>Backup Duration:</em> Grows progressively longer each day as cumulative changes accumulate over the week. <em>Restore Speed:</em> Very fast and simple—requires exactly two backup sets (the original Full backup + the latest Differential backup).</li>
        <li><strong>Incremental Backup:</strong> Backs up only files modified since the last backup of ANY kind (Full or Incremental). It clears the archive bit. <em>Backup Duration:</em> Extremely fast every night, as only that day's small delta is captured. <em>Restore Speed:</em> Slow and fragile—requires restoring the Full backup followed by every single sequential daily incremental tape in exact chronological order. If any single incremental tape is lost or corrupt, the entire restore chain fails from that point forward.</li>
      </ul>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q4: Define Recovery Point Objective (RPO) and Recovery Time Objective (RTO) with real-world enterprise examples.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Recovery Point Objective (RPO):</strong> The maximum acceptable age of files or data that an organization can afford to lose when an unexpected disaster strikes. It determines backup frequency. <em>Example:</em> A stock exchange trading platform requires an RPO &le; 0 seconds (zero data loss permitted, mandating real-time synchronous storage mirroring). Conversely, an internal employee training portal may have an RPO of 24 hours (daily night backups suffice).</li>
        <li><strong>Recovery Time Objective (RTO):</strong> The maximum acceptable duration of clock time permitted to restore systems and resume business operations following an outage. <em>Example:</em> An enterprise hospital emergency room system requires an RTO &le; 15 minutes (mandating automated failover clustering). An archival payroll reporting system may have an RTO of 72 hours without impacting immediate patient care.</li>
      </ul>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q5: Dissect the root cause of the Windows Stop Code `IRQL_NOT_LESS_OR_EQUAL` (0x0000000A).</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> In the Windows kernel architecture, processors execute at discrete Interrupt Request Levels (IRQLs) ranging from 0 (Passive level / user mode) to 31 (High level / hardware interrupts). When CPU execution is elevated to DISPATCH_LEVEL (IRQL 2) or higher, the kernel thread cannot block, yield, or invoke the virtual memory page fault handler.</p>
      <p>The bug check <code class="code-inline">IRQL_NOT_LESS_OR_EQUAL (0x0A)</code> occurs when a kernel routine or device driver executing at an elevated IRQL attempts to access memory marked as pageable (or an invalid null pointer). Because the page fault handler cannot be invoked at that elevated IRQL, the memory subsystem cannot page the data into RAM. To prevent silent kernel memory corruption, the operating system halts execution immediately and generates a Blue Screen of Death.</p>
    </div>
  </div>
</article>

<!-- UNIT 6 SUBJECTIVE LONG SCENARIOS (10M) -->
<article class="doc-page" id="practice-subj-long-s6">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Assessment • Scenario Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q3</span> Architectural &amp; Triage Scenarios (10 Marks Each)</h2>
    <p class="lead-para">
      Enterprise scenarios requiring BSOD memory dump triage, disaster recovery failover execution, and MTU black-hole packet drop troubleshooting.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 1: Triaging Recurrent Enterprise BSOD Crashes with WinDbg Kernel Dump Analysis</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A core virtualization host running Windows Server 2022 experiences random kernel crashes every 48 to 72 hours with the bug check <code class="code-inline">PAGE_FAULT_IN_NONPAGED_AREA (0x50)</code>. Junior technicians have rebooted the server multiple times without identifying the root cause. Detail the complete WinDbg diagnostic workflow to identify the culprit driver.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> WINDBG KERNEL DUMP ANALYSIS WORKFLOW</div>
        <div class="callout-body">
          <ol style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Retrieve Kernel Memory Dump:</strong> Locate the crash dump file at <code class="code-inline">C:\Windows\MEMORY.DMP</code> or <code class="code-inline">C:\Windows\Minidump\*.dmp</code>.</li>
            <li><strong>Configure WinDbg Environment:</strong> Open WinDbg as Administrator. Set the Microsoft Symbol Server path:
              <pre class="code-block"><code class="language-text">.sympath srv*https://msdl.microsoft.com/download/symbols
.reload</code></pre>
            </li>
            <li><strong>Execute Automated Bug Check Analysis:</strong> Issue the command:
              <pre class="code-block"><code class="language-text">!analyze -v</code></pre>
              Inspect the output fields:
              <ul style="margin-left: 1rem;">
                <li><code class="code-inline">BUGCHECK_CODE</code>: 0x50 (PAGE_FAULT_IN_NONPAGED_AREA)</li>
                <li><code class="code-inline">MODULE_NAME</code>: Displays the specific driver binary (e.g. <code class="code-inline">ql2300.sys</code> or <code class="code-inline">e1rexpress.sys</code>).</li>
                <li><code class="code-inline">IMAGE_NAME</code>: Identifies the vendor file path.</li>
                <li><code class="code-inline">STACK_TEXT</code>: Displays the exact function call chain immediately preceding the invalid memory dereference.</li>
              </ul>
            </li>
            <li><strong>Remediation:</strong> If a third-party storage or network driver is identified, download and install the certified, updated driver from the hardware vendor's HCL portal. If the driver is clean, execute comprehensive hardware diagnostic memory tests (e.g. MemTest86 / UEFI Memory Diagnostics) to isolate failing physical ECC RAM modules.</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 2: Executing an Emergency Disaster Recovery Failover from Primary to Secondary Datacenter</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A catastrophic power grid explosion destroys the substation powering Primary Datacenter A. The secondary Hot Site (Datacenter B) holds asynchronous storage replicas with an RPO of 5 minutes. Detail the step-by-step failover execution plan to restore enterprise operations within a 30-minute RTO.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="check-check"></i> DISASTER RECOVERY RUNBOOK EXECUTION</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Phase 1: Quorum &amp; Storage Promotion (Minutes 0–8):</strong> Break asynchronous storage replication mirrors on Datacenter B's storage arrays. Promote replica storage LUNs from read-only to read-write. Mount storage volumes to Datacenter B's virtualization cluster hosts.</li>
            <li><strong>Phase 2: Virtual Machine Boot Sequence (Minutes 8–18):</strong> Boot virtual machines in strict dependency order:
              <ol style="margin-left: 1rem;">
                <li>Active Directory Domain Controllers &amp; DNS Servers (first to enable Kerberos and identity binding).</li>
                <li>Database Clusters (Microsoft SQL Server / Oracle RAC) and verify database integrity.</li>
                <li>Application Servers and Middleware services.</li>
                <li>Front-End Web Servers and Reverse Proxies.</li>
              </ol>
            </li>
            <li><strong>Phase 3: Public Traffic Redirection (Minutes 18–25):</strong> Update external DNS Anycast / Route 53 failover records to point public IP prefixes to Datacenter B's edge routers. Issue BGP route advertisements from Datacenter B's autonomous system (AS).</li>
            <li><strong>Phase 4: Health Verification (Minutes 25–30):</strong> Execute synthetic web transactions verifying end-user checkout and authentication pipelines. Confirm RTO &le; 30 minutes achieved.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 3: Triaging Intermittent File Transfer Freezes Caused by an MTU "Black Hole"</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> After upgrading datacenter switches, an enterprise file server (<code class="code-inline">10.0.1.50</code>) experiences bizarre network behavior: users can establish SSH sessions, ping the server, and browse small folder lists, but attempting to download any file larger than 100KB causes the transfer to freeze indefinitely.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> DIAGNOSTIC ROOT CAUSE &amp; PING SWEEP TRIAGE</div>
        <div class="callout-body">
          <p><strong>1. Root Cause Identification:</strong> This is a classic **PMTU (Path MTU) Black Hole**. The file server's NIC has Jumbo Frames enabled (9000 bytes MTU). Small packets (SSH keystrokes, ICMP pings, SMB directory listings) are smaller than 1500 bytes and traverse the network without issue. However, when large file transfers occur, the server sends 9000-byte frames with the Don't Fragment (DF) bit set in the IP header. An intermediate switch port configured with standard 1500 MTU silently drops the frames because they exceed its buffer, without generating an ICMP "Fragmentation Needed" (Type 3, Code 4) packet back to the sender.</p>
          <p><strong>2. Diagnostic Validation (Ping Sweep with DF Bit):</strong> Execute ping sweeps from the client to identify the exact maximum transmission unit:
            <pre class="code-block"><code class="language-cmd"># Test with DF bit set and 8972 byte payload (8972 + 28 bytes header = 9000)
ping 10.0.1.50 -f -l 8972
# Packet needs to be fragmented but DF set.
# Test standard 1472 byte payload (1472 + 28 bytes header = 1500)
ping 10.0.1.50 -f -l 1472
# Reply from 10.0.1.50: bytes=1472 time=1ms TTL=128</code></pre>
          </p>
          <p><strong>3. Remediation:</strong> Either configure Jumbo Frames (9000 MTU) consistently across EVERY switch port and router along the physical transit path, or reset the server's NIC MTU back to standard 1500 bytes.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 4: Designing an Immutable 3-2-1-1-0 Backup Topology Defeating Insider Ransomware Threats</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A sophisticated ransomware group compromises enterprise Domain Admin credentials. The attackers log into the backup console and attempt to delete all historical backup snapshots before encrypting production databases. Architect a resilient 3-2-1-1-0 backup topology that guarantees complete recovery even with compromised root credentials.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="shield-check"></i> IMMUTABLE BACKUP ARCHITECTURAL DESIGN</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Hardened Linux Repository with Immutability:</strong> Deploy a dedicated, non-domain-joined Linux backup repository using XFS with reflink support. Enable Linux immutable file attributes (<code class="code-inline">chattr +i</code>) orchestrated via single-use non-root credentials. Even if the backup server is compromised, the Linux repository forbids file deletion or modification until the retention timer expires.</li>
            <li><strong>Cloud Object Storage with Compliance-Mode WORM:</strong> Replicate backups to cloud object storage (e.g. AWS S3 / Azure Blob) with <strong>Object Lock enabled in Compliance Mode</strong>. In Compliance Mode, NO ONE—not even the AWS root account or corporate IT directors—can delete the backup objects until the 30-day retention clock lapses.</li>
            <li><strong>Physical Air-Gapped Magnetic Tape:</strong> Write weekly full backups to LTO-9 magnetic tape drives. Eject the tapes and store them inside an off-site, fire-rated physical vault. Because the tapes are physically unpowered and disconnected from all networks, remote ransomware cannot reach or encrypt them.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</article>

<!-- UNIT 6 MASTER ANSWER KEY -->
<article class="doc-page" id="mcq-answer-key-s6">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 06 • Master Verification Key</span>
    <h2 class="section-title"><span class="sec-num">KEY.6</span> Unit 6 Master Answer Key &amp; Technical Verification Matrix</h2>
    <p class="lead-para">
      Complete answer key and architectural validation matrix for Unit 6 practice bank questions 1 through 30.
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
        <tr><td>Q01</td><td><strong>C</strong></td><td>Incremental restore requires Full + all sequential incrementals</td><td>Backup Architecture Standards</td></tr>
        <tr><td>Q02</td><td><strong>B</strong></td><td>!analyze -v parses crash dump in WinDbg</td><td>Windows Kernel Debugging</td></tr>
        <tr><td>Q03</td><td><strong>D</strong></td><td>Hot Site provides near-zero RTO with active replication</td><td>Disaster Recovery Topologies</td></tr>
        <tr><td>Q04</td><td><strong>A</strong></td><td>IEEE 802.1ax / 802.3ad dynamic LACP standard</td><td>IEEE Standards Association</td></tr>
        <tr><td>Q05</td><td><strong>C</strong></td><td>RPO (Recovery Point Objective): Maximum acceptable data loss</td><td>Business Continuity Management</td></tr>
        <tr><td>Q06</td><td><strong>B</strong></td><td>WinRM HTTPS PowerShell remoting on TCP port 5986</td><td>Windows Remote Management</td></tr>
        <tr><td>Q07</td><td><strong>D</strong></td><td>OS2 Singlemode fiber (9 &mu;m) transmits up to 40 km</td><td>TIA-568 Optical Standards</td></tr>
        <tr><td>Q08</td><td><strong>A</strong></td><td>CompTIA Step 1: Identify the problem</td><td>CompTIA Troubleshooting Model</td></tr>
        <tr><td>Q09</td><td><strong>C</strong></td><td>INACCESSIBLE_BOOT_DEVICE (0x7B) storage driver fault</td><td>Windows Bugcheck Architecture</td></tr>
        <tr><td>Q10</td><td><strong>B</strong></td><td>Synthetic Full backup merges deltas on storage target</td><td>Enterprise Backup Systems</td></tr>
        <tr><td>Q11</td><td><strong>D</strong></td><td>LDAPS encrypted directory queries on TCP port 636</td><td>RFC 4513 LDAP Security Spec</td></tr>
        <tr><td>Q12</td><td><strong>A</strong></td><td>VSS captures application-consistent snapshots in real-time</td><td>Volume Shadow Copy Service</td></tr>
        <tr><td>Q13</td><td><strong>C</strong></td><td>RTO (Recovery Time Objective): Maximum acceptable clock downtime</td><td>Disaster Recovery SLAs</td></tr>
        <tr><td>Q14</td><td><strong>B</strong></td><td>netstat -ano displays active sockets, states, and PIDs</td><td>TCP/IP Diagnostic Utilities</td></tr>
        <tr><td>Q15</td><td><strong>D</strong></td><td>Synchronous zero RPO (&lt;100km); Asynchronous long distance</td><td>Storage Replication Modes</td></tr>
        <tr><td>Q16</td><td><strong>A</strong></td><td>Archive bit signals that file has been modified</td><td>Filesystem Metadata Attributes</td></tr>
        <tr><td>Q17</td><td><strong>C</strong></td><td>kdump / kexec captures Linux kernel panic crash dumps</td><td>Linux Kernel Crash Diagnostics</td></tr>
        <tr><td>Q18</td><td><strong>B</strong></td><td>Address Hash distributes traffic using IP/port hash</td><td>Windows Server NIC Teaming</td></tr>
        <tr><td>Q19</td><td><strong>D</strong></td><td>POST Card displays hex codes for pre-boot hardware errors</td><td>Server Hardware Diagnostics</td></tr>
        <tr><td>Q20</td><td><strong>A</strong></td><td>MTU mismatch drops large DF frames (black hole router)</td><td>RFC 1191 Path MTU Discovery</td></tr>
        <tr><td>Q21</td><td><strong>C</strong></td><td>OTDR measures fiber signal loss and distance to breaks</td><td>Optical Fiber Test Standards</td></tr>
        <tr><td>Q22</td><td><strong>B</strong></td><td>CompTIA Step 7: Document findings, actions, and outcomes</td><td>CompTIA Diagnostic Framework</td></tr>
        <tr><td>Q23</td><td><strong>D</strong></td><td>Crash dump filter driver dumps RAM directly to pagefile</td><td>Windows Kernel Dump Architecture</td></tr>
        <tr><td>Q24</td><td><strong>A</strong></td><td>Global Catalog LDAP queries on TCP port 3268</td><td>Active Directory Directory Store</td></tr>
        <tr><td>Q25</td><td><strong>C</strong></td><td>Split-brain occurs when isolated nodes claim shared disks</td><td>High Availability Clustering</td></tr>
        <tr><td>Q26</td><td><strong>B</strong></td><td>Hyper-V Port mode pins VM vNICs to physical NIC team</td><td>Hyper-V Network Virtualization</td></tr>
        <tr><td>Q27</td><td><strong>D</strong></td><td>dmesg -T displays kernel ring buffer with timestamps</td><td>Linux Kernel Diagnostic Tools</td></tr>
        <tr><td>Q28</td><td><strong>A</strong></td><td>Differential restore requires only Full + latest Differential</td><td>Backup Restoration Performance</td></tr>
        <tr><td>Q29</td><td><strong>C</strong></td><td>TDR measures copper reflections to locate wire faults</td><td>Copper Cabling Test Standards</td></tr>
        <tr><td>Q30</td><td><strong>B</strong></td><td>Get-ComputerInfo dumps comprehensive system report</td><td>PowerShell Hardware Profiling</td></tr>
      </tbody>
    </table>
  </div>
</article>
"""
