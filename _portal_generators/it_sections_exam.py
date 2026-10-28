# -*- coding: utf-8 -*-
"""
Unit 8: Master Comprehensive Examination Bank
Formatted in Engineering Standard .doc-page style with 10-mark questions, 5-mark questions, and full course outcome matrix.
"""

IT_EXAM_HTML = """
<!-- ==========================================================================
     UNIT 08: MASTER COMPREHENSIVE EXAMINATION BANK
     ========================================================================== -->

<article class="doc-page" id="it-exam">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 08 • Final Assessment Bank</span>
    <span class="meta-tag">CO1&ndash;CO5 Mapped • 100 Marks Structure</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">47.</span> Master Comprehensive Examination Bank (CO1&ndash;CO5 Mapped)
  </h2>

  <p class="lead-para">
    Curated repository of university end-semester examination questions categorized by Bloom's Taxonomy cognitive domains and Course Outcomes (CO1 to CO5).
  </p>

  <!-- Part I: 10-Mark Analytical Problems -->
  <h3 style="font-size:1.25rem; font-weight:700; margin:2rem 0 1rem; color:var(--text-main); display:flex; align-items:center; gap:0.5rem;">
    <i data-lucide="award" style="color:var(--primary);"></i>
    Part I • Long Answer Analytical &amp; Design Problems (10 Marks Each)
  </h3>

  <div class="subj-grid">
    <!-- Exam Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO1 • 10M</span> Comprehensive Motherboard Engineering: Analyze Form Factors, PCIe 5.0 Bus Signaling, and Memory Daisy-Chain Trace Topology</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Question Statement:</strong> An enterprise hardware vendor is designing a dual-GPU AI workstation. (a) Contrast ATX, Extended ATX (E-ATX), and Micro-ATX form factors regarding physical standoff patterns, board area, and expansion slot capacity. (b) Explain how PCIe 5.0 achieves 32 GT/s per lane using 128b/130b line encoding compared to PCIe 2.0's 8b/10b encoding. (c) Provide a detailed schematic explanation of Daisy-Chain vs T-Topology memory trace routing on four-DIMM motherboards, justifying why modules must be installed in slots A2 and B2 first.</p>
        <p><strong>Evaluation Criteria &amp; Model Response:</strong></p>
        <ul>
          <li><strong>Part (a) Form Factors (3 Marks):</strong> Detailed table with standard dimensions (ATX: 12&times;9.6 in, 9-10 standoffs, 7 slots; E-ATX: 12&times;13 in, 12 standoffs, 8 slots; mATX: 9.6&times;9.6 in, 8 standoffs, 4 slots). Notes on chassis grounding and short-circuit hazards of missing standoffs.</li>
          <li><strong>Part (b) PCIe 5.0 Line Encoding (3 Marks):</strong> 128b/130b prepends 2 framing bits to 128 data bits (1.53% overhead). At 32 GT/s, bandwidth per lane is \(32 \times (128/130) / 8 \approx 3.94\text{ GB/s}\). PCIe 2.0 used 8b/10b with 20% overhead (5 GT/s &rarr; 500 MB/s).</li>
          <li><strong>Part (c) Daisy-Chain Routing (4 Marks):</strong> Traces route from CPU to Slot 1 and continue to Slot 2. Populating Slot 1 while leaving Slot 2 empty leaves an open copper stub that reflects RF signals, corrupting memory packets at DDR5 frequencies &gt;4800 MT/s. Populating Slot 2 (A2/B2) terminates the transmission line cleanly.</li>
        </ul>
      </div>
    </div>

    <!-- Exam Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO2 • 10M</span> Enterprise Subnetting &amp; Spanning Tree Protocol: Design a Multi-VLAN Topology with RSTP Convergence</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Question Statement:</strong> Given the allocated classless private block `172.16.0.0/20`: (a) Subnet this block using VLSM to support four departmental VLANs: Engineering (500 hosts), Sales (250 hosts), Management (100 hosts), and DMZ (50 hosts). (b) Explain the root cause of Layer 2 broadcast storms in redundant switched meshes without STP. (c) Detail the RSTP (IEEE 802.1w) port states (Discarding, Learning, Forwarding) and explain how the Proposal/Agreement handshake achieves sub-second convergence.</p>
        <p><strong>Model Breakdown:</strong></p>
        <ul>
          <li><strong>Part (a) Subnetting Math (4 Marks):</strong>
            <br>&bull; Engineering (500 hosts): Needs 9 host bits (\(2^9-2 = 510\)) &rarr; Prefix: <strong>/23</strong> (`172.16.0.0/23`, Mask `255.255.254.0`, Range `.0.1` to `.1.254`, Broadcast `.1.255`).
            <br>&bull; Sales (250 hosts): Needs 8 host bits (\(2^8-2 = 254\)) &rarr; Prefix: <strong>/24</strong> (`172.16.2.0/24`, Mask `255.255.255.0`, Range `.2.1` to `.2.254`, Broadcast `.2.255`).
            <br>&bull; Management (100 hosts): Needs 7 host bits (\(2^7-2 = 126\)) &rarr; Prefix: <strong>/25</strong> (`172.16.3.0/25`, Mask `255.255.255.128`, Range `.3.1` to `.3.126`, Broadcast `.3.127`).
            <br>&bull; DMZ (50 hosts): Needs 6 host bits (\(2^6-2 = 62\)) &rarr; Prefix: <strong>/26</strong> (`172.16.3.128/26`, Mask `255.255.255.192`, Range `.3.129` to `.3.190`, Broadcast `.3.191`).
          </li>
          <li><strong>Part (b) Broadcast Storms (3 Marks):</strong> Ethernet lacks a TTL field; broadcast frames loop perpetually, saturating switch ASICs and causing CAM table thrashing within seconds.</li>
          <li><strong>Part (c) RSTP Proposal/Agreement (3 Marks):</strong> Replaces 50-second timer-based 802.1D convergence with rapid point-to-point explicit handshakes on full-duplex links, syncing port states across root ports and designated ports in under 1 second.</li>
        </ul>
      </div>
    </div>

    <!-- Exam Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO3 • 10M</span> Windows NT Executive Internals: The End-to-End Silicon Execution Path of a Process Launch</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Question Statement:</strong> Detail the step-by-step internal execution narrative when a user double-clicks `chrome.exe` on Windows 11. Trace the execution through: Shell Execution, Windows Subsystem (`csrss.exe`), Windows Executive Process Manager (`NtCreateUserProcess`), Object Manager, Memory Manager (VAD allocation & Page Faults), Security Reference Monitor (Primary Token assignment), and the Microkernel Scheduler (Thread Dispatch at IRQL 0).</p>
      </div>
    </div>

    <!-- Exam Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO4 • 10M</span> Linux Operating System Security: PAM Architecture, Inode Allocation, and Bash Hardening</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Question Statement:</strong> (a) Describe the architecture of Pluggable Authentication Modules (PAM) on enterprise Linux, explaining the four management groups (`auth`, `account`, `password`, `session`) and control flags (`required`, `requisite`, `sufficient`, `optional`). (b) Explain how the ext4 filesystem represents files using Inodes, detailing direct block pointers, indirect pointers, and directory file mapping. (c) Write a secure Bash administration script that audits user accounts with UID &ge; 1000, checks for empty password fields in `/etc/shadow`, and reports accounts with active SUID binaries.</p>
      </div>
    </div>
  </div>

  <!-- Part II: 5-Mark High-Yield Questions -->
  <h3 style="font-size:1.25rem; font-weight:700; margin:2.5rem 0 1rem; color:var(--text-main); display:flex; align-items:center; gap:0.5rem;">
    <i data-lucide="file-text" style="color:var(--primary);"></i>
    Part II • High-Yield Short Conceptual Questions (5 Marks Each)
  </h3>

  <div class="subj-grid">
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO1 • 5M</span> State the 6 Stages of the Electrophotographic Laser Printing Cycle in strict chronological order and explain the physical role of the heated fuser roller.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>6 Stages:</strong> Cleaning &rarr; Conditioning &rarr; Writing &rarr; Developing &rarr; Transferring &rarr; Fusing.</p>
        <p><strong>Role of Fuser Roller:</strong> Heated to 180&deg;C-200&deg;C using an internal halogen lamp. As paper passes between the heat roller and pressure roller, the plastic polymer resin in toner melts and is pressed permanently into the cellulose fibers of the paper. Without fusing, toner wipes off as loose powder.</p>
      </div>
    </div>

    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO2 • 5M</span> Differentiate Cat 6 and Cat 6a twisted pair cabling regarding maximum frequency, 10 Gbps certified distance, and alien crosstalk mitigation.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Cat 6:</strong> Rated up to 250 MHz. Supports 10 Gbps (10GBASE-T) up to <strong>55 meters</strong> only (or 37m under heavy alien crosstalk). Uses an internal plastic spline to separate pairs.</p>
        <p><strong>Cat 6a (Augmented):</strong> Rated up to 500 MHz. Supports full 10 Gbps up to the complete standard <strong>100-meter channel distance</strong>. Uses thicker outer insulation and individual pair shielding (STP/FTP) to completely eliminate alien crosstalk (ANEXT) between adjacent bundled cables.</p>
      </div>
    </div>

    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO3 • 5M</span> Contrast Kerberos v5 and NTLMv2 authentication protocols: ticket grant sequence vs challenge-response handshake.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Kerberos v5:</strong> Third-party ticket-based mutual authentication. The client authenticates once with the KDC Authentication Service (AS-REQ &rarr; AS-REP) to receive a Ticket Granting Ticket (TGT). For service access, it presents the TGT to the Ticket Granting Service (TGS-REQ &rarr; TGS-REP) to obtain a Service Ticket. Uses symmetric AES-256 session keys; credentials never traverse the wire.</p>
        <p><strong>NTLMv2:</strong> Point-to-point 3-way challenge-response. Server transmits an 8-byte random challenge; client encrypts challenge with its NTLM password hash; server forwards response to Domain Controller for verification. Lacks mutual authentication (client cannot verify server identity) and is vulnerable to pass-the-hash and relay attacks.</p>
      </div>
    </div>

    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">CO4 • 5M</span> Explain how WPA3 Simultaneous Authentication of Equals (SAE) prevents offline dictionary attacks compared to WPA2-PSK.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>In WPA2-PSK, an attacker who captures the 4-Way EAPOL Handshake can run dictionary passphrases through `PBKDF2(Passphrase, SSID)` offline at billions of attempts per second using GPUs.</p>
        <p>In WPA3-Personal, SAE uses the Dragonfly zero-knowledge handshake based on elliptic curve cryptography. Both devices establish a shared secret dynamically without transmitting password-derived hashes. An attacker cannot verify whether a password guess is correct without actively engaging in an interactive online exchange with the access point, which enforces rate-limiting to prevent brute force.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Course Evaluation Bank Complete</span>
    <span>Unit 08 • Final Assessment Bank</span>
  </div>
</article>
"""
