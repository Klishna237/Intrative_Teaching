# -*- coding: utf-8 -*-
"""
Assembles the complete master-grade IT_Fundamentals_Portal/index.html
Fusing the gold standard styling and 32 articles from external_it_fundamentals.html
with Unit 1 (Hardware), Unit 2 (Networking), Unit 3 (Mobile/Printing),
Unit 5 (SOHO Security), Unit 6 (10 Labs), Unit 7 (Simulators & Dual CLI),
and Unit 8 (Comprehensive Exam Bank).
"""

import re
from it_sections_u1 import IT_UNIT1_HTML
from it_sections_u2 import IT_UNIT2_HTML
from it_sections_u3 import IT_UNIT3_HTML
from it_sections_u4 import IT_UNIT4_HTML
from it_sections_u5 import IT_UNIT5_HTML
from it_sections_u6 import IT_UNIT6_HTML
from it_sections_soho import IT_SOHO_HTML
import os
from it_sections_labs import IT_LABS_HTML
from it_sections_sims import IT_SIMS_HTML
from it_sections_exam import IT_EXAM_HTML

ext_path = '_portal_generators/external_it_fundamentals.html' if os.path.exists('_portal_generators/external_it_fundamentals.html') else 'external_it_fundamentals.html'
with open(ext_path, 'r', encoding='utf-8', errors='ignore') as f:
    ext_html = f.read()

# 1. Extract CSS and Head
head_m = re.search(r'<head>(.*?)</head>', ext_html, re.DOTALL)
head_content = head_m.group(1) if head_m else ""
head_content = re.sub(r'<meta name="viewport"[^>]*>', "", head_content, flags=re.I)
head_content = re.sub(r'<title>.*?</title>', '', head_content, flags=re.DOTALL)
head_content = re.sub(r'<meta\s+charset=[^>]+>', '', head_content)
head_content = re.sub(r'<meta name="viewport"[^>]*>', "", head_content, flags=re.I)

# 2. Extract Engineering Standard articles from external_it_fundamentals.html
# We want sec1 through sec13 (Unit 1 in Engineering Standard, now part of Unit 4)
# practice-mcq-u1, practice-subj-short-u1, practice-subj-long-u1
# sec14 through sec27 (Unit 2 in Engineering Standard, now part of Unit 4 Security)
# practice-mcq-u2, practice-subj-short-u2, practice-subj-long-u2
# sec28 through sec40 (Unit 3 in Engineering Standard, now part of Unit 5 Linux)
# practice-mcq-u3, practice-subj-short-u3, practice-subj-long-u3

main_m = re.search(r'<main class="document-wrapper">(.*?)</main>', ext_html, re.DOTALL)
ext_main = main_m.group(1) if main_m else ""

# 3. Build the Master ToC Drawer Sidebar
TOC_HTML = """
    <div class="toc-header">
      <div class="toc-title">
        <i data-lucide="bookmark" style="width: 18px; height: 18px; color: var(--primary);"></i>
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
        <a href="../Cloud_Administration_Portal/index.html" class="toc-link" style="display: flex; align-items: center; gap: 0.5rem; font-size: 12px; padding: 0.35rem 0.5rem; border-radius: 6px; text-decoration: none; color: var(--text-muted);">
          <span>☁️</span> <strong>Cloud Administration (AWS)</strong>
        </a>
        <a href="../Server_Administration_Portal/index.html" class="toc-link" style="display: flex; align-items: center; gap: 0.5rem; font-size: 12px; padding: 0.35rem 0.5rem; border-radius: 6px; text-decoration: none; color: var(--text-muted);">
          <span>🖥️</span> <strong>Server Administration</strong>
        </a>
      </div>
    </div>

    <div class="toc-content">

      <!-- ==========================================
           UNIT 01: PC HARDWARE AND CONFIGURATION
           ========================================== -->
      <div class="toc-unit" id="tocUnit1HW">
        <button class="toc-unit-header" type="button" aria-expanded="true">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 01</span>
            <span class="toc-unit-title">PC Hardware and Configuration</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupHwCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Core PC Hardware &amp; Connectors</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it1-formfactors" class="toc-link active"><span class="toc-link-num">01.</span> Motherboards, Form Factors &amp; Standoffs</a>
              <a href="#it1-chipset" class="toc-link"><span class="toc-link-num">02.</span> Chipset Architectures &amp; PCIe 5.0 Bus</a>
              <a href="#it1-cpu" class="toc-link"><span class="toc-link-num">03.</span> CPU Sockets (LGA/PGA) &amp; Cache Architecture</a>
              <a href="#it1-ram" class="toc-link"><span class="toc-link-num">04.</span> Dynamic RAM (DDR4/DDR5) &amp; Latency Math</a>
              <a href="#it1-psu" class="toc-link"><span class="toc-link-num">05.</span> Power Supplies (SMPS) &amp; 80 Plus Efficiency</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupHwPractice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 01 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-u1-hw" class="toc-link"><span class="toc-link-num">06.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-u1-hw" class="toc-link"><span class="toc-link-num">07.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-u1-hw" class="toc-link"><span class="toc-link-num">08.</span> Analytical &amp; Scenario Problems (4 Sets)</a>
              <a href="#mcq-answer-key-u1-hw" class="toc-link"><span class="toc-link-num">09.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 02: NETWORKING FUNDAMENTALS
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit2Net">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 02</span>
            <span class="toc-unit-title">Networking Fundamentals</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupNetCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Topologies, Hardware &amp; Protocols</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it2-topologies" class="toc-link"><span class="toc-link-num">10.</span> Network Types (LAN, WAN, PAN) &amp; Topologies</a>
              <a href="#it2-cables" class="toc-link"><span class="toc-link-num">11.</span> Structured Cabling (Cat5e-8, Fiber) &amp; T568A/B</a>
              <a href="#it2-switching" class="toc-link"><span class="toc-link-num">12.</span> Layer 2 Switching, Routing &amp; Domain Boundaries</a>
              <a href="#it2-encapsulation" class="toc-link"><span class="toc-link-num">13.</span> OSI 7-Layer vs TCP/IP Encapsulation</a>
              <a href="#it2-subnetting" class="toc-link"><span class="toc-link-num">14.</span> IPv4 CIDR Subnetting, IPv6 &amp; Virtualization/Cloud</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupNetPractice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 02 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-u2-net" class="toc-link"><span class="toc-link-num">15.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-u2-net" class="toc-link"><span class="toc-link-num">16.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-u2-net" class="toc-link"><span class="toc-link-num">17.</span> Analytical &amp; Scenario Problems (4 Sets)</a>
              <a href="#mcq-answer-key-u2-net" class="toc-link"><span class="toc-link-num">18.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 03: MOBILE AND PERIPHERAL DEVICES
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit3Dev">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 03</span>
            <span class="toc-unit-title">Mobile and Peripheral Devices</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupDevCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Devices, Printers &amp; SOHO Wireless</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it3-mobile" class="toc-link"><span class="toc-link-num">19.</span> Mobile Hardware, Laptops &amp; Upgrades</a>
              <a href="#it3-peripherals" class="toc-link"><span class="toc-link-num">20.</span> USB4, Thunderbolt 4 &amp; Peripheral Buses</a>
              <a href="#it3-laser" class="toc-link"><span class="toc-link-num">21.</span> Laser Printing Engine &amp; Defect Analysis</a>
              <a href="#it3-storage" class="toc-link"><span class="toc-link-num">22.</span> Storage Devices (NVMe M.2 vs SATA SSD)</a>
              <a href="#it3-printing-types" class="toc-link"><span class="toc-link-num">23.</span> Inkjet, Thermal, Impact &amp; Wireless Configuration</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupDevPractice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 03 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-u3-dev" class="toc-link"><span class="toc-link-num">24.</span> Self-Testing Bank: 30 MCQs</a>
              <a href="#practice-subj-short-u3-dev" class="toc-link"><span class="toc-link-num">25.</span> Short Conceptual Questions (5 Sets)</a>
              <a href="#practice-subj-long-u3-dev" class="toc-link"><span class="toc-link-num">26.</span> Analytical &amp; Scenario Problems (4 Sets)</a>
              <a href="#mcq-answer-key-u3-dev" class="toc-link"><span class="toc-link-num">27.</span> Master Answer Key Table</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 04: SECURITY AND SYSTEM PROTECTION
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit4NT">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 04</span>
            <span class="toc-unit-title">Security and System Protection</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupNTCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • OS Architecture &amp; Subsystems</span>
                <span class="toc-group-count">8 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#sec1" class="toc-link"><span class="toc-link-num">01.</span> Windows NT Design Goals &amp; OS Editions</a>
              <a href="#sec2" class="toc-link"><span class="toc-link-num">02.</span> Layered NT Architecture Stack</a>
              <a href="#sec3" class="toc-link"><span class="toc-link-num">03.</span> User Mode vs Kernel Mode Protection</a>
              <a href="#sec4" class="toc-link"><span class="toc-link-num">04.</span> The 8 NT Executive Managers</a>
              <a href="#sec5" class="toc-link"><span class="toc-link-num">05.</span> Microkernel &amp; Interrupt Request Levels (IRQLs)</a>
              <a href="#sec6" class="toc-link"><span class="toc-link-num">06.</span> Hardware Abstraction Layer (HAL)</a>
              <a href="#sec8" class="toc-link"><span class="toc-link-num">08.</span> I/O Stack &amp; IRP Dispatch Architecture</a>
              <a href="#sec9" class="toc-link"><span class="toc-link-num">09.</span> Process Launch &amp; Memory Allocation</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupNTSec">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Security, Filesystems &amp; Registry</span>
                <span class="toc-group-count">8 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#sec14" class="toc-link"><span class="toc-link-num">14.</span> Windows Security Subsystem (LSA &amp; SRM)</a>
              <a href="#sec15" class="toc-link"><span class="toc-link-num">15.</span> User Accounts &amp; SID Architecture</a>
              <a href="#sec16" class="toc-link"><span class="toc-link-num">16.</span> Authentication: Kerberos v5 vs NTLMv2</a>
              <a href="#sec18" class="toc-link"><span class="toc-link-num">18.</span> Access Control (Tokens, DACLs &amp; SACLs)</a>
              <a href="#sec20" class="toc-link"><span class="toc-link-num">20.</span> Defender, UAC &amp; Integrity Levels</a>
              <a href="#sec26-sysfiles" class="toc-link"><span class="toc-link-num">26.</span> Core Windows System Files (.dll, .sys, .exe)</a>
              <a href="#sec27-registry" class="toc-link"><span class="toc-link-num">27.</span> Windows Registry Architecture &amp; Hives</a>
              <a href="#sec11" class="toc-link"><span class="toc-link-num">11.</span> NTFS File Save Path &amp; Permissions</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupNTPractice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART III • Unit 04 Assessment</span>
                <span class="toc-group-count">78 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-u1" class="toc-link"><span class="toc-link-num">U4.</span> Core OS MCQ Bank (30 Qs)</a>
              <a href="#practice-subj-short-u1" class="toc-link"><span class="toc-link-num">U4.</span> OS Architecture Conceptual Q&amp;A</a>
              <a href="#practice-subj-long-u1" class="toc-link"><span class="toc-link-num">U4.</span> System Protection Scenario Problems</a>
              <a href="#practice-mcq-u2" class="toc-link"><span class="toc-link-num">U4.</span> Security Subsystem MCQ Bank (30 Qs)</a>
              <a href="#practice-subj-short-u2" class="toc-link"><span class="toc-link-num">U4.</span> Access Control Conceptual Q&amp;A</a>
              <a href="#practice-subj-long-u2" class="toc-link"><span class="toc-link-num">U4.</span> Privilege Escalation Scenarios</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 05: OS TROUBLESHOOTING AND COMMAND LINE
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit5Linux">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 05</span>
            <span class="toc-unit-title">OS Troubleshooting &amp; Command Line</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupOSTrouble">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • CLI Diagnostics &amp; OS Triage</span>
                <span class="toc-group-count">4 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#sec13" class="toc-link"><span class="toc-link-num">01.</span> Administrative CLI (CMD &amp; PowerShell)</a>
              <a href="#sec28-bash" class="toc-link"><span class="toc-link-num">02.</span> Linux &amp; macOS Architecture Overview</a>
              <a href="#sec29-syntax" class="toc-link"><span class="toc-link-num">03.</span> CLI File Permissions &amp; chmod Execution</a>
              <a href="#it5-soho-gateway" class="toc-link"><span class="toc-link-num">04.</span> Windows Network Triage &amp; IP Configuration</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupLinuxPractice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Unit 05 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-u5" class="toc-link"><span class="toc-link-num">05.</span> OS Troubleshooting MCQ Bank (30 Qs)</a>
              <a href="#practice-subj-short-u5" class="toc-link"><span class="toc-link-num">06.</span> Command Line Conceptual Q&amp;A</a>
              <a href="#practice-subj-long-u5" class="toc-link"><span class="toc-link-num">07.</span> OS Triage &amp; Recovery Scenarios</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 06: SCRIPTING, REMOTE SUPPORT, AND SAFETY
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit6Script">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 06</span>
            <span class="toc-unit-title">Scripting, Remote Support &amp; Safety</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupScriptCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Mobile Security &amp; Scripting</span>
                <span class="toc-group-count">6 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it6-mobile-security" class="toc-link"><span class="toc-link-num">01.</span> Mobile OS Security &amp; Sandboxing</a>
              <a href="#it6-scripting-languages" class="toc-link"><span class="toc-link-num">02.</span> Batch, PowerShell &amp; Python 3 Basics</a>
              <a href="#sec31-arith" class="toc-link"><span class="toc-link-num">03.</span> Bash Arithmetic, Input &amp; Arrays</a>
              <a href="#sec34-cond" class="toc-link"><span class="toc-link-num">04.</span> Conditional Testing &amp; Loops</a>
              <a href="#sec37-func" class="toc-link"><span class="toc-link-num">05.</span> Functions, Scope &amp; Signal Traps</a>
              <a href="#sec40-progs" class="toc-link"><span class="toc-link-num">06.</span> 10 Production Automation Problem Scripts</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupPerimeterCore">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Remote Support, Safety &amp; Exams</span>
                <span class="toc-group-count">3 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it6-remote-support-communication" class="toc-link"><span class="toc-link-num">07.</span> Remote Access Tools &amp; Professionalism</a>
              <a href="#it6-safety-operational" class="toc-link"><span class="toc-link-num">08.</span> Safety, ESD Controls &amp; 3-2-1 Backups</a>
              <a href="#practice-mcq-u6" class="toc-link"><span class="toc-link-num">09.</span> Unit 06 Practice Examination Bank (39 Problems)</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           HANDS-ON LABORATORY MANUAL
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnitItLabs">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <i data-lucide="flask-conical" style="width: 15px; height: 15px; color: #10b981; margin-right: 0.35rem;"></i>
            <span class="toc-unit-title">Practical Hands-on Lab Manual</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#it-labs" class="toc-link"><span class="toc-link-num">48.</span> 10 Practical Experiments &amp; Viva Voce</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           ENGINEERING SIMULATORS & DUAL CLI
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnitItSims">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <i data-lucide="terminal" style="width: 15px; height: 15px; color: #f59e0b; margin-right: 0.35rem;"></i>
            <span class="toc-unit-title">Engineering Simulators &amp; Dual CLI</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#it-sims" class="toc-link"><span class="toc-link-num">49.</span> Calculators &amp; Interactive Terminal</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           COMPREHENSIVE FINAL EXAM BANK
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnitItExam">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <i data-lucide="award" style="width: 15px; height: 15px; color: #ec4899; margin-right: 0.35rem;"></i>
            <span class="toc-unit-title">Master Comprehensive Exam Bank</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#it-exam" class="toc-link"><span class="toc-link-num">50.</span> CO1&ndash;CO5 Mapped 10M &amp; 5M Question Bank</a>
          </div>
        </div>
      </div>

    </div>
"""

# 4. Assemble the Main Document
FULL_MAIN = f"""
  <main class="document-wrapper">
    <!-- ======================================================================
         COURSE OVERVIEW & 6-UNIT CURRICULUM SYLLABUS BANNER
         ====================================================================== -->
    <article class="doc-page" id="curriculum-overview" style="margin-bottom: 2rem; border-left: 4px solid var(--primary); background: var(--bg-surface); padding: 1.5rem 1.75rem; border-radius: 12px; box-shadow: var(--shadow-sm); border: 1px solid var(--border-subtle); border-left: 4px solid var(--primary);">
      <div class="page-header-meta" style="margin-bottom: 0.75rem;">
        <span class="meta-tag" style="background: rgba(37, 99, 235, 0.15); color: var(--primary); font-weight: 800;">CSC104 • OFFICIAL 6-UNIT SYLLABUS</span>
        <span class="meta-tag">30 Lecture Hours</span>
        <span class="meta-tag">10 Laboratory Experiments</span>
        <span class="meta-tag">Credits: 04</span>
      </div>

      <h1 style="font-family: var(--font-display); font-size: 1.6rem; font-weight: 800; color: var(--text-main); margin-bottom: 0.5rem; letter-spacing: -0.02em;">
        IT Fundamentals &amp; Computer Architecture (CSC104)
      </h1>
      <p class="lead-para" style="margin-bottom: 1.25rem; font-size: 0.92rem; color: var(--text-muted); line-height: 1.6;">
        Welcome to the comprehensive IT Fundamentals knowledge portal. This course covers the official 6-unit syllabus and 30-lecture curriculum conforming to NBA/NAAC outcome-based engineering standards. Jump directly to any unit, practical lab, or interactive engineering simulator below:
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0.75rem; margin-top: 1rem;">
        <a href="#it1-formfactors" style="text-decoration:none; padding: 0.75rem 1rem; border-radius: 8px; background: var(--bg-page); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.25rem; transition: transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-mono); font-size: 11px; font-weight: 800; color: #10b981;">UNIT 01</span>
            <span style="font-size: 10px; color: var(--text-subtle); font-family: var(--font-mono);">Lectures 1–5</span>
          </div>
          <strong style="color: var(--text-main); font-size: 13px;">PC Hardware and Configuration</strong>
          <span style="color: var(--text-muted); font-size: 11px; line-height: 1.4;">Cables (USB, HDMI, DP, TB4, SATA), Motherboards, CPUs, RAM, PSUs, POST errors &amp; overheating.</span>
        </a>

        <a href="#it2-topologies" style="text-decoration:none; padding: 0.75rem 1rem; border-radius: 8px; background: var(--bg-page); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.25rem; transition: transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-mono); font-size: 11px; font-weight: 800; color: #3b82f6;">UNIT 02</span>
            <span style="font-size: 10px; color: var(--text-subtle); font-family: var(--font-mono);">Lectures 6–10</span>
          </div>
          <strong style="color: var(--text-main); font-size: 13px;">Networking Fundamentals</strong>
          <span style="color: var(--text-muted); font-size: 11px; line-height: 1.4;">LAN/WAN/PAN, hardware, IPv4/IPv6, CIDR subnetting, TCP/IP, DHCP, DNS, NAT, virtualization &amp; cloud.</span>
        </a>

        <a href="#it3-mobile" style="text-decoration:none; padding: 0.75rem 1rem; border-radius: 8px; background: var(--bg-page); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.25rem; transition: transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-mono); font-size: 11px; font-weight: 800; color: #8b5cf6;">UNIT 03</span>
            <span style="font-size: 10px; color: var(--text-subtle); font-family: var(--font-mono);">Lectures 11–15</span>
          </div>
          <strong style="color: var(--text-main); font-size: 13px;">Mobile and Peripheral Devices</strong>
          <span style="color: var(--text-muted); font-size: 11px; line-height: 1.4;">Laptops, peripherals, printers (laser, inkjet, thermal, impact), queues, SOHO routers &amp; WPA3 wireless.</span>
        </a>

        <a href="#sec1" style="text-decoration:none; padding: 0.75rem 1rem; border-radius: 8px; background: var(--bg-page); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.25rem; transition: transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-mono); font-size: 11px; font-weight: 800; color: #ec4899;">UNIT 04</span>
            <span style="font-size: 10px; color: var(--text-subtle); font-family: var(--font-mono);">Lectures 16–20</span>
          </div>
          <strong style="color: var(--text-main); font-size: 13px;">Security and System Protection</strong>
          <span style="color: var(--text-muted); font-size: 11px; line-height: 1.4;">OS types, Windows architecture stack, clean installs, user profiles, NTFS permissions, Defender &amp; Registry.</span>
        </a>

        <a href="#sec13" style="text-decoration:none; padding: 0.75rem 1rem; border-radius: 8px; background: var(--bg-page); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.25rem; transition: transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-mono); font-size: 11px; font-weight: 800; color: #f59e0b;">UNIT 05</span>
            <span style="font-size: 10px; color: var(--text-subtle); font-family: var(--font-mono);">Lectures 21–25</span>
          </div>
          <strong style="color: var(--text-main); font-size: 13px;">OS Troubleshooting and Command Line</strong>
          <span style="color: var(--text-muted); font-size: 11px; line-height: 1.4;">Boot failures, BSODs, Windows networking, firewall rules, RDP, macOS/Linux features &amp; chmod.</span>
        </a>

        <a href="#it6-mobile-security" style="text-decoration:none; padding: 0.75rem 1rem; border-radius: 8px; background: var(--bg-page); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.25rem; transition: transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='var(--border-subtle)'">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <span style="font-family: var(--font-mono); font-size: 11px; font-weight: 800; color: #06b6d4;">UNIT 06</span>
            <span style="font-size: 10px; color: var(--text-subtle); font-family: var(--font-mono);">Lectures 26–30</span>
          </div>
          <strong style="color: var(--text-main); font-size: 13px;">Scripting, Remote Support, and Safety</strong>
          <span style="color: var(--text-muted); font-size: 11px; line-height: 1.4;">Mobile security, biometrics, remote wipe, scripting (batch, PowerShell, Python), ESD &amp; 3-2-1 backups.</span>
        </a>
      </div>

      <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; padding-top: 0.85rem; border-top: 1px solid var(--border-subtle);">
        <a href="#it-labs" class="btn-tool active" style="text-decoration:none; font-size: 11px; padding: 0.35rem 0.75rem;"><i data-lucide="flask-conical" style="width:13px;height:13px;"></i> 10 Practical Labs &amp; Viva</a>
        <a href="#it-sims" class="btn-tool" style="text-decoration:none; font-size: 11px; padding: 0.35rem 0.75rem;"><i data-lucide="terminal" style="width:13px;height:13px;"></i> 4 Simulators &amp; Live CLI</a>
        <a href="#it-exam" class="btn-tool" style="text-decoration:none; font-size: 11px; padding: 0.35rem 0.75rem;"><i data-lucide="award" style="width:13px;height:13px;"></i> Comprehensive Final Exam Bank</a>
        <a href="../index.html" class="btn-tool" style="text-decoration:none; font-size: 11px; padding: 0.35rem 0.75rem;"><i data-lucide="arrow-left" style="width:13px;height:13px;"></i> Master Academic Hub</a>
      </div>
    </article>

    <!-- UNIT 01: PC HARDWARE AND CONFIGURATION -->
    {IT_UNIT1_HTML}

    <!-- UNIT 02: NETWORKING FUNDAMENTALS -->
    {IT_UNIT2_HTML}

    <!-- UNIT 03: MOBILE AND PERIPHERAL DEVICES -->
    {IT_UNIT3_HTML}

    <!-- UNIT 04: SECURITY AND SYSTEM PROTECTION -->
    {IT_UNIT4_HTML}

    <!-- UNIT 05: OS TROUBLESHOOTING AND COMMAND LINE -->
    {IT_UNIT5_HTML}

    <!-- SOHO GATEWAY & PERIMETER SECURITY -->
    {IT_SOHO_HTML}

    <!-- UNIT 06: SCRIPTING, REMOTE SUPPORT, AND SAFETY -->
    {IT_UNIT6_HTML}

    <!-- HANDS-ON LABORATORY PRACTICUM -->
    {IT_LABS_HTML}

    <!-- ENGINEERING SIMULATORS & DUAL CLI SANDBOXES -->
    {IT_SIMS_HTML}

    <!-- MASTER COMPREHENSIVE FINAL EXAMINATION BANK -->
    {IT_EXAM_HTML}
  </main>
"""

# 5. Extract and Upgrade the Script at Bottom
script_m = re.search(r'<script>(.*?)</script>', ext_html, re.DOTALL)
ext_script = script_m.group(1) if script_m else ""

# Enhanced interactive scripts for RAM calc, CIDR calc, Chmod calc, Printer defect ruler, and Live Terminal
EXTRA_SCRIPTS = """
    // 8. Custom Engineering Simulators Interactive Scripts
    function calcRamLatency() {
      const val = document.getElementById('ramCalcDDR').value.split(',');
      const mt = parseFloat(val[0]);
      const cl = parseFloat(val[1]);
      const latency = (cl / (mt / 2)) * 1000;
      const clock = mt / 2;
      const cycleTime = 1000 / clock;
      document.getElementById('ramCalcResult').innerHTML = 
        `True Latency: <strong>${latency.toFixed(2)} ns</strong> • Bus Clock: <strong>${clock.toFixed(0)} MHz</strong> • Cycle Time: <strong>${cycleTime.toFixed(3)} ns</strong>`;
    }

    function calcCidrPrefix() {
      const p = parseInt(document.getElementById('cidrPrefixSelect').value);
      const hostBits = 32 - p;
      const total = Math.pow(2, hostBits);
      const usable = total > 2 ? total - 2 : total;
      const blockSize = Math.pow(2, 32 - p);
      document.getElementById('cidrCalcResult').innerHTML = 
        `Total IPs: <strong>${total}</strong> • Usable Hosts: <strong>${usable}</strong> • Block Size: <strong>${blockSize}</strong>`;
    }

    function updateChmod() {
      let u = 0, g = 0, o = 0;
      if (document.getElementById('chkU_R').checked) u += 4;
      if (document.getElementById('chkU_W').checked) u += 2;
      if (document.getElementById('chkU_X').checked) u += 1;
      if (document.getElementById('chkG_R').checked) g += 4;
      if (document.getElementById('chkG_W').checked) g += 2;
      if (document.getElementById('chkG_X').checked) g += 1;
      if (document.getElementById('chkO_R').checked) o += 4;
      if (document.getElementById('chkO_W').checked) o += 2;
      if (document.getElementById('chkO_X').checked) o += 1;

      const sym = '-' +
        (u & 4 ? 'r' : '-') + (u & 2 ? 'w' : '-') + (u & 1 ? 'x' : '-') +
        (g & 4 ? 'r' : '-') + (g & 2 ? 'w' : '-') + (g & 1 ? 'x' : '-') +
        (o & 4 ? 'r' : '-') + (o & 2 ? 'w' : '-') + (o & 1 ? 'x' : '-');

      document.getElementById('chmodResult').innerHTML = 
        `Octal: <strong>chmod ${u}${g}${o}</strong> • Symbolic: <strong>${sym}</strong>`;
    }

    function diagnosePrinterDefect() {
      const v = document.getElementById('defectIntervalSelect').value;
      let comp = '', cause = '';
      if (v === 'drum') {
        comp = 'OPC Imaging Drum (30 mm diameter)';
        cause = 'Scratched organic photoconductor coating or light shock fatigue';
      } else if (v === 'fuser') {
        comp = 'Fuser Upper Heat Roller (24.2 mm diameter)';
        cause = 'Gouged Teflon coating, dried toner cake, or defective thermistor';
      } else if (v === 'pcr') {
        comp = 'Primary Charge Roller / PCR (12 mm diameter)';
        cause = 'Dirty sponge roller or uniform charge leak';
      } else if (v === 'transfer') {
        comp = 'Transfer Roller (16.2 mm diameter)';
        cause = 'Fingerprint skin oil contamination or toner dust buildup';
      }
      document.getElementById('printerDefectResult').innerHTML = 
        `Component: <strong>${comp}</strong> • Cause: <strong>${cause}</strong>`;
    }

    // 9. Live Interactive Systems Administration Terminal
    function clearTermScreen() {
      document.getElementById('itTerminalOutput').innerHTML = '<div style="color:#94a3b8;">Terminal cleared. Type help for commands.</div><br>';
    }

    function handleTermKey(e) {
      if (e.key === 'Enter') {
        const input = document.getElementById('itTermInput');
        const cmd = input.value.trim();
        if (!cmd) return;
        input.value = '';

        const term = document.getElementById('itTerminalOutput');
        term.innerHTML += `<div><span style="color:#38bdf8;">C:\\Admin&gt;</span> <span style="color:#f8fafc; font-weight:700;">${cmd}</span></div>`;

        let resp = '';
        const lower = cmd.toLowerCase();

        if (lower === 'help') {
          resp = `Available Commands:
  ipconfig          - Display IP configuration
  ipconfig /all     - Display detailed TCP/IP parameters
  ping 8.8.8.8      - Test ICMP connectivity to Google DNS
  arp -a            - Display ARP cache table (IP to MAC mapping)
  netstat -ano      - Display active TCP/UDP connections
  ls -la            - List Linux directory contents with octal permissions
  uname -a          - Display Linux kernel version
  whoami            - Display current active user security context
  clear             - Clear terminal display`;
        } else if (lower === 'ipconfig') {
          resp = `Windows IP Configuration

Ethernet adapter vEthernet (Default Switch):
   Connection-specific DNS Suffix  . : corp.contoso.com
   Link-local IPv6 Address . . . . . : fe80::d418:b7f2:99a1:430c%12
   IPv4 Address. . . . . . . . . . . : 192.168.1.105
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1`;
        } else if (lower.startsWith('ping')) {
          resp = `Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=11ms TTL=117
Reply from 8.8.8.8: bytes=32 time=12ms TTL=117
Reply from 8.8.8.8: bytes=32 time=10ms TTL=117
Reply from 8.8.8.8: bytes=32 time=11ms TTL=117

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 10ms, Maximum = 12ms, Average = 11ms`;
        } else if (lower === 'arp -a') {
          resp = `Interface: 192.168.1.105 --- 0xc
  Internet Address      Physical Address      Type
  192.168.1.1           00-11-32-84-ae-19     dynamic
  192.168.1.50          08-00-27-4a-9c-12     dynamic
  192.168.1.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static`;
        } else if (lower.startsWith('netstat')) {
          resp = `Active Connections
  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       840
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    192.168.1.105:54120    142.250.190.46:443     ESTABLISHED     4820
  TCP    192.168.1.105:54122    151.101.1.140:443      ESTABLISHED     4820`;
        } else if (lower === 'whoami') {
          resp = `contoso\\devops_admin (Mandatory Label\\High Mandatory Level)`;
        } else if (lower === 'uname -a') {
          resp = `Linux server-node-01 6.8.0-40-generic #40-Ubuntu SMP PREEMPT_DYNAMIC x86_64 GNU/Linux`;
        } else if (lower === 'ls -la') {
          resp = `total 24
drwxr-xr-x 4 devops_admin developers 4096 Oct 27 15:00 .
drwxr-xr-x 8 root         root       4096 Oct 27 14:00 ..
-rw-r--r-- 1 devops_admin developers  220 Oct 27 15:00 .bashrc
-rwxr-xr-x 1 devops_admin developers 1048 Oct 27 15:15 backup.sh
-rw------- 1 devops_admin developers  450 Oct 27 15:20 .env`;
        } else if (lower === 'clear') {
          clearTermScreen();
          return;
        } else {
          resp = `'${cmd}' is not recognized as an internal or external command. Type 'help' for available commands.`;
        }

        term.innerHTML += `<div style="color:#94a3b8; white-space:pre-wrap; margin-bottom:0.75rem;">${resp}</div>`;
        term.scrollTop = term.scrollHeight;
      }
    }
"""

# 6. Put everything together
FULL_HTML = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IT Fundamentals (CSC104) — Official 6-Unit Curriculum &amp; Knowledge Portal</title>
  {head_content}
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
        <i data-lucide="book-open" style="width: 14px; height: 14px;"></i>
        IT FUNDAMENTALS • CSC104
      </span>

      <!-- Sister Portal Quick Pills -->
      <a href="../index.html" class="btn-tool" title="Back to Master University Hub" style="text-decoration:none;">
        <i data-lucide="home" style="width: 14px; height: 14px;"></i>
        <span>Hub</span>
      </a>
      <a href="../Cloud_Administration_Portal/index.html" class="btn-tool" title="Cloud Administration AWS" style="text-decoration:none;">
        <i data-lucide="cloud" style="width: 14px; height: 14px;"></i>
        <span>Cloud</span>
      </a>
      <a href="../Server_Administration_Portal/index.html" class="btn-tool" title="Server Administration" style="text-decoration:none;">
        <i data-lucide="server" style="width: 14px; height: 14px;"></i>
        <span>Server</span>
      </a>
    </div>

    <div class="toolbar-right">
      <div class="search-box">
        <i data-lucide="search" class="search-icon" style="width: 15px; height: 15px;"></i>
        <input type="text" id="quickSearchInput" class="search-input" placeholder="Search hardware, network, kernel, or shell...">
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
    {ext_script}
    {EXTRA_SCRIPTS}
  </script>
</body>
</html>
"""

with open('IT_Fundamentals_Portal/index.html', 'w', encoding='utf-8') as f:
    f.write(FULL_HTML)

print(f"Master IT Fundamentals Portal assembled! Total size: {len(FULL_HTML)} bytes, {len(FULL_HTML.splitlines())} lines.")