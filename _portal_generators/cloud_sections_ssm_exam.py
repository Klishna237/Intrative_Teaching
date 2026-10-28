# -*- coding: utf-8 -*-
"""
Cloud Administration Portal - Master Comprehensive Examination Bank
Master Gold Standard with Course Outcome (CO1-CO5) Alignment & Bloom's Taxonomy
"""

CLOUD_EXAM_HTML = r"""
<!-- ===================================================================
     MASTER COMPREHENSIVE EXAMINATION BANK & COURSE OUTCOMES
     =================================================================== -->
<article class="doc-page" id="cloud-exam-bank">
  <header class="doc-page-header">
    <span class="page-header-meta">Assessment Blueprint • Course Outcomes CO1–CO5 • Examination Papers</span>
    <h2 class="section-title"><span class="sec-num">EXAM.1</span> Master Comprehensive Examination Bank &amp; University Assessment Blueprint</h2>
    <p class="lead-para">
      Rigorous academic assessment papers designed according to Academic Examination Guidelines. Contains complete Mid-Semester Tests (MST-1 &amp; MST-2) and the End-Semester Final Examination with Bloom's Revised Taxonomy levels, Course Outcome (CO) mapping, and detailed analytical model solutions.
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
              <td>Evaluate cloud computing architectural models (IaaS, PaaS, SaaS) and global physical infrastructure resilience.</td>
              <td>Level 4 (Analyze) &amp; Level 5 (Evaluate)</td>
              <td>75% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO2</strong></td>
              <td>Engineer scalable virtual compute systems, Nitro hypervisors, and dynamic auto-scaling clusters.</td>
              <td>Level 3 (Apply) &amp; Level 4 (Analyze)</td>
              <td>75% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO3</strong></td>
              <td>Design durable distributed storage topologies, S3 lifecycle tiers, EBS IOPS configurations, and multi-region CDNs.</td>
              <td>Level 4 (Analyze) &amp; Level 6 (Create)</td>
              <td>70% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO4</strong></td>
              <td>Architect enterprise software-defined networks, multi-AZ VPC subnets, NAT gateways, and hybrid Direct Connect tunnels.</td>
              <td>Level 5 (Evaluate) &amp; Level 6 (Create)</td>
              <td>70% score &ge; 60%</td>
            </tr>
            <tr>
              <td><strong>CO5</strong></td>
              <td>Implement cloud security controls, IAM least privilege, KMS envelope encryption, and disaster recovery architectures meeting strict RTO/RPO SLAs.</td>
              <td>Level 5 (Evaluate) &amp; Level 6 (Create)</td>
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
      <div class="subj-title">Q1: Comprehensive Virtualization Analysis &amp; The AWS Nitro Hypervisor Architecture [CO1, CO2 • Bloom: Level 5]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> Contrast Type-1 (Bare Metal) and Type-2 (Hosted) hypervisors. Analyze why the traditional Xen software hypervisor architecture induced performance jitter in high-throughput workloads, and dissect how the modular AWS Nitro System offloads VPC networking, EBS storage, and hardware security onto dedicated PCIe ASICs to deliver near bare-metal performance.</p>
      <div class="callout callout-tip">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> MODEL SOLUTION OUTLINE &amp; MARKING RUBRIC (10 MARKS)</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Type-1 vs Type-2 Hypervisor Comparison (3 Marks):</strong> Direct hardware access via ring 0 / VMX root operation vs OS kernel scheduling abstraction; context-switching penalties.</li>
            <li><strong>Xen Architecture Bottlenecks (3 Marks):</strong> Dom0 kernel trapping of network and disk I/O; CPU interrupt processing stealing compute cycles from tenant workloads.</li>
            <li><strong>AWS Nitro Modular Offload Subsystems (4 Marks):</strong> Nitro Card for VPC (SR-IOV / ENA Direct Memory Access), Nitro Card for EBS (NVMe controller hardware engine), and Nitro Security Chip (secure hardware root-of-trust, memory isolation).</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">MST1 • 10M</div>
      <div class="subj-title">Q2: Architectural Design: Resilient Auto-Scaling &amp; Compute Cost Optimization [CO2 • Bloom: Level 6]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> An e-commerce platform experiences baseline traffic of 10,000 requests/sec, spiking to 80,000 requests/sec during 3-day flash sales. Design a cost-optimized compute topology combining On-Demand, Savings Plans, and EC2 Spot Instances across multiple Availability Zones with Target Tracking scaling policies and warm pools.</p>
      <div class="callout callout-tip">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> MODEL SOLUTION OUTLINE (10 MARKS)</div>
        <div class="callout-body">
          Design a 3-tier compute fleet utilizing: (1) 3-Year Compute Savings Plans for predictable baseline capacity (up to 72% discount); (2) Auto Scaling Group with mixed instance types (m6i, m6a, c6i) across 3 AZs for Spot Instances to absorb flash spikes with Spot Capacity-Optimized allocation; (3) ALB target tracking policy keyed on <code class="code-inline">ALBRequestCountPerTarget</code> with a 300s warm pool to avoid cold-boot latency.
        </div>
      </div>
    </div>
  </div>

  <!-- MID SEMESTER TEST 2 -->
  <h3 style="margin-top: 2.5rem; color: var(--text-normal); font-size: 18px;">Mid-Semester Test 2 (MST-2) Paper [Units 3 &amp; 4 • Max Marks: 30]</h3>

  <div class="subj-card" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">MST2 • 10M</div>
      <div class="subj-title">Q3: Distributed Storage Trade-Offs &amp; S3 Consistency Guarantees [CO3 • Bloom: Level 5]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> Compare Amazon S3 (Object), Amazon EBS (Block), and Amazon EFS (File) across latency, access protocols, file system locking, and durability guarantees. Explain the mechanism behind Amazon S3's strong read-after-write consistency for PUT and DELETE operations without performance degradation.</p>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">MST2 • 10M</div>
      <div class="subj-title">Q4: Multi-VPC Transit Hub Network Engineering with Disaster Recovery Failover [CO4 • Bloom: Level 6]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem Statement:</strong> An enterprise has 20 VPCs across Development, Production, and Shared Services. Architect a hub-and-spoke network using AWS Transit Gateway, dedicated route domains, centralized NAT Gateway inspection VPC, and an AWS Direct Connect with IPSec VPN backup.</p>
    </div>
  </div>

  <!-- FINAL UNIVERSITY EXAMINATION PAPER -->
  <h3 style="margin-top: 2.5rem; color: var(--text-normal); font-size: 18px;">Department of Computer Science & Engineering End-Semester Comprehensive Examination Paper [Units 1–6 • Max Marks: 60]</h3>

  <div class="subj-card revealed" style="margin-top: 1rem;">
    <div class="subj-header">
      <div class="subj-q-badge">FINAL • 10M</div>
      <div class="subj-title">Section C • Comprehensive Capstone Architecture Problem [CO1–CO5 • Bloom: Level 6]</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Enterprise Scenario:</strong> A multinational financial banking institution requires a mission-critical web application with strict compliance mandates: RPO &le; 1 second, RTO &le; 2 minutes, PCI-DSS Level 1 compliance, end-to-end data encryption at rest and in transit, protection against Layer 7 DDoS and SQL injection, and active-passive cross-region disaster recovery between Mumbai (<code class="code-inline">ap-south-1</code>) and Hyderabad (<code class="code-inline">ap-south-2</code>).</p>
      
      <p><strong>Deliverables Required:</strong></p>
      <ol style="margin-left: 1.5rem; line-height: 1.8;">
        <li>Draw and document the complete multi-tier network topology (Route 53, CloudFront, ALB, Private EC2 ASG, Aurora Multi-AZ).</li>
        <li>Specify the cryptographic envelope encryption workflow utilizing AWS KMS Customer Managed Keys (CMKs) with key rotation.</li>
        <li>Detail the automated cross-region failover mechanism utilizing Route 53 health checks and Aurora Global Database storage replication.</li>
        <li>Provide the complete IAM policy enforcing Least Privilege access and IP CIDR restriction.</li>
      </ol>

      <div class="callout callout-deep" style="margin-top: 1.5rem;">
        <div class="callout-label"><i data-lucide="check-check"></i> MASTER GRADING RUBRIC (10 MARKS TOTAL)</div>
        <div class="callout-body">
          • <strong>Topology &amp; Tier Isolation (2.5M):</strong> Correct multi-AZ private subnetting, IGW/NAT separation, ALB and WAF placement.<br>
          • <strong>KMS Envelope Encryption (2.5M):</strong> KMS GenerateDataKey API trace, plaintext DEK in memory, ciphertext DEK stored with encrypted blob.<br>
          • <strong>Cross-Region DR &amp; RPO/RTO SLA (2.5M):</strong> Aurora Global Database sub-second physical storage replication (&lt;1s RPO) and automated Route 53 DNS failover (&lt;2min RTO).<br>
          • <strong>IAM Least Privilege &amp; Compliance (2.5M):</strong> Explicit Deny statements, Condition keys (<code class="code-inline">aws:PrincipalArn</code>, <code class="code-inline">aws:SourceIp</code>), KMS key policy isolation.
        </div>
      </div>
    </div>
  </div>

</article>
"""
