# -*- coding: utf-8 -*-
"""
Master Assembler for Server Administration Knowledge Portal
Generates d:\CU - Teach\Server_Administration_Portal\index.html
SSM Engineering Standard Gold Standard Architecture matching IT Fundamentals
"""

import os
import re

# Import the 6 core unit modules and specialized sections
import server_sections_ssm_u1
import server_sections_ssm_u2
import server_sections_ssm_u3
import server_sections_ssm_u4
import server_sections_ssm_u5
import server_sections_ssm_u6
import server_sections_ssm_trace
import server_sections_ssm_labs
import server_sections_ssm_sims
import server_sections_ssm_exam

# Load CSS template
with open('_portal_generators/portal_style.css', 'r', encoding='utf-8') as f:
    CSS_CONTENT = f.read()

# Build ToC HTML exactly matching IT Fundamentals two-tier accordion structure
TOC_HTML = """
    <div class="toc-header">
      <div class="toc-title">
        <i data-lucide="server" style="width: 18px; height: 18px; color: var(--primary);"></i>
        <span>Course Navigator</span>
      </div>
      <button class="btn-tool" id="btnCloseToc" title="Close ToC Sidebar">
        <i data-lucide="x" style="width: 15px; height: 15px;"></i>
      </button>
    </div>

    <!-- Sister Portals & Master Hub Quick Links -->
    <div style="padding: 0.75rem 1rem; border-bottom: 1px solid var(--border-subtle); background: var(--bg-surface);">
      <div style="font-size: 10px; font-weight: 800; font-family: var(--font-mono); color: var(--text-subtle); text-transform: uppercase; margin-bottom: 0.5rem; letter-spacing: 0.05em;">
        Academic Portals
      </div>
      <div style="display: flex; flex-direction: column; gap: 0.35rem;">
        <a href="../index.html" class="toc-link" style="display: flex; align-items: center; gap: 0.5rem; font-size: 12px; padding: 0.35rem 0.5rem; border-radius: 6px; text-decoration: none; color: var(--text-muted);">
          <span>🏠</span> <strong>Master Academic Hub</strong>
        </a>
        <a href="../IT_Fundamentals_Portal/index.html" class="toc-link" style="display: flex; align-items: center; gap: 0.5rem; font-size: 12px; padding: 0.35rem 0.5rem; border-radius: 6px; text-decoration: none; color: var(--text-muted);">
          <span>💻</span> <strong>IT Fundamentals (CSC104)</strong>
        </a>
        <a href="../Cloud_Administration_Portal/index.html" class="toc-link" style="display: flex; align-items: center; gap: 0.5rem; font-size: 12px; padding: 0.35rem 0.5rem; border-radius: 6px; text-decoration: none; color: var(--text-muted);">
          <span>☁️</span> <strong>Cloud Administration (CSC205)</strong>
        </a>
      </div>
    </div>

    <div class="toc-content">

      <!-- ==========================================
           UNIT 01: SERVER HARDWARE FUNDAMENTALS
           ========================================== -->
      <div class="toc-unit" id="tocUnit1Server">
        <button class="toc-unit-header" type="button" aria-expanded="true">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 01</span>
            <span class="toc-unit-title">Server Hardware Fundamentals</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupS1Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Hardware Engineering</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#s1-hardware" class="toc-link active"><span class="toc-link-num">01.</span> Chassis, Form Factors &amp; Out-of-Band (BMC)</a>
              <a href="#s1-cpu" class="toc-link"><span class="toc-link-num">02.</span> Multi-Socket Processors &amp; NUMA Architecture</a>
              <a href="#s1-ram" class="toc-link"><span class="toc-link-num">03.</span> ECC Memory Architecture &amp; SECDED Math</a>
              <a href="#s1-expansion" class="toc-link"><span class="toc-link-num">04.</span> PCIe Risers, OCP 3.0 &amp; NVMe Backplanes</a>
              <a href="#s1-power-cooling" class="toc-link"><span class="toc-link-num">05.</span> Power Redundancy (2N) &amp; Hot/Cold Aisle</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupS1Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 01 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-s1" class="toc-link"><span class="toc-link-num">06.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-s1" class="toc-link"><span class="toc-link-num">07.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-s1" class="toc-link"><span class="toc-link-num">08.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-s1" class="toc-link"><span class="toc-link-num">09.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 02: SERVER INSTALLATION & VIRTUALIZATION
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit2Server">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 02</span>
            <span class="toc-unit-title">Installation &amp; Virtualization</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupS2Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • OS &amp; Hypervisors</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#s2-os-install" class="toc-link"><span class="toc-link-num">10.</span> Windows Server vs RHEL Automated Deployments</a>
              <a href="#s2-partitioning" class="toc-link"><span class="toc-link-num">11.</span> GPT vs MBR &amp; Filesystems (NTFS, ReFS, XFS)</a>
              <a href="#s2-virt" class="toc-link"><span class="toc-link-num">12.</span> Type-1 Bare-Metal Hypervisors (ESXi &amp; KVM)</a>
              <a href="#s2-memory-ballooning" class="toc-link"><span class="toc-link-num">13.</span> Hypervisor Memory Ballooning &amp; Overcommit</a>
              <a href="#s2-virtual-networking" class="toc-link"><span class="toc-link-num">14.</span> Virtual Switching (vSwitch) &amp; VLAN Trunking</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupS2Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 02 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-s2" class="toc-link"><span class="toc-link-num">15.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-s2" class="toc-link"><span class="toc-link-num">16.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-s2" class="toc-link"><span class="toc-link-num">17.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-s2" class="toc-link"><span class="toc-link-num">18.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 03: SERVER ROLES & CLUSTERING
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit3Server">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 03</span>
            <span class="toc-unit-title">Server Roles &amp; High Availability</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupS3Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Roles &amp; Services</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#s3-ad-roles" class="toc-link"><span class="toc-link-num">19.</span> Active Directory DS &amp; FSMO Roles</a>
              <a href="#s3-network-services" class="toc-link"><span class="toc-link-num">20.</span> Core Infrastructure: DNS, DHCP Failover &amp; IPAM</a>
              <a href="#s3-web-app" class="toc-link"><span class="toc-link-num">21.</span> Enterprise Web Services: IIS Worker Processes &amp; NGINX</a>
              <a href="#s3-patching" class="toc-link"><span class="toc-link-num">22.</span> Patch Management Architecture: WSUS &amp; Satellite</a>
              <a href="#s3-clustering" class="toc-link"><span class="toc-link-num">23.</span> Failover Clustering (WSFC) &amp; Quorum Mechanics</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupS3Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 03 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-s3" class="toc-link"><span class="toc-link-num">24.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-s3" class="toc-link"><span class="toc-link-num">25.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-s3" class="toc-link"><span class="toc-link-num">26.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-s3" class="toc-link"><span class="toc-link-num">27.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 04: STORAGE ARCHITECTURES & RAID
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit4Server">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 04</span>
            <span class="toc-unit-title">Storage Architectures &amp; RAID</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupS4Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Enterprise Storage</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#s4-storage-arch" class="toc-link"><span class="toc-link-num">28.</span> DAS, NAS &amp; SAN Topologies (FC, FCoE, iSCSI)</a>
              <a href="#s4-protocols" class="toc-link"><span class="toc-link-num">29.</span> Storage Protocol Stack &amp; NVMe-oF Low Latency</a>
              <a href="#s4-raid" class="toc-link"><span class="toc-link-num">30.</span> Hardware RAID Levels &amp; XOR Galois Math</a>
              <a href="#s4-write-penalty" class="toc-link"><span class="toc-link-num">31.</span> RAID Write Penalty Math &amp; IOPS Sizing</a>
              <a href="#s4-capacity" class="toc-link"><span class="toc-link-num">32.</span> Binary vs Decimal Storage &amp; Storage Spaces Direct</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupS4Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 04 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-s4" class="toc-link"><span class="toc-link-num">33.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-s4" class="toc-link"><span class="toc-link-num">34.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-s4" class="toc-link"><span class="toc-link-num">35.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-s4" class="toc-link"><span class="toc-link-num">36.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 05: SERVER HARDENING & PKI SECURITY
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit5Server">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 05</span>
            <span class="toc-unit-title">Server Hardening &amp; Security</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupS5Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Defense &amp; Hardening</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#s5-hardening" class="toc-link"><span class="toc-link-num">37.</span> OS Hardening Baselines: CIS Benchmarks &amp; GPO</a>
              <a href="#s5-auth-pki" class="toc-link"><span class="toc-link-num">38.</span> Enterprise PKI: AD CS, Certificate Chains &amp; Kerberos</a>
              <a href="#s5-network-security" class="toc-link"><span class="toc-link-num">39.</span> Host Firewalls &amp; Zero Trust Microsegmentation</a>
              <a href="#s5-storage-encryption" class="toc-link"><span class="toc-link-num">40.</span> At-Rest Cryptography: BitLocker &amp; Linux LUKS2</a>
              <a href="#s5-audit-compliance" class="toc-link"><span class="toc-link-num">41.</span> SIEM Event Forwarding &amp; Compliance Auditing</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupS5Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 05 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-s5" class="toc-link"><span class="toc-link-num">42.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-s5" class="toc-link"><span class="toc-link-num">43.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-s5" class="toc-link"><span class="toc-link-num">44.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-s5" class="toc-link"><span class="toc-link-num">45.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 06: DISASTER RECOVERY & TRIAGE
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit6Server">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 06</span>
            <span class="toc-unit-title">Disaster Recovery &amp; Triage</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupS6Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Recovery &amp; Troubleshooting</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#s6-networking" class="toc-link"><span class="toc-link-num">46.</span> NIC Teaming &amp; Link Aggregation (LACP)</a>
              <a href="#s6-ports" class="toc-link"><span class="toc-link-num">47.</span> Enterprise Server Port Architectures</a>
              <a href="#s6-dr" class="toc-link"><span class="toc-link-num">48.</span> Disaster Recovery Planning: RTO, RPO &amp; Sites</a>
              <a href="#s6-backups" class="toc-link"><span class="toc-link-num">49.</span> 3-2-1 Backup Rule, VSS Snapshots &amp; GFS</a>
              <a href="#s6-triage" class="toc-link"><span class="toc-link-num">50.</span> Hardware Triage: BSOD, Kernel Panic &amp; POST</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupS6Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 06 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-s6" class="toc-link"><span class="toc-link-num">51.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-s6" class="toc-link"><span class="toc-link-num">52.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-s6" class="toc-link"><span class="toc-link-num">53.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-s6" class="toc-link"><span class="toc-link-num">54.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 07: DEEP PACKET TRACE & BUS FLOW
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit7ServerTrace">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 07</span>
            <span class="toc-unit-title">Packet Trace &amp; Bus Architecture</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#server-trace-packet" class="toc-link"><span class="toc-link-num">55.</span> End-to-End Enterprise PCIe &amp; Memory Bus Flow</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 08: PRACTICAL LAB MANUAL
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit8ServerLabs">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 08</span>
            <span class="toc-unit-title">Practical Hands-on Lab Manual</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#server-labs-manual" class="toc-link"><span class="toc-link-num">56.</span> 10 Hands-on Enterprise Server Lab Practicals</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 09: SIMULATORS & SERVER CLI SANDBOX
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit9ServerSims">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 09</span>
            <span class="toc-unit-title">Simulators &amp; Interactive Server CLI</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#server-simulators-tools" class="toc-link"><span class="toc-link-num">57.</span> Interactive Simulators &amp; Dual PowerShell/Bash CLI</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 10: COMPREHENSIVE FINAL EXAM BANK
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit10ServerExam">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 10</span>
            <span class="toc-unit-title">Final Examination Question Bank</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#server-exam-bank" class="toc-link"><span class="toc-link-num">58.</span> CO1&ndash;CO5 Mapped 10M &amp; 5M Question Bank</a>
          </div>
        </div>
      </div>

    </div>
"""

FULL_MAIN = f"""
  <main class="document-wrapper" id="documentWrapper">
    <!-- INJECTED UNITS 1 TO 6 -->
    {server_sections_ssm_u1.SERVER_UNIT1_HTML}
    {server_sections_ssm_u2.SERVER_UNIT2_HTML}
    {server_sections_ssm_u3.SERVER_UNIT3_HTML}
    {server_sections_ssm_u4.SERVER_UNIT4_HTML}
    {server_sections_ssm_u5.SERVER_UNIT5_HTML}
    {server_sections_ssm_u6.SERVER_UNIT6_HTML}

    <!-- DEEP PACKET TRACE -->
    {server_sections_ssm_trace.SERVER_TRACE_HTML}

    <!-- PRACTICAL LAB MANUAL -->
    {server_sections_ssm_labs.SERVER_LABS_HTML}

    <!-- SIMULATORS & SERVER CLI SANDBOX -->
    {server_sections_ssm_sims.SERVER_SIMS_HTML}

    <!-- EXAMINATION BANK -->
    {server_sections_ssm_exam.SERVER_EXAM_HTML}
  </main>
"""

# Client script matching IT Fundamentals gold standard
CLIENT_SCRIPT = """
    document.addEventListener('DOMContentLoaded', () => {
      // 1. Initialize Lucide Vector Icons
      if (window.lucide) {
        lucide.createIcons();
      }

      // 2. Reading Progress Bar
      const progressBar = document.getElementById('readingProgress');
      window.addEventListener('scroll', () => {
        const docElem = document.documentElement;
        const totalHeight = docElem.scrollHeight - docElem.clientHeight;
        if (totalHeight > 0 && progressBar) {
          const progress = (docElem.scrollTop / totalHeight) * 100;
          progressBar.style.width = progress + '%';
        }
      });

      // 3. MCQ Interactive Evaluation & Scoring Engine (30 MCQs per Unit)
      const unitScores = {
        'S1': 0, 'S2': 0, 'S3': 0, 'S4': 0, 'S5': 0, 'S6': 0,
        's1': 0, 's2': 0, 's3': 0, 's4': 0, 's5': 0, 's6': 0
      };
      const unitTotals = {
        'S1': 30, 'S2': 30, 'S3': 30, 'S4': 30, 'S5': 30, 'S6': 30,
        's1': 30, 's2': 30, 's3': 30, 's4': 30, 's5': 30, 's6': 30
      };

      function updateScoreBadge(unit) {
        const uUpper = unit.toUpperCase();
        const badge = document.getElementById(`mcqScore${uUpper}`) || 
                      document.getElementById(`mcqScore${unit}`) ||
                      document.getElementById(`mcqScoreU${uUpper}`);
        if (badge) {
          const total = unitTotals[unit] || 30;
          const score = unitScores[unit] || 0;
          badge.textContent = `Score: ${score} / ${total}`;
          if (score >= 24) {
            badge.style.background = 'rgba(34, 197, 94, 0.3)';
          }
        }
      }

      document.querySelectorAll('.mcq-card').forEach(card => {
        const unit = card.getAttribute('data-unit') || 'S1';
        const correctOpt = card.getAttribute('data-correct');
        const options = card.querySelectorAll('.mcq-option');
        const explanation = card.querySelector('.mcq-explanation');

        options.forEach(opt => {
          opt.addEventListener('click', () => {
            // If already answered, do not evaluate again
            if (card.classList.contains('answered')) return;
            card.classList.add('answered');

            const selectedOpt = opt.getAttribute('data-opt');
            if (selectedOpt === correctOpt) {
              opt.classList.add('correct-choice');
              unitScores[unit] = (unitScores[unit] || 0) + 1;
              const uUpper = unit.toUpperCase();
              if (unit !== uUpper) unitScores[uUpper] = unitScores[unit];
              updateScoreBadge(unit);
            } else {
              opt.classList.add('wrong-choice');
              // Highlight the actual correct option
              options.forEach(o => {
                if (o.getAttribute('data-opt') === correctOpt) {
                  o.classList.add('correct-choice');
                }
              });
            }

            if (explanation) {
              explanation.classList.add('visible');
            }
          });
        });
      });

      // 4. Interactive Terminal Block Engine: Comments Toggle & Smart Copy
      document.querySelectorAll('.terminal-block').forEach(term => {
        const btnToggle = term.querySelector('.btn-toggle-comments');
        const btnCopy = term.querySelector('.btn-copy-code');
        const preCode = term.querySelector('.code-pre code') || term.querySelector('.code-pre');

        // Toggle Comments
        if (btnToggle) {
          btnToggle.addEventListener('click', () => {
            term.classList.toggle('comments-hidden');
            const isHidden = term.classList.contains('comments-hidden');
            btnToggle.classList.toggle('active', !isHidden);
            const label = btnToggle.querySelector('span');
            if (label) {
              label.textContent = isHidden ? 'Comments' : 'Hide Comments';
            }
          });
        }

        // Smart Copy Button
        if (btnCopy && preCode) {
          btnCopy.addEventListener('click', async () => {
            let textToCopy = '';
            const isHidden = term.classList.contains('comments-hidden');

            if (isHidden) {
              const clone = preCode.cloneNode(true);
              clone.querySelectorAll('.code-comment').forEach(node => node.remove());
              textToCopy = clone.innerText.trim();
            } else {
              textToCopy = preCode.innerText.trim();
            }

            try {
              await navigator.clipboard.writeText(textToCopy);
              const label = btnCopy.querySelector('span');
              const origText = label ? label.textContent : 'Copy';
              if (label) label.textContent = 'Copied!';
              btnCopy.classList.add('active');
              setTimeout(() => {
                if (label) label.textContent = origText;
                btnCopy.classList.remove('active');
              }, 1800);
            } catch (err) {
              console.error('Clipboard copy failed:', err);
            }
          });
        }
      });

      // 5. Subjective Q&A Accordion Cards
      document.querySelectorAll('.subj-card').forEach(card => {
        const header = card.querySelector('.subj-header');
        if (header) {
          header.addEventListener('click', () => {
            card.classList.toggle('revealed');
          });
        }
      });

      // 6. Table of Contents Drawer & Layout Toggle
      const btnToggleTocLeft = document.getElementById('btnToggleTocLeft');
      const btnCloseToc = document.getElementById('btnCloseToc');
      const tocDrawer = document.getElementById('tocDrawer');

      function toggleToc() {
        const isOpen = tocDrawer.classList.toggle('open');
        document.body.classList.toggle('toc-open', isOpen);
        if (btnToggleTocLeft) btnToggleTocLeft.classList.toggle('active', isOpen);
      }

      if (btnToggleTocLeft) btnToggleTocLeft.addEventListener('click', toggleToc);
      if (btnCloseToc) btnCloseToc.addEventListener('click', toggleToc);

      // On initial desktop load, open ToC
      if (window.innerWidth > 1024) {
        document.body.classList.add('toc-open');
        if (tocDrawer) tocDrawer.classList.add('open');
        if (btnToggleTocLeft) btnToggleTocLeft.classList.add('active');
      }

      // 7. ToC Single-Accordion Architecture (Units & Groups)
      document.querySelectorAll('.toc-unit-header').forEach(btn => {
        btn.addEventListener('click', () => {
          const currentUnit = btn.closest('.toc-unit');
          const isCollapsed = currentUnit.classList.contains('collapsed');

          // Collapse other units
          document.querySelectorAll('.toc-unit').forEach(u => {
            if (u !== currentUnit) u.classList.add('collapsed');
          });

          // Toggle current unit
          currentUnit.classList.toggle('collapsed', !isCollapsed);
        });
      });

      document.querySelectorAll('.toc-group-header').forEach(btn => {
        btn.addEventListener('click', () => {
          const currentGroup = btn.closest('.toc-group');
          const parentUnit = currentGroup.closest('.toc-unit');
          const isCollapsed = currentGroup.classList.contains('collapsed');

          // Collapse other groups in the same unit
          if (parentUnit) {
            parentUnit.querySelectorAll('.toc-group').forEach(g => {
              if (g !== currentGroup) g.classList.add('collapsed');
            });
          }

          currentGroup.classList.toggle('collapsed', !isCollapsed);
        });
      });

      // Close drawer on link click on small screens
      document.querySelectorAll('.toc-link').forEach(link => {
        link.addEventListener('click', () => {
          if (window.innerWidth <= 1024) {
            if (tocDrawer) tocDrawer.classList.remove('open');
            document.body.classList.remove('toc-open');
            if (btnToggleTocLeft) btnToggleTocLeft.classList.remove('active');
          }
        });
      });

      // 8. ScrollSpy & Dynamic Accordion Expansion
      const trackedSections = [
        's1-hardware', 's1-cpu', 's1-ram', 's1-expansion', 's1-power-cooling',
        'practice-mcq-s1', 'practice-subj-short-s1', 'practice-subj-long-s1', 'mcq-answer-key-s1',
        's2-os-install', 's2-partitioning', 's2-virt', 's2-memory-ballooning', 's2-virtual-networking',
        'practice-mcq-s2', 'practice-subj-short-s2', 'practice-subj-long-s2', 'mcq-answer-key-s2',
        's3-ad-roles', 's3-network-services', 's3-web-app', 's3-patching', 's3-clustering',
        'practice-mcq-s3', 'practice-subj-short-s3', 'practice-subj-long-s3', 'mcq-answer-key-s3',
        's4-storage-arch', 's4-protocols', 's4-raid', 's4-write-penalty', 's4-capacity',
        'practice-mcq-s4', 'practice-subj-short-s4', 'practice-subj-long-s4', 'mcq-answer-key-s4',
        's5-hardening', 's5-auth-pki', 's5-network-security', 's5-storage-encryption', 's5-audit-compliance',
        'practice-mcq-s5', 'practice-subj-short-s5', 'practice-subj-long-s5', 'mcq-answer-key-s5',
        's6-networking', 's6-ports', 's6-dr', 's6-backups', 's6-triage',
        'practice-mcq-s6', 'practice-subj-short-s6', 'practice-subj-long-s6', 'mcq-answer-key-s6',
        'server-trace-packet', 'server-labs-manual', 'server-simulators-tools', 'server-exam-bank'
      ];

      const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px',
        threshold: 0
      };

      const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            const activeLink = document.querySelector(`.toc-link[href="#${id}"]`);

            if (activeLink) {
              document.querySelectorAll('.toc-link').forEach(l => l.classList.remove('active'));
              activeLink.classList.add('active');

              // Automatically expand parent group & unit, and collapse siblings
              const parentGroup = activeLink.closest('.toc-group');
              const parentUnit = activeLink.closest('.toc-unit');

              if (parentUnit) {
                document.querySelectorAll('.toc-unit').forEach(u => {
                  if (u !== parentUnit) u.classList.add('collapsed');
                  else u.classList.remove('collapsed');
                });
              }

              if (parentGroup && parentUnit) {
                parentUnit.querySelectorAll('.toc-group').forEach(g => {
                  if (g !== parentGroup) g.classList.add('collapsed');
                  else g.classList.remove('collapsed');
                });
              }
            }
          }
        });
      }, observerOptions);

      trackedSections.forEach(id => {
        const el = document.getElementById(id);
        if (el) scrollObserver.observe(el);
      });

      // 9. Live Search Filter
      const searchInput = document.getElementById('quickSearchInput');
      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          const query = e.target.value.toLowerCase().trim();
          if (!query) {
            document.querySelectorAll('.toc-link, .doc-page, .mcq-card, .subj-card').forEach(el => el.style.display = '');
            return;
          }

          document.querySelectorAll('.toc-link').forEach(item => {
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(query) ? '' : 'none';
          });

          // Expand all groups and units during search
          document.querySelectorAll('.toc-unit, .toc-group').forEach(el => el.classList.remove('collapsed'));
        });
      }

      // 10. Theme Cycle Switcher (Light / Sepia / Dark)
      const btnThemeToggle = document.getElementById('btnThemeToggle');
      const themeLabel = document.getElementById('themeLabel');
      const themes = ['light', 'sepia', 'dark'];
      let currentThemeIdx = 0;

      if (btnThemeToggle) {
        btnThemeToggle.addEventListener('click', () => {
          currentThemeIdx = (currentThemeIdx + 1) % themes.length;
          const nextTheme = themes[currentThemeIdx];
          document.documentElement.setAttribute('data-theme', nextTheme);
          if (themeLabel) {
            themeLabel.textContent = nextTheme.charAt(0).toUpperCase() + nextTheme.slice(1);
          }
        });
      }
    });
"""

FULL_HTML = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Server Administration (CSC204) — Master Engineering &amp; Knowledge Portal</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:ital,wght@0,400;0,500;0,700;0,800;1,400&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
{CSS_CONTENT}
  </style>
</head>
<body>
  <!-- Reading Progress Bar -->
  <div id="readingProgress" class="reading-progress-bar"></div>

  <!-- Top Toolbar -->
  <header class="top-toolbar">
    <div class="toolbar-left">
      <button class="btn-tool active" id="btnToggleTocLeft" title="Toggle Table of Contents Menu">
        <i data-lucide="menu" style="width: 15px; height: 15px;"></i>
        <span>ToC</span>
      </button>

      <span class="course-badge">
        <i data-lucide="server" style="width: 14px; height: 14px;"></i>
        SERVER ADMINISTRATION • CSC204
      </span>

      <!-- Sister Portal Quick Pills -->
      <a href="../index.html" class="btn-tool" title="Back to Master University Hub" style="text-decoration:none;">
        <i data-lucide="home" style="width: 14px; height: 14px;"></i>
        <span>Hub</span>
      </a>
      <a href="../IT_Fundamentals_Portal/index.html" class="btn-tool" title="IT Fundamentals Portal" style="text-decoration:none;">
        <i data-lucide="monitor" style="width: 14px; height: 14px;"></i>
        <span>IT Fund</span>
      </a>
      <a href="../Cloud_Administration_Portal/index.html" class="btn-tool" title="Cloud Administration Portal" style="text-decoration:none;">
        <i data-lucide="cloud" style="width: 14px; height: 14px;"></i>
        <span>Cloud</span>
      </a>
    </div>

    <div class="toolbar-right">
      <div class="search-box">
        <i data-lucide="search" class="search-icon" style="width: 15px; height: 15px;"></i>
        <input type="text" id="quickSearchInput" class="search-input" placeholder="Search AD, RAID, PKI, PowerShell, Linux...">
      </div>

      <button class="btn-tool" id="btnThemeToggle" title="Cycle themes (Light / Sepia / Dark)">
        <i data-lucide="sun-moon" style="width: 15px; height: 15px;"></i>
        <span id="themeLabel">Light</span>
      </button>
    </div>
  </header>

  <!-- Left Sidebar ToC Drawer -->
  <aside class="toc-drawer open" id="tocDrawer">
{TOC_HTML}
  </aside>

  <!-- Main Content Area -->
{FULL_MAIN}

  <!-- Scripts -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
{CLIENT_SCRIPT}
  </script>
</body>
</html>
"""

# Write to target path
out_path = os.path.join("Server_Administration_Portal", "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(FULL_HTML)

print(f"Master Server Administration Portal assembled successfully at {out_path}!")
print(f"File size: {len(FULL_HTML):,} bytes | Total lines: {len(FULL_HTML.splitlines()):,}")
