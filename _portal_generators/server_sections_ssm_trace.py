# -*- coding: utf-8 -*-
"""
Server Administration Portal - End-to-End Architectural Deep Traces
SSM Engineering Standard Gold Standard Architecture
"""

SERVER_TRACE_HTML = r"""
<!-- ===================================================================
     SPECIAL DEEP DIVE: END-TO-END SILICON & PROTOCOL ARCHITECTURAL TRACES
     =================================================================== -->
<article class="doc-page" id="server-trace-packet">
  <header class="doc-page-header">
    <span class="page-header-meta">Architectural Masterclass • Deep Trace • Subsystem Lifecycle</span>
    <h2 class="section-title"><span class="sec-num">TR.1</span> Silicon, Register &amp; Wire Trace: Active Directory Kerberos Authentication &amp; RAID 5 Parity Rebuild</h2>
    <p class="lead-para">
      Enterprise server administration requires tracking operations from the physical wire and disk platters up to operating system kernel memory structures. This masterclass provides two end-to-end execution traces: the complete cryptographic packet flow of an enterprise Kerberos authentication request, and the sub-millisecond hardware lifecycle of a degraded RAID 5 disk rebuild.
    </p>
  </header>

  <!-- TRACE 1: KERBEROS AUTHENTICATION FLOW -->
  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">Trace A: Anatomy of an Enterprise Kerberos v5 Authentication Sequence</h3>
  <p>
    When an employee logs into workstation <code class="code-inline">WS104</code> using username <code class="code-inline">alice@corp.contoso.com</code> and accesses a restricted network share <code class="code-inline">\\fs01.corp.contoso.com\finance</code>, the following 6-stage cryptographic handshake occurs over the network:
  </p>

  <div class="diagram-container">
    <div style="font-family: var(--font-mono); font-size: 12px; line-height: 1.6; color: var(--text-muted);">
      <div style="color: var(--primary); font-weight: bold; margin-bottom: 0.5rem;">[CLIENT: WS104 • Alice]</div>
      &nbsp;&nbsp;│ (1) AS-REQ: Pre-auth timestamp encrypted with Alice's password hash ──► KDC (UDP 88)<br>
      &nbsp;&nbsp;│ (2) AS-REP: Returns TGT (encrypted with krbtgt key) + Logon Session Key ◄── KDC<br>
      &nbsp;&nbsp;│<br>
      &nbsp;&nbsp;│ (3) TGS-REQ: Sends TGT + Authenticator + SPN "cifs/fs01.corp.contoso.com" ──► KDC (UDP 88)<br>
      &nbsp;&nbsp;│ (4) TGS-REP: Returns Service Ticket (encrypted with FS01's computer key) ◄── KDC<br>
      &nbsp;&nbsp;▼<br>
      <div style="color: #60a5fa; font-weight: bold; margin-bottom: 0.5rem;">[TARGET SERVER: fs01.corp.contoso.com • SMB Port 445]</div>
      &nbsp;&nbsp;│ (5) AP-REQ: Client delivers Service Ticket + Client Authenticator token ──► FS01<br>
      &nbsp;&nbsp;│ (6) Target server kernel decrypts Service Ticket, extracts Privilege Attribute Certificate (PAC)<br>
      &nbsp;&nbsp;│ (7) Local Security Authority (LSA) checks SIDs against NTFS DACL on C:\Shares\Finance<br>
      &nbsp;&nbsp;└─► ACCESS GRANTED! SMB session established over TCP 445 with AES-256 session encryption.
    </div>
  </div>

  <div class="table-container" style="margin-top: 1.5rem;">
    <table>
      <thead>
        <tr>
          <th>Step #</th>
          <th>Protocol Message</th>
          <th>Cryptographic Key Utilized</th>
          <th>Payload Data &amp; Security Validation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Step 1</strong></td>
          <td><code class="code-inline">KRB_AS_REQ</code></td>
          <td>Derived from user password via PBKDF2 (AES-256)</td>
          <td>Client encrypts current microsecond timestamp; prevents offline dictionary attacks without knowledge of password.</td>
        </tr>
        <tr>
          <td><strong>Step 2</strong></td>
          <td><code class="code-inline">KRB_AS_REP</code></td>
          <td>Encrypted with Domain Controller's <code class="code-inline">krbtgt</code> secret key</td>
          <td>Delivers Ticket Granting Ticket (TGT) and Logon Session Key. Client cannot alter TGT because it cannot decrypt <code class="code-inline">krbtgt</code> key.</td>
        </tr>
        <tr>
          <td><strong>Step 3</strong></td>
          <td><code class="code-inline">KRB_TGS_REQ</code></td>
          <td>Logon Session Key</td>
          <td>Client sends TGT along with Authenticator token and target Service Principal Name (<code class="code-inline">cifs/fs01</code>).</td>
        </tr>
        <tr>
          <td><strong>Step 4</strong></td>
          <td><code class="code-inline">KRB_TGS_REP</code></td>
          <td>Encrypted with Target Server's AD account password hash</td>
          <td>KDC generates Service Ticket (ST) containing user SID and group SIDs signed in the Privilege Attribute Certificate (PAC).</td>
        </tr>
        <tr>
          <td><strong>Step 5</strong></td>
          <td><code class="code-inline">KRB_AP_REQ</code></td>
          <td>Service Session Key</td>
          <td>Client presents Service Ticket to target server over SMB (TCP 445). Server decrypts ticket with its own computer account password.</td>
        </tr>
        <tr>
          <td><strong>Step 6</strong></td>
          <td><code class="code-inline">PAC Evaluation</code></td>
          <td>KDC Signature in PAC</td>
          <td>Target server extracts SIDs, generates Windows Access Token, and compares against NTFS Discretionary Access Control Lists (DACLs).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- TRACE 2: RAID 5 PARITY REBUILD -->
  <h3 style="margin-top: 2.5rem; color: var(--text-normal); font-size: 18px;">Trace B: Microsecond Lifecycle of a Degraded RAID 5 Disk Failure &amp; Online Rebuild</h3>
  <p>
    When hard disk drive 3 in a 4-disk hardware RAID 5 array encounters a catastrophic spindle motor seizure while supporting active enterprise SQL transactions:
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Phase</th>
          <th>Hardware Subsystem</th>
          <th>Physical / Logical Action</th>
          <th>Latency / Duration</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Failure Detection</strong></td>
          <td>SAS HBA Controller &amp; Expander</td>
          <td>Drive 3 fails to respond to SCSI command within 7,000 ms. SAS backplane senses link drop; controller sets drive status to <code class="code-inline">FAILED</code>.</td>
          <td>7.0 seconds</td>
        </tr>
        <tr>
          <td><strong>2. Array Degraded State</strong></td>
          <td>RAID-on-Chip (ROC) Engine</td>
          <td>Array transitions to <strong>Degraded Mode</strong>. Operating system experiences zero downtime! Incoming reads for Drive 3 are synthesized in real-time via XOR math on surviving drives: \(D_3 = D_1 \oplus D_2 \oplus P\).</td>
          <td>Instantaneous (&lt;5 &mu;s per I/O)</td>
        </tr>
        <tr>
          <td><strong>3. Hot Spare Activation</strong></td>
          <td>Enclosure Backplane</td>
          <td>Controller automatically allocates pre-inserted online Hot Spare drive (Drive 4) and initiates background rebuild process.</td>
          <td>&lt; 500 ms</td>
        </tr>
        <tr>
          <td><strong>4. Sequential Stripe Traversal</strong></td>
          <td>ROC Hardware XOR ASIC</td>
          <td>Controller reads sequential 64KB stripe chunks from surviving Disks 1, 2, and Parity. XOR ASIC computes missing blocks and writes to Hot Spare at ~250 MB/s.</td>
          <td>4 to 8 hours (for 4TB drives)</td>
        </tr>
        <tr>
          <td><strong>5. Array State Normalization</strong></td>
          <td>RAID Firmware Engine</td>
          <td>Final stripe parity verified. Enclosure drive LED changes from blinking amber to solid green. Array state transitions from <code class="code-inline">REBUILDING</code> to <code class="code-inline">OPTIMAL</code>.</td>
          <td>Full fault tolerance restored!</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>
"""
