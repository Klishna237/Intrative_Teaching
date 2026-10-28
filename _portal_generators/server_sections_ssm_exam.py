# -*- coding: utf-8 -*-
"""
Server Administration Portal - Master Comprehensive Examination Bank
Master Gold Standard with Course Outcome (CO1-CO5) Alignment & Bloom's Taxonomy
"""

SERVER_EXAM_HTML = r"""
<!-- ===================================================================
     MASTER COMPREHENSIVE EXAMINATION BANK & COURSE OUTCOMES
     =================================================================== -->
<article class="doc-page" id="server-exam-bank">
  <header class="doc-page-header">
    <span class="page-header-meta">Assessment Blueprint • Course Outcomes CO1–CO5 • University Examination Papers</span>
    <h2 class="section-title"><span class="sec-num">EXAM.1</span> Master Comprehensive Examination Bank &amp; University Assessment Blueprint</h2>
    <p class="lead-para">
      Academic assessment blueprints and rigorous examination papers designed according to Academic Examination Guidelines. Contains Mid-Semester Tests (MST-1 &amp; MST-2) and the End-Semester Final Examination with Bloom's Revised Taxonomy levels, Course Outcome (CO) mapping, and detailed analytical model solutions.
    </p>
  </header>

  <!-- COURSE OUTCOMES MATRIX -->
  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="award"></i> Course Outcomes (CO) MATRIX</div>
    <div class="callout-body">
      <div class="table-container" style="margin-top: 0.5rem;">
        <table>
          <thead>
            <tr>
              <th>CO #</th>
              <th>Course Outcome Statement</th>
              <th>Bloom's Taxonomy Level</th>
              <th>Target Attainment</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CO1</strong></td>
              <td>Understand server hardware architecture, components, form factors, and power redundancy.</td>
              <td>Level 2 (Understand) &amp; Level 4 (Analyze)</td>
              <td>75% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO2</strong></td>
              <td>Install, configure, and manage server operating systems, automated PXE provisioning, and virtualization platforms.</td>
              <td>Level 3 (Apply) &amp; Level 4 (Analyze)</td>
              <td>75% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO3</strong></td>
              <td>Implement server roles, Active Directory services, patch management, fault tolerance, and high availability.</td>
              <td>Level 3 (Apply) &amp; Level 5 (Evaluate)</td>
              <td>70% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO4</strong></td>
              <td>Configure storage technologies including RAID parity math, write penalties, iSCSI fabrics, and capacity planning.</td>
              <td>Level 4 (Analyze) &amp; Level 6 (Create)</td>
              <td>70% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO5</strong></td>
              <td>Apply networking, security controls, disaster recovery, and troubleshooting techniques for server infrastructure.</td>
              <td>Level 4 (Analyze) &amp; Level 5 (Evaluate)</td>
              <td>75% score &ge; 60%</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- MID SEMESTER TEST 1 -->
  <h3 style="margin-top: 2.5rem; color: var(--text-normal); font-size: 18px;">Mid-Semester Test 1 (MST-1) Paper [Units 1 &amp; 2 • Max Marks: 30]</h3>

  <div class="subj-card revealed" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">MST1 • 10M</div>
      <div class="subj-title">Q1: Multi-Socket NUMA Memory Architecture &amp; Virtual Machine vNUMA Alignment [CO1, CO2 • Bloom: Level 5]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> In a dual-socket enterprise server (Intel Xeon Scalable or AMD EPYC), compare local vs remote memory access latencies across point-to-point interconnects (UPI / Infinity Fabric). Analyze why scheduling a 384GB virtual machine across a host containing 256GB per socket induces severe transactional performance degradation when vNUMA is disabled, and propose the architectural solution.</p>
      <div class="callout callout-tip">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> MODEL SOLUTION OUTLINE (10 MARKS)</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>NUMA Hardware Topology (3M):</strong> Dedicated memory controllers per physical socket; local latency (~70ns) vs remote UPI transit latency (~130ns, 1.8x penalty).</li>
            <li><strong>vNUMA Misconfiguration Analysis (3M):</strong> Disabling vNUMA exposes flat non-NUMA memory to guest OS; OS schedules threads on Socket 0 while buffer pools reside on Socket 1, saturating inter-socket bus.</li>
            <li><strong>Remediation Architecture (4M):</strong> Enable vNUMA topology presentation, set SQL Server NUMA node affinity, and enforce memory reservations matching physical node boundaries.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">MST1 • 10M</div>
      <div class="subj-title">Q2: Enterprise PXE Network Boot Architecture &amp; Automated Kickstart Provisioning [CO2 • Bloom: Level 6]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> Detail the 6-stage protocol sequence of a PXE network installation from DHCP Option 66/67 to kernel handover. Design a zero-touch Kickstart (<code class="code-inline">ks.cfg</code>) automated partitioning recipe for an enterprise server mandating GPT, UEFI Secure Boot, LVM logical volume separation, and encrypted swap.</p>
    </div>
  </div>

  <!-- MID SEMESTER TEST 2 -->
  <h3 style="margin-top: 2.5rem; color: var(--text-normal); font-size: 18px;">Mid-Semester Test 2 (MST-2) Paper [Units 3 &amp; 4 • Max Marks: 30]</h3>

  <div class="subj-card" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">MST2 • 10M</div>
      <div class="subj-title">Q3: Active Directory FSMO Master Role Failure Analysis &amp; Seizure Protocols [CO3 • Bloom: Level 5]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> Evaluate the immediate vs long-term operational impacts of an unexpected outage of the PDC Emulator, RID Master, and Schema Master FSMO roles. Detail the exact PowerShell procedures to execute an emergency forced role seizure, and explain why the dead DC must never be allowed to reconnect to the network.</p>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">MST2 • 10M</div>
      <div class="subj-title">Q4: Enterprise Storage Sizing: The RAID 5/6 Write Penalty &amp; IOPS Mathematics [CO4 • Bloom: Level 6]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> Prove mathematically why a RAID 5 array incurs a 4-IOPS write penalty and a RAID 6 array incurs a 6-IOPS write penalty. Given an enterprise database issuing 4,000 IOPS (60% writes, 40% reads), calculate the backend physical disk IOPS required for RAID 10, RAID 5, and RAID 6.</p>
    </div>
  </div>

  <!-- FINAL UNIVERSITY EXAMINATION PAPER -->
  <h3 style="margin-top: 2.5rem; color: var(--text-normal); font-size: 18px;">Department of Computer Science & Engineering End-Semester Comprehensive Examination Paper [Units 1–6 • Max Marks: 60]</h3>

  <div class="subj-card revealed" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">FINAL • 10M</div>
      <div class="subj-title">Section C • Capstone Infrastructure Resilience &amp; Security Problem [CO1–CO5 • Bloom: Level 6]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Enterprise Scenario:</strong> A financial institution requires a complete redesign of its core server and storage architecture following a major outage. The new system must satisfy the following mandates: 99.99% availability, zero single points of failure across compute, power, and storage fabrics, protection against ransomware encrypting backup repositories, RTO &le; 15 minutes, RPO &le; 1 minute, and isolation of Kerberos credentials from kernel memory dumps.</p>
      
      <p><strong>Deliverables Required:</strong></p>
      <ol style="margin-left: 1.5rem; line-height: 1.8;">
        <li>Design the physical compute and power infrastructure (2N CRPS power feeds, multi-socket NUMA hosts, ECC RDIMM, 100GbE NIC teaming in Switch Independent mode).</li>
        <li>Specify the storage fabric architecture (All-Flash NVMe RAID 10 vs RAID 6, MPIO Round-Robin, LUN masking).</li>
        <li>Design the Active Directory security architecture (Credential Guard VBS isolation, gMSA service accounts, and tiered administrative OU models).</li>
        <li>Specify the immutable 3-2-1-1-0 backup strategy and disaster recovery failover runbook.</li>
      </ol>

      <div class="callout callout-deep" style="margin-top: 1.5rem;">
        <div class="callout-label"><i data-lucide="check-check"></i> MASTER GRADING RUBRIC (10 MARKS TOTAL)</div>
        <div class="callout-body">
          • <strong>Compute &amp; Power Architecture (2.5M):</strong> Correct 2N dual-feed CRPS electrical design, NUMA socket pinning, and switch-independent NIC teaming.<br>
          • <strong>Storage &amp; MPIO Fabrics (2.5M):</strong> Accurate write-penalty calculation, RAID 10 selection for random writes, and redundant dual-fabric MPIO configuration.<br>
          • <strong>Active Directory &amp; Credential Defense (2.5M):</strong> Credential Guard VTL 1 isolation, gMSA automated 30-day password rotation, and Kerberoasting defense.<br>
          • <strong>Immutable Backup &amp; DR SLA (2.5M):</strong> 3-2-1-1-0 topology with S3 Object Lock compliance mode or air-gapped tape, meeting RTO &le; 15m and RPO &le; 1m.
        </div>
      </div>
    </div>
  </div>

</article>
"""
