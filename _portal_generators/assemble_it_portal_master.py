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
           UNIT 01: COMPUTER HARDWARE & MOTHERBOARDS
           ========================================== -->
      <div class="toc-unit" id="tocUnit1HW">
        <button class="toc-unit-header" type="button" aria-expanded="true">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 01</span>
            <span class="toc-unit-title">Computer Hardware &amp; Motherboards</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupHwCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Core Hardware Subsystems</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it1-formfactors" class="toc-link active"><span class="toc-link-num">01.</span> Motherboard Form Factors &amp; Standoffs</a>
              <a href="#it1-chipset" class="toc-link"><span class="toc-link-num">02.</span> Chipset Architectures &amp; PCIe 5.0 Bus</a>
              <a href="#it1-cpu" class="toc-link"><span class="toc-link-num">03.</span> CPU Sockets (LGA/PGA) &amp; SRAM Cache</a>
              <a href="#it1-ram" class="toc-link"><span class="toc-link-num">04.</span> Dynamic RAM (DDR4/DDR5) &amp; Latency Math</a>
              <a href="#it1-psu" class="toc-link"><span class="toc-link-num">05.</span> Power Supplies &amp; 80 Plus Efficiency</a>
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
           UNIT 02: COMPUTER NETWORKING TOPOLOGIES
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit2Net">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 02</span>
            <span class="toc-unit-title">Networking Topologies &amp; Protocols</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupNetCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Network Architecture</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it2-topologies" class="toc-link"><span class="toc-link-num">10.</span> Physical &amp; Logical Topologies</a>
              <a href="#it2-cables" class="toc-link"><span class="toc-link-num">11.</span> Structured Cabling (Cat5e-8) &amp; T568A/B</a>
              <a href="#it2-switching" class="toc-link"><span class="toc-link-num">12.</span> Layer 2 Switching &amp; Domain Boundaries</a>
              <a href="#it2-encapsulation" class="toc-link"><span class="toc-link-num">13.</span> OSI 7-Layer vs TCP/IP Encapsulation</a>
              <a href="#it2-subnetting" class="toc-link"><span class="toc-link-num">14.</span> IPv4 CIDR Subnetting &amp; IPv6 SLAAC</a>
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
           UNIT 03: MOBILE & PERIPHERALS
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit3Dev">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 03</span>
            <span class="toc-unit-title">Mobile Devices &amp; Printing Tech</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupDevCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Devices &amp; Peripherals</span>
                <span class="toc-group-count">5 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it3-mobile" class="toc-link"><span class="toc-link-num">19.</span> Mobile SoC &amp; OS Sandboxing</a>
              <a href="#it3-peripherals" class="toc-link"><span class="toc-link-num">20.</span> USB4, Thunderbolt 4 &amp; Tunneling</a>
              <a href="#it3-laser" class="toc-link"><span class="toc-link-num">21.</span> The 6-Stage Laser Printing Engine</a>
              <a href="#it3-storage" class="toc-link"><span class="toc-link-num">22.</span> NVMe over PCIe vs SATA AHCI</a>
              <a href="#it3-printing-types" class="toc-link"><span class="toc-link-num">23.</span> Inkjet, Thermal, Impact &amp; 3D</a>
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
           UNIT 04: WINDOWS NT ARCHITECTURE & SECURITY
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit4NT">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 04</span>
            <span class="toc-unit-title">Windows NT Architecture &amp; Security</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupNTCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Core NT Architecture</span>
                <span class="toc-group-count">10 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#sec1" class="toc-link"><span class="toc-link-num">01.</span> Windows NT Design Goals (PRESC)</a>
              <a href="#sec2" class="toc-link"><span class="toc-link-num">02.</span> Layered NT Architecture Stack</a>
              <a href="#sec3" class="toc-link"><span class="toc-link-num">03.</span> User Mode vs Kernel Mode</a>
              <a href="#sec4" class="toc-link"><span class="toc-link-num">04.</span> The 8 NT Executive Managers</a>
              <a href="#sec5" class="toc-link"><span class="toc-link-num">05.</span> Microkernel &amp; IRQLs (0 to 31)</a>
              <a href="#sec6" class="toc-link"><span class="toc-link-num">06.</span> Hardware Abstraction Layer (HAL)</a>
              <a href="#sec8" class="toc-link"><span class="toc-link-num">08.</span> I/O Stack &amp; IRP Dispatch</a>
              <a href="#sec9" class="toc-link"><span class="toc-link-num">09.</span> Process Launch (chrome.exe Trace)</a>
              <a href="#sec11" class="toc-link"><span class="toc-link-num">11.</span> End-to-End File Save Path</a>
              <a href="#sec13" class="toc-link"><span class="toc-link-num">13.</span> Windows Administrative CLI</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupNTSec">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • Security &amp; Registry</span>
                <span class="toc-group-count">7 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#sec14" class="toc-link"><span class="toc-link-num">14.</span> Security Subsystem (LSA &amp; SRM)</a>
              <a href="#sec15" class="toc-link"><span class="toc-link-num">15.</span> Accounts &amp; SID Architecture</a>
              <a href="#sec16" class="toc-link"><span class="toc-link-num">16.</span> Kerberos v5 vs NTLMv2</a>
              <a href="#sec18" class="toc-link"><span class="toc-link-num">18.</span> Access Control (Tokens, DACLs, SACLs)</a>
              <a href="#sec20" class="toc-link"><span class="toc-link-num">20.</span> Defender, UAC &amp; Integrity Levels</a>
              <a href="#sec26-sysfiles" class="toc-link"><span class="toc-link-num">26.</span> Core Windows System Files</a>
              <a href="#sec27-registry" class="toc-link"><span class="toc-link-num">27.</span> Windows Registry Architecture &amp; Hives</a>
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
              <a href="#practice-mcq-u1" class="toc-link"><span class="toc-link-num">U1.</span> Core NT MCQ Bank (30 Qs)</a>
              <a href="#practice-subj-short-u1" class="toc-link"><span class="toc-link-num">U1.</span> Core NT Conceptual Q&amp;A</a>
              <a href="#practice-subj-long-u1" class="toc-link"><span class="toc-link-num">U1.</span> Core NT Scenario Problems</a>
              <a href="#practice-mcq-u2" class="toc-link"><span class="toc-link-num">U2.</span> Security Subsystem MCQ Bank (30 Qs)</a>
              <a href="#practice-subj-short-u2" class="toc-link"><span class="toc-link-num">U2.</span> Security Conceptual Q&amp;A</a>
              <a href="#practice-subj-long-u2" class="toc-link"><span class="toc-link-num">U2.</span> Security Scenario Problems</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 05: LINUX OS & SOHO SECURITY
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit5Linux">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 05</span>
            <span class="toc-unit-title">Linux OS, Shell &amp; SOHO Security</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group" id="groupLinuxCore">
            <button class="toc-group-header" type="button" aria-expanded="true">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART I • Linux Architecture &amp; Bash</span>
                <span class="toc-group-count">7 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#sec28-bash" class="toc-link"><span class="toc-link-num">28.</span> Linux OS Architecture &amp; Shell</a>
              <a href="#sec29-syntax" class="toc-link"><span class="toc-link-num">29.</span> Permissions &amp; Script Execution</a>
              <a href="#sec31-arith" class="toc-link"><span class="toc-link-num">31.</span> Arithmetic Operators &amp; Calculations</a>
              <a href="#sec34-cond" class="toc-link"><span class="toc-link-num">34.</span> Conditional Testing &amp; Operators</a>
              <a href="#sec37-func" class="toc-link"><span class="toc-link-num">37.</span> Functions, Local Scope &amp; Exit Codes</a>
              <a href="#sec40-progs" class="toc-link"><span class="toc-link-num">40.</span> 10 Practical Production Shell Scripts</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupSOHOCore">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART II • SOHO Network Security</span>
                <span class="toc-group-count">4 Topics</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#it5-soho-gateway" class="toc-link"><span class="toc-link-num">41.</span> SOHO Gateway &amp; DHCP DORA</a>
              <a href="#it5-nat-pat" class="toc-link"><span class="toc-link-num">42.</span> NAT vs PAT Socket Translation</a>
              <a href="#it5-wifi-security" class="toc-link"><span class="toc-link-num">43.</span> Wireless Security: WPA2 vs WPA3 SAE</a>
              <a href="#it5-firewall-dmz" class="toc-link"><span class="toc-link-num">44.</span> SPI Firewalls, Port Forwarding &amp; DMZ</a>
            </div>
          </div>
          <div class="toc-group collapsed" id="groupLinuxPractice">
            <button class="toc-group-header" type="button" aria-expanded="false">
              <div class="toc-group-header-left">
                <span class="toc-group-title">PART III • Unit 05 Assessment</span>
                <span class="toc-group-count">39 Problems</span>
              </div>
              <i data-lucide="chevron-down" class="toc-chevron"></i>
            </button>
            <div class="toc-group-body">
              <a href="#practice-mcq-u3" class="toc-link"><span class="toc-link-num">45.</span> Linux MCQ Bank (30 Qs)</a>
              <a href="#practice-subj-short-u3" class="toc-link"><span class="toc-link-num">46.</span> Linux Conceptual Q&amp;A</a>
              <a href="#practice-subj-long-u3" class="toc-link"><span class="toc-link-num">47.</span> Linux Analytical Scenarios</a>
            </div>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 06: LAB PRACTICUM
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit6Labs">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 06</span>
            <span class="toc-unit-title">Hands-On Laboratory Manual</span>
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
           UNIT 07: SIMULATORS & SANDBOXES
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit7Sims">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 07</span>
            <span class="toc-unit-title">Engineering Simulators &amp; CLI</span>
          </div>
          <i data-lucide="chevron-down" class="toc-unit-chevron"></i>
        </button>
        <div class="toc-unit-body">
          <div class="toc-group-body">
            <a href="#it-sims" class="toc-link"><span class="toc-link-num">49.</span> 16 Interactive Tools &amp; Dual Terminal</a>
          </div>
        </div>
      </div>

      <!-- ==========================================
           UNIT 08: COMPREHENSIVE EXAM BANK
           ========================================== -->
      <div class="toc-unit collapsed" id="tocUnit8Exam">
        <button class="toc-unit-header" type="button" aria-expanded="false">
          <div class="toc-unit-header-left">
            <span class="toc-unit-badge">UNIT 08</span>
            <span class="toc-unit-title">Final Examination Bank</span>
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
    <!-- UNIT 01: COMPUTER HARDWARE & MOTHERBOARDS -->
    {IT_UNIT1_HTML}

    <!-- UNIT 02: NETWORKING TOPOLOGIES & PROTOCOLS -->
    {IT_UNIT2_HTML}

    <!-- UNIT 03: MOBILE & PERIPHERALS -->
    {IT_UNIT3_HTML}

    <!-- UNIT 04 & 05: OPERATING SYSTEM NT & LINUX ARTICLES (sec1 to sec40) -->
    {ext_main}

    <!-- SOHO SECURITY (PART OF UNIT 05) -->
    {IT_SOHO_HTML}

    <!-- UNIT 06: HANDS-ON LABORATORY PRACTICUM -->
    {IT_LABS_HTML}

    <!-- UNIT 07: ENGINEERING SIMULATORS & DUAL CLI SANDBOXES -->
    {IT_SIMS_HTML}

    <!-- UNIT 08: COMPREHENSIVE FINAL EXAM BANK -->
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
  <title>IT Fundamentals (CSC104) — Master Engineering & Knowledge Portal</title>
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
