# -*- coding: utf-8 -*-
"""
Master Assembler for Cloud Administration (AWS) Knowledge Portal
Generates d:\CU - Teach\Cloud_Administration_Portal\index.html
SSM Engineering Standard Gold Standard Architecture matching IT Fundamentals
"""

import os
import re

# Import the core unit modules
import cloud_sections_ssm_u1
import cloud_sections_ssm_u2
import cloud_sections_ssm_u3
import cloud_sections_ssm_u4
import cloud_sections_ssm_u5
import cloud_sections_ssm_u6
import cloud_sections_ssm_trace
import cloud_sections_ssm_labs
import cloud_sections_ssm_sims
import cloud_sections_ssm_exam

# Load CSS template
with open('_portal_generators/portal_style.css', 'r', encoding='utf-8') as f:
    CSS_CONTENT = f.read()

# Build ToC HTML exactly matching IT Fundamentals two-tier accordion structure
TOC_HTML = """
    <div class="toc-header">
      <div class="toc-title">
        <i data-lucide="cloud" style="width: 18px; height: 18px; color: var(--primary);"></i>
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
        <a href="../Server_Administration_Portal/index.html" class="toc-link" style="display: flex; align-items: center; gap: 0.5rem; font-size: 12px; padding: 0.35rem 0.5rem; border-radius: 6px; text-decoration: none; color: var(--text-muted);">
          <span>🖥️</span> <strong>Server Administration (CSC204)</strong>
        </a>
      </div>
    </div>

    <div class="toc-content">

      <!-- ==========================================
           UNIT 01: CLOUD CONCEPTS & GLOBAL INFRA
           ========================================== -->
      <div class="toc-unit" id="tocUnit1Cloud">
        <button class="toc-unit-header" type="button" aria-expanded="true">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 01</span>
            <span class="toc-unit-title">Cloud Concepts &amp; Global Infra</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupC1Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Core Cloud Concepts</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#c1-concepts" class="toc-link active"><span class="toc-link-num">01.</span> Delivery Models: IaaS, PaaS, SaaS</a>
              <a href="#c1-virt" class="toc-link"><span class="toc-link-num">02.</span> Virtualization &amp; Hypervisors</a>
              <a href="#c1-infra" class="toc-link"><span class="toc-link-num">03.</span> AWS Global Infrastructure</a>
              <a href="#c1-shared" class="toc-link"><span class="toc-link-num">04.</span> Shared Responsibility Model</a>
              <a href="#c1-econ" class="toc-link"><span class="toc-link-num">05.</span> Cloud Economics &amp; TCO Models</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupC1Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 01 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-c1" class="toc-link"><span class="toc-link-num">06.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-c1" class="toc-link"><span class="toc-link-num">07.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-c1" class="toc-link"><span class="toc-link-num">08.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-c1" class="toc-link"><span class="toc-link-num">09.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 02: CLOUD COMPUTE & VIRTUALIZATION
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit2Cloud">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 02</span>
            <span class="toc-unit-title">Cloud Compute &amp; Virtualization</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupC2Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Compute Architectures</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#c2-ec2" class="toc-link"><span class="toc-link-num">10.</span> Amazon EC2 Instance Types</a>
              <a href="#c2-pricing" class="toc-link"><span class="toc-link-num">11.</span> EC2 Pricing &amp; Capacity Strategy</a>
              <a href="#c2-nitro" class="toc-link"><span class="toc-link-num">12.</span> AWS Nitro Hardware Acceleration</a>
              <a href="#c2-scaling" class="toc-link"><span class="toc-link-num">13.</span> Elastic Load Balancing &amp; ASG</a>
              <a href="#c2-serverless" class="toc-link"><span class="toc-link-num">14.</span> Serverless Compute: AWS Lambda</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupC2Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 02 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-c2" class="toc-link"><span class="toc-link-num">15.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-c2" class="toc-link"><span class="toc-link-num">16.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-c2" class="toc-link"><span class="toc-link-num">17.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-c2" class="toc-link"><span class="toc-link-num">18.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 03: CLOUD STORAGE & CDN SERVICES
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit3Cloud">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 03</span>
            <span class="toc-unit-title">Cloud Storage &amp; Content Delivery</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupC3Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Storage Subsystems</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#c3-s3" class="toc-link"><span class="toc-link-num">19.</span> Amazon S3 Architecture &amp; Tiers</a>
              <a href="#c3-s3deep" class="toc-link"><span class="toc-link-num">20.</span> S3 Versioning, Locking &amp; Lifecycle</a>
              <a href="#c3-ebs" class="toc-link"><span class="toc-link-num">21.</span> Amazon Elastic Block Store (EBS)</a>
              <a href="#c3-efs" class="toc-link"><span class="toc-link-num">22.</span> Elastic File System &amp; FSx Lustre</a>
              <a href="#c3-cdn" class="toc-link"><span class="toc-link-num">23.</span> Amazon CloudFront &amp; Edge Security</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupC3Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 03 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-c3" class="toc-link"><span class="toc-link-num">24.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-c3" class="toc-link"><span class="toc-link-num">25.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-c3" class="toc-link"><span class="toc-link-num">26.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-c3" class="toc-link"><span class="toc-link-num">27.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 04: CLOUD NETWORKING & VPC
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit4Cloud">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 04</span>
            <span class="toc-unit-title">Cloud Networking &amp; VPC</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupC4Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • VPC Architecture</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#c4-vpc" class="toc-link"><span class="toc-link-num">28.</span> Amazon VPC Subnet Topologies</a>
              <a href="#c4-routing" class="toc-link"><span class="toc-link-num">29.</span> Route Tables, IGW &amp; NAT Gateways</a>
              <a href="#c4-security" class="toc-link"><span class="toc-link-num">30.</span> Security Groups vs Network ACLs</a>
              <a href="#c4-peering" class="toc-link"><span class="toc-link-num">31.</span> VPC Peering &amp; Transit Gateway</a>
              <a href="#c4-hybrid" class="toc-link"><span class="toc-link-num">32.</span> Site-to-Site VPN &amp; Direct Connect</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupC4Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 04 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-c4" class="toc-link"><span class="toc-link-num">33.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-c4" class="toc-link"><span class="toc-link-num">34.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-c4" class="toc-link"><span class="toc-link-num">35.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-c4" class="toc-link"><span class="toc-link-num">36.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 05: CLOUD DATABASES & ANALYTICS
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit5Cloud">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 05</span>
            <span class="toc-unit-title">Cloud Databases &amp; Analytics</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupC5Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Database Architectures</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#c5-rds" class="toc-link"><span class="toc-link-num">37.</span> Amazon RDS &amp; Multi-AZ Replication</a>
              <a href="#c5-aurora" class="toc-link"><span class="toc-link-num">38.</span> Amazon Aurora Storage Architecture</a>
              <a href="#c5-dynamo" class="toc-link"><span class="toc-link-num">39.</span> DynamoDB Partitioning &amp; Global Tables</a>
              <a href="#c5-cache" class="toc-link"><span class="toc-link-num">40.</span> ElastiCache (Redis / Memcached)</a>
              <a href="#c5-bigdata" class="toc-link"><span class="toc-link-num">41.</span> Cloud Analytics: Redshift, Athena, EMR</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupC5Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 05 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-c5" class="toc-link"><span class="toc-link-num">42.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-c5" class="toc-link"><span class="toc-link-num">43.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-c5" class="toc-link"><span class="toc-link-num">44.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-c5" class="toc-link"><span class="toc-link-num">45.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 06: SECURITY, IAM & COMPLIANCE
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit6Cloud">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 06</span>
            <span class="toc-unit-title">Cloud Security, IAM &amp; WAF</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupC6Core">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Identity &amp; Defense</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#c6-iam" class="toc-link"><span class="toc-link-num">46.</span> IAM Policies, Roles &amp; STS Tokens</a>
              <a href="#c6-kms" class="toc-link"><span class="toc-link-num">47.</span> AWS KMS Envelope Encryption</a>
              <a href="#c6-monitoring" class="toc-link"><span class="toc-link-num">48.</span> CloudWatch &amp; CloudTrail Auditing</a>
              <a href="#c6-defense" class="toc-link"><span class="toc-link-num">49.</span> GuardDuty, Security Hub &amp; Inspector</a>
              <a href="#c6-waf-framework" class="toc-link"><span class="toc-link-num">50.</span> AWS WAF &amp; Well-Architected Framework</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupC6Practice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 06 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-c6" class="toc-link"><span class="toc-link-num">51.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-c6" class="toc-link"><span class="toc-link-num">52.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-c6" class="toc-link"><span class="toc-link-num">53.</span> Architectural Scenarios (4 Sets)</a>
              <a href="#mcq-answer-key-c6" class="toc-link"><span class="toc-link-num">54.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 07: DEEP PACKET TRACE & PROTOCOL
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit7CloudTrace">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 07</span>
            <span class="toc-unit-title">Packet Trace &amp; Silicon Architecture</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#cloud-trace-packet" class="toc-link"><span class="toc-link-num">55.</span> End-to-End AWS VPC Silicon Packet Flow</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 08: PRACTICAL LAB MANUAL
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit8CloudLabs">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 08</span>
            <span class="toc-unit-title">Practical Hands-on Lab Manual</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#cloud-labs-manual" class="toc-link"><span class="toc-link-num">56.</span> 10 Hands-on Enterprise AWS Lab Practicals</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 09: SIMULATORS & AWS CLI SANDBOX
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit9CloudSims">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 09</span>
            <span class="toc-unit-title">Simulators &amp; Interactive AWS CLI</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#cloud-simulators-tools" class="toc-link"><span class="toc-link-num">57.</span> Interactive Simulators &amp; Live CLI Sandbox</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 10: COMPREHENSIVE FINAL EXAM BANK
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit10CloudExam">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 10</span>
            <span class="toc-unit-title">Final Examination Question Bank</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#cloud-exam-bank" class="toc-link"><span class="toc-link-num">58.</span> CO1&ndash;CO5 Mapped 10M &amp; 5M Question Bank</a>
          </div>
        </div>
      </div>

    </div>
"""

FULL_MAIN = f"""
  <main class="document-wrapper" id="documentWrapper">
    <!-- INJECTED UNITS 1 TO 6 -->
    {cloud_sections_ssm_u1.CLOUD_UNIT1_HTML}
    {cloud_sections_ssm_u2.CLOUD_UNIT2_HTML}
    {cloud_sections_ssm_u3.CLOUD_UNIT3_HTML}
    {cloud_sections_ssm_u4.CLOUD_UNIT4_HTML}
    {cloud_sections_ssm_u5.CLOUD_UNIT5_HTML}
    {cloud_sections_ssm_u6.CLOUD_UNIT6_HTML}

    <!-- DEEP PACKET TRACE -->
    {cloud_sections_ssm_trace.CLOUD_TRACE_HTML}

    <!-- PRACTICAL LAB MANUAL -->
    {cloud_sections_ssm_labs.CLOUD_LABS_HTML}

    <!-- SIMULATORS & AWS CLI SANDBOX -->
    {cloud_sections_ssm_sims.CLOUD_SIMS_HTML}

    <!-- EXAMINATION BANK -->
    {cloud_sections_ssm_exam.CLOUD_EXAM_HTML}
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
        'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0,
        'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0
      };
      const unitTotals = {
        'C1': 30, 'C2': 30, 'C3': 30, 'C4': 30, 'C5': 30, 'C6': 30,
        'c1': 30, 'c2': 30, 'c3': 30, 'c4': 30, 'c5': 30, 'c6': 30
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
        const unit = card.getAttribute('data-unit') || 'C1';
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
        'c1-concepts', 'c1-virt', 'c1-infra', 'c1-shared', 'c1-econ',
        'practice-mcq-c1', 'practice-subj-short-c1', 'practice-subj-long-c1', 'mcq-answer-key-c1',
        'c2-ec2', 'c2-pricing', 'c2-nitro', 'c2-scaling', 'c2-serverless',
        'practice-mcq-c2', 'practice-subj-short-c2', 'practice-subj-long-c2', 'mcq-answer-key-c2',
        'c3-s3', 'c3-s3deep', 'c3-ebs', 'c3-efs', 'c3-cdn',
        'practice-mcq-c3', 'practice-subj-short-c3', 'practice-subj-long-c3', 'mcq-answer-key-c3',
        'c4-vpc', 'c4-routing', 'c4-security', 'c4-peering', 'c4-hybrid',
        'practice-mcq-c4', 'practice-subj-short-c4', 'practice-subj-long-c4', 'mcq-answer-key-c4',
        'c5-rds', 'c5-aurora', 'c5-dynamo', 'c5-cache', 'c5-bigdata',
        'practice-mcq-c5', 'practice-subj-short-c5', 'practice-subj-long-c5', 'mcq-answer-key-c5',
        'c6-iam', 'c6-kms', 'c6-monitoring', 'c6-defense', 'c6-waf-framework',
        'practice-mcq-c6', 'practice-subj-short-c6', 'practice-subj-long-c6', 'mcq-answer-key-c6',
        'cloud-trace-packet', 'cloud-labs-manual', 'cloud-simulators-tools', 'cloud-exam-bank'
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
  <title>Cloud Administration (AWS) — Master Engineering &amp; Knowledge Portal</title>
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
        <i data-lucide="cloud" style="width: 14px; height: 14px;"></i>
        CLOUD ADMINISTRATION (AWS) • CSC205
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
      <a href="../Server_Administration_Portal/index.html" class="btn-tool" title="Server Administration" style="text-decoration:none;">
        <i data-lucide="server" style="width: 14px; height: 14px;"></i>
        <span>Server</span>
      </a>
    </div>

    <div class="toolbar-right">
      <div class="search-box">
        <i data-lucide="search" class="search-icon" style="width: 15px; height: 15px;"></i>
        <input type="text" id="quickSearchInput" class="search-input" placeholder="Search EC2, VPC, IAM, S3, Aurora...">
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
out_path = os.path.join("Cloud_Administration_Portal", "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(FULL_HTML)

print(f"Master Cloud Administration Portal assembled successfully at {out_path}!")
print(f"File size: {len(FULL_HTML):,} bytes | Total lines: {len(FULL_HTML.splitlines()):,}")
