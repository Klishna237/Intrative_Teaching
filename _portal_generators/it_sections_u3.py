# -*- coding: utf-8 -*-
"""
Unit 3: Mobile Devices, Peripherals & Electrophotographic Printing
In-depth Engineering Standard style:
- Article it3-mobile: Mobile Device Architectures: ARM SoC, Display Tech & OS Sandboxing
- Article it3-peripherals: High-Speed Peripheral Buses: USB4, Thunderbolt 4 & Protocol Tunneling
- Article it3-laser: The 6-Stage Electrophotographic Laser Printing Engine In-Depth
- Article it3-storage: Mass Storage Protocols: NVMe (PCIe) vs SATA (AHCI) & M.2 Keying
- Article it3-printing-types: Comparative Printing Technologies: Inkjet, Thermal, Impact & 3D
- Article practice-mcq-u3-dev: Unit 3 Self-Testing Bank: 30 Multiple Choice Questions
- Article practice-subj-short-u3-dev: Short Conceptual Questions (5 Sets)
- Article practice-subj-long-u3-dev: Analytical & Scenario Problems (4 Sets)
- Article mcq-answer-key-u3-dev: Master Answer Key Table
"""

IT_UNIT3_HTML = """
<!-- ==========================================================================
     UNIT 03: MOBILE DEVICES, PERIPHERALS & ELECTROPHOTOGRAPHIC PRINTING
     ========================================================================== -->

<!-- Page 1: Mobile SoC -->
<article class="doc-page" id="it3-mobile">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 03 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">19.</span> Mobile System-on-Chip (SoC) Architectures, Battery Chemistry & Sandboxing
  </h2>

  <p class="lead-para">
    Unlike modular desktop personal computers, mobile platforms integrate the processor cores, graphical processing unit, neural processing engine, cellular baseband modem, memory controller, and security cryptographic coprocessor onto a monolithic silicon die designated as a System-on-Chip (SoC).
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Silicon Implementation</th>
          <th>Operational Role</th>
          <th>Power &amp; Performance Trade-off</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Heterogeneous CPU</strong></td>
          <td>ARM big.LITTLE / DynamIQ</td>
          <td>High-performance cores (Cortex-X / Performance) paired with high-efficiency cores (Cortex-A / Efficiency)</td>
          <td>OS scheduler migrates background tasks to efficiency cores to conserve milliwatts; ramps performance cores only during active UI rendering</td>
        </tr>
        <tr>
          <td><strong>Unified RAM</strong></td>
          <td>LPDDR5 / LPDDR5X (Package-on-Package)</td>
          <td>Soldered directly on top of the SoC silicon substrate via microscopic ball micro-bumps</td>
          <td>Zero modular upgradeability; delivers ultra-low trace capacitance, 8533 MT/s transfer speeds, and deep self-refresh idle sleep</td>
        </tr>
        <tr>
          <td><strong>Secure Enclave / TPM</strong></td>
          <td>Hardware-isolated cryptographic core</td>
          <td>Stores biometric hashes (FaceID / Fingerprint), disk encryption keys, and hardware Root of Trust</td>
          <td>Physically runs an independent microkernel with dedicated encrypted memory; completely inaccessible to the primary host OS kernel</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="shield"></i> Mobile OS Sandboxing: Android Zygote vs iOS Darwin XNU</div>
    <p>
      Both modern mobile operating systems enforce strict application sandboxing to prevent malware lateral movement:
    </p>
    <ul>
      <li><strong>Android (Linux Kernel + ART):</strong> Every application is assigned a unique Linux User Identifier (UID e.g. `u0_a142`) at installation. Under standard Linux DAC (Discretionary Access Control), processes running under UID `u0_a142` cannot read files owned by `u0_a143`. Applications spawn from a pre-warmed template process called <em>Zygote</em> and execute inside the Android Runtime (ART) with mandatory SELinux MAC policies restricting hardware calls.</li>
      <li><strong>iOS (Mach/BSD Kernel + Darwin):</strong> All third-party apps execute inside an isolated container directory with randomized UUIDs. The kernel enforces mandatory code-signing; unsigned dynamic libraries cannot be injected into process memory. Direct filesystem access outside the container requires explicit Entitlements and user runtime consent prompts.</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: High-Speed Peripheral Interfaces</span>
    <span>Unit 03 • Page 01</span>
  </div>
</article>

<!-- Page 2: Peripheral Interfaces -->
<article class="doc-page" id="it3-peripherals">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 03 • Page 02</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">20.</span> High-Speed Peripheral Interconnects: USB4, Thunderbolt 4 & Protocol Tunneling
  </h2>

  <p class="lead-para">
    Modern peripheral bus architectures have converged onto the 24-pin reversible USB Type-C physical connector. Behind this universal physical form factor lies sophisticated protocol tunneling technology capable of multiplexing PCIe storage lanes, DisplayPort video streams, and USB data simultaneously across a single physical differential copper cable.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Standard Specification</th>
          <th>Marketing Name</th>
          <th>Max Physical Bandwidth</th>
          <th>Protocol Tunneling Support</th>
          <th>Power Delivery Capability</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>USB 2.0</strong></td>
          <td>HighSpeed USB</td>
          <td>480 Mbps (60 MB/s)</td>
          <td>None (Half-duplex differential D+/D- pair)</td>
          <td>5V @ 0.5A (2.5 Watts)</td>
        </tr>
        <tr>
          <td><strong>USB 3.2 Gen 2&times;1</strong></td>
          <td>SuperSpeed USB 10Gbps</td>
          <td>10 Gbps (1.25 GB/s)</td>
          <td>Native USB packet framing only</td>
          <td>Up to 100W (USB-PD 20V @ 5A)</td>
        </tr>
        <tr>
          <td><strong>USB4 (Gen 3&times;2)</strong></td>
          <td>USB4 40Gbps</td>
          <td>40 Gbps (5 GB/s)</td>
          <td>Tunnels PCIe 3.0, DisplayPort 1.4a &amp; USB 3.2</td>
          <td>Up to 240W (USB-PD 3.1 Extended Power Range)</td>
        </tr>
        <tr>
          <td><strong>Thunderbolt 4</strong></td>
          <td>Thunderbolt 4</td>
          <td>40 Gbps (Mandated 32 Gbps PCIe min)</td>
          <td>Mandatory dual 4K/60Hz or single 8K DisplayPort + PCIe &times;4</td>
          <td>Mandatory 100W host charging + 15W device power</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> High-Speed Physics: Protocol Tunneling Over USB Type-C</div>
    <p>
      Under Thunderbolt 4 and USB4, native protocols are not converted into USB packets. Instead, a hardware router engine packages raw native PCIe TLPs (Transaction Layer Packets) and DisplayPort video packets into fixed-size <strong>transport layer tunnel frames</strong>. At the dock or endpoint controller, the frames are de-tunneled with microscopic latency, allowing external GPUs (eGPUs) and multi-gigabit NVMe scratch drives to communicate directly with the host CPU's PCIe root complex as if physically installed in a motherboard slot!
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: The 6-Stage Electrophotographic Laser Engine</span>
    <span>Unit 03 • Page 02</span>
  </div>
</article>

<!-- Page 3: Laser Printing Engine -->
<article class="doc-page" id="it3-laser">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 03 • Page 03</span>
    <span class="meta-tag">Bloom's: Understand / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">21.</span> The 6-Stage Electrophotographic (EP) Laser Printing Engine
  </h2>

  <p class="lead-para">
    Laser printers utilize electrophotography—a precision physics process combining electrostatic charge differentials, optical laser scanning, and thermal fusion to transfer dry polymer toner powder onto paper fibers at high throughput.
  </p>

  <div class="diagram-container">
    <div class="diagram-title">The 6-Step Electrophotographic Printing Cycle</div>
    <div class="arch-stack-visual">
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">STAGE 1: CLEANING</span>
        <div class="tier-desc">Rubber cleaning blade scrapes residual toner into waste reservoir • Discharge erase lamp floods drum with light to neutralize residual electrostatic charges</div>
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">STAGE 2: CONDITIONING (CHARGING)</span>
        <div class="tier-desc">Primary Corona Wire or Primary Charge Roller (PCR) applies a uniform high-voltage negative electrostatic charge (-600V to -1000V DC) across the organic photoconductor (OPC) drum</div>
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">STAGE 3: WRITING (EXPOSING)</span>
        <div class="tier-desc">Precision semiconductor laser diode reflects off a multi-faceted rotating polygonal mirror, sweeping across the drum • Light discharges exposed image points to ~ -100V, creating the invisible <strong>latent electrostatic image</strong></div>
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">STAGE 4: DEVELOPING</span>
        <div class="tier-desc">Developer roller coated with magnetized toner particles charged to -300V • Because -300V is more positive than -600V, toner is repelled by unexposed drum areas and electrostatically leaps onto the -100V discharged latent image</div>
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">STAGE 5: TRANSFERRING</span>
        <div class="tier-desc">Transfer Roller applies a strong positive charge (+600V DC) to the underside of the paper as it passes beneath the drum • Strong positive charge draws negatively charged toner powder from the drum onto the paper fibers</div>
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">STAGE 6: FUSING</span>
        <div class="tier-desc">Paper passes between a heated halogen/ceramic Teflon roller (180&deg;C to 205&deg;C) and a high-pressure rubber backing roller • Heat and pressure melt plastic polymer resin in toner, permanently bonding it into paper cellulose</div>
      </div>
    </div>
  </div>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="zap"></i> Mnemonic Acronym for the 6 Laser Stages: CCW-DTF</div>
    <p>
      <strong>C</strong>leaning &rarr; <strong>C</strong>onditioning &rarr; <strong>W</strong>riting &rarr; <strong>D</strong>eveloping &rarr; <strong>T</strong>ransferring &rarr; <strong>F</strong>using.
      <br><em>Remember:</em> "<strong>C</strong>an <strong>C</strong>omputers <strong>W</strong>rite <strong>D</strong>ata <strong>T</strong>o <strong>F</strong>iles?"
    </p>
  </div>

  <div class="callout callout-alert">
    <div class="callout-header"><i data-lucide="alert-triangle"></i> Hardware Triage: Identifying Component Failures by Print Defects</div>
    <p>
      Field engineers diagnose laser printer mechanical failures by inspecting printed output artifacts:
    </p>
    <ul>
      <li><strong>Smearing Image / Toner Wipes Off with Finger:</strong> Fuser assembly failure. The ceramic heating element has failed, or fuser thermal sensors (thermistors) are not reaching 180&deg;C.</li>
      <li><strong>Completely Blank White Page:</strong> Transfer roller failure (no positive charge applied to pull toner) or primary laser shutter is stuck closed.</li>
      <li><strong>Completely Solid Black Page:</strong> Primary Corona Wire / Charging Roller failure. Without the uniform -600V negative conditioning charge, the entire drum defaults to 0V (neutral/attractive), causing toner to flood the entire page!</li>
      <li><strong>Repetitive Marks or Ghosting at Fixed Intervals:</strong> Damaged OPC drum, dirty charging roller, or scratched fuser roller. Distance between repeated defects matches the exact circumference: \(D = \pi \times \text{Diameter}\).</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: Mass Storage Protocols & M.2 Keying</span>
    <span>Unit 03 • Page 03</span>
  </div>
</article>

<!-- Page 4: Storage Protocols -->
<article class="doc-page" id="it3-storage">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 03 • Page 04</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">22.</span> Mass Storage Protocols: NVMe over PCIe vs SATA AHCI & M.2 Form Factors
  </h2>

  <p class="lead-para">
    Solid-State Drives (SSDs) replaced mechanical spinning magnetic hard drives, exposing the severe latency and throughput bottlenecks of legacy storage bus protocols originally engineered for rotating platters.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Specification Metric</th>
          <th>SATA 3.0 with AHCI Protocol</th>
          <th>NVMe (Non-Volatile Memory Express)</th>
          <th>Architectural Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Underlying Bus</strong></td>
          <td>Serial ATA (Legacy Southbridge controller)</td>
          <td>PCIe Gen 3/4/5 (Direct point-to-point to CPU)</td>
          <td>Bypasses Southbridge DMI bottlenecks completely</td>
        </tr>
        <tr>
          <td><strong>Maximum Physical Bandwidth</strong></td>
          <td>6 Gbps (~550 MB/s real-world ceiling)</td>
          <td>PCIe 4.0 &times;4 = 7.88 GB/s; PCIe 5.0 &times;4 = 15.75 GB/s</td>
          <td><strong>&gt;14&times; to 28&times; higher throughput</strong> for streaming I/O</td>
        </tr>
        <tr>
          <td><strong>Command Queue Depth</strong></td>
          <td>Single queue with 32 commands max</td>
          <td><strong>64,000 queues with 64,000 commands each</strong></td>
          <td>Matches massive parallel CPU core execution threads</td>
        </tr>
        <tr>
          <td><strong>Host Controller Latency</strong></td>
          <td>~6.0 microseconds (Heavy register overhead)</td>
          <td>~2.5 microseconds (Single-register doorbell mechanism)</td>
          <td>Cuts CPU wait cycles by more than 50% per I/O transaction</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> Physical M.2 Module Keying Standards</div>
    <p>
      M.2 expansion cards feature physical notched cutouts ("keys") preventing accidental insertion into incompatible electrical sockets:
    </p>
    <ul>
      <li><strong>B-Key (Socket 2):</strong> Notch at pins 12-19. Supports SATA and PCIe &times;2. Commonly used for cellular LTE/5G WWAN modules.</li>
      <li><strong>M-Key (Socket 3):</strong> Notch at pins 59-66. Supports high-speed PCIe &times;4 NVMe storage cards and PCIe 5.0 SSDs.</li>
      <li><strong>B+M Key:</strong> Features two cutouts, allowing backward compatibility with both B-key and M-key slots (limited to SATA or PCIe &times;2 speeds).</li>
      <li><strong>Size Designation (e.g. 2280):</strong> The first two digits specify width in millimeters (22 mm); the remaining digits specify length in millimeters (80 mm). 2230 is common in handhelds (Steam Deck); 2280 is standard desktop/laptop.</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: Comparative Printing Technologies</span>
    <span>Unit 03 • Page 04</span>
  </div>
</article>

<!-- Page 5: Printing Types -->
<article class="doc-page" id="it3-printing-types">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 03 • Page 05</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">23.</span> Comparative Printing Technologies: Inkjet, Thermal, Impact & 3D Additive
  </h2>

  <p class="lead-para">
    Depending on environmental durability, operational speed, color fidelity, and multipart physical form requirements, enterprise IT systems deploy diverse printing physical engines.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Printing Technology</th>
          <th>Operational Mechanism</th>
          <th>Consumables Required</th>
          <th>Primary Enterprise Deployment Target</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Thermal Bubble Inkjet</strong></td>
          <td>Resistors flash-boil ink chamber, creating a microscopic steam vapor bubble that forces a droplet out the nozzle</td>
          <td>Liquid dye/pigment CMYK ink cartridges</td>
          <td>High-resolution photo printing, marketing graphics, home office</td>
        </tr>
        <tr>
          <td><strong>Piezoelectric Inkjet</strong></td>
          <td>Piezo crystal vibrates mechanically upon electrical charge, pumping precise ink droplets without heat</td>
          <td>Specialized solvent, UV-curable, or archival pigment inks</td>
          <td>Industrial wide-format architectural plotters (Epson PrecisionCore)</td>
        </tr>
        <tr>
          <td><strong>Direct Thermal</strong></td>
          <td>Heated thermal printhead selectively warms chemically coated, heat-sensitive paper (turns black upon heating)</td>
          <td>Thermal roll paper (Zero ink, toner, or ribbon required!)</td>
          <td>Retail Point-of-Sale (POS) cash registers, parking receipt kiosks, shipping label printers (Zebra)</td>
        </tr>
        <tr>
          <td><strong>Thermal Transfer</strong></td>
          <td>Heated thermal printhead melts wax/resin ribbon onto plain labels or polyester tags</td>
          <td>Thermal transfer wax/resin ribbon + standard paper/synthetic labels</td>
          <td>Industrial warehouse asset tagging, outdoor weatherproof barcodes, medical specimen labels</td>
        </tr>
        <tr>
          <td><strong>Impact / Dot Matrix</strong></td>
          <td>Solenoid pins (9-pin or 24-pin printhead) physically strike an inked fabric ribbon against paper</td>
          <td>Inked fabric ribbon + tractor-feed pin-fed paper</td>
          <td>Multipart carbonless carbon forms (invoices, logistics bills of lading) requiring physical mechanical force to copy to layers beneath</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Laptop Architecture & Mobile Upgrades</span>
    <span>Unit 03 • Page 05</span>
  </div>
</article>
<!-- Page 6: Laptop Component Upgrades & Mobile Power Management -->
<article class="doc-page" id="it3-laptop-upgrades">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 03 • Page 06</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">24.</span> Laptop Modular Architecture, Component Upgrades &amp; Battery Telemetry
  </h2>

  <p class="lead-para">
    Laptop and mobile workstations require specialized micro-form-factor engineering due to severe chassis volumetric constraints, tight thermal envelopes (15W–45W TDP), and delicate ribbon cable interconnects. Technicians must distinguish between field-replaceable modular components and permanent surface-mounted (BGA) silicon.
  </p>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="laptop"></i> FIELD-REPLACEABLE UNITS (FRUS) VS SOLDERED HARDWARE</div>
    <div class="callout-body">
      Traditional enterprise business laptops (e.g. ThinkPad, Latitude, EliteBook) support field upgrades of <strong>SODIMM memory</strong>, <strong>M.2 NVMe storage drives</strong>, <strong>Wi-Fi WLAN/WWAN cards</strong>, and <strong>internal battery packs</strong>. Ultra-thin consumer notebooks increasingly solder LPDDR5 memory and Wi-Fi modules directly onto the motherboard PCB to minimize chassis thickness.
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Laptop Component Upgrade Protocols
  </h3>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Subsystem / FRU</th>
          <th>Physical Interface</th>
          <th>Installation &amp; Upgrade Procedure</th>
          <th>Diagnostic Precautions</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>System Memory</strong></td>
          <td>SODIMM 260-pin (DDR4) / 262-pin (DDR5)</td>
          <td>Insert module at 30-degree angle until seated firmly into socket; press down until spring clips click securely into place.</td>
          <td>Disconnect battery before touching RAM. Notch offset prevents backward insertion; DDR4 and DDR5 SODIMMs are mechanically incompatible.</td>
        </tr>
        <tr>
          <td><strong>Mass Storage</strong></td>
          <td>M.2 2280 PCIe NVMe SSD (M-Key)</td>
          <td>Slide NVMe drive into 30-degree M-key slot; secure retaining standoff screw (M2&times;3mm); apply phase-change thermal pad.</td>
          <td>Ensure SSD is single-sided if the chassis lacks bottom clearance. Over-torquing the standoff screw flexes and fractures the PCB substrate.</td>
        </tr>
        <tr>
          <td><strong>Wireless WLAN Card</strong></td>
          <td>M.2 2230 (A+E Key) PCIe / CNVi</td>
          <td>Slide card into slot; attach microscopic coaxial antenna leads (Main = Gray, Aux/MIMO = Black) using plastic spudger.</td>
          <td>Antenna U.FL/MHF4 connectors deform easily. Never force connectors at an angle; verify snapping tactile feedback.</td>
        </tr>
        <tr>
          <td><strong>Rechargeable Battery</strong></td>
          <td>Proprietary multi-pin wiring harness</td>
          <td>Unscrew perimeter captive screws; lift battery by tabs; disconnect multi-pin harness from system board without pulling individual wires.</td>
          <td>Never puncture or bend Li-ion pouch cells (produces thermal runaway fire). Recycle swollen batteries immediately in fireproof sand.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    2. Battery Health Telemetry &amp; Power Calibration
  </h3>

  <p>
    Lithium-ion polymer battery cells degrade chemically over charge cycles, accumulating internal resistance. Operating systems estimate battery percentage by measuring cell terminal voltage across a calibrated fuel-gauge IC:
  </p>

  <div class="terminal-block full-width-module">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span>
        <span class="term-dot dot-yellow"></span>
        <span class="term-dot dot-green"></span>
        <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Windows CMD / PowerShell • Battery Health Telemetry</span>
      </div>
      <div class="terminal-actions">
        <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
        <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
      </div>
    </div>
    <div class="terminal-body">
      <pre class="code-pre"><code><span class="code-comment"># 1. Generate comprehensive battery health diagnostic report (HTML)</span>
powercfg /batteryreport /output "C:\battery_report.html"

<span class="code-comment"># 2. Inspect Design Capacity vs Full Charge Capacity (Capacity Loss Ratio)</span>
<span class="code-comment"># Health % = (Full Charge Capacity / Design Capacity) * 100</span>
<span class="code-comment"># If Health % < 60% or Cycle Count > 500, replace the battery pack.</span>

<span class="code-comment"># 3. Query active sleep states supported by motherboard firmware (Modern Standby S0ix vs S3)</span>
powercfg /a</code></pre>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: SOHO Wireless Settings &amp; Printer Queue Triage</span>
    <span>Unit 03 • Page 06</span>
  </div>
</article>

<!-- Page 7: SOHO Wireless Settings & Printer Queue Triage -->
<article class="doc-page" id="it3-soho-wireless-printers">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 03 • Page 07</span>
    <span class="meta-tag">Bloom's: Apply / Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">25.</span> SOHO Wireless Security, Frequency Band Planning &amp; Printer Queue Triage
  </h2>

  <p class="lead-para">
    Securing the edge of Small Office / Home Office (SOHO) networks mandates proper radio frequency (RF) channel planning, deployment of cryptographically robust authentication suites (WPA3 SAE), elimination of legacy attack vectors (WPS), and end-to-end spooler queue management for shared networked printers.
  </p>

  <div class="callout callout-key">
    <div class="callout-label"><i data-lucide="wifi"></i> RF SPECTRUM ALLOCATION: 2.4 GHz VS 5 GHz VS 6 GHz</div>
    <div class="callout-body">
      <ul style="margin-top:0.4rem; margin-left:1.25rem; line-height:1.6;">
        <li><strong>2.4 GHz Band (802.11b/g/n/ax):</strong> Spans 2.412–2.484 GHz. High physical penetration through drywall and concrete, but severe congestion. Exactly <strong>three non-overlapping 20 MHz channels</strong> exist in North America / ITU: <strong>Channel 1, Channel 6, and Channel 11</strong>.</li>
        <li><strong>5 GHz Band (802.11a/n/ac/ax):</strong> Spans 5.150–5.850 GHz. Up to 25 non-overlapping 20 MHz channels. Supports 40 MHz, 80 MHz, and 160 MHz channel bonding for gigabit throughput. Lower range and attenuated by solid obstacles.</li>
        <li><strong>6 GHz Band (Wi-Fi 6E / Wi-Fi 7 - 802.11ax/be):</strong> Spans 5.925–7.125 GHz (1,200 MHz contiguous spectrum). Offers up to 14 channels at 80 MHz or 7 channels at 160/320 MHz width with zero legacy Wi-Fi 4/5 backwards-compatibility contention!</li>
      </ul>
    </div>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-main);">
    1. Wireless Security Suite Comparison &amp; Attack Vectors
  </h3>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Security Standard</th>
          <th>Encryption Cipher</th>
          <th>Key Exchange Mechanism</th>
          <th>Vulnerabilities &amp; Current Industry Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>WEP (Wired Equivalent Privacy)</strong></td>
          <td>RC4 Stream Cipher (40/104-bit)</td>
          <td>Static 24-bit Initialization Vector (IV)</td>
          <td><strong>BROKEN:</strong> Weak IV repetition allows total key decryption in under 60 seconds using <code>aircrack-ng</code>. Deprecated by IEEE.</td>
        </tr>
        <tr>
          <td><strong>WPA-Personal</strong></td>
          <td>RC4 with TKIP (Temporal Key Integrity)</td>
          <td>Pre-Shared Key (PSK) / 4-Way Handshake</td>
          <td><strong>DEPRECATED:</strong> Intermediate band-aid designed for legacy WEP silicon; vulnerable to Beck-Tews keystream recovery attacks.</td>
        </tr>
        <tr>
          <td><strong>WPA2-Personal</strong></td>
          <td>AES-CCMP (Counter Mode CBC-MAC)</td>
          <td>Pre-Shared Key (PSK) 4-Way Handshake</td>
          <td><strong>LEGACY ACTIVE:</strong> 4-way handshake vulnerable to offline dictionary/brute-force attacks when captured (WPA 4-way EAPOL capture) and KRACK nonce reuse.</td>
        </tr>
        <tr>
          <td><strong>WPA3-Personal</strong></td>
          <td>AES-GCMP-256 (Galois/Counter Mode)</td>
          <td>Simultaneous Authentication of Equals (SAE)</td>
          <td><strong>CURRENT GOLD STANDARD:</strong> Uses Dragonfly handshake (Zero-Knowledge Proof). Immune to offline dictionary cracking; provides Forward Secrecy; mandates Protected Management Frames (PMF).</td>
        </tr>
        <tr>
          <td><strong>WPS (Wi-Fi Protected Setup)</strong></td>
          <td>PIN / Push-Button method</td>
          <td>8-digit numeric PIN</td>
          <td><strong>CRITICAL VULNERABILITY:</strong> PIN split into 4-digit and 3-digit halves with checksum; vulnerable to Reaver brute-force attacks in ~4 hours. <em>Must be disabled immediately on all SOHO routers!</em></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="font-size: 1.15rem; font-weight: 700; margin-top: 1.75rem; margin-bottom: 0.75rem; color: var(--text-main);">
    2. Network Print Spooler Triage &amp; Driver Models
  </h3>

  <p>
    Network printers connect using either <strong>Standard TCP/IP Port (Port 9100 RAW)</strong> or <strong>Internet Printing Protocol (IPP over Port 631 HTTPS)</strong>. When print jobs freeze or corrupt memory buffers, the print spooler queue must be cleared via CLI:
  </p>

  <div class="terminal-block full-width-module">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span>
        <span class="term-dot dot-yellow"></span>
        <span class="term-dot dot-green"></span>
        <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Administrative CMD • Print Spooler Queue Purge &amp; Reset</span>
      </div>
      <div class="terminal-actions">
        <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
        <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
      </div>
    </div>
    <div class="terminal-body">
      <pre class="code-pre"><code><span class="code-comment"># 1. Stop the Windows Print Spooler service to unlock locked print spool files</span>
net stop spooler

<span class="code-comment"># 2. Force delete all stuck .SHD (Shadow header) and .SPL (Spool data) files</span>
del /Q /F "%systemroot%\System32\Spool\Printers\*.*"

<span class="code-comment"># 3. Restart Print Spooler service in pristine clean state</span>
net start spooler

<span class="code-comment"># 4. Verify printer ports and driver status in PowerShell</span>
Get-Printer | Select-Object Name, PortName, DriverName, PrinterStatus</code></pre>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 03 Practice MCQ Bank</span>
    <span>Unit 03 • Page 07</span>
  </div>
</article>


<!-- Page 6: Unit 3 Practice MCQ Bank (30 Questions) -->
<article class="doc-page" id="practice-mcq-u3-dev">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 03</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreU3Dev">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">24.</span> Unit 03 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Test your diagnostic and engineering knowledge of mobile architectures, peripheral interfaces, electrophotographic printing engines, and storage protocols.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 01 • Laser Print Defect Analysis</div>
      <div class="mcq-q">A laser printer produces printed pages where the text and graphics smear off easily when touched by a finger. Which component has failed?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Primary Charge Roller</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Fuser Assembly (Heating / Pressure Roller)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Transfer Corona Wire</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Polygon Mirror Scanner Motor</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The fuser assembly uses heat (180&deg;C-200&deg;C) and mechanical pressure to melt the plastic polymer resin of toner into paper fibers. If the heating element fails, toner remains loose powder on the page.
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 02 • Solid Black Page Defect</div>
      <div class="mcq-q">If a laser printer outputs a completely solid black page from edge to edge, what physical failure has occurred?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The laser diode is burned out</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The paper tray has the wrong paper weight</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The fuser roller is overheating</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The Primary Corona Wire or Charging Roller failed to apply a negative conditioning charge to the drum</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The Primary Charging Roller applies a uniform -600V charge that repels toner from unwritten areas. If charging fails, the entire drum sits at 0V (attractive), attracting toner across the entire surface.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="3Dev" data-correct="A">
      <div class="mcq-num">Question 03 • NVMe Queue Architecture</div>
      <div class="mcq-q">How many command queues and commands per queue does the NVMe storage protocol support compared to SATA AHCI's single 32-command queue?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Up to 64,000 queues with 64,000 commands each</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Exactly 128 queues with 256 commands each</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 4 queues with 16 commands each</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Unlimited queues with 1 command each</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> NVMe was architected specifically for multi-core parallelism, supporting 64,000 submission and completion queues, each capable of holding 64,000 concurrent commands.
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="3Dev" data-correct="C">
      <div class="mcq-num">Question 04 • Thunderbolt 4 PCIe Allocation</div>
      <div class="mcq-q">What is the mandatory minimum PCIe data bandwidth requirement enforced by the Intel Thunderbolt 4 certification standard?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 10 Gbps</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 16 Gbps</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 32 Gbps (PCIe &times;4 link)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 64 Gbps</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> While Thunderbolt 3 made PCIe 32 Gbps optional (some laptops only wired 16 Gbps), Thunderbolt 4 strictly mandates a full 32 Gbps PCIe link capable of sustaining 3,000 MB/s storage transfers.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 05 • Multipart Carbon Forms</div>
      <div class="mcq-q">Which printing technology must be selected when an application requires generating physical multipart continuous carbon copy invoice forms?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Color Laser Printer</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Impact / Dot Matrix Printer</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Thermal Wax Transfer Printer</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Piezoelectric Inkjet Printer</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Multipart carbon forms require physical mechanical pressure from printhead pins striking through the top sheet to transfer the carbon or chemical dye onto underlying sheets.
      </div>
    </div>

    <!-- Q6 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 06 • M.2 Keying Architecture</div>
      <div class="mcq-q">Which physical M.2 module key supports up to four PCIe lanes (PCIe &times;4) for high-performance NVMe solid-state storage?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A-Key</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> E-Key</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> B-Key</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> M-Key (Socket 3)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> M-Key modules feature a physical notch at pins 59-66 and support the full PCIe &times;4 link required by high-speed NVMe drives.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="A">
      <div class="mcq-num">Question 07 • Laser Printing Transfer Stage</div>
      <div class="mcq-q">What electrical charge does the Transfer Roller apply to the back of the paper during Stage 5 of the laser printing process?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Strong Positive Charge (+600V DC)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Negative Charge (-600V DC)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Neutral Ground (0V)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> High-frequency AC signal</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Because toner particles carry a negative charge (-300V), applying a strong positive charge (+600V) to the rear of the paper electrostatically pulls the toner off the drum onto the paper.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 08 • Direct Thermal Degradation</div>
      <div class="mcq-q">Why are Direct Thermal printers unsuitable for long-term legal archiving or outdoor barcode labels?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> They require liquid ink that evaporates quickly</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Chemically treated thermal paper darkens or fades when exposed to heat, UV sunlight, or friction</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> They can only print on aluminum foil</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The printhead requires cleaning every 10 pages</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Direct thermal paper contains leuco dyes that react to heat. Heat from friction, car dashboards, or UV exposure turns the entire paper black or fades printed text completely within months.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="C">
      <div class="mcq-num">Question 09 • USB Power Delivery 3.1</div>
      <div class="mcq-q">What is the maximum electrical power delivery supported by the USB-PD 3.1 Extended Power Range (EPR) standard over Type-C?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 60 Watts (20V @ 3A)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 100 Watts (20V @ 5A)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 240 Watts (48V @ 5A)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 500 Watts (100V @ 5A)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> USB-PD 3.1 introduced EPR, scaling voltages up to 48V at 5A to deliver up to 240W of DC charging power, sufficient for high-power gaming and workstation laptops.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 10 • Mobile OS Sandboxing</div>
      <div class="mcq-q">How does the Android OS isolate running application processes from one another at the kernel level?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By running each app in a separate hardware BIOS emulator</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By requiring users to enter passwords when switching apps</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By encrypting the entire RAM every 5 minutes</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> By assigning each installed application its own unique Linux User ID (UID) and enforcing Linux DAC / SELinux policies</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Android assigns each application a distinct UID (e.g. `u0_a210`). The underlying Linux kernel enforces filesystem permissions so apps cannot access each other's data directories without explicit permissions.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="A">
      <div class="mcq-num">Question 11 • Laser Printer Drum Cleaning</div>
      <div class="mcq-q">During Stage 1 (Cleaning) of the laser printing cycle, which component neutralizes any residual electrostatic charge remaining on the drum?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Discharge Erase Lamp</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Fuser Heating Lamp</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Primary Corona Wire</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Rubber Squeegee Blade</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> The rubber cleaning blade physically scrapes off leftover toner powder, while the discharge erase lamp (or discharge LED array) floods the OPC drum with light to neutralize all lingering electrical charges.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 12 • OLED vs IPS LCD</div>
      <div class="mcq-q">What engineering characteristic distinguishes OLED smartphone displays from IPS LCD displays?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> OLED requires a high-voltage fluorescent backlight bulb</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> OLED pixels are self-emissive organic diodes that emit their own light, allowing true infinite black levels when pixels are turned completely off</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> OLED cannot display color</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> IPS LCD consumes zero battery power on black screens</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> OLED pixels emit their own light, allowing individual pixels to shut off completely to produce true 0-nit black and infinite contrast ratio. LCD relies on an active LED backlight that always bleeds through dark pixels.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="C">
      <div class="mcq-num">Question 13 • M.2 2280 Dimension Code</div>
      <div class="mcq-q">What are the physical dimensions of an M.2 SSD labeled as form factor '2280'?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 22 inches wide by 80 inches long</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 2.2 cm wide by 8.0 cm thick</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 22 millimeters wide by 80 millimeters long</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 22 pin connector with 80 GB capacity</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> In M.2 nomenclature, the first two digits designate width in mm (22 mm), and the subsequent digits designate length in mm (80 mm).
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 14 • Printer Ghosting Defect</div>
      <div class="mcq-q">What mechanical defect causes a faint "ghost" duplicate image of previously printed text to repeat down a page at exact 3-inch intervals?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Out-of-date printer driver on client PC</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Low Wi-Fi signal strength to printer</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Paper tray friction separation pad is worn</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Damaged OPC drum, defective cleaning blade, or damaged fuser roller coating repeating every revolution</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Ghosting occurs when a roller fails to clean or discharge completely, leaving latent toner residue that re-stamps the page on every complete rotation (where interval = &pi; &times; diameter).
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="A">
      <div class="mcq-num">Question 15 • Mobile MDM Remote Wipe</div>
      <div class="mcq-q">What enterprise capability enables IT systems administrators to erase corporate data from a lost employee mobile device?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Mobile Device Management (MDM) / Mobile Application Management (MAM) Remote Wipe</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Bluetooth Low Energy ping</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Sending an SMS with the word "RESET"</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Calling the cellular carrier to destroy the SIM card</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Enterprise MDM platforms (e.g. Microsoft Intune) communicate with enrolled device OS agents to issue cryptographic remote wipes, securely destroying corporate encryption keys.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 16 • Thermal Paste Thermal Conductivity</div>
      <div class="mcq-q">What typical thermal conductivity rating distinguishes high-performance thermal paste compared to trapped air?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Paste: 0.026 W/mK vs Air: 50 W/mK</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Paste: 5 to 12 W/mK vs Trapped Air: ~0.026 W/mK (Paste is &gt;200&times; better conductor!)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Both have identical thermal conductivity</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Paste: 0 W/mK (Pure insulator)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Trapped air is an outstanding thermal insulator (0.026 W/mK). Thermal paste conducts heat at 5-12 W/mK, bridging microscopic surface valleys to conduct heat efficiently into copper heatpipes.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="C">
      <div class="mcq-num">Question 17 • DisplayPort Daisy Chaining</div>
      <div class="mcq-q">Which DisplayPort feature allows multiple independent monitors to connect in a daisy-chain from a single host GPU output port?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Single-Stream Transport (SST)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> High-Bandwidth Digital Content Protection (HDCP)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Multi-Stream Transport (MST)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Dual-Link DVI</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> DisplayPort 1.2+ Multi-Stream Transport (MST) multiplexes multiple distinct video and audio streams over a single physical cable, allowing daisy-chaining from monitor to monitor.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 18 • Piezoelectric Inkjet Mechanism</div>
      <div class="mcq-q">How does a piezoelectric inkjet printhead eject ink droplets without heating the ink liquid?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Using compressed air tanks</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Using spinning micro-fans behind each nozzle</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Using laser evaporation</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> By applying an electrical charge to a piezoelectric crystal, causing it to change shape and flex, physically pumping ink out the nozzle</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Piezo crystals mechanically distort when voltage is applied, acting like a microscopic pump. Because heat is not used, it supports specialized temperature-sensitive industrial inks.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="A">
      <div class="mcq-num">Question 19 • Laser Printer Writing Stage</div>
      <div class="mcq-q">What physical change occurs to the photosensitive OPC drum during Stage 3 (Writing / Exposing)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Laser light strikes specific image points, lowering electrical resistance and discharging those points from -600V to ~ -100V</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The drum surface is physically etched with tiny grooves by the laser</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Toner is melted onto the drum</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The drum voltage increases to +10,000V</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Photoconductive materials conduct electricity only when illuminated. The laser light drains negative charge to ground, leaving a discharged -100V latent electrostatic image.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 20 • Lithium-ion Degradation</div>
      <div class="mcq-q">Which environmental condition accelerates physical degradation and swelling of lithium-ion mobile batteries?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Operating at room temperature (20&deg;C)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Sustained high temperatures (&gt;40&deg;C) while maintained at 100% continuous state-of-charge</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Discharging to 50% state-of-charge</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Keeping the screen brightness low</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> High ambient heat combined with maximum cell voltage (4.2V-4.4V at 100% charge) accelerates electrolyte decomposition and gas generation, leading to battery swelling and capacity loss.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="C">
      <div class="mcq-num">Question 21 • Thermal Wax Transfer Ribbon</div>
      <div class="mcq-q">Which printing technology uses a thermal printhead to melt a wax- or resin-based ribbon onto synthetic durable label stock?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Direct Thermal</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Impact Dot Matrix</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Thermal Transfer</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Electrophotographic Laser</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Thermal Transfer uses a heated element to melt wax/resin from an ink ribbon onto standard media, creating durable, weatherproof, scratch-resistant barcode labels.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 22 • Touchscreen Digitizer Types</div>
      <div class="mcq-q">Why have Projected Capacitive touchscreens completely replaced resistive touchscreens on modern smartphones?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Resistive screens were too expensive</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Capacitive screens require a plastic stylus to work</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Resistive screens consumed high voltage AC power</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Capacitive screens support multi-touch gestures (pinch-to-zoom), offer superior optical clarity, and detect electrical distortion from human fingers without requiring mechanical pressure</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Capacitive screens detect electrostatic alterations when a conductive finger touches the glass matrix, supporting multi-touch and eliminating the flexible, easily scratched plastic layers of resistive screens.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="A">
      <div class="mcq-num">Question 23 • USB Type-C Reversibility</div>
      <div class="mcq-q">Which pins inside the USB Type-C receptacle negotiate plug orientation and power delivery roles (Source vs Sink)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> CC1 and CC2 (Configuration Channel pins)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> D+ and D- pins</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> VBUS pins</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Shield ground pins</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> The Configuration Channel pins (CC1 and CC2) detect cable orientation upon insertion, establish host/device data roles, and negotiate USB-PD voltage/current contracts.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 24 • Laser Drum Photosensitivity</div>
      <div class="mcq-q">Why must technicians never expose a laser printer Organic Photoconductor (OPC) drum to room lighting for more than a few minutes?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Room light causes the drum to melt</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Prolonged ambient light causes light fatigue (photochemical degradation), permanently damaging the drum's ability to retain electrostatic charge</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Room light permanently magnetizes the drum core</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Light causes toner inside the waste bin to explode</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The OPC layer is sensitive to photons. Extended ambient light exposure causes permanent photo-oxidation and light shock, resulting in faded or blank vertical bands across future printouts.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="C">
      <div class="mcq-num">Question 25 • SATA AHCI Overhead</div>
      <div class="mcq-q">What is the primary architectural factor capping SATA 3.0 SSD real-world performance at ~550 MB/s?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Flash memory chips cannot read faster than 500 MB/s</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Modern operating systems do not support fast SATA drives</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The physical 6 Gbps SATA signaling rate with 8b/10b line encoding limits theoretical raw bus bandwidth to 600 MB/s</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> SATA cables are too thin to carry data</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> SATA 3.0 runs at 6.0 GHz with 8b/10b encoding (20% overhead), providing a maximum theoretical throughput of 600 MB/s (yielding ~550 MB/s net after protocol overhead).
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 26 • Hardware Security Enclave</div>
      <div class="mcq-q">What security advantage is provided by Apple's Secure Enclave or Android Titan M2 security chips?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> They speed up 3D gaming graphics</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> They allow infinite password attempts</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> They double the cellular download bandwidth</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> They process biometrics and disk encryption keys in an isolated CPU core with hardware tamper protection and side-channel attack resistance</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Dedicated security co-processors run their own verified microkernel, separate from the application processor, preventing compromised OS kernels from extracting private encryption keys.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="A">
      <div class="mcq-num">Question 27 • 3D Printing Technologies</div>
      <div class="mcq-q">Which 3D printing technology cures liquid photopolymer resin using an ultraviolet (UV) light projector or laser?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Stereolithography (SLA) / Digital Light Processing (DLP)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Fused Deposition Modeling (FDM)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Selective Laser Sintering (SLS) of nylon powder</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Direct Thermal Deposition</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> SLA/DLP 3D printers use UV light to photo-polymerize liquid resin layer-by-layer, achieving microscopic layer heights (25-50 &mu;m) for high-precision dental and jewelry models.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="B">
      <div class="mcq-num">Question 28 • Laser Printer Maintenance Kits</div>
      <div class="mcq-q">What core hardware components are typically replaced during scheduled laser printer preventative maintenance?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Wi-Fi antenna and RAM chips</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Fuser assembly, transfer roller, paper pickup rollers, and separation pads</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Formatter board and power supply</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Flatbed scanner glass and USB port</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Laser printer maintenance kits replace mechanical wear items: the fuser assembly, transfer roller, and rubber paper-feed rollers/pads that glaze over after thousands of pages.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="C">
      <div class="mcq-num">Question 29 • PCIe Protocol Tunneling</div>
      <div class="mcq-q">Which interface standard allows external desktop graphics cards (eGPUs) to communicate directly with CPU PCIe lanes over a single cable?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> USB 2.0</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> HDMI 2.1</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Thunderbolt 3 / 4 (and USB4 with PCIe tunneling enabled)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Gigabit Ethernet</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Thunderbolt 3/4 encapsulates native PCIe Transaction Layer Packets (TLPs), bridging the host CPU's PCIe root complex to an external chassis at up to 32 Gbps.
      </div>
    </div>

    <div class="mcq-card" data-unit="3Dev" data-correct="D">
      <div class="mcq-num">Question 30 • Direct Thermal Printhead Cleaning</div>
      <div class="mcq-q">What solvent should technicians use to clean carbon and adhesive residue from a thermal label printhead?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Tap water with dish soap</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> WD-40 lubricant</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Acetone (paint thinner)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 99% pure Isopropyl Alcohol (IPA) with a lint-free swab</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> 99% Isopropyl Alcohol rapidly dissolves adhesive residues without leaving conductive water deposits or chemically eroding the glass protective glaze over the thermal resistors.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 03 Conceptual Questions</span>
    <span>Unit 03 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 3 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-u3-dev">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 03</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">25.</span> Unit 3 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted explanations of electrophotography physics, NVMe queueing, and mobile peripheral protocols.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Detail the electrical charge differentials across the OPC drum, developer roller, and paper during the Developing and Transferring stages of laser printing.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>1. Developing Stage:</strong> The unwritten drum surface retains a uniform <strong>-600V</strong> charge. Exposed latent image points are discharged by the laser to <strong>-100V</strong>. The developer roller carries toner charged to <strong>-300V</strong>. Because -300V is more positive than -600V, toner is electrostatically repelled by the unexposed drum areas and leaps onto the more positive -100V discharged latent image.</p>
        <p><strong>2. Transferring Stage:</strong> The toner on the drum sits at -300V. As plain paper passes beneath, the Transfer Roller behind the paper applies a strong positive charge (<strong>+600V DC</strong>). The strong positive electrical field overcomes the drum's attraction, drawing the negatively charged toner particles onto the paper fibers.</p>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Why did legacy SATA AHCI become a massive performance bottleneck for solid-state storage, and how did NVMe resolve this bottleneck?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>SATA AHCI Bottlenecks:</strong> AHCI was engineered in 2004 for spinning mechanical hard drives with high rotational latency. It features only <em>one single command queue</em> limited to 32 commands, connects through the chipset via slow SATA links (capped at 600 MB/s), and requires un-cacheable register reads that waste CPU cycles.</p>
        <p><strong>NVMe Architecture:</strong> NVMe connects directly to CPU PCIe lanes (15.75 GB/s on Gen 5 &times;4). It supports <strong>64,000 independent command queues</strong>, each holding 64,000 commands, allowing multi-core CPUs to submit I/O requests in parallel without locking. In addition, NVMe streamlined the command set and uses a lightweight "doorbell register" write mechanism, cutting host latency by more than 50%.</p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> Contrast Thermal Bubble (Thermal Inkjet) and Piezoelectric Inkjet printhead technologies.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Thermal Bubble Inkjet (Canon / HP):</strong> Uses microscopic resistors inside each ink chamber. When an electrical pulse passes through the resistor, it heats ink to over 300&deg;C in microseconds, creating an expanding vapor steam bubble. The bubble expands, forcing a tiny droplet out of the nozzle. As the bubble collapses, it draws fresh ink into the chamber. <em>Limitation:</em> Heat degrades sensitive dyes and limits ink chemistry.</p>
        <p><strong>Piezoelectric Inkjet (Epson):</strong> Uses a piezo-ceramic crystal behind each nozzle. When an electrical charge is applied, the crystal changes shape and flexes mechanically, acting as an acoustic pump that ejects the droplet. <em>Advantages:</em> Completely cold operation, highly precise droplet volume modulation (variable droplet sizing), and compatibility with diverse industrial solvent, UV-curable, and textile inks.</p>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> Explain how protocol tunneling works over USB4 and Thunderbolt 4 cables to deliver simultaneous display, PCIe, and USB traffic.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>Protocol tunneling multiplexes multiple independent protocol streams into a single high-speed physical transmission link. Instead of translating DisplayPort video or PCIe storage commands into USB packets (which would introduce latency and protocol overhead), the Thunderbolt / USB4 router controller packages native DisplayPort and PCIe Transaction Layer Packets (TLPs) into fixed-size <strong>transport layer tunnel frames</strong>.</p>
        <p>The 40 Gbps physical link dynamically allocates time slots based on demand: video packets receive guaranteed isochronous bandwidth, while storage transfers consume remaining available bandwidth. At the docking station, hardware de-tunneling engines extract the original native packets and forward them to external DisplayPort and PCIe slots with sub-microsecond latency.</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> How does Enterprise Mobile Application Management (MAM) protect corporate data on personal employee smartphones (BYOD)?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>MAM Containerization:</strong> In Bring-Your-Own-Device (BYOD) environments, employees resist full MDM device management because IT could view personal photos or wipe the entire phone. MAM creates an encrypted sandbox containing only managed corporate applications (e.g. Outlook, Teams, OneDrive).</p>
        <p><strong>Security Controls Enforced:</strong>
          <br>&bull; <em>Clipboard Isolation:</em> Disallows copying text from corporate apps into personal apps (e.g. cannot copy text from corporate email into WhatsApp).
          <br>&bull; <em>Encrypted Storage:</em> Corporate files are stored on an isolated AES-256 partition with keys held in device secure enclave.
          <br>&bull; <em>Selective Wipe:</em> If the employee leaves the company, IT issues a <em>Selective Wipe</em> that erases only corporate emails and documents, leaving personal photos, apps, and contacts completely untouched.
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 03 Analytical Problems</span>
    <span>Unit 03 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 3 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-u3-dev">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 03</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">26.</span> Unit 3 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Real-world hardware failure triage, printer electrophotography defect isolation, and high-performance peripheral bus architecture scenarios.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Printer Defect Triage: Diagnosing Repetitive Dark Smudges on Enterprise Network Laser Printer Output</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A department's shared laser printer produces legal documents with a distinct horizontal black smudge repeating down every page at exact 3.0-inch (76 mm) intervals. In addition, toner can be lightly smudged with a thumb on heavy cardstock.</p>
        <p><strong>Diagnostic & Engineering Isolation Protocol:</strong></p>
        <ol>
          <li><strong>The Repetitive Defect Ruler Calculation:</strong> Every rotating cylinder inside a laser printer has a fixed physical diameter (\(d\)). As it rotates, any scratch, pinhole burn, or hardened toner spot on its surface stamps the paper once per revolution. The distance between repeated defects equals the cylinder's circumference:
            $$\text{Distance} = \pi \times \text{Diameter} \implies \text{Diameter} = \frac{76.2\text{ mm}}{3.14159} \approx \mathbf{24.2\text{ mm}}$$
          </li>
          <li><strong>Identify the Defective Component:</strong> Consulting the printer's service manual repetitive defect table reveals:
            <br>&bull; OPC Drum Diameter: 30 mm &rarr; Repeat interval: 94.2 mm (3.7 inches)
            <br>&bull; Primary Charge Roller Diameter: 12 mm &rarr; Repeat interval: 37.7 mm (1.5 inches)
            <br>&bull; <strong>Fuser Upper Heat Roller Diameter: 24.2 mm &rarr; Repeat interval: 76.2 mm (3.0 inches)!</strong>
          </li>
          <li><strong>Root Cause Confirmation:</strong> The Teflon non-stick coating on the upper fuser roller has been physically gouged by a foreign object (such as a paperclip or staple run through the paper feed). Toner accumulates inside the scratch, baking onto the roller and transferring a repeating dark smudge onto every page. Furthermore, the gouge prevents proper thermal conduction, explaining the smudging on heavy cardstock.</li>
          <li><strong>Remediation:</strong> Replace the entire fuser assembly unit and educate staff on removing staples prior to scanning or printing.</li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> Storage Bus Architecture: M.2 NVMe Thermal Throttling in High-Performance Mobile Workstation</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Engineering Challenge:</strong> A software developer running local Docker Kubernetes clusters on a thin laptop experiences severe compilation slowdowns during large builds. Disk benchmarks reveal that a Gen 4 PCIe &times;4 NVMe SSD starts reads at 7,000 MB/s, but after 45 seconds of continuous writing, speed plummets to 350 MB/s—slower than a legacy SATA drive!</p>
        <p><strong>Technical Analysis & Resolution:</strong></p>
        <ul>
          <li><strong>Thermal Throttling Threshold:</strong> High-performance NVMe controllers consume 6 to 9 Watts during sustained sequential writes. Without airflow, the SSD controller ASIC reaches its critical thermal threshold (typically 75&deg;C to 80&deg;C). To protect the NAND flash and controller from thermal damage, the firmware invokes aggressive thermal throttling, inserting idle wait cycles that slash transfer rates to 350 MB/s.</li>
          <li><strong>SLC Cache Exhaustion:</strong> Modern high-density consumer SSDs use TLC (3 bits/cell) or QLC (4 bits/cell) NAND flash, which writes slowly natively (~150-300 MB/s). To advertise multi-gigabyte speeds, SSDs configure a dynamic pseudo-SLC cache buffer (running in fast 1-bit mode). Once the 100GB SLC cache fills during sustained compilation writes, the drive must fold cached data while writing incoming data directly to slow TLC NAND, compounding the thermal speed drop.</li>
          <li><strong>Hardware Fix:</strong> Install a high-conductivity thermal pad (6.0 W/mK) between the M.2 SSD controller and the laptop's aluminum bottom chassis plate, utilizing the chassis as a massive heat sink. Configure the OS power plan to enable PCIe Active State Power Management (ASPM L1.2).</li>
        </ul>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> Mobile Battery Triage: Swollen Lithium-Polymer Cell in Corporate Laptop Fleet</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A corporate executive submits a laptop reporting that the physical glass trackpad is protruding above the palmrest, the left/right click buttons cannot be physically depressed, and the laptop rocks unevenly on a flat conference table.</p>
        <p><strong>Chemical & Safety Analysis:</strong></p>
        <ol>
          <li><strong>Immediate Hazard Identification:</strong> A protruding trackpad is the definitive symptom of a <strong>swollen lithium-ion polymer (LiPo) battery pack</strong> located directly beneath the trackpad. Gaseous swelling occurs due to electrolyte breakdown (outgassing of carbon dioxide, carbon monoxide, and flammable hydrocarbons) caused by excessive heat, overcharging, or internal dendritic short-circuits.</li>
          <li><strong>Critical Safety Protocol:</strong>
            <br>&bull; <em>Fire Risk:</em> Swollen batteries are under mechanical tension. If punctured with a screwdriver or bent, the separator will breach, causing an instantaneous <strong>thermal runaway fire</strong> reaching 600&deg;C with self-oxygenating flame jets that cannot be extinguished by standard water extinguishers.
            <br>&bull; <em>Action:</em> Immediately disconnect the AC adapter. Power down the laptop. Do <em>not</em> charge or puncture the pack. Place the device inside an approved fireproof LiPo safety bag or metal bucket filled with sand.</li>
          <li><strong>Fleet Root Cause:</strong> The laptop spent 18 months docked continuously to a Thunderbolt 4 desk monitor at 100% state-of-charge with high ambient heat. Enforcing a BIOS battery management policy capping maximum charge at <strong>80%</strong> prevents high-voltage electrolyte breakdown across corporate fleets.</li>
        </ol>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> Peripheral Protocol Tunneling: Dual 4K/60Hz Display Bandwidth Contention on Thunderbolt 4 Docks</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>System Engineering Request:</strong> A financial trading desk connects two 4K (3840 &times; 2160) 60Hz 10-bit HDR monitors, a 10GbE network adapter, and an external NVMe scratch drive to a single Thunderbolt 4 dock connected to an Intel Core Ultra laptop.</p>
        <p><strong>Bandwidth Budget Calculation:</strong></p>
        <ul>
          <li><strong>Uncompressed Video Bandwidth:</strong> A single 4K/60Hz 10-bit RGB stream requires:
            $$3840 \times 2160 \times 60\text{ fps} \times 30\text{ bits/pixel} \times 1.25\text{ (8b/10b overhead)} \approx \mathbf{15.68\text{ Gbps}}$$
            Two 4K/60Hz monitors require \(15.68 \times 2 = \mathbf{31.36\text{ Gbps}}\) of continuous DisplayPort video bandwidth!</li>
          <li><strong>Thunderbolt 4 Total Capacity:</strong> The physical cable ceiling is 40 Gbps. If uncompressed video consumes 31.36 Gbps, only ~8.64 Gbps remains for PCIe data, heavily throttling the 10GbE NIC and NVMe SSD.</li>
          <li><strong>Architectural Solution (Display Stream Compression / DSC):</strong> Modern GPUs and Thunderbolt 4 docks utilize VESA <strong>Display Stream Compression (DSC 1.2a)</strong>. DSC provides visually lossless 3:1 compression, reducing each 4K video stream from 15.68 Gbps down to ~5.3 Gbps. Dual 4K displays consume only ~10.6 Gbps, leaving nearly <strong>30 Gbps of pure PCIe bandwidth</strong> for full-speed 10GbE networking and maximum NVMe disk throughput!</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 03 Master MCQ Answer Key</span>
    <span>Unit 03 • Page 08</span>
  </div>
</article>

<!-- Page 9: Master Answer Key Table -->
<article class="doc-page" id="mcq-answer-key-u3-dev">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 03</span>
    <span class="meta-tag">Master Answer Key • 30 Questions</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">27.</span> Unit 3 Master Answer Key Table & Verification Matrix
  </h2>

  <p class="lead-para">
    Complete verified answer keys and core learning objectives for all 30 multiple choice questions in Unit 3.
  </p>

  <div class="table-container">
    <table class="answer-key-table">
      <thead>
        <tr>
          <th>Q#</th>
          <th>Key</th>
          <th>Core Learning Objective & Architectural Topic</th>
          <th>Q#</th>
          <th>Key</th>
          <th>Core Learning Objective & Architectural Topic</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>01</td><td><strong style="color:var(--primary);">B</strong></td><td>Fuser assembly thermal melting of toner into paper</td><td>16</td><td><strong style="color:var(--primary);">B</strong></td><td>Thermal paste conductivity (5-12 W/mK) vs air (0.026 W/mK)</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">D</strong></td><td>Solid black page caused by Primary Corona charging failure</td><td>17</td><td><strong style="color:var(--primary);">C</strong></td><td>DisplayPort Multi-Stream Transport (MST) daisy chaining</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">A</strong></td><td>NVMe 64,000 parallel command queue architecture</td><td>18</td><td><strong style="color:var(--primary);">D</strong></td><td>Piezoelectric crystal mechanical flexing ink ejection</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">C</strong></td><td>Thunderbolt 4 mandated 32 Gbps minimum PCIe link</td><td>19</td><td><strong style="color:var(--primary);">A</strong></td><td>Laser writing stage discharging drum from -600V to -100V</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">B</strong></td><td>Impact dot-matrix mechanical strike for carbon copies</td><td>20</td><td><strong style="color:var(--primary);">B</strong></td><td>High heat and 100% state-of-charge battery swelling</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">D</strong></td><td>M.2 M-Key (Socket 3) PCIe &times;4 high-speed storage standard</td><td>21</td><td><strong style="color:var(--primary);">C</strong></td><td>Thermal transfer wax/resin ribbon durable barcode printing</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">A</strong></td><td>Transfer roller positive electrical charge (+600V DC)</td><td>22</td><td><strong style="color:var(--primary);">D</strong></td><td>Projected Capacitive touchscreen multi-touch advantages</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">B</strong></td><td>Direct thermal paper UV and heat sensitivity degradation</td><td>23</td><td><strong style="color:var(--primary);">A</strong></td><td>USB Type-C Configuration Channel (CC1/CC2) negotiation</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">C</strong></td><td>USB-PD 3.1 Extended Power Range maximum wattage (240W)</td><td>24</td><td><strong style="color:var(--primary);">B</strong></td><td>OPC drum light shock photo-oxidation damage</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">D</strong></td><td>Android Linux unique UID process sandboxing</td><td>25</td><td><strong style="color:var(--primary);">C</strong></td><td>SATA 3.0 6Gbps physical 8b/10b 550 MB/s speed ceiling</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">A</strong></td><td>Discharge erase lamp neutralizing residual drum charge</td><td>26</td><td><strong style="color:var(--primary);">D</strong></td><td>Secure Enclave isolated cryptographic hardware security</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">B</strong></td><td>OLED self-emissive pixels and infinite contrast blacks</td><td>27</td><td><strong style="color:var(--primary);">A</strong></td><td>SLA / DLP photopolymer UV liquid resin curing</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">C</strong></td><td>M.2 2280 metric dimensions (22 mm width &times; 80 mm length)</td><td>28</td><td><strong style="color:var(--primary);">B</strong></td><td>Laser printer maintenance kit wearable mechanical parts</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">D</strong></td><td>Ghosting defects repeating at roller circumference intervals</td><td>29</td><td><strong style="color:var(--primary);">C</strong></td><td>Thunderbolt PCIe protocol tunneling for external GPUs</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">A</strong></td><td>Mobile Device Management (MDM) cryptographic remote wipe</td><td>30</td><td><strong style="color:var(--primary);">D</strong></td><td>99% Isopropyl Alcohol (IPA) thermal printhead cleaning</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 03 Complete • Next: Unit 04 Windows NT Architecture</span>
    <span>Unit 03 • Page 09</span>
  </div>
</article>
"""
