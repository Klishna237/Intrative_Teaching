# -*- coding: utf-8 -*-
"""
Server Administration Portal - Unit 5: Server Security & Hardening
SSM Engineering Standard Gold Standard Architecture
"""

SERVER_UNIT5_HTML = r"""
<!-- ===================================================================
     UNIT 05: SERVER SECURITY & HARDENING
     =================================================================== -->

<!-- ARTICLE 21: SERVER OS HARDENING & CIS BENCHMARKS -->
<article class="doc-page" id="s5-hardening">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Server Security • Article 21</span>
    <h2 class="section-title"><span class="sec-num">21</span> Enterprise Operating System Hardening &amp; CIS Benchmarks</h2>
    <p class="lead-para">
      Default out-of-the-box server operating system configurations prioritize ease-of-use and legacy backwards compatibility, leaving exposed network services, weak cipher suites, and default administrative permissions. Enterprise server hardening systematically reduces the attack surface according to Center for Internet Security (CIS) Level 1 and Level 2 benchmarks.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Core Operating System Hardening Pillars</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Hardening Domain</th>
          <th>Windows Server 2022 Implementation</th>
          <th>Enterprise Linux (RHEL / Ubuntu) Implementation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Service Minimization</strong></td>
          <td>Disable Print Spooler on non-print servers, Xbox Live Auth, Computer Browser, Remote Registry</td>
          <td>Disable <code class="code-inline">cups</code>, <code class="code-inline">rpcbind</code>, <code class="code-inline">avahi-daemon</code>, <code class="code-inline">telnet-server</code> via <code class="code-inline">systemctl disable --now</code></td>
        </tr>
        <tr>
          <td><strong>Kernel Memory Protection</strong></td>
          <td>Enable Windows Defender Credential Guard (Virtualization-Based Security VBS isolates LSASS.exe in Ring -1)</td>
          <td>Enable SELinux in <code class="code-inline">Enforcing</code> mode, Kernel Page Table Isolation (KPTI), disable core dumps in <code class="code-inline">/etc/security/limits.conf</code></td>
        </tr>
        <tr>
          <td><strong>Access Control &amp; Elevation</strong></td>
          <td>Enforce User Account Control (UAC) at maximum level; rename local Administrator account; disable Guest</td>
          <td>Restrict <code class="code-inline">/etc/sudoers</code> via <code class="code-inline">visudo</code>; configure Pluggable Authentication Modules (PAM) with <code class="code-inline">pam_pwquality</code> and <code class="code-inline">pam_faillock</code></td>
        </tr>
        <tr>
          <td><strong>Cryptographic Protocols</strong></td>
          <td>Disable SSL 2.0/3.0, TLS 1.0, TLS 1.1; disable 3DES and RC4; enforce TLS 1.2 and TLS 1.3 exclusively via registry</td>
          <td>Configure system-wide crypto policies: <code class="code-inline">update-crypto-policies --set FUTURE</code> (disables SHA-1, RSA &lt; 3072-bit)</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 22: ENTERPRISE AUTHENTICATION & PKI -->
<article class="doc-page" id="s5-auth-pki">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Server Security • Article 22</span>
    <h2 class="section-title"><span class="sec-num">22</span> Authentication Protocols &amp; Public Key Infrastructure (PKI)</h2>
    <p class="lead-para">
      Enterprise identity relies on cryptographic protocols to authenticate human operators and service daemons. Kerberos v5 provides ticket-granting security across Active Directory domains, while X.509 Public Key Infrastructure (PKI) underpins SSL/TLS server certificates, smart cards, and code signing.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. The 6-Stage Kerberos v5 Authentication Ticket Pipeline</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Stage</th>
          <th>Protocol Message</th>
          <th>Client &harr; KDC Interaction</th>
          <th>Payload &amp; Security Token</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Authentication Request</strong></td>
          <td><code class="code-inline">AS-REQ</code></td>
          <td>Client sends timestamp encrypted with user password hash to Kerberos Key Distribution Center (UDP 88).</td>
          <td>Pre-authentication timestamp (verifies password without sending it!)</td>
        </tr>
        <tr>
          <td><strong>2. Authentication Reply</strong></td>
          <td><code class="code-inline">AS-REP</code></td>
          <td>KDC decrypts timestamp. If valid, generates and returns Ticket Granting Ticket (TGT) and Session Key.</td>
          <td>TGT (encrypted with <code class="code-inline">krbtgt</code> account master secret key)</td>
        </tr>
        <tr>
          <td><strong>3. Ticket Granting Request</strong></td>
          <td><code class="code-inline">TGS-REQ</code></td>
          <td>Client presents TGT and requests access to a target service (e.g. <code class="code-inline">cifs/fileserver.domain.com</code>).</td>
          <td>TGT + Authenticator token + Service Principal Name (SPN)</td>
        </tr>
        <tr>
          <td><strong>4. Ticket Granting Reply</strong></td>
          <td><code class="code-inline">TGS-REP</code></td>
          <td>KDC verifies TGT, generates Service Ticket (ST), and returns it to the client.</td>
          <td>Service Ticket (encrypted with target server's secret account key)</td>
        </tr>
        <tr>
          <td><strong>5. Application Request</strong></td>
          <td><code class="code-inline">AP-REQ</code></td>
          <td>Client sends Service Ticket to target server daemon (e.g. File Server SMB port 445).</td>
          <td>Service Ticket + Mutual Auth request</td>
        </tr>
        <tr>
          <td><strong>6. Privilege Attribute Validation</strong></td>
          <td><code class="code-inline">PAC Check</code></td>
          <td>Target server decrypts Service Ticket, extracts user Security Identifiers (SIDs) from Privilege Attribute Certificate (PAC).</td>
          <td>User granted access with specific security token permissions!</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 23: FIREWALLS, DMZ & IPSEC -->
<article class="doc-page" id="s5-network-security">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Server Security • Article 23</span>
    <h2 class="section-title"><span class="sec-num">23</span> Host-Based Firewalls, Security Zones &amp; IPsec Architecture</h2>
    <p class="lead-para">
      Enterprise servers must defend themselves against lateral movement even if network perimeter firewalls are breached. Host-based stateful firewalls (FirewallD/nftables, Windows Defender Firewall) and IPsec cryptographic tunnels enforce micro-segmentation across security zones.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. IPsec Modes: Transport vs Tunnel</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Attribute</th>
          <th>IPsec Transport Mode</th>
          <th>IPsec Tunnel Mode</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Encapsulation Scope</strong></td>
          <td>Encrypts ONLY the L4 payload (TCP/UDP); preserves original IP header</td>
          <td>Encrypts the ENTIRE original IP packet (header + payload); appends new outer IP header</td>
        </tr>
        <tr>
          <td><strong>Endpoints</strong></td>
          <td>End-to-End host-to-host communication (Server &harr; Server within internal datacenter)</td>
          <td>Gateway-to-Gateway (Site-to-Site VPN) or Host-to-Gateway (Remote Access VPN)</td>
        </tr>
        <tr>
          <td><strong>Packet Header Overhead</strong></td>
          <td>Lower overhead (~20–40 bytes)</td>
          <td>Higher overhead (~40–60 bytes due to new outer IP header)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="shield"></i> DEMILITARIZED ZONE (DMZ) DUAL-FIREWALL ARCHITECTURE</div>
    <div class="callout-body">
      Enterprise datacenters segregate untrusted traffic through a physical or logical DMZ:
      <ul style="margin-left: 1.2rem; margin-top: 0.5rem; line-height: 1.8;">
        <li><strong>Outer Perimeter Firewall:</strong> Terminates public Internet traffic, permitting only port 80/443 directly to DMZ reverse proxies.</li>
        <li><strong>DMZ Tier:</strong> Houses public-facing NGINX/IIS web reverse proxies and mail relays. Servers in the DMZ must **never** be joined to the internal Active Directory production domain!</li>
        <li><strong>Inner Core Firewall:</strong> Allows strictly restricted, inspected traffic (e.g., port 1433 to SQL Server, port 389 to LDAP) originating from DMZ reverse proxies into the internal corporate network. Inbound connections originating from the DMZ to the internal domain are explicitly blocked by default.</li>
      </ul>
    </div>
  </div>
</article>

<!-- ARTICLE 24: STORAGE ENCRYPTION & DATA SANITIZATION -->
<article class="doc-page" id="s5-storage-encryption">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Server Security • Article 24</span>
    <h2 class="section-title"><span class="sec-num">24</span> Enterprise Storage Encryption &amp; Media Sanitization Standards</h2>
    <p class="lead-para">
      Data at rest must be protected against physical drive theft, decommission compromises, and supply-chain tampering. Hardware-based Full Disk Encryption (BitLocker with TPM 2.0, Linux LUKS2) and certified sanitization standards (NIST SP 800-88, DoD 5220.22-M) safeguard data across the entire hardware lifecycle.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Certified Media Sanitization Standards</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Standard</th>
          <th>Sanitization Level</th>
          <th>Methodology &amp; Passes</th>
          <th>Target Media &amp; Application</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>DoD 5220.22-M (Legacy Military)</strong></td>
          <td>Overwrite Clearing</td>
          <td>3-Pass overwrite: Pass 1 writes binary zeros, Pass 2 writes binary ones, Pass 3 writes pseudo-random characters with read verification.</td>
          <td>Magnetic spinning hard disk drives (HDDs); completely ineffective on modern SSD wear-leveled flash!</td>
        </tr>
        <tr>
          <td><strong>NIST SP 800-88: Clear</strong></td>
          <td>Logical Overwrite</td>
          <td>Single-pass logical overwrite with zeros using standard user-accessible read/write commands.</td>
          <td>Re-deploying drives internally within the same security clearance zone.</td>
        </tr>
        <tr>
          <td><strong>NIST SP 800-88: Purge</strong></td>
          <td>Cryptographic Erase / Secure Erase</td>
          <td>Executes hardware ATA/NVMe **Cryptographic Erase (CE)** (purging the internal AES-256 Media Encryption Key in milliseconds, making all ciphertext forever irrecoverable) or low-level block erase.</td>
          <td>Enterprise SSDs and Self-Encrypting Drives (SEDs) being decommissioned or returned to vendors under warranty.</td>
        </tr>
        <tr>
          <td><strong>NIST SP 800-88: Destroy</strong></td>
          <td>Physical Destruction</td>
          <td>Physical degaussing (for magnetic platters), shredding (particle size &le; 2mm for flash memory chips), or thermal incineration.</td>
          <td>Top-secret data drives leaving controlled physical security perimeters.</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 25: AUDIT LOGGING & COMPLIANCE -->
<article class="doc-page" id="s5-audit-compliance">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Server Security • Article 25</span>
    <h2 class="section-title"><span class="sec-num">25</span> Security Audit Logging, SIEM Integration &amp; Event Analysis</h2>
    <p class="lead-para">
      Non-repudiation and forensic incident response depend on unalterable audit trails. Security Information and Event Management (SIEM) systems ingest high-fidelity Windows Security Event Logs and Linux auditd telemetry to detect adversary compromise in real time.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Critical Windows Security Event IDs</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Event ID</th>
          <th>Event Description</th>
          <th>Security Significance &amp; Threat Indicator</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>4624</strong></td>
          <td>An account was successfully logged on</td>
          <td>Inspect Logon Type (Type 2 = Interactive console; Type 3 = Network share; Type 10 = Remote Desktop RDP; Type 4 = Batch service).</td>
        </tr>
        <tr>
          <td><strong>4625</strong></td>
          <td>An account failed to log on</td>
          <td>High volume indicates brute-force or password spraying attack; inspect sub-status codes (e.g. <code class="code-inline">0xC000006A</code> = bad password).</td>
        </tr>
        <tr>
          <td><strong>4720</strong></td>
          <td>A user account was created</td>
          <td>Privileged user creation; unauthorized accounts indicate persistence mechanisms.</td>
        </tr>
        <tr>
          <td><strong>4728 / 4732</strong></td>
          <td>A member was added to a security group</td>
          <td>Alert immediately if users are added to <code class="code-inline">Domain Admins</code>, <code class="code-inline">Enterprise Admins</code>, or local <code class="code-inline">Administrators</code>.</td>
        </tr>
        <tr>
          <td><strong>4672</strong></td>
          <td>Special privileges assigned to new logon</td>
          <td>Administrative user elevation; indicates logon with <code class="code-inline">SeDebugPrivilege</code> or <code class="code-inline">SeTakeOwnershipPrivilege</code>.</td>
        </tr>
        <tr>
          <td><strong>1102</strong></td>
          <td>The audit log was cleared</td>
          <td><strong>CRITICAL ALERT!</strong> Adversaries clear security logs to eliminate forensic footprints before lateral movement.</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- UNIT 5 PRACTICE BANK: 30 MCQS -->
<article class="doc-page" id="practice-mcq-s5">
  <div class="page-header-meta">
    <span class="meta-tag">Server Administration • Unit 05</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreS5">Score: 0 / 30</span>
  </div>
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Assessment • Practice Bank</span>
    <h2 class="section-title"><span class="sec-num">Q1</span> Unit 5 Practice Bank: 30 Interactive Examination MCQs</h2>
    <p class="lead-para">
      Comprehensive assessment questions matching CompTIA Server+, CompTIA Security+, and Microsoft Cybersecurity Architect standards.
    </p>
  </header>

  <div class="callout callout-deep" style="margin-bottom: 2rem;">
    <div class="callout-label"><i data-lucide="award"></i> REAL-TIME SCORE ENGINE</div>
    <div class="callout-body">
      Select your answer for each question. Instant feedback will highlight correct answers in green and explanations will appear automatically.
    </div>
  </div>

  <!-- MCQ 1 -->
  <div class="mcq-card" data-unit="s5" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q1</span>
      <div class="mcq-question-text">Which Windows security feature utilizes Virtualization-Based Security (VBS) to isolate the Local Security Authority Subsystem Service (LSASS) inside a secure virtual container, preventing tools like Mimikatz from dumping plaintext passwords and Kerberos tickets from memory?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Windows Defender SmartScreen</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Windows Defender Credential Guard</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> BitLocker Network Unlock</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Encrypting File System (EFS)</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B (Windows Defender Credential Guard).</strong> Credential Guard uses Hyper-V virtualization to run an isolated process (<code class="code-inline">LsaIso.exe</code>) inside an isolated virtual trust level (VTL 1). Even a local administrator or kernel driver in the main host OS (VTL 0) cannot read LSASS memory secrets.
    </div>
  </div>

  <!-- MCQ 2 -->
  <div class="mcq-card" data-unit="s5" data-correct="C">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q2</span>
      <div class="mcq-question-text">In Kerberos v5 authentication, what account's secret key is utilized by the Key Distribution Center (KDC) to encrypt the Ticket Granting Ticket (TGT)?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The requesting user's password hash</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The target file server's computer account key</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The master password hash of the domain's krbtgt account</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The public key of the root CA</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: C.</strong> The TGT is encrypted with the secret key of the domain's <code class="code-inline">krbtgt</code> account. Because only KDCs possess this key, client machines cannot tamper with or forge the contents of the TGT.
    </div>
  </div>

  <!-- MCQ 3 -->
  <div class="mcq-card" data-unit="s5" data-correct="A">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q3</span>
      <div class="mcq-question-text">According to NIST SP 800-88 guidelines, what is the most rapid, cryptographically verified method to sanitize a Self-Encrypting Solid-State Drive (SED) before decommissioning?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Cryptographic Erase (CE) / Instant Secure Erase (purges the internal Media Encryption Key)</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 3-Pass DoD 5220.22-M binary pattern overwrite</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Defragmenting the filesystem with defrag.exe</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Formatting the drive as FAT32</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: A.</strong> Cryptographic Erase instantly generates a new internal AES Media Encryption Key (MEK) and purges the old key, rendering all existing ciphertext on the NAND flash mathematically unrecoverable in sub-second time without inducing SSD write wear.
    </div>
  </div>

  <!-- MCQ 4 -->
  <div class="mcq-card" data-unit="s5" data-correct="D">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q4</span>
      <div class="mcq-question-text">Which Windows Security Event ID is generated when a malicious actor or administrator deliberately clears the Security Audit Log?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Event ID 4624</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Event ID 4625</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Event ID 4720</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Event ID 1102 (The audit log was cleared)</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: D (Event ID 1102).</strong> Windows explicitly logs Event ID 1102 when the security event log file is purged, recording the username and session ID of the account that executed the action.
    </div>
  </div>

  <!-- MCQ 5 -->
  <div class="mcq-card" data-unit="s5" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q5</span>
      <div class="mcq-question-text">Why must servers deployed in a Demilitarized Zone (DMZ) NEVER be joined to the internal Active Directory production domain?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Windows Server does not support Active Directory in virtual machines.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Joining the domain requires opening dozens of inbound RPC, LDAP, SMB, and Kerberos ports from the DMZ directly into internal Domain Controllers, completely compromising the perimeter boundary if a DMZ host is hacked.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> DMZ servers are legally prohibited from running Windows.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Active Directory only works on 100Mbps Ethernet.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B.</strong> Joining a DMZ server to the domain creates an open highway into the heart of the internal network. Compromise of a public web server would immediately allow attackers to execute DCSync attacks or Kerberoasting against internal DCs.
    </div>
  </div>

  <!-- MCQs 6 to 30 concise cards -->
  <div class="mcq-card" data-unit="s5" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q6</span><div class="mcq-question-text">What IPsec protocol provides data confidentiality (encryption) along with authentication and integrity for network traffic?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Authentication Header (AH)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Internet Control Message Protocol (ICMP)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Encapsulating Security Payload (ESP - IP Protocol 50)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Telnet</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> ESP provides symmetric encryption (confidentiality) plus message authentication and anti-replay protection. AH provides integrity and authentication only, with zero encryption.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q7</span><div class="mcq-question-text">In Windows Security Event Logs, what does Logon Type 10 signify for Event ID 4624?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> RemoteInteractive logon (Logon via Remote Desktop / Terminal Services)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Local interactive physical console logon</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Network share connection (SMB)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Service account startup</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Logon Type 10 explicitly designates a remote desktop (RDP) session initiation over port 3389. Type 2 represents physical console login; Type 3 represents network share access.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q8</span><div class="mcq-question-text">Which Linux command displays the current operational state of Security-Enhanced Linux (SELinux)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> iptables -L</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ufw status</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> systemctl status firewalld</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> getenforce</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> <code class="code-inline">getenforce</code> returns the active SELinux mode: <code class="code-inline">Enforcing</code>, <code class="code-inline">Permissive</code>, or <code class="code-inline">Disabled</code>.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q9</span><div class="mcq-question-text">What technology prevents an adversary from successfully booting a stolen server hard drive on a different physical motherboard?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> SATA password</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Full Disk Encryption bound to Trusted Platform Module (TPM 2.0) Platform Configuration Registers (PCRs)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Anti-static wrist strap</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> DNSSEC</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> The TPM seals encryption keys against hardware state hashes (PCR 0/2/4/7). If the drive is moved to a foreign motherboard or bootloader integrity is altered, the TPM refuses to release the key.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q10</span><div class="mcq-question-text">What is the risk of utilizing the legacy NTLMv1 or NTLMv2 authentication protocol instead of Kerberos on an enterprise network?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> NTLM uses 50% more CPU power than Kerberos.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> NTLM only works over Wi-Fi.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Vulnerable to Pass-the-Hash (PtH) and relay attacks; lacks mutual authentication; uses weaker cryptographic hash algorithms (MD4/HMAC-MD5).</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> NTLM causes hard drive head crashes.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> NTLM challenge-response sends password hashes over the wire that can be captured and relayed via tools like Responder, granting attackers unauthorized domain access.</div></div>

  <!-- MCQs 11 to 30 -->
  <div class="mcq-card" data-unit="s5" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q11</span><div class="mcq-question-text">What is the function of the "Privilege Attribute Certificate" (PAC) embedded within an Active Directory Kerberos ticket?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Contains the user's Security Identifier (SID), group SIDs, and administrative privileges signed by the KDC.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Stores user email attachments.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Encrypts the computer's swap space.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Authorizes internet browser bookmarks.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> The PAC is signed by the KDC. When the target server receives the Kerberos ticket, it inspects the PAC to build the user's security token and determine file permissions.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q12</span><div class="mcq-question-text">Which command in Linux securely edits the `/etc/sudoers` file, validating syntax before saving to prevent locking out administrative access?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> nano /etc/sudoers</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> cat &gt; /etc/sudoers</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> chmod 777 /etc/sudoers</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> visudo</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> <code class="code-inline">visudo</code> locks the sudoers file, provides syntax checking on save, and refuses to write corrupt syntax that could permanently break administrator privilege elevation.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q13</span><div class="mcq-question-text">What is the purpose of an Online Certificate Status Protocol (OCSP) Responder in an enterprise PKI environment?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Backs up private keys to magnetic tape.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Provides real-time certificate revocation status checks for a specific certificate over HTTP, replacing large, slow Certificate Revocation Lists (CRLs).</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Issues free SSL certificates to any anonymous computer.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Automatically changes root passwords every 30 days.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> OCSP queries return an instant "Good", "Revoked", or "Unknown" status for a single certificate serial number, avoiding downloading multi-megabyte CRL files.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q14</span><div class="mcq-question-text">What is the function of the "BitLocker Network Unlock" feature on Windows Server?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Allows any Wi-Fi user to access server hard drives without passwords.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Automatically disables firewalls on internal subnets.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Allows domain-joined servers to automatically unlock BitLocker-encrypted boot volumes via WDS/DHCP over a trusted corporate LAN during reboots without entering a PIN.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Connects servers to public cloud storage.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Network Unlock uses UEFI network firmware and a WDS key server to unlock servers during automated reboot cycles, while remaining securely locked if stolen off-premises.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q15</span><div class="mcq-question-text">Which Linux security module manages user authentication, account policies, session limits, and password complexity in modular configuration files under `/etc/pam.d/`?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Pluggable Authentication Modules (PAM)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> OpenSSL</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> GRUB2</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Systemd</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> PAM decouples system applications from authentication technologies, providing four management interfaces: auth, account, password, and session.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q16</span><div class="mcq-question-text">In enterprise security architecture, what is "Defense in Depth"?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Burying server racks underground in concrete bunkers.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Purchasing twice as many firewalls from the same vendor.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Using 64-character passwords exclusively.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Layering multiple independent security controls (perimeter firewalls, host firewalls, micro-segmentation, MFA, least privilege, endpoint EDR, and encryption) so failure of one control does not compromise the asset.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Defense in Depth ensures that an attacker penetrating the network perimeter is stopped by secondary layers (e.g. host firewalls, PAM authentication, Credential Guard).</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q17</span><div class="mcq-question-text">What is the consequence of configuring a physical degausser on an enterprise Solid-State Drive (SSD) to destroy confidential data?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It completely purges all data within 5 seconds.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Completely ineffective! Degaussing disrupts magnetic domains on spinning magnetic disks; SSDs store data using electrical charge in floating-gate transistors and are unaffected by magnetic fields.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It formats the drive with ext4.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It doubles the storage capacity of the SSD.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Degaussing only works on magnetic media (HDDs, tapes). Flash memory relies on trapped electrical electrons; degaussing an SSD leaves 100% of data fully readable! Solid-state media must be purged via Cryptographic Erase or physically shredded.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q18</span><div class="mcq-question-text">Which Windows Security Event ID indicates that a user account was added to a privileged security group (such as Domain Admins)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Event ID 4624</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Event ID 4634</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Event ID 4728 (Security-enabled global group member added)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Event ID 7036</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Event ID 4728 is logged whenever a user is added to a global security group, recording the target user SID and the actor SID performing the addition.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q19</span><div class="mcq-question-text">What is the primary role of a "Bastion Host" (Jump Server) in an enterprise server infrastructure?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A heavily hardened, single-purpose gateway through which system administrators must authenticate (via MFA and session recording) to access internal isolated servers.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A fast torrent server used to distribute software ISOs.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> A server that hosts company public email.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> A backup power generator controller.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> A Bastion Host provides a single, closely audited entry point into production environments, enforcing multi-factor authentication, proxying SSH/RDP sessions, and logging all keystrokes.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q20</span><div class="mcq-question-text">What command on Linux RHEL 9 adds a permanent rule to FirewallD allowing HTTPS traffic?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ufw allow 443</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> iptables -A INPUT -p tcp --dport 443 -j ACCEPT</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> netsh advfirewall firewall add rule</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> firewall-cmd --permanent --add-service=https &amp;&amp; firewall-cmd --reload</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> In RHEL/CentOS/Rocky, <code class="code-inline">firewall-cmd --permanent --add-service=https</code> updates the XML configuration persistently, and <code class="code-inline">--reload</code> applies the rules without dropping active connections.</div></div>

  <!-- MCQs 21 to 30 -->
  <div class="mcq-card" data-unit="s5" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q21</span><div class="mcq-question-text">What is "Kerberoasting"?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Physically burning Domain Controller motherboard components.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A post-exploitation attack where an attacker requests Kerberos Service Tickets (TGS) for accounts with registered Service Principal Names (SPNs) and cracks the ticket offline to recover service account passwords.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Sending millions of fake emails to a mail server.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Disconnecting server cooling fans.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Because any valid domain user can request a TGS for any registered SPN, attackers extract the encrypted ticket payload and crack the service account's password offline using GPU hashcrackers.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q22</span><div class="mcq-question-text">Which Linux utility configures kernel cryptographic volume encryption using the Linux Unified Key Setup (LUKS2) specification?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> fdisk</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> lvm</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> cryptsetup luksFormat /dev/sdb1</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> mkfs.ext4</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> <code class="code-inline">cryptsetup luksFormat</code> initializes the LUKS partition header and key slots, enabling AES-XTS full-disk encryption under dm-crypt.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q23</span><div class="mcq-question-text">What is the function of the "Principle of Least Privilege" (PoLP) in server administration?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Granting users and services only the minimum necessary permissions required to perform their specific job functions, and for no longer than needed.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Giving every employee Domain Admin access to avoid IT tickets.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Disabling all antivirus software to increase performance.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Restricting server rooms to executive managers only.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Least privilege minimizes blast radius: if an account or service is compromised, the attacker cannot execute lateral administrative actions.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q24</span><div class="mcq-question-text">What technology allows a client to verify the revocation status of a certificate by receiving a digitally signed, timestamped proof bundled directly with the TLS handshake from the server, eliminating client-side OCSP lookups?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> DNSSEC</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> WPA3</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> BitLocker</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> OCSP Stapling (TLS Certificate Status Request extension)</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> OCSP Stapling allows the web server to cache the signed revocation proof from the CA and "staple" it into the initial TLS handshake, enhancing privacy and speeding up connection setup.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q25</span><div class="mcq-question-text">What command on Windows Server enforces immediate re-application of all Active Directory Group Policy Objects without waiting for the 90-minute refresh interval?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ipconfig /renew</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> gpupdate /force</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> net restart gpo</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> sfc /scannow</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> <code class="code-inline">gpupdate /force</code> instructs the Windows Group Policy client to reapply all Computer and User policy extensions immediately from the Domain Controller.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q26</span><div class="mcq-question-text">In enterprise PKI, what is the offline root CA security architecture?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A Certificate Authority that has no power cables.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A CA server connected directly to public Wi-Fi.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The Root CA signs the Intermediate/Issuing CA certificates and is permanently disconnected from the network and powered down in a secure safe, protected from cyber compromise.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> An open-source CA that runs in a web browser.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Keeping the Root CA air-gapped and offline ensures its master private key cannot be compromised remotely. Subordinate Issuing CAs handle day-to-day certificate issuance.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q27</span><div class="mcq-question-text">What is the function of the "auditd" daemon on enterprise Linux servers?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Kernel audit subsystem that logs system calls, file access modifications, unauthorized execution attempts, and authentication events to `/var/log/audit/audit.log`.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Automatically pays cloud hosting invoices.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Cleans up unused desktop icons.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Compresses user home directories.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> <code class="code-inline">auditd</code> hooks into Linux kernel system calls, providing non-repudiation audit trails for compliance with PCI-DSS and SOC 2 frameworks.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q28</span><div class="mcq-question-text">Which Windows Defender feature prevents malicious scripts and macros from injecting code into other processes or downloading executable payloads?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Disk Cleanup</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Network Map</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Storage Spaces</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Attack Surface Reduction (ASR) rules</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Attack Surface Reduction (ASR) rules block common malware attack vectors (e.g. blocking Office applications from creating child processes or stealing Windows credentials).</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q29</span><div class="mcq-question-text">What is the function of an "Air-Gap" in high-security backup and server architectures?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> An air conditioning vent located behind server racks.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Complete physical and logical isolation of a system or backup repository from all external networks and the Internet, making remote cyber attacks physically impossible.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> A gap between server memory modules to allow airflow.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Running fiber optic cables through open windows.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> An air-gap disconnects all network cables, wireless interfaces, and optical paths. Attackers cannot reach air-gapped repositories over the network to encrypt or delete backups during ransomware campaigns.</div></div>

  <div class="mcq-card" data-unit="s5" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q30</span><div class="mcq-question-text">What command on Windows displays the active Resultant Set of Policy (RSoP) applied to the computer and logged-on user?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ipconfig /all</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> netstat -an</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> gpresult /v /r</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> route print</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> <code class="code-inline">gpresult /v /r</code> outputs the summary of applied GPOs, security group memberships, and precedence orders for both machine and user scopes.</div></div>

</article>

<!-- UNIT 5 SUBJECTIVE SHORT CONCEPTUAL Q&A (5M) -->
<article class="doc-page" id="practice-subj-short-s5">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Assessment • Conceptual Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q2</span> Conceptual Review Questions (5 Marks Each)</h2>
    <p class="lead-para">
      Five focused technical problems analyzing Windows Credential Guard, the Kerberos authentication handshake, IPsec transport vs tunnel modes, NIST SP 800-88 sanitization, and security event log analysis.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q1: Explain how Windows Defender Credential Guard utilizes Virtualization-Based Security (VBS) to defeat Pass-the-Hash and Mimikatz.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> In standard Windows architectures, the Local Security Authority Subsystem Service (<code class="code-inline">LSASS.exe</code>) runs in user mode at ring 3, storing plaintext credentials, NTLM hashes, and Kerberos Ticket Granting Tickets (TGTs) in its process memory. If an attacker gains local Administrator or SYSTEM privileges, tools like Mimikatz read LSASS process memory directly to execute Pass-the-Hash attacks.</p>
      <p>Windows Defender Credential Guard utilizes Hyper-V Virtualization-Based Security (VBS) to partition operating system execution into two Virtual Trust Levels (VTL):</p>
      <ul>
        <li><strong>VTL 0 (Normal World):</strong> Runs the standard Windows kernel, drivers, and user applications (including standard <code class="code-inline">lsass.exe</code>).</li>
        <li><strong>VTL 1 (Secure World):</strong> Runs an isolated micro-kernel and the isolated LSA process (<code class="code-inline">LsaIso.exe</code>) inside an isolated memory sandbox protected by Second Level Address Translation (SLAT) and IOMMU.</li>
      </ul>
      <p>Secret credential keys and Kerberos ticket-decryption routines reside strictly in VTL 1. Even if an attacker has full kernel-level ring 0 control in VTL 0, hardware memory isolation prevents them from reading VTL 1 memory, rendering credential-dumping tools completely powerless.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q2: Diagram and trace the 6 messages in the Kerberos v5 ticket-granting sequence (AS and TGS exchanges).</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ol style="margin-left: 1.2rem; line-height: 1.8;">
        <li><code class="code-inline">AS-REQ</code>: Client sends pre-authentication timestamp encrypted with the user's password hash to the KDC Authentication Service.</li>
        <li><code class="code-inline">AS-REP</code>: KDC verifies timestamp, creates a Ticket Granting Ticket (TGT) encrypted with the master <code class="code-inline">krbtgt</code> key, and returns it with a Logon Session Key encrypted with user's key.</li>
        <li><code class="code-inline">TGS-REQ</code>: Client forwards the TGT, an Authenticator, and the target Service Principal Name (SPN) to the Ticket Granting Service.</li>
        <li><code class="code-inline">TGS-REP</code>: KDC verifies TGT, generates a Service Ticket (ST) encrypted with the target service account's secret key, and sends it to the client.</li>
        <li><code class="code-inline">AP-REQ</code>: Client presents the Service Ticket directly to the application server (e.g., SMB or SQL Server).</li>
        <li><code class="code-inline">AP-REP</code>: (Optional mutual auth) Server proves its identity back to the client; access is granted.</li>
      </ol>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q3: Contrast IPsec Transport Mode with Tunnel Mode across header structures and deployment topologies.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Transport Mode:</strong> Encapsulates only the upper-layer payload (Transport Layer / Layer 4, such as TCP/UDP and application data). The original IP header (Layer 3) is preserved and exposed. Because the original IP header is intact, routers inspect the true source and destination IP addresses. It is strictly used for <strong>Host-to-Host</strong> communications (e.g., securing SQL traffic between an application server and a database server on the same subnet).</li>
        <li><strong>Tunnel Mode:</strong> Encapsulates the <strong>entire</strong> original IP packet (the original IP header + payload). It encrypts the entire original packet and prepends a brand-new outer IP header. The true internal source and destination IP addresses are hidden from intermediate networks. It is utilized for <strong>Gateway-to-Gateway</strong> (Site-to-Site VPNs) and <strong>Host-to-Gateway</strong> (Remote Access VPNs).</li>
      </ul>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q4: Why does a 3-Pass DoD 5220.22-M overwrite fail to sanitize modern Solid-State Drives, and what does NIST SP 800-88 mandate instead?</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> The DoD 5220.22-M specification was formulated for magnetic hard disk drives, assuming that issuing a logical write command to LBA sector 100 directly overwrites the physical magnetic tracks at sector 100. Modern SSDs utilize Flash Translation Layers (FTL) and Wear Leveling algorithms that decouple logical LBA addresses from physical flash blocks. Writing zeros to LBA 100 simply allocates a new physical block; the old block containing confidential data is placed in over-provisioned spare blocks or garbage collection queues, leaving confidential data fully recoverable via chip-off forensic techniques!</p>
      <p>NIST SP 800-88 mandates <strong>Cryptographic Erase (Purge)</strong> or physical destruction for SSDs. Cryptographic Erase destroys the internal AES Media Encryption Key (MEK) inside the drive controller, instantly rendering all raw NAND data irrecoverable.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q5: Explain the forensic significance of Windows Security Event IDs 4624, 4625, 4728, and 1102 during incident response.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Event ID 4624 (Logon Success):</strong> Crucial for identifying lateral movement. Analyzing Logon Types (e.g. Type 10 = RDP, Type 3 = Network share) identifies how an attacker pivoted across systems.</li>
        <li><strong>Event ID 4625 (Logon Failure):</strong> High volume spikes indicate automated credential brute-forcing, password spraying, or compromised service accounts with expired credentials.</li>
        <li><strong>Event ID 4728 (Member Added to Global Security Group):</strong> Critical privilege escalation alert. Generated immediately when an attacker adds a compromised user account to groups like <code class="code-inline">Domain Admins</code>.</li>
        <li><strong>Event ID 1102 (Audit Log Cleared):</strong> Immediate indicator of compromise (IoC). Attackers clear the security log (<code class="code-inline">wevtutil cl Security</code>) to blind defenders; Event 1102 records the exact account that cleared the audit trail.</li>
      </ul>
    </div>
  </div>
</article>

<!-- UNIT 5 SUBJECTIVE LONG SCENARIOS (10M) -->
<article class="doc-page" id="practice-subj-long-s5">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Assessment • Scenario Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q3</span> Architectural &amp; Triage Scenarios (10 Marks Each)</h2>
    <p class="lead-para">
      Enterprise scenarios requiring ransomware lateral movement containment, Kerberoasting defense engineering, and PKI certificate expiration triage.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 1: Defending Against Kerberoasting and Service Account Privilege Escalation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A penetration testing team successfully executes a Kerberoasting attack against an enterprise Active Directory domain. By requesting a service ticket for <code class="code-inline">MSSQLSvc/sql01.corp.local:1433</code>, they crack the service account password offline within 4 hours because the password was simple (<code class="code-inline">Summer2024!</code>). Because that service account was mistakenly placed in Domain Admins, the testers achieve full enterprise forest compromise.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="shield-alert"></i> ARCHITECTURAL HARDENING BLUEPRINT</div>
        <div class="callout-body">
          <ol style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Immediate Remediation:</strong> Strip the SQL service account from the Domain Admins and local Administrators groups. Reset its password to a complex 30+ character random string.</li>
            <li><strong>Migrate to Group Managed Service Accounts (gMSA):</strong> Replace traditional user accounts running services with <strong>Group Managed Service Accounts (gMSA)</strong>:
              <pre class="code-block"><code class="language-powershell">New-ADServiceAccount -Name "gMSASqlSvc" -DNSHostName "sql01.corp.local" `
    -PrincipalsAllowedToRetrieveManagedPassword "SQLServersGroup" `
    -KerberosEncryptionType AES128,AES256</code></pre>
              Active Directory automatically rotates the 120-character binary password every 30 days. No human knows the password, completely neutralizing offline dictionary cracking attacks!
            </li>
            <li><strong>Enforce AES Kerberos Encryption:</strong> Disable weak RC4-HMAC encryption in Kerberos ticket generation, mandating AES-256 exclusively (<code class="code-inline">msDS-SupportedEncryptionTypes = 0x18</code>).</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 2: Containing an Active Lateral Movement Ransomware Attack in an Enterprise Datacenter</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> Security operations detects automated lateral movement across the server farm: ransomware is propagating via SMB port 445 and WMI/WinRM (ports 5985/5986), attempting to encrypt hypervisor storage repositories. Detail the emergency containment procedures and long-term micro-segmentation architecture.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> INCIDENT CONTAINMENT &amp; ZERO-TRUST ARCHITECTURE</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Phase 1: Emergency Network Isolation:</strong> Push emergency Group Policy and firewall scripts immediately:
              <pre class="code-block"><code class="language-powershell"># Block inbound SMB and WinRM from workstation subnets
netsh advfirewall firewall set rule name="File and Printer Sharing (SMB-In)" new enable=No
netsh advfirewall firewall set rule name="Windows Remote Management (HTTP-In)" new enable=No</code></pre>
              Isolate affected subnets at the core layer-3 switches, cutting off north-south and east-west transit.
            </li>
            <li><strong>Phase 2: Immutable Storage Defense:</strong> Verify that backup repositories have active Object Lock (WORM - Write Once Read Many) or physical air-gaps enabled, preventing ransomware from issuing backup deletion commands.</li>
            <li><strong>Phase 3: Host-to-Host Micro-Segmentation:</strong> Implement IPsec Server Isolation policies: servers only accept incoming connections from specifically authenticated IPsec peers matching strict Kerberos computer certificates.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 3: Triaging Catastrophic Enterprise Outage Caused by PKI Issuing CA Certificate Expiration</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> At 00:00 UTC, the Subordinate Issuing Certificate Authority (CA) certificate expires. Instantly, all internal web applications, VPN connections, Wi-Fi 802.1X authentications, and smart card logons fail across 5,000 corporate devices with certificate chain validation errors.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> ROOT-CAUSE ANALYSIS &amp; PKI RECOVERY</div>
        <div class="callout-body">
          <p><strong>1. Root Cause:</strong> In an X.509 PKI trust hierarchy, if an intermediate CA certificate in the chain expires, all end-entity certificates issued by that CA are immediately marked invalid by client cryptographic engines, even if the end-entity certificates have years of validity remaining.</p>
          <p><strong>2. Emergency Recovery Workflow:</strong>
            <ol style="margin-left: 1.2rem; line-height: 1.8;">
              <li>Retrieve the Offline Root CA from the physical secure safe and power it on in an isolated offline vault.</li>
              <li>On the Issuing CA, generate a Certificate Renewal Request (<code class="code-inline">certutil -renewCert</code>) with existing key pair.</li>
              <li>Transfer the request file via air-gapped encrypted USB drive to the Root CA.</li>
              <li>On the Root CA, submit and sign the renewal request, extending validity for another 5 years.</li>
              <li>Transfer the signed certificate back to the Issuing CA, install the certificate, and publish the new Certificate Revocation List (CRL) to active HTTP CRL Distribution Points (CDP).</li>
              <li>Run <code class="code-inline">certutil -pulse</code> across domain workstations to refresh client certificate chain caches.</li>
            </ol>
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 4: Secure Data Sanitization Compliance Audit for 100 Decommissioned Enterprise Servers</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A healthcare organization must decommission 100 2U rack servers containing a mix of spinning SAS drives and NVMe SSDs containing sensitive patient health records (HIPAA compliance). Design an auditable, legally compliant media sanitization procedure satisfying NIST SP 800-88 standards.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="check-check"></i> NIST SP 800-88 SANITIZATION PLAN</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Drive Triage by Media Type:</strong> Segregate mechanical hard drives (HDDs) from solid-state drives (SSDs).</li>
            <li><strong>For NVMe / SAS SSDs (NIST Purge):</strong> Execute ATA/NVMe Cryptographic Erase (CE) or NVMe Format with User Data Erase:
              <pre class="code-block"><code class="language-bash"># NVMe Cryptographic Erase command
nvme format /dev/nvme0n1 --namespace-id=1 --ses=2</code></pre>
              This command purges the internal encryption key and zeroes out user LBA blocks, verified via hex dump inspection (<code class="code-inline">hexdump /dev/nvme0n1</code>).
            </li>
            <li><strong>For Mechanical HDDs (NIST Clear/Purge):</strong> Execute ATA Secure Erase firmware commands or 1-pass full zero overwrite.</li>
            <li><strong>Audit Certification:</strong> Automatically capture drive serial numbers, WWNs, sanitization timestamps, and verification hashes into a signed PDF Certificate of Sanitization for regulatory compliance auditors. Drives failing sanitization are routed to a physical industrial shredder (particle size &le; 2mm).</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</article>

<!-- UNIT 5 MASTER ANSWER KEY -->
<article class="doc-page" id="mcq-answer-key-s5">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 05 • Master Verification Key</span>
    <h2 class="section-title"><span class="sec-num">KEY.5</span> Unit 5 Master Answer Key &amp; Technical Verification Matrix</h2>
    <p class="lead-para">
      Complete answer key and architectural validation matrix for Unit 5 practice bank questions 1 through 30.
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
        <tr><td>Q01</td><td><strong>B</strong></td><td>Windows Defender Credential Guard VBS LSASS isolation</td><td>Virtualization-Based Security</td></tr>
        <tr><td>Q02</td><td><strong>C</strong></td><td>TGT encrypted with master krbtgt account secret key</td><td>RFC 4120 Kerberos V5 Spec</td></tr>
        <tr><td>Q03</td><td><strong>A</strong></td><td>Cryptographic Erase purges Media Encryption Key on SEDs</td><td>NIST SP 800-88 Rev 1 Spec</td></tr>
        <tr><td>Q04</td><td><strong>D</strong></td><td>Event ID 1102: The audit log was cleared</td><td>Windows Security Event Auditing</td></tr>
        <tr><td>Q05</td><td><strong>B</strong></td><td>DMZ servers must not join domain (attack highway)</td><td>Enterprise DMZ Architecture</td></tr>
        <tr><td>Q06</td><td><strong>C</strong></td><td>ESP (Protocol 50) provides confidentiality and integrity</td><td>RFC 4303 IPsec ESP Spec</td></tr>
        <tr><td>Q07</td><td><strong>A</strong></td><td>Logon Type 10: RemoteInteractive (RDP session)</td><td>Windows Logon Types Reference</td></tr>
        <tr><td>Q08</td><td><strong>D</strong></td><td>getenforce displays active SELinux operating mode</td><td>SELinux Administration Guide</td></tr>
        <tr><td>Q09</td><td><strong>B</strong></td><td>TPM 2.0 PCR hardware attestation seals BitLocker keys</td><td>TCG TPM 2.0 Specification</td></tr>
        <tr><td>Q10</td><td><strong>C</strong></td><td>NTLM vulnerable to Pass-the-Hash and relay attacks</td><td>Enterprise Identity Security</td></tr>
        <tr><td>Q11</td><td><strong>A</strong></td><td>PAC stores user SIDs and group memberships signed by KDC</td><td>Microsoft MS-PAC Protocol</td></tr>
        <tr><td>Q12</td><td><strong>D</strong></td><td>visudo validates sudoers syntax to prevent lockouts</td><td>Linux System Administration</td></tr>
        <tr><td>Q13</td><td><strong>B</strong></td><td>OCSP Responder provides real-time revocation checks</td><td>RFC 6960 OCSP Protocol</td></tr>
        <tr><td>Q14</td><td><strong>C</strong></td><td>BitLocker Network Unlock auto-unlocks over trusted LAN</td><td>Windows Server BitLocker</td></tr>
        <tr><td>Q15</td><td><strong>A</strong></td><td>PAM provides modular authentication interfaces on Linux</td><td>Linux-PAM Architecture Guide</td></tr>
        <tr><td>Q16</td><td><strong>D</strong></td><td>Defense in Depth layers multiple independent controls</td><td>NIST Cybersecurity Framework</td></tr>
        <tr><td>Q17</td><td><strong>B</strong></td><td>Degaussing is ineffective on SSDs (electrical charge)</td><td>NIST SP 800-88 Flash Media</td></tr>
        <tr><td>Q18</td><td><strong>C</strong></td><td>Event ID 4728: Member added to security group</td><td>Active Directory Security Audit</td></tr>
        <tr><td>Q19</td><td><strong>A</strong></td><td>Bastion host jump server enforces MFA and auditing</td><td>Zero Trust Enterprise Access</td></tr>
        <tr><td>Q20</td><td><strong>D</strong></td><td>firewall-cmd --permanent --add-service=https</td><td>FirewallD Administration Guide</td></tr>
        <tr><td>Q21</td><td><strong>B</strong></td><td>Kerberoasting cracks offline service ticket hashes</td><td>Active Directory Threat Matrix</td></tr>
        <tr><td>Q22</td><td><strong>C</strong></td><td>cryptsetup luksFormat initializes LUKS2 encryption</td><td>Linux cryptsetup Reference</td></tr>
        <tr><td>Q23</td><td><strong>A</strong></td><td>Principle of Least Privilege minimizes blast radius</td><td>Information Security Principles</td></tr>
        <tr><td>Q24</td><td><strong>D</strong></td><td>OCSP Stapling delivers signed status in TLS handshake</td><td>RFC 6066 TLS Extensions</td></tr>
        <tr><td>Q25</td><td><strong>B</strong></td><td>gpupdate /force reapplies Group Policy immediately</td><td>Windows Group Policy Tools</td></tr>
        <tr><td>Q26</td><td><strong>C</strong></td><td>Offline Root CA stays powered off in physical safe</td><td>PKI Architecture Standards</td></tr>
        <tr><td>Q27</td><td><strong>A</strong></td><td>auditd kernel audit subsystem logs system calls</td><td>Linux Kernel Audit Framework</td></tr>
        <tr><td>Q28</td><td><strong>D</strong></td><td>Attack Surface Reduction (ASR) rules block malware</td><td>Microsoft Defender for Endpoint</td></tr>
        <tr><td>Q29</td><td><strong>B</strong></td><td>Air-gap provides complete physical network isolation</td><td>Disaster Recovery &amp; Ransomware</td></tr>
        <tr><td>Q30</td><td><strong>C</strong></td><td>gpresult /v /r displays applied GPOs and precedence</td><td>Windows Group Policy Diagnostics</td></tr>
      </tbody>
    </table>
  </div>
</article>
"""
