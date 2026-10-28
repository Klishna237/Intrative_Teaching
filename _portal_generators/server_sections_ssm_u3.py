# -*- coding: utf-8 -*-
"""
Server Administration Portal - Unit 3: Server Roles, Maintenance & High Availability
SSM Engineering Standard Gold Standard Architecture
"""

SERVER_UNIT3_HTML = r"""
<!-- ===================================================================
     UNIT 03: SERVER ROLES AND MAINTENANCE
     =================================================================== -->

<!-- ARTICLE 11: ACTIVE DIRECTORY ARCHITECTURE & FSMO ROLES -->
<article class="doc-page" id="s3-ad-roles">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Server Roles &amp; Maintenance • Article 11</span>
    <h2 class="section-title"><span class="sec-num">11</span> Active Directory Domain Services Architecture &amp; The 5 FSMO Roles</h2>
    <p class="lead-para">
      Active Directory Domain Services (AD DS) provides the central identity, authentication, and authorization backbone for enterprise enterprise networks. While modern domain controllers utilize multi-master replication for most database updates, critical schema and identity operations mandate single-master authority governed by the five Flexible Single Master Operation (FSMO) roles.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. The 5 FSMO Master Roles</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Role Name</th>
          <th>Scope</th>
          <th>Core Operational Responsibility</th>
          <th>Failure Impact &amp; Seizure Risk</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Schema Master</strong></td>
          <td>Forest-Wide (1 per forest)</td>
          <td>Governs all modifications, class additions, and attribute extensions to the Active Directory schema database (<code class="code-inline">schema.msc</code>).</td>
          <td>Low immediate impact; schema updates and Exchange/Lync installations blocked. Can be seized if original DC is dead.</td>
        </tr>
        <tr>
          <td><strong>Domain Naming Master</strong></td>
          <td>Forest-Wide (1 per forest)</td>
          <td>Controls the addition, removal, or renaming of domains, application directory partitions, and trust paths within the forest.</td>
          <td>Low immediate impact; cannot add/remove domains or alter cross-forest trusts while offline.</td>
        </tr>
        <tr>
          <td><strong>RID Master (Relative ID)</strong></td>
          <td>Domain-Wide (1 per domain)</td>
          <td>Allocates pools of 500 Relative Identifiers (RIDs) to each Domain Controller for generating unique Security Identifiers (SIDs) for new users, groups, and computers.</td>
          <td>Moderate impact; DCs can create objects until their local 500-RID pool is exhausted. If exhausted, object creation halts completely.</td>
        </tr>
        <tr>
          <td><strong>PDC Emulator</strong></td>
          <td>Domain-Wide (1 per domain)</td>
          <td>Authoritative time source (NTP stratum 1), processes password changes immediately, handles account lockouts, and primary target for Group Policy editing.</td>
          <td><strong>CRITICAL IMMEDIATE IMPACT!</strong> Time drift breaks Kerberos (&gt;5 mins skew = auth failures); password changes not synchronized; account lockouts delayed.</td>
        </tr>
        <tr>
          <td><strong>Infrastructure Master</strong></td>
          <td>Domain-Wide (1 per domain)</td>
          <td>Updates cross-domain object references (e.g. user in Domain A added to group in Domain B). Translates SIDs, GUIDs, and DNs across domains.</td>
          <td>Low immediate impact in single-domain environments; note: must NOT reside on a Global Catalog (GC) server unless all DCs are GCs!</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="key"></i> FSMO ROLE TRANSFER VS SEIZURE</div>
    <div class="callout-body">
      <ul style="margin-left: 1.2rem; line-height: 1.8;">
        <li><strong>Graceful Role Transfer (<code class="code-inline">Move-ADDirectoryServerOperationMasterRole</code>):</strong> Executed when both Domain Controllers are online and operational. The source DC synchronizes its state and relinquishes the role cleanly.</li>
        <li><strong>Forced Role Seizure (<code class="code-inline">-Force</code> switch in PowerShell / <code class="code-inline">ntdsutil</code>):</strong> Performed ONLY when the role holder has suffered catastrophic, irrecoverable hardware failure. <strong>WARNING:</strong> A seized Schema, Domain Naming, or RID Master role holder must NEVER be allowed back online on the network! Doing so creates split-brain directory corruption, requiring immediate metadata cleanup (<code class="code-inline">ntdsutil metadata cleanup</code>).</li>
      </ul>
    </div>
  </div>
</article>

<!-- ARTICLE 12: ENTERPRISE NETWORK SERVICES & DNS/DHCP -->
<article class="doc-page" id="s3-network-services">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Server Roles &amp; Maintenance • Article 12</span>
    <h2 class="section-title"><span class="sec-num">12</span> Enterprise Network Services: Active Directory Integrated DNS &amp; DHCP Failover</h2>
    <p class="lead-para">
      Domain authentication cannot function without deterministic DNS name resolution. Active Directory relies on DNS Service Location (SRV) records to enable domain members to locate Domain Controllers, Kerberos Key Distribution Centers (KDCs), and Global Catalog servers.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Critical Active Directory DNS SRV Records</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>SRV Record Name</th>
          <th>Port &amp; Protocol</th>
          <th>Locates Subsystem</th>
          <th>Impact if Record Missing / Corrupt</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code class="code-inline">_ldap._tcp.dc._msdcs.&lt;domain&gt;</code></td>
          <td>TCP 389 (LDAP)</td>
          <td>Domain Controller Locator for LDAP directory binding</td>
          <td>Clients cannot join domain; <code class="code-inline">nltest /dsgetdc:</code> fails</td>
        </tr>
        <tr>
          <td><code class="code-inline">_kerberos._tcp.dc._msdcs.&lt;domain&gt;</code></td>
          <td>TCP/UDP 88 (Kerberos)</td>
          <td>Kerberos Key Distribution Center (KDC) for ticket granting</td>
          <td>Clients fall back to slow NTLMv2 authentication or fail auth</td>
        </tr>
        <tr>
          <td><code class="code-inline">_gc._tcp.&lt;forest-root&gt;</code></td>
          <td>TCP 3268 (Global Catalog)</td>
          <td>Global Catalog servers across the entire forest</td>
          <td>Multi-domain logons fail; universal group membership unresolvable</td>
        </tr>
        <tr>
          <td><code class="code-inline">_kpasswd._tcp.&lt;domain&gt;</code></td>
          <td>TCP/UDP 464 (Kerberos Change)</td>
          <td>Kerberos password change service daemon</td>
          <td>Users cannot change expired passwords during logon</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">2. DHCP Failover: Load-Sharing vs Hot-Standby</h3>
  <p>
    Windows Server DHCP Failover provides high-availability IP lease allocation without requiring complex cluster shared storage:
  </p>
  <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.8;">
    <li><strong>Load-Sharing Mode (Default):</strong> Both DHCP servers actively service requests concurrently across the scope. Leases are split based on a configured percentage (e.g., 50/50). Servers synchronize lease states in real-time over TCP port 647. Ideal for single-site environments with balanced loads.</li>
    <li><strong>Hot-Standby Mode:</strong> One server is designated Active and services 100% of lease requests. The secondary Standby server remains idle. If the Active server fails to heartbeat within the <strong>Maximum Client Lead Time (MCLT)</strong> window (typically 1 hour), the Standby server assumes full ownership of the scope. Ideal for hub-and-spoke branch office architectures.</li>
  </ul>
</article>

<!-- ARTICLE 13: WEB & APPLICATION SERVERS -->
<article class="doc-page" id="s3-web-app">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Server Roles &amp; Maintenance • Article 13</span>
    <h2 class="section-title"><span class="sec-num">13</span> Web &amp; Application Server Roles: IIS Architecture &amp; Linux Web Stacks</h2>
    <p class="lead-para">
      Enterprise web servers run mission-critical web applications, APIs, and portals. Understanding the internal process isolation models of Microsoft Internet Information Services (IIS) and Linux NGINX/Apache architectures is essential for performance tuning and fault isolation.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Microsoft IIS Architecture: HTTP.sys &amp; Worker Processes</h3>
  <p>
    IIS splits execution between kernel-mode request dispatching and user-mode isolated worker processes:
  </p>
  <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.8;">
    <li><strong>HTTP.sys (Kernel Mode Listener):</strong> Operates as an OS kernel-mode device driver. It terminates incoming TCP connections, parses HTTP request headers, manages kernel-mode response caching, and queues requests directly into the appropriate Application Pool queue. Because HTTP.sys runs in ring 0, it operates with extreme throughput and continues queuing requests even if user-mode worker processes crash!</li>
    <li><strong>World Wide Web Publishing Service (W3SVC / WAS):</strong> Windows Activation Service manages the lifecycle of Application Pools, launching and terminating worker processes on demand.</li>
    <li><strong>Worker Process (<code class="code-inline">w3wp.exe</code> - User Mode):</strong> The isolated execution boundary where .NET, ASP.NET Core, or PHP code runs. If an unhandled application exception crashes a worker process, only that specific Application Pool dies—neighboring websites in separate App Pools continue running uninterrupted.</li>
  </ul>
</article>

<!-- ARTICLE 14: ENTERPRISE PATCHING & WSUS -->
<article class="doc-page" id="s3-patching">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Server Roles &amp; Maintenance • Article 14</span>
    <h2 class="section-title"><span class="sec-num">14</span> Enterprise Patch Management: WSUS, Staging Rings &amp; Change Governance</h2>
    <p class="lead-para">
      Uncontrolled operating system updates can crash production clusters, corrupt database schemas, and violate enterprise Service Level Agreements (SLAs). Enterprise patch management establishes rigorous staging rings, WSUS synchronization hierarchies, and automated rollback baselines.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. The 4-Tier Patch Deployment Ring Architecture</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Ring Tier</th>
          <th>Target Server Cohort</th>
          <th>Soak Time Window</th>
          <th>Approval &amp; Rollback Gates</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Ring 0: Canary / Lab</strong></td>
          <td>Non-production test environments, dev virtualization hosts</td>
          <td>Immediate (Day 1 of Patch Tuesday)</td>
          <td>Automated regression tests; verify OS boot, NIC teaming, and storage mounting</td>
        </tr>
        <tr>
          <td><strong>Ring 1: Pilot / UAT</strong></td>
          <td>Staging servers, secondary replica database nodes, non-critical internal apps</td>
          <td>3 to 5 business days</td>
          <td>User Acceptance Testing; verify line-of-business application compatibility</td>
        </tr>
        <tr>
          <td><strong>Ring 2: Broad Production</strong></td>
          <td>50% of production cluster nodes (Node A of all 2-node HA clusters)</td>
          <td>7 business days</td>
          <td>Staggered cluster-aware updating (CAU); zero client downtime maintained</td>
        </tr>
        <tr>
          <td><strong>Ring 3: Critical Final</strong></td>
          <td>Remaining 50% of cluster nodes (Node B), core domain controllers, billing databases</td>
          <td>14 business days after release</td>
          <td>Final change advisory board (CAB) sign-off; complete change window documentation</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 15: FAILOVER CLUSTERING & HIGH AVAILABILITY -->
<article class="doc-page" id="s3-clustering">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Server Roles &amp; Maintenance • Article 15</span>
    <h2 class="section-title"><span class="sec-num">15</span> Windows Server Failover Clustering (WSFC), Quorum &amp; Split-Brain Prevention</h2>
    <p class="lead-para">
      High Availability (HA) clusters eliminate single points of failure by joining multiple physical or virtual servers into a unified failover domain. Maintaining deterministic cluster state requires mathematically rigorous quorum witness arbitration to prevent catastrophic split-brain scenarios.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. The Split-Brain Threat &amp; Quorum Mathematics</h3>
  <p>
    If the private heartbeat network linking two cluster nodes fails, both nodes might assume the other has died and simultaneously attempt to mount shared disk volumes. This is known as <strong>Split-Brain</strong>, and results in instant, unrecoverable filesystem corruption!
  </p>
  <div class="callout callout-alert">
    <div class="callout-label"><i data-lucide="alert-octagon"></i> QUORUM FORMULA: 50% + 1 MAJORITY VOTE</div>
    <div class="callout-body">
      A cluster remains operational if and only if the number of voting members exceeds 50%:
      \[\text{Quorum} = \left\lfloor \frac{N_{\text{total}}}{2} \right\rfloor + 1\]
      To prevent ties in even-numbered clusters (e.g. 2 nodes or 4 nodes), an external **Quorum Witness** (Disk Witness, File Share Witness, or Azure Cloud Witness) is added to provide an odd total number of votes.
    </div>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Cluster Configuration</th>
          <th>Node Votes</th>
          <th>Witness Vote</th>
          <th>Total Votes</th>
          <th>Quorum Majority Needed</th>
          <th>Fault Tolerance</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>2-Node Cluster (No Witness)</strong></td>
          <td>2</td>
          <td>0</td>
          <td>2</td>
          <td><strong>2 votes (100% required!)</strong></td>
          <td><strong>Zero fault tolerance;</strong> losing 1 node loses quorum immediately!</td>
        </tr>
        <tr>
          <td><strong>2-Node Cluster + Witness</strong></td>
          <td>2</td>
          <td>1 (File Share / Cloud)</td>
          <td>3</td>
          <td><strong>2 votes</strong></td>
          <td>Survives failure of either Node 1 OR Node 2!</td>
        </tr>
        <tr>
          <td><strong>3-Node Cluster (No Witness)</strong></td>
          <td>3</td>
          <td>0</td>
          <td>3</td>
          <td><strong>2 votes</strong></td>
          <td>Survives loss of any 1 node without requiring witness.</td>
        </tr>
        <tr>
          <td><strong>4-Node Cluster + Witness</strong></td>
          <td>4</td>
          <td>1 (Disk / Cloud)</td>
          <td>5</td>
          <td><strong>3 votes</strong></td>
          <td>Survives simultaneous loss of any 2 nodes!</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- UNIT 3 PRACTICE BANK: 30 MCQS -->
<article class="doc-page" id="practice-mcq-s3">
  <div class="page-header-meta">
    <span class="meta-tag">Server Administration • Unit 03</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreS3">Score: 0 / 30</span>
  </div>
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Assessment • Practice Bank</span>
    <h2 class="section-title"><span class="sec-num">Q1</span> Unit 3 Practice Bank: 30 Interactive Examination MCQs</h2>
    <p class="lead-para">
      Comprehensive assessment questions evaluating Active Directory FSMO roles, DNS SRV records, DHCP failover, IIS worker process architecture, and Failover Clustering quorum models.
    </p>
  </header>

  <div class="callout callout-deep" style="margin-bottom: 2rem;">
    <div class="callout-label"><i data-lucide="award"></i> REAL-TIME SCORE ENGINE</div>
    <div class="callout-body">
      Select your answer for each question. Instant feedback will highlight correct answers in green and explanations will appear automatically.
    </div>
  </div>

  <!-- MCQ 1 -->
  <div class="mcq-card" data-unit="s3" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q1</span>
      <div class="mcq-question-text">Which Active Directory FSMO role acts as the authoritative stratum-1 time synchronization source for the entire enterprise domain and processes password changes immediately?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Schema Master</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> PDC Emulator (Primary Domain Controller Emulator)</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> RID Master</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Infrastructure Master</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B (PDC Emulator).</strong> The PDC Emulator manages time synchronization across the domain (crucial for Kerberos 5-minute maximum clock skew), handles account lockouts, receives urgent password replication, and serves as the master target for Group Policy editing.
    </div>
  </div>

  <!-- MCQ 2 -->
  <div class="mcq-card" data-unit="s3" data-correct="C">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q2</span>
      <div class="mcq-question-text">In a Windows Server Failover Cluster (WSFC) containing 2 physical nodes and NO configured quorum witness, what happens if Node 2 suffers an abrupt power loss?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Node 1 absorbs 100% of the workload with zero impact.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The cluster automatically creates a virtual witness on Node 1's local C: drive.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The cluster loses quorum and immediately shuts down all clustered services on Node 1.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Node 1 reboots automatically into Safe Mode.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: C.</strong> In a 2-node cluster without a witness, total votes = 2. Majority required = \(\lfloor 2/2 \rfloor + 1 = 2\). When Node 2 dies, Node 1 has only 1 vote out of 2 (50%, not a majority!). Quorum is lost and clustered roles are terminated to prevent potential split-brain.
    </div>
  </div>

  <!-- MCQ 3 -->
  <div class="mcq-card" data-unit="s3" data-correct="D">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q3</span>
      <div class="mcq-question-text">What DNS SRV record allows Windows domain client computers to dynamically locate Kerberos Key Distribution Center (KDC) services during authentication?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> _http._tcp.dc._msdcs.&lt;domain&gt;</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> _ssh._tcp.&lt;domain&gt;</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> _smb._tcp.dc._msdcs.&lt;domain&gt;</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> _kerberos._tcp.dc._msdcs.&lt;domain&gt;</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: D.</strong> The <code class="code-inline">_kerberos._tcp.dc._msdcs.&lt;domain&gt;</code> SRV record points clients to port 88 on active Domain Controllers running the Kerberos KDC service.
    </div>
  </div>

  <!-- MCQ 4 -->
  <div class="mcq-card" data-unit="s3" data-correct="A">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q4</span>
      <div class="mcq-question-text">In Microsoft IIS web server architecture, which component executes in kernel mode (Ring 0), terminating incoming HTTP TCP connections and queuing requests directly into Application Pool queues?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> HTTP.sys</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> w3wp.exe</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> inetinfo.exe</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> aspnet_wp.exe</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: A.</strong> <code class="code-inline">HTTP.sys</code> is the kernel-mode HTTP listener driver. It operates at ring 0, handling SSL termination, kernel response caching, and direct request queueing without requiring user-mode context switches.
    </div>
  </div>

  <!-- MCQ 5 -->
  <div class="mcq-card" data-unit="s3" data-correct="C">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q5</span>
      <div class="mcq-question-text">Why must an Active Directory Domain Controller that previously held a seized Schema Master or RID Master role NEVER be reconnected to the production network?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It will trigger an electrical short circuit on the switch port.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It will automatically format all member workstations.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It will induce split-brain directory corruption by issuing conflicting duplicate RIDs or outdated schema definitions.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It will invalidate all client Windows licenses.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: C.</strong> Role seizure is non-negotiable. If the old DC reconnects, both it and the new role holder will claim single-master authority, allocating duplicate RIDs (creating security vulnerabilities) and causing irrecoverable replication divergence.
    </div>
  </div>

  <!-- MCQs 6 to 30 concise cards -->
  <div class="mcq-card" data-unit="s3" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q6</span><div class="mcq-question-text">In Windows Server DHCP Failover configured in Hot-Standby mode, what parameter defines the time window before the standby server assumes 100% control of the active server's IP address pool?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> TCP SYN timeout</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Maximum Client Lead Time (MCLT)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> DNS TTL</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> NetBIOS keepalive</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> The Maximum Client Lead Time (MCLT) is the maximum time a DHCP server can extend an IP lease beyond the partner server's state before fully transitioning the scope state.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q7</span><div class="mcq-question-text">Which FSMO role must NOT be co-located on a Domain Controller configured as a Global Catalog (GC) server in a multi-domain forest (unless all DCs are GCs)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> PDC Emulator</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Schema Master</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Domain Naming Master</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Infrastructure Master</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> The Infrastructure Master checks its database against the GC to detect outdated cross-domain references. If located on a GC, it assumes its data is always current and stops replicating cross-domain object updates to peers.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q8</span><div class="mcq-question-text">What is the primary benefit of deploying an Azure Cloud Witness for a Windows Server Failover Cluster instead of a traditional on-premises File Share Witness?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Provides an independent, highly available 3rd-party voting witness located in the public cloud, avoiding multi-site datacenter split-brain dependencies.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Backs up the entire cluster virtual disk images to the cloud for free.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Speeds up local PCIe NVMe storage operations.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Replaces the requirement for Active Directory Domain Services.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Cloud Witness uses Azure Blob Storage as an arbitration point. In a stretch cluster across two physical datacenters, placing the witness in Azure prevents either datacenter from being unable to achieve quorum if the other site loses power.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q9</span><div class="mcq-question-text">What command in Windows PowerShell transfers a FSMO role gracefully from one Domain Controller to another?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Set-ADForest -TransferAll</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ntdsutil metadata cleanup</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Move-ADDirectoryServerOperationMasterRole -Identity "TargetDC" -OperationMasterRole PDCEmulator</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Import-Module ActiveDirectory -ForceRole</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> <code class="code-inline">Move-ADDirectoryServerOperationMasterRole</code> transfers one or more FSMO roles gracefully between active domain controllers.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q10</span><div class="mcq-question-text">In Windows Server Update Services (WSUS), what architecture allows branch offices to download approved update metadata from a central server while fetching actual binary files locally?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> BitTorrent Peer-to-Peer</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> WSUS Downstream Replica Server with BranchCache or Local Content Hosting</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> FTP mirror</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Dynamic DNS round-robin</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> WSUS Downstream Replica servers synchronize approvals from the central Upstream server, caching binaries locally to eliminate WAN bandwidth saturation.</div></div>

  <!-- MCQs 11 to 30 -->
  <div class="mcq-card" data-unit="s3" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q11</span><div class="mcq-question-text">What happens when an IIS Application Pool crashes due to an unhandled memory exception in an ASP.NET application?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The specific worker process (w3wp.exe) terminates and is automatically recycled by WAS; other Application Pools continue running unaffected.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The entire Windows Server immediately reboots.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> All websites on the server are permanently deleted from disk.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> HTTP.sys stops listening on port 80 and port 443.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Application Pools provide process isolation. An unhandled crash in one worker process does not impact adjacent Application Pools or the kernel-mode <code class="code-inline">HTTP.sys</code> listener.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q12</span><div class="mcq-question-text">Which FSMO role is responsible for ensuring that security group membership updates are reflected across domain boundaries in a multi-domain forest?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Schema Master</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Domain Naming Master</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> PDC Emulator</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Infrastructure Master</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> The Infrastructure Master translates cross-domain SIDs and Distinguished Names, keeping phantom records synchronized when users are added to groups in other domains.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q13</span><div class="mcq-question-text">What feature of Windows Server Failover Clustering automatically drains virtual machines, applies security updates, reboots nodes sequentially, and restores workloads with zero downtime?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Windows Defender Offline</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Cluster-Aware Updating (CAU)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> System Restore</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Safe Mode with Networking</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Cluster-Aware Updating (CAU) automates cluster patch orchestration: it pauses a node, drains VMs via live migration, installs updates, reboots the host, resumes the node, and repeats across the cluster.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q14</span><div class="mcq-question-text">In an enterprise Windows network, how do client machines synchronize their system clocks?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Each computer contacts time.google.com over HTTP.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The user manually adjusts the clock in Control Panel every Monday.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Domain hierarchy NTP: Clients synchronize with their authenticating DC; DCs synchronize with the PDC Emulator; the PDC Emulator synchronizes with an external Stratum 1 NTP source.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Clock synchronization is not required on local networks.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> The Windows Time service (W32Time) enforces a strict hierarchy: clients &rarr; authenticating DC &rarr; forest root PDC Emulator &rarr; external stratum 1 hardware clock.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q15</span><div class="mcq-question-text">What is the consequence if the time skew between a domain workstation and the Domain Controller exceeds 5 minutes?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Kerberos authentication fails with error KRB_AP_ERR_SKEW (Clock skew too great), preventing user logons.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The workstation's hard drive automatically reformats.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The monitor resolution drops to 640x480.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Network cards are permanently disabled.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Kerberos embeds timestamps in ticket-granting requests to prevent replay attacks. If the clock difference exceeds the default 5-minute tolerance, ticket validation fails.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q16</span><div class="mcq-question-text">What is the purpose of the "Dynamic Quorum" feature introduced in modern Windows Server Failover Clustering?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Overclocks the cluster processors during peak traffic.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Automatically deletes inactive user accounts.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Allows non-cluster servers to join without passwords.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Dynamically removes voting rights from nodes that are gracefully shut down, preventing quorum loss when servers are removed sequentially for maintenance.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Dynamic Quorum adjusts quorum majority calculations in real-time. If a 5-node cluster gracefully loses 2 nodes, total votes adjust to 3, requiring only 2 votes for quorum instead of 3 out of 5.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q17</span><div class="mcq-question-text">Which Linux package provides enterprise directory services, SMB file sharing, and Domain Controller emulation for Windows clients?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Postfix</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Samba 4 (smbd / winbindd)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> BIND 9</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Squid Proxy</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Samba 4 provides full Active Directory Domain Controller emulation, Kerberos KDC, LDAP services, and SMB3 file sharing on Linux.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q18</span><div class="mcq-question-text">What diagnostic command on a Windows domain member tests secure channel connectivity and locates the active authenticating Domain Controller?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ping localhost</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ipconfig /release</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> nltest /sc_query:&lt;domain&gt; /dsgetdc:&lt;domain&gt;</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> tracert 8.8.8.8</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> <code class="code-inline">nltest /sc_query:</code> tests the workstation's secure channel trust with the DC, while <code class="code-inline">nltest /dsgetdc:</code> queries DNS and returns the IP, site, and flags of the responding DC.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q19</span><div class="mcq-question-text">What is the function of a File Share Witness in a Windows Server Failover Cluster?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> An SMB share hosted on an external server where cluster nodes lock a witness.log file to cast an arbitration vote, breaking ties in even-numbered clusters.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A shared folder where users download movies and music.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> A backup location for SQL database dumps.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> A proxy cache for internet web traffic.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> A File Share Witness provides a tie-breaking vote. Nodes arbitrate for the share by placing an exclusive SMB lock on the witness file; the first node to lock the file secures the witness vote and maintains quorum.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q20</span><div class="mcq-question-text">What is the ITIL term for the formal documentation of system modifications, risk assessments, and rollback procedures presented to a review board before executing server updates?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Incident Ticket</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Service Request</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Problem Report</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Request for Change (RFC) submitted to the Change Advisory Board (CAB)</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> An RFC outlines the technical plan, business justification, downtime window, testing validation, and backout plan evaluated by the Change Advisory Board.</div></div>

  <!-- MCQs 21 to 30 -->
  <div class="mcq-card" data-unit="s3" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q21</span><div class="mcq-question-text">What is the function of the "Recycle Bin" feature in Active Directory Domain Services?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Deletes all inactive computers every 30 days.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Allows recovering accidentally deleted user, group, and computer objects with all their original SIDs, group memberships, and attributes preserved without restoring from backup tapes.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Compresses directory database log files.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Empties the Windows temporary folder on client machines.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> The AD Recycle Bin preserves the object's tombstone state with full attribute retention, allowing instant restoration via <code class="code-inline">Restore-ADObject</code>.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q22</span><div class="mcq-question-text">Which service in Windows Server acts as a software router, NAT gateway, and VPN server for remote corporate workers?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Hyper-V</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Active Directory Rights Management</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Routing and Remote Access Service (RRAS)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Windows Media Services</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> RRAS provides software routing (RIP, BGP), NAT translation, and enterprise VPN termination (IKEv2, SSTP, L2TP/IPsec).</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q23</span><div class="mcq-question-text">What is the function of the Active Directory Global Catalog (GC) server?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Maintains a full replica of its own domain plus a searchable partial attribute set (PAS) of all objects across every domain in the forest.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Catalogs all installed software licenses on user laptops.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Stores physical GPS coordinates of all datacenter racks.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Hosts the company public website.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> The Global Catalog allows rapid forest-wide searching and universal group membership evaluation during logon without requiring cross-domain queries.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q24</span><div class="mcq-question-text">In enterprise patch management, what is "Patch Tuesday"?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The day when all servers must be physically powered off for cleaning.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The day when IT staff receive annual performance reviews.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The day when new hard drives are ordered.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The second Tuesday of each month when Microsoft publicly releases security patches and cumulative updates.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Microsoft releases standardized security and cumulative updates on the second Tuesday of each month at 10:00 AM Pacific Time.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q25</span><div class="mcq-question-text">What is the difference between Windows Server Failover Clustering (WSFC) and Network Load Balancing (NLB)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> WSFC only runs on Linux, while NLB only runs on Windows.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> WSFC is designed for stateful applications with shared storage (SQL Server, Hyper-V) providing automated failover; NLB is designed for stateless applications (IIS Web Farms) distributing traffic across independent nodes.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> NLB requires dedicated fiber optic cables, while WSFC uses Wi-Fi.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> There is no difference; they are identical technologies.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> WSFC protects stateful services requiring single-instance ownership and automated failover; NLB balances stateless incoming TCP/UDP requests across parallel web servers.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q26</span><div class="mcq-question-text">What command on Windows Server forcibly purges and reregisters all Active Directory DNS service records with the DNS server?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ipconfig /flushdns</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> format c: /q</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> nltest /dsregdns &amp;&amp; ipconfig /registerdns</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> net stop spooler</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> <code class="code-inline">nltest /dsregdns</code> instructs the Netlogon service to reregister all domain controller SRV records, while <code class="code-inline">ipconfig /registerdns</code> refreshes host A and PTR records.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q27</span><div class="mcq-question-text">In high-availability clustering, what is the dedicated private network connection used exclusively by cluster nodes to exchange health heartbeats and state transitions called?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Heartbeat / Interconnect Network</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Public Internet Gateway</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Guest Wi-Fi Network</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Out-of-band IPMI interface</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> The heartbeat network carries continuous UDP ping pulses and state synchronization between cluster nodes to monitor peer vitality.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q28</span><div class="mcq-question-text">What is the consequence if the RID Master FSMO role is offline and a Domain Controller exhausts its local pool of Relative Identifiers?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The Domain Controller automatically deletes itself from the domain.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Existing users can no longer log in.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> All computer passwords expire instantly.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Administrators can no longer create new security principals (users, groups, computer accounts) on that Domain Controller.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Security Identifiers require unique RIDs. When the local pool runs out, the DC cannot allocate unique SIDs, blocking creation of any new users or computers.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q29</span><div class="mcq-question-text">What is the function of the "Schema Master" FSMO role during an enterprise Microsoft Exchange or Lync Server installation?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Formats the email database storage drives.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Extends the Active Directory schema database with hundreds of new classes and attributes required by Exchange (e.g. mailNickName, homeMDB).</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Generates SSL certificates for mobile email access.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Backs up the email database to optical media.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> The Schema Master is the sole authority permitted to modify the directory schema rules, classes, and attributes across the entire enterprise forest.</div></div>

  <div class="mcq-card" data-unit="s3" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q30</span><div class="mcq-question-text">What is the Service Level Agreement (SLA) term representing the percentage of time a system is fully operational and accessible over a given period?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Mean Time Between Failures (MTBF)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Mean Time to Repair (MTTR)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> System Availability / Uptime (e.g. "Four Nines" = 99.99% availability)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Total Cost of Ownership (TCO)</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Availability measures operational uptime percentage. "Four Nines" (99.99%) permits a maximum of 52.6 minutes of total unplanned downtime per calendar year.</div></div>

</article>

<!-- UNIT 3 SUBJECTIVE SHORT CONCEPTUAL Q&A (5M) -->
<article class="doc-page" id="practice-subj-short-s3">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Assessment • Conceptual Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q2</span> Conceptual Review Questions (5 Marks Each)</h2>
    <p class="lead-para">
      Five focused technical problems evaluating Active Directory FSMO roles, DNS SRV locator records, DHCP failover modes, IIS worker process isolation, and quorum voting rules.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q1: Detail the functional responsibilities of the PDC Emulator FSMO role and explain the consequences of its prolonged failure.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> The PDC Emulator is the most critical domain-wide FSMO role with five vital functions:</p>
      <ol style="margin-left: 1.2rem; line-height: 1.8;">
        <li><strong>Time Master:</strong> Acts as the authoritative NTP Stratum 1 time source for all DCs in the domain.</li>
        <li><strong>Password Master:</strong> Receives immediate, synchronous replication of all user password changes. When a user authentication fails on another DC, that DC checks with the PDC Emulator before denying the logon.</li>
        <li><strong>Account Lockout Authority:</strong> Processes all failed authentication lockouts centrally.</li>
        <li><strong>GPO Editing Target:</strong> By default, the Group Policy Management Console (GPMC) reads and writes policies directly to the PDC Emulator to prevent replication merge conflicts.</li>
        <li><strong>Legacy Master:</strong> Emulates a Windows NT 4.0 PDC for legacy clients and BDCs.</li>
      </ol>
      <p><strong>Prolonged Failure Impact:</strong> Time drift exceeds 5 minutes, breaking Kerberos authentication across the domain; password updates fail to synchronize, locking out users; and GPO editing experiences version skew.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q2: Explain how DNS SRV records enable client workstations to discover and bind to Active Directory Domain Controllers.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> When a domain member boots or a user logs on, the Netlogon service executes the DC Locator algorithm (RFC 2782). The client sends a DNS query for the SRV record <code class="code-inline">_ldap._tcp.dc._msdcs.&lt;DomainName&gt;</code>. The DNS server returns a list of target hostnames, TCP ports (389), priorities, and weights. The client sends a lightweight LDAP ping (CLDAP) over UDP port 389 to the closest DC based on Active Directory Sites and Services IP subnet mapping. Once acknowledged, the client queries <code class="code-inline">_kerberos._tcp.dc._msdcs.&lt;DomainName&gt;</code> to establish a Kerberos authentication session.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q3: Contrast DHCP Failover in Load-Sharing mode vs Hot-Standby mode.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>Load-Sharing Mode:</strong> Both DHCP servers concurrently answer DISCOVER packets. The IP address pool is partitioned between them (e.g. 50/50 or 80/20). A client MAC hash determines which server responds to which client. Both servers synchronize lease allocation state across a persistent TCP connection (port 647). Best suited for high-density, single-datacenter environments.</li>
        <li><strong>Hot-Standby Mode:</strong> One server is designated Primary (Active) and services 100% of client lease requests. The Secondary (Standby) server answers nothing as long as heartbeats are received. If the Primary fails to respond within the Maximum Client Lead Time (MCLT) window, the Standby server transitions to active state and assumes lease management. Ideal for hub-and-spoke multi-site topologies where the standby server resides at a central site.</li>
      </ul>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q4: Explain how IIS Application Pool isolation prevents a single faulty web application from crashing other hosted sites.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> IIS enforces process isolation by assigning websites to discrete <strong>Application Pools</strong>. Each Application Pool spawns a dedicated user-mode worker process (<code class="code-inline">w3wp.exe</code>) operating in its own memory address space with unique security credentials (AppPoolIdentity). Incoming requests are queued in the kernel by <code class="code-inline">HTTP.sys</code>. If an unhandled memory exception, infinite loop, or buffer overflow occurs in Site A, its specific <code class="code-inline">w3wp.exe</code> process crashes and terminates. The Windows Activation Service (WAS) detects process termination and recycles it. Because Site B executes inside a completely independent <code class="code-inline">w3wp.exe</code> process with separate virtual memory, it continues processing requests with zero interruption.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q5: Why is a Quorum Witness mandatory in a 2-node Windows Server Failover Cluster, and what is the Split-Brain risk?</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> In a 2-node cluster without a witness, each node has 1 vote (total 2 votes). Quorum majority requires \(\lfloor 2/2 \rfloor + 1 = 2\) votes. If the private heartbeat network linking the nodes is severed, each node sees the other missing and assumes it has died. If both nodes attempt to mount the shared SAN volume and run the clustered application simultaneously, they will overwrite each other's disk sectors, causing catastrophic <strong>Split-Brain</strong> data corruption.</p>
      <p>Adding a Quorum Witness (e.g. File Share Witness or Cloud Witness) provides a 3rd vote (total 3 votes, majority = 2). When the heartbeat drops, both nodes race to place an exclusive lock on the witness. The first node to acquire the witness secures 2 votes (Node + Witness = 2) and remains active; the losing node has only 1 vote and immediately terminates its clustered roles, preventing split-brain.</p>
    </div>
  </div>
</article>

<!-- UNIT 3 SUBJECTIVE LONG SCENARIOS (10M) -->
<article class="doc-page" id="practice-subj-long-s3">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Assessment • Scenario Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q3</span> Architectural &amp; Triage Scenarios (10 Marks Each)</h2>
    <p class="lead-para">
      Enterprise scenarios requiring emergency FSMO role seizure, domain-wide time synchronization recovery, and cluster quorum disaster triage.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 1: Emergency Seizure of FSMO Roles Following Motherboard Fire on the Primary DC</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> The primary Domain Controller (<code class="code-inline">DC01</code>) holding all 5 FSMO roles suffers a catastrophic motherboard fire in the server room and is completely unrecoverable. Administrators report that user password resets are failing, new computer accounts cannot be created, and time synchronization warnings are flooding event logs on secondary Domain Controller <code class="code-inline">DC02</code>.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> EMERGENCY INCIDENT REMEDIATION PROCEDURE</div>
        <div class="callout-body">
          <ol style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Isolate Physical Network:</strong> Ensure the burned server (<code class="code-inline">DC01</code>) is unplugged from the network and can NEVER be powered back on.</li>
            <li><strong>Execute Forced FSMO Seizure via PowerShell:</strong> On secondary Domain Controller <code class="code-inline">DC02</code>, open an elevated PowerShell prompt and seize all 5 roles:
              <pre class="code-block"><code class="language-powershell">Move-ADDirectoryServerOperationMasterRole -Identity "DC02" `
    -OperationMasterRole SchemaMaster,DomainNamingMaster,PDCEmulator,RIDMaster,InfrastructureMaster `
    -Force</code></pre>
            </li>
            <li><strong>Perform Active Directory Metadata Cleanup:</strong> Remove the dead <code class="code-inline">DC01</code> computer object, NTDS Settings object, and FRS/DFSR replication partners to prevent replication errors:
              <pre class="code-block"><code class="language-powershell"># Clean dead DC metadata from directory
Remove-ADComputer -Identity "DC01" -Confirm:$false</code></pre>
            </li>
            <li><strong>Reconfigure Domain Time Synchronization:</strong> Configure <code class="code-inline">DC02</code> (the new PDC Emulator) to sync with an external stratum-1 NTP source and announce itself as authoritative:
              <pre class="code-block"><code class="language-powershell">w32tm /config /manualpeerlist:"pool.ntp.org,0x1" /syncfromflags:manual /reliable:yes /update
Restart-Service w32time
w32tm /resync /rediscover</code></pre>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 2: Triaging Massive Kerberos Authentication Failures Caused by VM Clock Drift</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> On Monday morning, 500 enterprise employees report they cannot log on to their domain workstations, receiving the error: <em>"The system cannot log you on due to an error: The clocks on the client and server are out of sync."</em> Analysis reveals the virtualized Domain Controller hosting the PDC Emulator had host-time-synchronization enabled on an ESXi host whose clock had drifted by 14 minutes over the weekend.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> ROOT-CAUSE ANALYSIS &amp; ARCHITECTURAL HARDENING</div>
        <div class="callout-body">
          <p><strong>1. Root Cause:</strong> Kerberos v5 enforces a maximum clock skew of 300 seconds (5 minutes) to protect against ticket replay attacks. The virtualized PDC Emulator had VMware Tools periodic time synchronization enabled. The underlying ESXi host drifted by 14 minutes, pulling the PDC Emulator's clock out of sync with client workstations and other DCs, causing immediate Kerberos authentication halts.</p>
          <p><strong>2. Emergency Recovery:</strong> Manually force the PDC Emulator's clock back into synchronization with an external internet NTP source (<code class="code-inline">w32tm /resync /force</code>). Once corrected, client clocks will resync upon next contact.</p>
          <p><strong>3. Permanent Virtual DC Hardening Rule:</strong> Disable host time synchronization in the virtual machine parameters for all virtualized Domain Controllers:
            <pre class="code-block"><code class="language-text">tools.syncTime = "0"
time.synchronize.continue = "0"
time.synchronize.restore = "0"
time.synchronize.resume.disk = "0"</code></pre>
            Ensure all physical ESXi hypervisor hosts synchronize directly with the corporate core NTP hardware appliances.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 3: Designing a Staged WSUS Patching Pipeline with Cluster-Aware Updating (CAU)</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> Design a corporate patch management architecture for 500 Windows Servers, including a 4-node Hyper-V failover cluster hosting mission-critical patient record databases, guaranteeing zero unplanned downtime and compliance with 14-day SLA patch windows.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="check-check"></i> ARCHITECTURAL SPECIFICATION</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>WSUS Hierarchy:</strong> Deploy an Upstream WSUS Server in the core datacenter synchronizing metadata from Microsoft Update over HTTPS. Deploy Downstream WSUS servers in regional datacenters using BranchCache for content delivery.</li>
            <li><strong>GPO Client-Side Targeting:</strong> Configure Active Directory Group Policy to assign servers to 4 distinct Computer Groups: Ring 0 (Dev/Test), Ring 1 (Pilot), Ring 2 (Production Phase 1), and Ring 3 (Production Phase 2).</li>
            <li><strong>Cluster-Aware Updating (CAU):</strong> For the 4-node Hyper-V cluster, configure CAU in Self-Updating mode:
              <pre class="code-block"><code class="language-powershell">Add-CauClusterRole -ClusterName "HVCluster01" -EnableFirewallRules `
    -MaxFailedNodes 0 -RequireAllNodesOnline -FailoverThreshold 1 `
    -DaysOfWeek Tuesday -WeeksOfMonth Third -PreRebootScript "\\share\scripts\pre-check.ps1"</code></pre>
              CAU safely live-migrates VMs off Node 1 to Nodes 2-4, applies approved updates, reboots Node 1, returns VMs, and proceeds sequentially through all nodes with zero downtime.
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 4: Triaging Split-Brain Outage in a Multi-Site Stretch Cluster</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A 2-node stretch cluster spanning Datacenter A and Datacenter B uses a local file share in Datacenter A as its Quorum Witness. A backhoe severs the dark fiber WAN link connecting Datacenter A and Datacenter B. Analyze the operational state of both datacenters and explain why Datacenter B shut down.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> QUORUM ARBITRATION ANALYSIS</div>
        <div class="callout-body">
          <p><strong>1. Vote Distribution:</strong> Node A (1 vote), Node B (1 vote), File Share Witness in Datacenter A (1 vote). Total votes = 3. Quorum majority required = 2 votes.</p>
          <p><strong>2. WAN Partition Impact:</strong> When the inter-site fiber drops:
            <ul style="margin-left: 1.2rem; line-height: 1.8;">
              <li><strong>Datacenter A:</strong> Node A can communicate with the File Share Witness on its local LAN. Node A (1) + Witness (1) = <strong>2 votes (Quorum Satisfied!)</strong>. Datacenter A remains online and active.</li>
              <li><strong>Datacenter B:</strong> Node B is isolated from both Node A and the File Share Witness across the severed WAN. Node B has only <strong>1 vote out of 3 (Quorum Lost!)</strong>. WSFC cluster service on Node B immediately terminates all clustered virtual machines to prevent Split-Brain.</li>
            </ul>
          </p>
          <p><strong>3. Architectural Flaw &amp; Fix:</strong> Hosting the witness inside Datacenter A biased the cluster toward Datacenter A. The architectural fix is to migrate the witness to an independent third site—such as an <strong>Azure Cloud Witness</strong>—ensuring neither datacenter has an unfair voting advantage.</p>
        </div>
      </div>
    </div>
  </div>
</article>

<!-- UNIT 3 MASTER ANSWER KEY -->
<article class="doc-page" id="mcq-answer-key-s3">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 03 • Master Verification Key</span>
    <h2 class="section-title"><span class="sec-num">KEY.3</span> Unit 3 Master Answer Key &amp; Technical Verification Matrix</h2>
    <p class="lead-para">
      Complete answer key and architectural validation matrix for Unit 3 practice bank questions 1 through 30.
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
        <tr><td>Q01</td><td><strong>B</strong></td><td>PDC Emulator authoritative time master and password sink</td><td>Active Directory Architecture</td></tr>
        <tr><td>Q02</td><td><strong>C</strong></td><td>2-node cluster without witness shuts down on 1 node failure</td><td>WSFC Quorum Specification</td></tr>
        <tr><td>Q03</td><td><strong>D</strong></td><td>_kerberos._tcp.dc._msdcs.&lt;domain&gt; SRV record for KDC</td><td>RFC 2782 DNS SRV Spec</td></tr>
        <tr><td>Q04</td><td><strong>A</strong></td><td>HTTP.sys kernel-mode HTTP listener at Ring 0</td><td>Microsoft IIS Architecture</td></tr>
        <tr><td>Q05</td><td><strong>C</strong></td><td>Seized FSMO holder must never reconnect (split-brain)</td><td>Active Directory Disaster Recovery</td></tr>
        <tr><td>Q06</td><td><strong>B</strong></td><td>MCLT (Maximum Client Lead Time) in DHCP failover</td><td>IETF DHCP Failover Protocol</td></tr>
        <tr><td>Q07</td><td><strong>D</strong></td><td>Infrastructure Master must not reside on GC server</td><td>Active Directory Multi-Domain Spec</td></tr>
        <tr><td>Q08</td><td><strong>A</strong></td><td>Azure Cloud Witness provides 3rd-party tie-breaking vote</td><td>WSFC Cloud Witness Spec</td></tr>
        <tr><td>Q09</td><td><strong>C</strong></td><td>Move-ADDirectoryServerOperationMasterRole cmdlet</td><td>Active Directory PowerShell</td></tr>
        <tr><td>Q10</td><td><strong>B</strong></td><td>WSUS downstream replica servers conserve WAN bandwidth</td><td>Windows Server Update Services</td></tr>
        <tr><td>Q11</td><td><strong>A</strong></td><td>Application Pool crashes isolate to w3wp.exe process</td><td>IIS Process Isolation Model</td></tr>
        <tr><td>Q12</td><td><strong>D</strong></td><td>Infrastructure Master translates cross-domain SIDs</td><td>Active Directory Group Replication</td></tr>
        <tr><td>Q13</td><td><strong>B</strong></td><td>Cluster-Aware Updating (CAU) patches nodes with zero downtime</td><td>Windows Failover Clustering</td></tr>
        <tr><td>Q14</td><td><strong>C</strong></td><td>Windows Time hierarchy: Clients &rarr; DC &rarr; PDC &rarr; NTP</td><td>RFC 1305 Network Time Protocol</td></tr>
        <tr><td>Q15</td><td><strong>A</strong></td><td>Kerberos clock skew limit: 5 minutes (300 seconds)</td><td>RFC 4120 Kerberos V5 Spec</td></tr>
        <tr><td>Q16</td><td><strong>D</strong></td><td>Dynamic Quorum adjusts voting rights during maintenance</td><td>WSFC Dynamic Witness Spec</td></tr>
        <tr><td>Q17</td><td><strong>B</strong></td><td>Samba 4 provides Active Directory DC services on Linux</td><td>Samba Architecture Guide</td></tr>
        <tr><td>Q18</td><td><strong>C</strong></td><td>nltest /sc_query and /dsgetdc for DC verification</td><td>Windows Server Netlogon Tools</td></tr>
        <tr><td>Q19</td><td><strong>A</strong></td><td>File Share Witness SMB lock casts arbitration vote</td><td>WSFC Quorum Architecture</td></tr>
        <tr><td>Q20</td><td><strong>D</strong></td><td>RFC (Request for Change) presented to CAB review board</td><td>ITIL Service Management</td></tr>
        <tr><td>Q21</td><td><strong>B</strong></td><td>AD Recycle Bin restores deleted objects with SIDs intact</td><td>Active Directory Administration</td></tr>
        <tr><td>Q22</td><td><strong>C</strong></td><td>Routing and Remote Access Service (RRAS) for VPN/NAT</td><td>Windows Server Networking</td></tr>
        <tr><td>Q23</td><td><strong>A</strong></td><td>Global Catalog stores partial attribute set (PAS) of forest</td><td>Active Directory Directory Store</td></tr>
        <tr><td>Q24</td><td><strong>D</strong></td><td>Patch Tuesday: 2nd Tuesday of each month</td><td>Enterprise Patch Lifecycle</td></tr>
        <tr><td>Q25</td><td><strong>B</strong></td><td>WSFC for stateful failover; NLB for stateless web farms</td><td>High Availability Architecture</td></tr>
        <tr><td>Q26</td><td><strong>C</strong></td><td>nltest /dsregdns reregisters DC SRV records in DNS</td><td>Netlogon Diagnostic Utilities</td></tr>
        <tr><td>Q27</td><td><strong>A</strong></td><td>Heartbeat network exchanges node vitality pulses</td><td>Cluster Interconnect Standards</td></tr>
        <tr><td>Q28</td><td><strong>D</strong></td><td>RID pool exhaustion prevents creating new users/computers</td><td>Security Identifier Architecture</td></tr>
        <tr><td>Q29</td><td><strong>B</strong></td><td>Schema Master extends directory classes for Exchange</td><td>Active Directory Schema Store</td></tr>
        <tr><td>Q30</td><td><strong>C</strong></td><td>Availability SLA: Four Nines = 99.99% uptime</td><td>Service Level Management</td></tr>
      </tbody>
    </table>
  </div>
</article>
"""
