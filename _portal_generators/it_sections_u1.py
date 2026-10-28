# -*- coding: utf-8 -*-
"""
Unit 1: Computer Hardware & Motherboard Architecture
In-depth Engineering Standard style:
- Article it1-formfactors: Motherboard Form Factors, Standoffs, Power Planes & Traces
- Article it1-chipset: Chipsets, PCIe 3.0/4.0/5.0 Bus Architecture, DMI & Lane Encoding
- Article it1-cpu: CPU Microarchitecture, Sockets (LGA vs PGA), Cache Hierarchies (L1/L2/L3)
- Article it1-ram: System Memory (DDR4/DDR5), Multi-Channel Interleaving, CAS Latency Formula
- Article it1-psu: Power Delivery Units (PSU), ATX 24-Pin, EPS12V, 80 Plus Efficiency Curves
- Article practice-mcq-u1-hw: Unit 1 Self-Testing Bank: 30 Multiple Choice Questions
- Article practice-subj-short-u1-hw: Short Conceptual Questions (5 Sets)
- Article practice-subj-long-u1-hw: Analytical & Scenario Problems (4 Sets)
- Article mcq-answer-key-u1-hw: Master Answer Key Table
"""

IT_UNIT1_HTML = """
<!-- ==========================================================================
     UNIT 01: COMPUTER HARDWARE & MOTHERBOARD ARCHITECTURE
     ========================================================================== -->

<!-- Page 1: Form Factors -->
<article class="doc-page" id="it1-formfactors">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 01 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">01.</span> Motherboard Form Factors, Physical Geometries & Electrical Grounding
  </h2>

  <p class="lead-para">
    The motherboard (system board / mainboard) serves as the primary printed circuit board (PCB) establishing high-speed copper interconnects, power distribution planes, and structural mounting points for all computing subsystems. Adherence to industry-standard physical dimensions, mounting hole patterns, and rear I/O shield geometries is dictated by standardized form factor specifications.
  </p>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="zap"></i> Core Acronym: ATX & ITX Evolution</div>
    <p><strong>ATX (Advanced Technology eXtended):</strong> Introduced by Intel in 1995 to replace legacy AT form factors. Defines standard dimensions (12 &times; 9.6 inches), standardized 24-pin power delivery, integrated rear I/O shield, and front-to-rear unidirectional cooling airflow.</p>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Form Factor</th>
          <th>Physical Dimensions</th>
          <th>Mounting Holes</th>
          <th>Max Expansion Slots</th>
          <th>Typical Deployment Target</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Standard ATX</strong></td>
          <td>12.0 &times; 9.6 inches (305 &times; 244 mm)</td>
          <td>9 to 10 mounting standoffs</td>
          <td>Up to 7 PCIe slots</td>
          <td>Enterprise workstations, dual-GPU compute towers</td>
        </tr>
        <tr>
          <td><strong>Micro-ATX (mATX)</strong></td>
          <td>9.6 &times; 9.6 inches (244 &times; 244 mm)</td>
          <td>8 mounting standoffs (backward compatible)</td>
          <td>Up to 4 PCIe slots</td>
          <td>Budget corporate desktops, compact lab nodes</td>
        </tr>
        <tr>
          <td><strong>Mini-ITX</strong></td>
          <td>6.7 &times; 6.7 inches (170 &times; 170 mm)</td>
          <td>4 corner standoffs</td>
          <td>Exactly 1 PCIe slot</td>
          <td>Edge IoT gateways, SOHO firewall appliances, POS terminals</td>
        </tr>
        <tr>
          <td><strong>E-ATX (Extended ATX)</strong></td>
          <td>12.0 &times; 13.0 inches (305 &times; 330 mm)</td>
          <td>12 mounting standoffs</td>
          <td>Up to 8 PCIe slots</td>
          <td>Dual-socket Xeon / EPYC rackmount workstations</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="cpu"></i> Silicon & Electrical Mechanics: PCB Layering & Ground Loops</div>
    <p>
      Modern motherboards utilize <strong>6 to 12 copper layers</strong> sandwiched between FR-4 flame-retardant fiberglass epoxy dielectrics. Dedicated internal copper planes provide pure uninterrupted ground reference (GND) and clean DC power (+12V, +5V, +3.3V). Brass standoffs screwed into the chassis tray are critical: they elevate electrical solder points from bare metal to prevent catastrophic direct short-circuits, while providing a structural chassis grounding path for ESD (Electrostatic Discharge) dissipation. Missing or misplaced brass standoffs under unused PCB areas will cause instantaneous power-rail over-current trip (OVP/UVP) or fire.
    </p>
  </div>

  <div class="callout callout-alert">
    <div class="callout-header"><i data-lucide="alert-triangle"></i> Field Engineering Trap: The I/O Shield Grounding Prongs</div>
    <p>
      The stamped stainless-steel rear I/O shield incorporates tiny flexible spring fingers designed to press tightly against the metal shells of RJ-45, HDMI, and USB ports to suppress electromagnetic interference (EMI). A common novice error is allowing a metal grounding spring prong to poke <em>inside</em> an RJ-45 or USB port during motherboard installation, shorting the 5V rail to ground and causing intermittent reboot loops or failed POST.
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Chipsets & PCIe Bus Topologies</span>
    <span>Unit 01 • Page 01</span>
  </div>
</article>

<!-- Page 2: Chipsets & PCIe -->
<article class="doc-page" id="it1-chipset">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 01 • Page 02</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">02.</span> Chipset Architectures, High-Speed Buses & PCIe Lane Math
  </h2>

  <p class="lead-para">
    The chipset acts as the nervous system of the motherboard, routing data between high-bandwidth peripherals, storage controllers, network controllers, and the CPU. Historically split into a Northbridge and Southbridge architecture, contemporary platforms integrate memory controllers and primary PCIe root complexes directly onto the CPU die, offloading secondary I/O to a unified Platform Controller Hub (PCH).
  </p>

  <div class="diagram-container">
    <div class="diagram-title">Modern SoC + PCH Interconnect Topology</div>
    <div class="arch-stack-visual">
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">CPU DIE (System-on-Chip Integration)</span>
        <div class="tier-desc">Integrated Memory Controller (IMC) • 16-24 Direct PCIe 5.0 Lanes • Integrated GPU • L1/L2/L3 Cache</div>
      </div>
      <div style="text-align: center; color: var(--primary); font-weight: 800; font-family: var(--font-mono); font-size: 11px;">
        &Updownarrow; Intel DMI 4.0 &times;8 (15.75 GB/s) / AMD PCIe 4.0 &times;4 Interconnect (7.88 GB/s) &Updownarrow;
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">PLATFORM CONTROLLER HUB (PCH / Southbridge)</span>
        <div class="tier-desc">SATA 6Gbps RAID • Secondary M.2 NVMe (PCIe 4.0) • USB 3.2 Gen 2x2 • 2.5GbE Ethernet • HD Audio • Intel ME / AMD PSP Firmware</div>
      </div>
    </div>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>PCIe Generation</th>
          <th>Raw Transfer Rate</th>
          <th>Line Encoding</th>
          <th>Bandwidth per Lane (&times;1)</th>
          <th>Bandwidth for Graphics (&times;16)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>PCIe 3.0</strong></td>
          <td>8.0 GT/s</td>
          <td>128b/130b (1.5% overhead)</td>
          <td>~985 MB/s (~1 GB/s)</td>
          <td>15.75 GB/s</td>
        </tr>
        <tr>
          <td><strong>PCIe 4.0</strong></td>
          <td>16.0 GT/s</td>
          <td>128b/130b (1.5% overhead)</td>
          <td>~1,969 MB/s (~2 GB/s)</td>
          <td>31.51 GB/s</td>
        </tr>
        <tr>
          <td><strong>PCIe 5.0</strong></td>
          <td>32.0 GT/s</td>
          <td>128b/130b (1.5% overhead)</td>
          <td>~3,938 MB/s (~4 GB/s)</td>
          <td>63.02 GB/s</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> High-Speed Physics: 128b/130b Encoding vs Legacy 8b/10b</div>
    <p>
      PCIe 1.0 and 2.0 utilized 8b/10b encoding, where 8 bits of data required 10 physical bits on the copper differential pair to maintain DC balance and clock recovery, incurring a massive <strong>20% bandwidth penalty</strong>. PCIe 3.0, 4.0, and 5.0 switched to 128b/130b encoding, where a 2-bit preamble is prepended to a 128-bit payload, slashing physical protocol overhead to just <strong>1.53%</strong>. This enables PCIe 4.0 to achieve 1.97 GB/s per lane from 16 GT/s signaling.
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: CPU Sockets & Cache Hierarchies</span>
    <span>Unit 01 • Page 02</span>
  </div>
</article>

<!-- Page 3: CPU & Cache -->
<article class="doc-page" id="it1-cpu">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 01 • Page 03</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">03.</span> CPU Microarchitecture, Sockets (LGA vs PGA) & SRAM Cache Hierarchy
  </h2>

  <p class="lead-para">
    The Central Processing Unit executes the stored program instruction stream via the hardware Fetch-Decode-Execute pipeline. The physical mounting socket governs pin density, signal integrity, and insertion force, while multi-level Static RAM (SRAM) caching mitigates the von Neumann memory wall latency disparity between register files and main DRAM.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Socket Standard</th>
          <th>Full Name</th>
          <th>Pin Location</th>
          <th>Vulnerable Component</th>
          <th>Typical Vendor Platforms</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>LGA</strong></td>
          <td>Land Grid Array</td>
          <td>Pins located inside motherboard socket; flat copper contact pads on CPU substrate</td>
          <td>Motherboard socket pins (easily bent by accidental drop or touch)</td>
          <td>Intel Core (LGA1700/1851), AMD Ryzen 7000+ (AM5 / LGA1718), Xeon/EPYC</td>
        </tr>
        <tr>
          <td><strong>PGA</strong></td>
          <td>Pin Grid Array</td>
          <td>Pins physically soldered onto bottom of CPU package; socket has receptacle holes (ZIF)</td>
          <td>CPU package pins (prone to bending if dropped or misaligned)</td>
          <td>Legacy AMD Ryzen (AM4), legacy Intel Pentium 4 / Core 2 Duo</td>
        </tr>
        <tr>
          <td><strong>BGA</strong></td>
          <td>Ball Grid Array</td>
          <td>Microscopic solder balls permanently reflowed directly onto motherboard PCB</td>
          <td>Non-removable; entire board requires replacement on CPU failure</td>
          <td>Laptops, smartphones, IoT gateways, embedded routers</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="database"></i> Silicon Hierarchy: Memory Latency Gap (Nanoseconds vs Clock Cycles)</div>
    <p>
      Modern CPUs operate at ~4.0 to 5.5 GHz (1 cycle &approx; 0.2 nanoseconds). Fetching data directly from DRAM takes ~50 to 70 ns (~300 clock cycles of pure pipeline stall). To prevent CPU starvation, a tiered SRAM cache hierarchy is placed directly on the silicon die:
    </p>
    <ul>
      <li><strong>L1 Cache:</strong> Split into L1 Instruction (L1i) and L1 Data (L1d). Ultra-fast (4-5 cycles / ~1 ns latency), private to each core, typical size 32-64 KB.</li>
      <li><strong>L2 Cache:</strong> Dedicated per-core buffer (12-14 cycles / ~3-4 ns latency), size 512 KB to 2 MB per core.</li>
      <li><strong>L3 Cache:</strong> Massive shared pool across all cores on the CCX (Compute Complex), ~35-45 cycles (~10-12 ns latency), size 16 MB to 96 MB (AMD 3D V-Cache).</li>
      <li><strong>Main Memory (DDR4/DDR5):</strong> Off-die DRAM, ~50-80 ns (~300 clock cycles).</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: DDR4 / DDR5 System RAM & Latency Math</span>
    <span>Unit 01 • Page 03</span>
  </div>
</article>

<!-- Page 4: RAM -->
<article class="doc-page" id="it1-ram">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 01 • Page 04</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">04.</span> Dynamic RAM (DDR4 vs DDR5), Multi-Channel Interleaving & True Latency Math
  </h2>

  <p class="lead-para">
    Synchronous Dynamic Random-Access Memory (SDRAM) utilizes microscopic capacitive storage cells requiring periodic electrical refresh cycles. Double Data Rate (DDR) memory transfers data on both the rising and falling edges of the clock signal, doubling operational throughput relative to base bus frequency.
  </p>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="calculator"></i> Mathematical Formula: True Memory Latency</div>
    <p>
      $$\text{True Latency (nanoseconds)} = \left(\frac{\text{CAS Latency (CL)}}{\text{Data Rate in MT/s} / 2}\right) \times 1000$$
      <strong>Example Comparison:</strong>
      <br>&bull; <em>DDR4-3200 CL16:</em> \((16 / 1600) \times 1000 = \mathbf{10.0\text{ ns}}\)
      <br>&bull; <em>DDR5-6000 CL30:</em> \((30 / 3000) \times 1000 = \mathbf{10.0\text{ ns}}\) (Identical first-word latency, but DDR5 delivers <strong>87.5% greater continuous burst bandwidth</strong>: 48 GB/s vs 25.6 GB/s!).
    </p>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Specification Metric</th>
          <th>DDR4 Standard</th>
          <th>DDR5 Standard</th>
          <th>Architectural Advantage</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Operating Voltage (VDD)</strong></td>
          <td>1.2 Volts</td>
          <td>1.1 Volts</td>
          <td>~20% power reduction and lower thermal dissipation</td>
        </tr>
        <tr>
          <td><strong>Power Management</strong></td>
          <td>Regulated by motherboard VRM</td>
          <td>Integrated PMIC directly on DIMM PCB</td>
          <td>Tighter voltage regulation, reduced mother board trace noise</td>
        </tr>
        <tr>
          <td><strong>Channel Architecture</strong></td>
          <td>Single 64-bit data channel per DIMM</td>
          <td>Dual independent 32-bit subchannels per DIMM</td>
          <td>Doubled concurrent memory access efficiency; reduced latency</td>
        </tr>
        <tr>
          <td><strong>Burst Length</strong></td>
          <td>BL8 (8 transfers per access)</td>
          <td>BL16 (16 transfers per access)</td>
          <td>Matches modern 64-byte CPU cache line in a single subchannel burst</td>
        </tr>
        <tr>
          <td><strong>On-Die ECC</strong></td>
          <td>None (Standard non-ECC)</td>
          <td>Native On-Die Single-Bit Error Correction</td>
          <td>Corrects bit-flips inside memory cell arrays at sub-10nm nodes</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="cpu"></i> Multi-Channel Interleaving: Channel A2 & B2 Priority</div>
    <p>
      To achieve dual-channel 128-bit memory bus width on a 4-DIMM motherboard, modules must be installed into <strong>Slots 2 and 4 (A2 and B2)</strong> counting outward from the CPU socket. This design choice is dictated by <em>daisy-chain motherboard trace topology</em>: placing memory modules at the physical termination point of the trace prevents signal reflection and stub interference, allowing high XMP/EXPO overclock frequencies (e.g. 6000+ MT/s) to remain stable without bit degradation.
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Power Supply Units & Voltage Regulation</span>
    <span>Unit 01 • Page 04</span>
  </div>
</article>

<!-- Page 5: PSU -->
<article class="doc-page" id="it1-psu">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 01 • Page 05</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">05.</span> Power Supply Units (PSU), Voltage Rails & 80 Plus Efficiency Curves
  </h2>

  <p class="lead-para">
    The Switched-Mode Power Supply (SMPS) rectifies alternating current (110V/230V AC mains at 50/60 Hz) into regulated, ripple-free direct current (DC) rails (+12V, +5V, +3.3V, +5VSB) required by delicate silicon transistors. Power delivery involves complex modular harness pinouts and hardware protection circuits.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>DC Voltage Rail</th>
          <th>Primary Silicon Components Powered</th>
          <th>Color Convention (ATX)</th>
          <th>Typical Modern Load Share</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>+12V Rail</strong></td>
          <td>CPU VRMs, Discrete GPU PCIe slots/cables, liquid cooling pumps, 12V fans, HDD spindle motors</td>
          <td>Yellow</td>
          <td><strong>&gt; 90% of total system wattage</strong></td>
        </tr>
        <tr>
          <td><strong>+5V Rail</strong></td>
          <td>SATA SSD/HDD logic controllers, USB port power (+5V DC), RGB lighting microcontrollers</td>
          <td>Red</td>
          <td>~5-7% of total wattage</td>
        </tr>
        <tr>
          <td><strong>+3.3V Rail</strong></td>
          <td>Motherboard chipset logic, PCIe slot auxiliary power, M.2 NVMe SSD controllers</td>
          <td>Orange</td>
          <td>~2-4% of total wattage</td>
        </tr>
        <tr>
          <td><strong>+5VSB (Standby)</strong></td>
          <td>Wake-on-LAN (WOL) NIC, motherboard power button sense circuit, USB wake devices while PC is soft-off</td>
          <td>Purple</td>
          <td>Max 2 to 3 Amps (~15 Watts)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="shield-check"></i> Power Supply Protection Circuits (OCP, OVP, UVP, SCP, OTP)</div>
    <p>
      High-grade enterprise power supplies incorporate a dedicated supervisory integrated circuit (e.g. Weltrend WT7527) monitoring physical voltage and current thresholds:
    </p>
    <ul>
      <li><strong>OCP (Over-Current Protection):</strong> Shuts down rail if load exceeds safe amperage (preventing melted 12VHPWR cables).</li>
      <li><strong>OVP / UVP (Over / Under-Voltage Protection):</strong> Trips if +12V swings above +13.2V or drops below +10.8V (&plusmn;10% tolerance limit).</li>
      <li><strong>SCP (Short-Circuit Protection):</strong> Disables primary switching transistors within <strong>sub-microsecond intervals</strong> if resistance to ground drops near zero.</li>
      <li><strong>PWR_OK (Power Good Signal):</strong> Pin 8 (Gray wire). The PSU holds this line at 0V until internal DC rails stabilize at proper voltages for 100-500 ms, then pulls it to +5V, signaling the motherboard clock generator to release the CPU reset line and commence POST.</li>
    </ul>
  </div>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="award"></i> 80 Plus Efficiency Hierarchy at 50% Typical Load</div>
    <p>
      PSUs achieve peak electrical efficiency at <strong>50% load</strong>. Energy lost is dissipated as pure heat:
      <br>&bull; <strong>80 Plus Standard:</strong> 80% efficiency (20% wasted as heat)
      <br>&bull; <strong>80 Plus Bronze:</strong> 85% efficiency
      <br>&bull; <strong>80 Plus Gold:</strong> 90% efficiency (Corporate IT deployment baseline)
      <br>&bull; <strong>80 Plus Platinum:</strong> 92% efficiency
      <br>&bull; <strong>80 Plus Titanium:</strong> 94% efficiency at 50% load, with mandated &ge;90% efficiency at light 10% load!
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 01 Practice MCQ Bank</span>
    <span>Unit 01 • Page 05</span>
  </div>
</article>

<!-- Page 6: Unit 1 Practice MCQ Bank (30 Questions) -->
<article class="doc-page" id="practice-mcq-u1-hw">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 01</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreU1HW">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">06.</span> Unit 01 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Test your mastery of motherboard architectures, CPU sockets, cache latency, RAM interleaving, and power supply electrical rails. Click any option for instant visual feedback and architectural rationale.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 01 • Motherboard Form Factors</div>
      <div class="mcq-q">What are the exact physical dimensions of a standard ATX motherboard?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 9.6 &times; 9.6 inches (244 &times; 244 mm)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 12.0 &times; 9.6 inches (305 &times; 244 mm)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 6.7 &times; 6.7 inches (170 &times; 170 mm)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 12.0 &times; 13.0 inches (305 &times; 330 mm)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Standard ATX dimensions are 12 &times; 9.6 inches (305 &times; 244 mm). 9.6 &times; 9.6 is Micro-ATX, and 6.7 &times; 6.7 is Mini-ITX.
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 02 • Mini-ITX Expansion</div>
      <div class="mcq-q">How many PCIe expansion slots are provided on a standard Mini-ITX motherboard?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 4 slots</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 2 slots</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Exactly 1 slot</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 7 slots</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Due to the ultra-compact 6.7 &times; 6.7 inch PCB area, Mini-ITX motherboards accommodate exactly one PCIe expansion slot.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="1HW" data-correct="D">
      <div class="mcq-num">Question 03 • Socket Architecture</div>
      <div class="mcq-q">In an LGA (Land Grid Array) socket, where are the delicate conductive pins physically located?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Soldered to the bottom of the CPU package</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Inside the PCIe expansion slots</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> On the heatsink baseplate</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Inside the motherboard socket itself</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> In LGA sockets (Intel LGA1700, AMD AM5), the spring-loaded conductive pins reside inside the motherboard socket, contacting flat gold pads on the CPU substrate.
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="1HW" data-correct="A">
      <div class="mcq-num">Question 04 • Modern Chipsets</div>
      <div class="mcq-q">Which critical controller was moved from the legacy Northbridge directly onto the CPU die in modern processors?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Integrated Memory Controller (IMC)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> SATA RAID Controller</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Realtek High-Definition Audio Codec</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Super I/O Controller</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Moving the Integrated Memory Controller (IMC) onto the CPU die eliminated the Front-Side Bus (FSB) bottleneck, drastically slashing memory access latency.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 05 • PCIe 4.0 Bandwidth</div>
      <div class="mcq-q">What is the approximate theoretical unidirectional bandwidth of a single PCIe 4.0 lane (&times;1)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ~500 MB/s</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ~1,969 MB/s (~2 GB/s)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> ~985 MB/s (~1 GB/s)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> ~3,938 MB/s (~4 GB/s)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> PCIe 4.0 transfers at 16 GT/s with 128b/130b encoding, delivering approximately 1.97 GB/s (~2 GB/s) per lane in each direction.
      </div>
    </div>

    <!-- Q6 -->
    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 06 • Memory Latency Formula</div>
      <div class="mcq-q">What is the true first-word latency of DDR4-3200 memory operating at CAS Latency 16 (CL16)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 5.0 nanoseconds</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 16.0 nanoseconds</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 10.0 nanoseconds</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 20.0 nanoseconds</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> True latency = (CL / (DataRate / 2)) * 1000 = (16 / 1600) * 1000 = 10.0 ns.
      </div>
    </div>

    <!-- Q7 -->
    <div class="mcq-card" data-unit="1HW" data-correct="A">
      <div class="mcq-num">Question 07 • DDR5 Channel Architecture</div>
      <div class="mcq-q">How does DDR5 redesign the memory channel architecture of a single physical DIMM?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It splits the single 64-bit channel into two independent 32-bit subchannels</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It combines two DIMMs into a single 16-bit channel</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It removes the memory bus completely in favor of serial PCIe</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It expands the data bus to a single 256-bit channel</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Each DDR5 DIMM features two independent 32-bit channels (plus 8-bit ECC), allowing concurrent command issuing and greater memory access concurrency.
      </div>
    </div>

    <!-- Q8 -->
    <div class="mcq-card" data-unit="1HW" data-correct="D">
      <div class="mcq-num">Question 08 • Motherboard Standoffs</div>
      <div class="mcq-q">What is the primary electrical hazard of failing to install brass motherboard standoffs?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> CPU socket pins will bend</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> RAM will only operate in single-channel mode</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The PSU fan will spin backwards</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Direct electrical short between PCB solder traces and the conductive chassis tray</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Standoffs elevate the motherboard PCB above the metal case tray. Direct metal contact shorts the voltage rails to ground, triggering PSU shutdown or catastrophic component damage.
      </div>
    </div>

    <!-- Q9 -->
    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 09 • Power Supply Rails</div>
      <div class="mcq-q">Which DC voltage rail supplies more than 90% of the electrical power consumed by modern CPUs and GPUs?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> +5V Rail</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> +12V Rail</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> +3.3V Rail</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> -12V Rail</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Modern computing architectures draw virtually all heavy power from the +12V rail, which is subsequently stepped down to sub-1.3V core voltages by motherboard and GPU VRMs.
      </div>
    </div>

    <!-- Q10 -->
    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 10 • Power Good Signal</div>
      <div class="mcq-q">What is the purpose of the PWR_OK (Power Good) wire (Pin 8, Gray) on the ATX 24-pin connector?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Powers the front-panel power LED</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Triggers a soft reboot of the operating system</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Signals the motherboard that DC voltages are stabilized so the CPU can begin POST</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Provides auxiliary +12V power to the PCIe slot</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> The PSU asserts +5V on the PWR_OK line only after internal DC voltages have stabilized within safe tolerances for 100-500 ms, releasing the CPU from reset.
      </div>
    </div>

    <!-- Q11 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="1HW" data-correct="A">
      <div class="mcq-num">Question 11 • CPU Caching</div>
      <div class="mcq-q">Which level of CPU cache is typically shared among all physical processor cores on a silicon CCX?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> L3 Cache</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> L1 Data Cache</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> L1 Instruction Cache</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> L2 Cache</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> L3 cache represents the Last-Level Cache (LLC) shared across all cores within a cluster, facilitating inter-core communication and coherent memory buffering.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 12 • DDR5 Power Regulation</div>
      <div class="mcq-q">Where is the Power Management Integrated Circuit (PMIC) located in a DDR5 memory architecture?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Inside the ATX power supply</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Mounted directly on the physical DIMM PCB</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Inside the motherboard chipset</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> In the CPU L2 cache controller</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> DDR5 relocated voltage regulation from the motherboard directly onto the memory module via an onboard PMIC, reducing electrical noise and trace impedance.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 13 • Dual-Channel Installation Priority</div>
      <div class="mcq-q">When installing two memory modules on a 4-slot motherboard with daisy-chain topology, which slots provide maximum signal stability?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Slots A1 and B1 (Slots 1 and 3)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Slots A1 and A2 (Slots 1 and 2)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Slots A2 and B2 (Slots 2 and 4)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Slots B1 and B2 (Slots 3 and 4)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Slots 2 and 4 (A2 and B2) sit at the physical termination of the daisy-chain traces. Installing modules here prevents unterminated trace stubs from reflecting electrical noise.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="D">
      <div class="mcq-num">Question 14 • 80 Plus Efficiency Benchmark</div>
      <div class="mcq-q">At what operational load percentage do standard switched-mode power supplies achieve their peak electrical efficiency?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 10% load</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 100% full capacity load</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 20% light load</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 50% typical load</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The efficiency curve of an SMPS peaks at approximately 50% load, which is why system builders size power supplies to operate near 50% during heavy workstation use.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="A">
      <div class="mcq-num">Question 15 • Line Encoding Efficiency</div>
      <div class="mcq-q">What is the physical protocol overhead of PCIe 3.0/4.0/5.0 using 128b/130b encoding compared to legacy 8b/10b?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ~1.5% overhead compared to 20% in 8b/10b</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ~50% overhead compared to 10% in 8b/10b</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 0% overhead (pure lossless transmission)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Exactly equal to 8b/10b overhead</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> 128b/130b encoding prepends only 2 framing bits to 128 data bits (1.53% overhead), whereas 8b/10b added 2 bits to every 8 data bits (20% overhead).
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 16 • Standby Power</div>
      <div class="mcq-q">Which power supply line remains active when the host computer is shut down in an ACPI G2/S5 soft-off state?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> +12V Primary Rail</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> +5VSB (Standby Rail)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> -12V Rail</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> PWR_OK Rail</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The +5VSB (Standby) rail powers the motherboard power-button logic, Wake-on-LAN network interfaces, and real-time clock circuitry even when the system is off.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 17 • Thermal Interface Material</div>
      <div class="mcq-q">What is the primary physical function of Thermal Interface Material (thermal paste) applied between CPU and heatsink?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Glues the heatsink permanently to the socket</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Acts as an electrical conductor to ground the CPU lid</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Fills microscopic air valleys between metal surfaces to eliminate insulating air pockets</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Insulates the CPU die against excessive fan airflow</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Microscopic imperfections on machined copper/aluminum surfaces trap air (a terrible heat conductor at 0.026 W/mK). Thermal paste (4-12 W/mK) displaces the air, establishing unbroken conduction.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="D">
      <div class="mcq-num">Question 18 • Over-Current Protection</div>
      <div class="mcq-q">Which PSU safety circuit shuts down the power supply if an excessive electrical current draw occurs on a specific voltage rail?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> OVP (Over-Voltage Protection)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> UVP (Under-Voltage Protection)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> OTP (Over-Temperature Protection)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> OCP (Over-Current Protection)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> OCP monitors current flow across individual rails via shunt resistors, tripping a latching shutdown if current exceeds safe amperage.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="A">
      <div class="mcq-num">Question 19 • DDR5 Operating Voltage</div>
      <div class="mcq-q">What is the standard JEDEC operating voltage for DDR5 memory modules?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 1.1 Volts</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 1.5 Volts</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 1.2 Volts</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 2.5 Volts</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> JEDEC standard DDR5 operates at 1.1V (down from 1.2V in DDR4 and 1.5V in DDR3), providing significant power savings.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 20 • POST Diagnostic Engine</div>
      <div class="mcq-q">During the Power-On Self-Test (POST), in what standard chronological sequence does the firmware initialize core hardware?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> GPU &rarr; Storage &rarr; CPU &rarr; RAM</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> CPU &rarr; RAM &rarr; GPU/Display &rarr; Boot Storage</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Storage &rarr; RAM &rarr; GPU &rarr; CPU</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> RAM &rarr; GPU &rarr; CPU &rarr; Storage</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> POST executes in a strict dependency sequence: first verify the CPU registers/ALU, second train and verify RAM, third initialize video (GPU) to enable diagnostic display, fourth enumerate boot drives.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 21 • BGA Package Application</div>
      <div class="mcq-q">Where is Ball Grid Array (BGA) CPU packaging almost universally encountered?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Dual-socket enterprise rackmount servers</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> High-end desktop user-upgradable gaming towers</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Ultra-thin laptops, smartphones, and embedded single-board computers</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Storage Area Network disk arrays</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> BGA chips are permanently soldered to the PCB using microscopic solder balls, maximizing compactness in thin laptops and mobile devices where user CPU swapping is impossible.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="D">
      <div class="mcq-num">Question 22 • CPU L1 Cache Characteristics</div>
      <div class="mcq-q">What is the typical access latency of a modern CPU L1 cache?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 50 to 80 nanoseconds</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 10 to 12 nanoseconds</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 250 to 500 clock cycles</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 4 to 5 clock cycles (~1 nanosecond)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> L1 cache is built from ultra-low-latency 6T/8T SRAM transistors located adjacent to the execution pipeline, executing loads in 4-5 clock cycles (~1 ns).
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="A">
      <div class="mcq-num">Question 23 • Voltage Ripple</div>
      <div class="mcq-q">Why is low DC voltage ripple (&lt;20 mV peak-to-peak) critical on the +12V rail supplying modern CPUs?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> High ripple introduces voltage spikes that destabilize sub-1.2V semiconductor switching thresholds</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> High ripple causes the power cord to overheat</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Ripple reverses the rotation direction of the CPU fan</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Low ripple prevents the monitor from going to sleep</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> At high clock frequencies and low core voltages (~1.0V), excessive ripple noise causes logic gate voltage ambiguity, causing spontaneous BSODs and corrupted register data.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 24 • On-Die ECC</div>
      <div class="mcq-q">What limitation distinguishes DDR5 On-Die ECC from true Enterprise Sideband ECC (72-bit)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> On-Die ECC only works when running Linux</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> On-Die ECC only corrects bit-flips inside the memory cell arrays, not data in flight over the bus to the CPU</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> On-Die ECC requires 12 extra pins on the motherboard</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> On-Die ECC cannot detect single-bit errors</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> DDR5 On-Die ECC corrects errors internal to the DRAM silicon dies during refresh. True enterprise ECC uses additional physical ICs to protect the entire bus transit path into the CPU IMC.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 25 • CPU Throttling</div>
      <div class="mcq-q">What hardware protective mechanism triggers when a CPU die reaches its TjMax (e.g. 100&deg;C)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The PSU instantly cuts all power</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The operating system formats the primary drive</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Thermal throttling automatically drops core clock multipliers and core voltages (PROCHOT#)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> All RAM channels are immediately disabled</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> At TjMax, the internal digital thermal sensor asserts PROCHOT# (Processor Hot), causing the internal power control unit (PCU) to throttle clock multipliers and reduce voltage to prevent silicon electromigration.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="D">
      <div class="mcq-num">Question 26 • DMI Interconnect</div>
      <div class="mcq-q">What is the role of Intel's Direct Media Interface (DMI) on modern desktop motherboards?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Connects the CPU directly to the primary graphics card</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Transfers audio signals to the front-panel headphone jack</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Bridges the primary RAM slots to the second RAM slots</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Serves as the point-to-point PCIe-based link between the CPU and the Platform Controller Hub (PCH)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> DMI (Direct Media Interface) is Intel's proprietary high-speed PCIe-based link connecting the processor to the Southbridge/PCH chipset.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="A">
      <div class="mcq-num">Question 27 • 12VHPWR Connector</div>
      <div class="mcq-q">What safety feature distinguishes the PCIe Gen 5 12VHPWR (12+4 pin) power connector from legacy 8-pin PCIe cables?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 4 sideband sense pins (SENSE0/SENSE1) that negotiate wattage limits (150W-600W) before drawing power</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It operates entirely on +5V instead of +12V</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It uses wireless induction to eliminate physical pins</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It has integrated liquid cooling tubes inside the cable sleeve</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> The four micro-sideband pins (SENSE0 and SENSE1) physically communicate the maximum wattage capability (150W, 300W, 450W, or 600W) between the PSU and GPU prior to power delivery.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="B">
      <div class="mcq-num">Question 28 • UEFI Secure Boot</div>
      <div class="mcq-q">Which cryptographic standard is verified by UEFI Secure Boot before executing the OS bootloader (bootmgfw.efi)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Symmetric AES-256 pre-shared key</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Digital signature verification against authorized database keys (db) enrolled in NVRAM</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> User plaintext password entered in BIOS</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Hardware MAC address hash</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Secure Boot checks the digital signature of all EFI binaries against the Signature Database (db) and rejects any binary matching the Revoked Signatures Database (dbx) to prevent bootkits.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="C">
      <div class="mcq-num">Question 29 • Front-Panel Pinout</div>
      <div class="mcq-q">Which front-panel motherboard header connector is NOT polarity-sensitive and can be installed in either orientation?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Power LED (PWR_LED)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Hard Drive Activity LED (HDD_LED)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Power Switch (PWR_SW) / Reset Switch (RESET_SW)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Internal Motherboard Speaker (SPK)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> The Power Switch and Reset Switch are momentary contact switches that simply bridge two pins to ground. Because LEDs are diodes, they require correct positive/negative polarity.
      </div>
    </div>

    <div class="mcq-card" data-unit="1HW" data-correct="D">
      <div class="mcq-num">Question 30 • PCIe Lane Bifurcation</div>
      <div class="mcq-q">What is PCIe lane bifurcation on a motherboard?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Doubling the clock frequency of the PCIe bus</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Switching a PCIe slot from Gen 4 to Gen 3 mode</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Converting an x16 slot into an HDMI video output</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Splitting a single physical x16 slot electrically into multiple logical links (e.g. x8/x8 or x4/x4/x4/x4)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Bifurcation configures the PCIe root complex to subdivide an x16 slot into independent channels (e.g. x4/x4/x4/x4), allowing quad M.2 NVMe carrier cards to address all four SSDs without an expensive PLX bridge chip.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 01 Conceptual Questions</span>
    <span>Unit 01 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 1 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-u1-hw">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 01</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">07.</span> Unit 1 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted technical explanations demonstrating mastery of hardware architectural principles. Click each card to reveal the engineering response.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Contrast Land Grid Array (LGA) and Pin Grid Array (PGA) packaging from an engineering and repairability perspective.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>1. Pin Placement:</strong> In LGA (Intel LGA1700, AMD AM5), the spring-loaded conductive pins reside inside the motherboard socket, contacting flat gold land pads on the CPU substrate. In PGA (legacy AM4), pins are soldered to the CPU package and insert into a Zero Insertion Force (ZIF) socket.</p>
        <p><strong>2. Failure Economics:</strong> LGA shifts mechanical risk from the expensive CPU to the motherboard. If a pin is bent during handling, replacing a motherboard is typically cheaper than replacing a high-tier workstation CPU. In addition, LGA supports substantially higher pin densities (e.g., LGA4677 server sockets) required for wide multi-channel memory and high PCIe lane counts.</p>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Explain how DDR5 On-Die ECC functions and why enterprise servers still mandate sideband Registered ECC (RDIMM).</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>DDR5 On-Die ECC:</strong> As semiconductor manufacturing scaled down below 14nm, memory cells became so densely packed that cell leakage and single-event upsets (bit flips) skyrocketed. DDR5 integrates an ECC engine directly on each DRAM silicon die that generates parity bits during write and corrects single-bit flips internally during read/refresh cycles.</p>
        <p><strong>Why Enterprise Still Requires RDIMM:</strong> On-Die ECC only protects data while sitting inside the DRAM cell array. It does <em>not</em> protect data in transit across the physical copper traces connecting the memory module to the CPU Integrated Memory Controller (IMC). Enterprise sideband ECC (72-bit bus with 64 data bits + 8 parity bits) uses an external register and parity checking to protect the entire end-to-end memory bus against electrical interference and trace noise.</p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> Detail the role of the ATX PWR_OK (Power Good) signal in preventing semiconductor logic corruption during cold boot.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>When an SMPS power supply is switched on, its internal capacitors, transformers, and switching MOSFETs require time (typically 100 to 500 milliseconds) to stabilize the +12V, +5V, and +3.3V rails within their strict &plusmn;5% voltage tolerance windows.</p>
        <p>If the CPU began executing instructions while voltages were fluctuating (e.g. +3.3V rail at +2.1V), logic gates would fail to switch reliably, causing random instruction execution, corrupted register states, and permanent disk sector damage. To prevent this, the PSU holds the PWR_OK line (Pin 8) low at 0V. The motherboard clock generator holds the CPU in a continuous hardware RESET state. Only after all voltage rails stabilize does the PSU pull PWR_OK high to +5V, releasing the CPU to execute the first firmware instruction from the reset vector (0xFFFFFFF0).</p>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> Why is Daisy-Chain motherboard memory trace topology preferred for high-speed two-DIMM overclocking, and why are slots A2/B2 populated first?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Daisy-Chain vs T-Topology:</strong> In daisy-chain routing, memory signal traces run directly from the CPU memory controller to Slot 1, and then continue onward to terminate at Slot 2. In T-Topology, the trace splits symmetrically into two branches of identical length.</p>
        <p><strong>Why A2 and B2 Must Be Populated:</strong> Slots 2 and 4 (A2 and B2) sit at the physical termination point of the copper trace. If a user installs memory into Slot 1 (A1) and leaves Slot 2 empty, the open copper trace extending past Slot 1 acts as an unterminated RF antenna (a "stub"). High-frequency electrical pulses (3+ GHz) reflect off the open end and bounce back into Slot 1, causing signal interference and bit corruption. Populating the end of the trace (A2/B2) properly terminates the line and ensures signal integrity.</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> Calculate the true first-word latency of DDR4-3600 CL18 vs DDR5-6000 CL36, and explain why DDR5 offers superior gaming and compute throughput despite identical latency.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>1. Latency Calculations:</strong>
          <br>&bull; DDR4-3600 CL18: \((18 / 1800) \times 1000 = \mathbf{10.0\text{ nanoseconds}}\)
          <br>&bull; DDR5-6000 CL36: \((36 / 3000) \times 1000 = \mathbf{12.0\text{ nanoseconds}}\)
        </p>
        <p><strong>2. Throughput Advantage:</strong> While the first-word access time is slightly higher on DDR5-6000, once the initial memory row is opened, DDR5 transfers data at 6000 MT/s (48.0 GB/s per channel) compared to 3600 MT/s (28.8 GB/s per channel) on DDR4. Furthermore, DDR5 features dual independent 32-bit subchannels per DIMM and doubled burst length (BL16), allowing it to service two memory requests concurrently and saturate modern multi-threaded CPU pipelines.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 01 Analytical Problems</span>
    <span>Unit 01 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 1 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-u1-hw">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 01</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">08.</span> Unit 1 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Rigorous real-world hardware triage and engineering design challenges modeling senior systems engineer responsibilities.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Root-Cause Analysis: Newly Assembled CAD Workstation Trips Power Instantly Upon Power-Button Press</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A systems technician completes assembly of an ATX workstation with an Intel Core i9-14900K and an 850W Gold PSU. When pressing the front power button, the case fans twitch for approximately 100 milliseconds, an audible "click" is heard from the power supply, and the system immediately powers off completely. Pressing the power button again does nothing until the AC power cord is unplugged and reconnected.</p>
        <p><strong>Step-by-Step Diagnostic Protocol:</strong></p>
        <ol>
          <li><strong>Identify the Protective State:</strong> The audible click followed by refusal to re-trigger until AC mains discharge indicates the PSU supervisory IC has tripped a <em>latching protection circuit</em> (specifically Short-Circuit Protection / SCP or Over-Current Protection / OCP).</li>
          <li><strong>Common Assembly Blunders:</strong>
            <ul>
              <li><em>Standoff Misplacement:</em> An extra brass motherboard standoff installed under the PCB where no mounting hole exists, directly shorting a +12V or +5V solder trace to the chassis tray.</li>
              <li><em>EPS12V vs PCIe Cable Reversal:</em> Novice builders frequently force an 8-pin PCIe power cable into the 8-pin EPS12V motherboard CPU power socket. PCIe 8-pin connectors have 3 yellow +12V wires on top and 5 grounds on bottom; EPS12V has 4 +12V wires on the latch side and 4 grounds on the other. Connecting a PCIe cable to EPS12V creates a direct, zero-resistance short of the +12V rail straight into ground!</li>
              <li><em>I/O Shield Grounding Tab:</em> An EMI grounding spring tab folded into the interior of an RJ-45 or USB-A port, bridging the +5V bus pin to chassis ground.</li>
            </ul>
          </li>
          <li><strong>Isolation Triage:</strong> Disconnect all internal modular cables. Execute the "paperclip test" on the 24-pin connector (short Pin 16 PS_ON# Green to Pin 17 Ground Black). If the PSU fan spins steadily, the PSU is functional and the short resides on the motherboard/cabling. Reinstall the motherboard outside the chassis on a non-conductive cardboard box (breadboarding) to eliminate chassis shorts.</li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> PCIe Bandwidth & Storage Architecture: Evaluating Quad M.2 NVMe Carrier Cards on Mainstream vs HEDT Platforms</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>System Engineering Request:</strong> A video editing studio requests an expansion card holding four PCIe 4.0 &times;4 M.2 NVMe SSDs in a single PCIe &times;16 slot to create a 32TB high-speed scratch disk array capable of 28 GB/s sustained read speeds.</p>
        <p><strong>Architectural Feasibility Analysis:</strong></p>
        <ul>
          <li><strong>Mainstream Desktop (e.g. Intel Z790 / AMD B650):</strong> Mainstream desktop CPUs only route 16 dedicated PCIe lanes to the primary expansion slot. To recognize four individual SSDs on a passive carrier card, the motherboard BIOS must support <em>PCIe Lane Bifurcation</em> to split the single &times;16 link into four independent &times;4/&times;4/&times;4/&times;4 root ports. If the motherboard does not support &times;4/&times;4/&times;4/&times;4 bifurcation, the system will only detect <em>one</em> single M.2 drive (the first SSD connected to lanes 0-3).</li>
          <li><strong>Active PLX / PEX Switching Solution:</strong> If bifurcation is unavailable, an active PCIe packet switch chip (e.g. Broadcom PEX8748) must be present on the carrier card. The PLX switch presents a single &times;16 endpoint to the CPU and multiplexes data packets across the four downstream &times;4 links.</li>
          <li><strong>PCH vs Direct CPU Lanes:</strong> If the carrier card is installed in a secondary &times;16 physical slot routed through the motherboard chipset (PCH), total bandwidth is severely bottlenecked by the DMI link (e.g. Intel DMI 4.0 &times;8 &approx; 15.75 GB/s), capping maximum aggregate throughput below the required 28 GB/s regardless of SSD speeds.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> Thermal Throttling Triage: High-Density Liquid Cooling Loop Failure Analysis</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A computational simulation workstation starts up normally, but after exactly 3 to 4 minutes of running finite element analysis (FEA), the system fans ramp to 100% maximum RPM, the OS interface experiences severe stuttering, and hardware monitoring shows CPU core temperatures pegged at 100&deg;C with core frequencies dropping from 5.4 GHz to 800 MHz.</p>
        <p><strong>Root Cause Matrix:</strong></p>
        <ol>
          <li><strong>Thermal Throttling Mechanics:</strong> At 100&deg;C (TjMax), the CPU asserts the PROCHOT# pin, dropping the internal clock multiplier to the lowest supported P-state (800 MHz base frequency) to prevent immediate thermal destruction.</li>
          <li><strong>Differentiating Pump Failure vs Heatsink Mounting:</strong>
            <ul>
              <li><em>Pump Failure:</em> The AIO liquid cooler pump is not spinning (RPM reads 0 in BIOS or 3-pin tachometer disconnected). The liquid inside the CPU block boils, but the radiator fins remain completely cold to the touch because heat is not being circulated.</li>
              <li><em>Plastic Peel Failure:</em> Novice builders often forget to remove the transparent protective plastic film covering the copper cold-plate before mounting. The plastic film acts as a thermal insulator. In this case, thermal paste is present, but heat cannot bridge the plastic barrier.</li>
              <li><em>Air Permeation & Vapor Lock:</em> Over years of operation, liquid coolant evaporates through flexible rubber tubes (permeation). If the radiator is mounted on the bottom of the case with tubes running upward, air bubbles accumulate inside the CPU pump block, unpriming the impeller and causing immediate thermal runaway.</li>
            </ul>
          </li>
        </ol>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> Power Sizing & Transient Spikes: The High-Power GPU ATX 3.0 Engineering Mandate</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Engineering Challenge:</strong> A workstation equipped with an RTX 4090 GPU (450W TDP) and an Intel Core i9-13900K (253W PL2) is powered by a high-end 850W ATX 2.4 certified power supply. Total calculated continuous load is ~750W. However, when launching intense GPU 3D rendering tasks, the entire system spontaneously reboots with zero Windows crash logs (Kernel-Power Event ID 41, BugcheckCode 0).</p>
        <p><strong>Technical Analysis:</strong></p>
        <ul>
          <li><strong>Transient Power Spikes (Microsecond Excursions):</strong> Modern high-performance GPUs generate microscopic transient power spikes lasting 1 to 10 milliseconds where power draw surges to <strong>200% to 250% of rated TDP</strong> (e.g. 450W TDP GPU spiking to 900W-1100W).</li>
          <li><strong>Legacy ATX 2.4 vs ATX 3.0:</strong> Older ATX 2.4 power supplies have strict, fast-acting Over-Current Protection (OCP) circuits designed for smooth resistive loads. When the GPU demands 900W for 2 milliseconds, the PSU OCP comparator detects an excessive current surge and immediately trips, dropping all rails.</li>
          <li><strong>ATX 3.0 Engineering Standard:</strong> The Intel ATX 3.0 specification mandates that power supplies must sustain <strong>200% power excursions for 100 microseconds</strong> without tripping OCP/OPP, and includes the native 12VHPWR cable with SENSE line communication to dynamically modulate GPU draw. Upgrading to an ATX 3.0 1000W+ PSU with high bulk capacitance resolves the transient tripping issue permanently.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 01 Master MCQ Answer Key</span>
    <span>Unit 01 • Page 08</span>
  </div>
</article>

<!-- Page 9: Master Answer Key Table -->
<article class="doc-page" id="mcq-answer-key-u1-hw">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 01</span>
    <span class="meta-tag">Master Answer Key • 30 Questions</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">09.</span> Unit 1 Master Answer Key Table & Verification Matrix
  </h2>

  <p class="lead-para">
    Complete verified answer keys and core learning objectives for all 30 multiple choice questions in Unit 1.
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
        <tr><td>01</td><td><strong style="color:var(--primary);">B</strong></td><td>Standard ATX physical dimensions (12 &times; 9.6 inches)</td><td>16</td><td><strong style="color:var(--primary);">B</strong></td><td>+5VSB Standby Rail operation in ACPI S5 state</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">C</strong></td><td>Mini-ITX expansion capacity (Exactly 1 PCIe slot)</td><td>17</td><td><strong style="color:var(--primary);">C</strong></td><td>Thermal paste microscopic air valley elimination</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">D</strong></td><td>LGA socket architecture (Pins located in socket)</td><td>18</td><td><strong style="color:var(--primary);">D</strong></td><td>Over-Current Protection (OCP) threshold monitoring</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">A</strong></td><td>Integrated Memory Controller (IMC) CPU die integration</td><td>19</td><td><strong style="color:var(--primary);">A</strong></td><td>DDR5 JEDEC standard voltage (1.1 Volts)</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">B</strong></td><td>PCIe 4.0 per-lane transfer throughput (~1.97 GB/s)</td><td>20</td><td><strong style="color:var(--primary);">B</strong></td><td>POST hardware initialization sequence (CPU&rarr;RAM&rarr;GPU)</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">C</strong></td><td>DDR4-3200 CL16 true first-word latency calculation (10.0 ns)</td><td>21</td><td><strong style="color:var(--primary);">C</strong></td><td>BGA packaging target deployments (Thin laptops/SoCs)</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">A</strong></td><td>DDR5 dual 32-bit subchannel memory architecture</td><td>22</td><td><strong style="color:var(--primary);">D</strong></td><td>CPU L1 cache access latency (4-5 cycles / ~1 ns)</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">D</strong></td><td>Motherboard standoff chassis grounding and short prevention</td><td>23</td><td><strong style="color:var(--primary);">A</strong></td><td>+12V voltage ripple impact on semiconductor switching</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">B</strong></td><td>+12V Rail heavy power distribution dominance (&gt;90%)</td><td>24</td><td><strong style="color:var(--primary);">B</strong></td><td>DDR5 On-Die ECC vs Enterprise Sideband Registered ECC</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">C</strong></td><td>ATX Pin 8 PWR_OK power stabilization signaling</td><td>25</td><td><strong style="color:var(--primary);">C</strong></td><td>PROCHOT# hardware thermal throttling invocation at TjMax</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">A</strong></td><td>CPU L3 Last-Level Cache (LLC) CCX sharing</td><td>26</td><td><strong style="color:var(--primary);">D</strong></td><td>Intel DMI interconnect bridging CPU to PCH chipset</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">B</strong></td><td>DDR5 On-board Power Management IC (PMIC) location</td><td>27</td><td><strong style="color:var(--primary);">A</strong></td><td>12VHPWR 4-pin sideband wattage negotiation protocol</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">C</strong></td><td>Daisy-Chain memory trace priority (Slots A2 and B2)</td><td>28</td><td><strong style="color:var(--primary);">B</strong></td><td>UEFI Secure Boot cryptographic signature validation (db)</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">D</strong></td><td>SMPS peak electrical efficiency load curve (50% load)</td><td>29</td><td><strong style="color:var(--primary);">C</strong></td><td>Non-polarity sensitive front-panel momentary switch headers</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">A</strong></td><td>PCIe 128b/130b line encoding protocol overhead (1.53%)</td><td>30</td><td><strong style="color:var(--primary);">D</strong></td><td>PCIe Lane Bifurcation x16 subdivision mechanics</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 01 Complete • Next: Unit 02 Networking & Topologies</span>
    <span>Unit 01 • Page 09</span>
  </div>
</article>
"""
