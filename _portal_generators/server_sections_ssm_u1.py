# -*- coding: utf-8 -*-
"""
Server Administration Portal - Unit 1: Server Hardware Fundamentals
SSM Engineering Standard Gold Standard Architecture
"""

SERVER_UNIT1_HTML = r"""
<!-- ===================================================================
     UNIT 01: SERVER HARDWARE FUNDAMENTALS
     =================================================================== -->

<!-- ARTICLE 1: SERVER FORM FACTORS & OUT-OF-BAND ARCHITECTURE -->
<article class="doc-page" id="s1-hardware">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Server Hardware • Article 01</span>
    <h2 class="section-title"><span class="sec-num">01</span> Server Form Factors, Chassis Engineering &amp; Out-of-Band Architecture</h2>
    <p class="lead-para">
      Enterprise servers differ fundamentally from consumer desktop workstations in redundancy, serviceability, compute density, and out-of-band remote telemetrics. Selecting the appropriate chassis topology—Tower, Rack-Mount, or Blade—dictates datacenter power delivery, thermal dissipation, cabling complexity, and mean time to repair (MTTR).
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Comparative Server Form Factor Topologies</h3>
  <p>
    Datacenter engineering balances compute density against power delivery and thermal exhaustion. The standard 19-inch rack unit (<strong>1U = 1.75 inches or 44.45 mm</strong>) defines the physical envelope:
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Form Factor</th>
          <th>Physical Envelope</th>
          <th>Expansion &amp; Drive Density</th>
          <th>Cooling &amp; Power Architecture</th>
          <th>Primary Enterprise Deployment</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Tower Server</strong></td>
          <td>Standalone upright pedestal chassis (convertible to 4U/5U rack)</td>
          <td>High internal volume; 8–16 3.5" SAS drives; 4–6 full-height PCIe slots</td>
          <td>Low noise fans (&lt;35 dB); single or dual redundant ATX PSUs; convective cooling</td>
          <td>Branch offices (ROBO), retail edge, small businesses without dedicated server rooms</td>
        </tr>
        <tr>
          <td><strong>Rack-Mount (1U/2U)</strong></td>
          <td>EIA-310 19" rack-mount; depth 28–36"; sliding rail kits</td>
          <td>1U: 4–10 2.5" SFF drives, 1–2 low-profile PCIe slots; 2U: 12–24 2.5" / 12 3.5" drives, 6–8 PCIe slots</td>
          <td>High-RPM counter-rotating fans (10,000–18,000 RPM); dual hot-plug CRPS PSUs; hot/cold aisle</td>
          <td>Standard datacenter workhorses, virtualization clusters, SAN storage heads, web tiers</td>
        </tr>
        <tr>
          <td><strong>Blade Server System</strong></td>
          <td>Modular compute sleds inserted into shared 6U–10U enclosure midplane</td>
          <td>Ultra-dense; 8–16 blades per chassis; mezzanine cards; zero internal PCIe slots</td>
          <td>Centralized chassis power pool (4–6 3000W PSUs) and shared high-CFM fan blowers</td>
          <td>Large-scale enterprise datacenters, high-density compute fabrics, VMware vSphere farms</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="cpu"></i> OUT-OF-BAND MANAGEMENT ARCHITECTURE (IPMI / iDRAC / iLO)</div>
    <div class="callout-body">
      Enterprise servers feature an independent, dedicated embedded microcontroller—the <strong>Baseboard Management Controller (BMC)</strong> (e.g., Dell iDRAC9, HPE iLO 6, Supermicro IPMI).
      <ul style="margin-left: 1.2rem; margin-top: 0.5rem; line-height: 1.8;">
        <li><strong>Physical Isolation:</strong> Powered by the standby +5VSB/12VSB power rail; operates 24/7/365 even when the host operating system is crashed, locked up, or powered off.</li>
        <li><strong>Dedicated Out-of-Band (OOB) NIC:</strong> Connects to an isolated management VLAN, entirely air-gapped from production data networks to prevent side-channel exploits.</li>
        <li><strong>Capabilities:</strong> IPMI 2.0 / Redfish RESTful APIs, Virtual KVM (HTML5 remote console), Virtual Media ISO mounting, remote power cycling (ACPI power states), hardware sensor monitoring (voltages, VRM temperatures, fan tachometers), and bare-metal firmware flashing.</li>
      </ul>
    </div>
  </div>
</article>

<!-- ARTICLE 2: MULTI-SOCKET PROCESSORS & NUMA ARCHITECTURE -->
<article class="doc-page" id="s1-cpu">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Server Hardware • Article 02</span>
    <h2 class="section-title"><span class="sec-num">02</span> Enterprise Multi-Socket Processors &amp; NUMA Architecture</h2>
    <p class="lead-para">
      Enterprise server motherboards host dual, quad, or octal processor sockets running hundreds of simultaneous hardware execution threads. Scaling beyond a single CPU introduces asymmetric memory access latencies governed by Non-Uniform Memory Access (NUMA) fabric topologies.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Symmetric Multiprocessing (SMP) vs Non-Uniform Memory Access (NUMA)</h3>
  <p>
    In legacy SMP systems, all processors shared a single centralized front-side bus (FSB) to access system RAM. As core counts exploded, the shared bus became a catastrophic bottleneck. Modern architectures (Intel Xeon Scalable Ultra Path Interconnect - UPI, and AMD EPYC Infinity Fabric) allocate integrated memory controllers directly inside each physical CPU socket:
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Memory Access Domain</th>
          <th>Access Mechanism &amp; Bus Route</th>
          <th>Average Latency</th>
          <th>Throughput Bandwidth</th>
          <th>Kernel / Hypervisor Optimization</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Local NUMA Node Memory</strong></td>
          <td>CPU core accesses RAM modules connected directly to its own socket's memory controller</td>
          <td><strong>~65 – 80 ns</strong></td>
          <td>Full memory channel bandwidth (e.g. 8 channels DDR5 = 307.2 GB/s)</td>
          <td>Operating system allocates threads and RAM pages within the same NUMA node (affinity)</td>
        </tr>
        <tr>
          <td><strong>Remote NUMA Node Memory</strong></td>
          <td>CPU core must transmit request across inter-socket interconnect (UPI / Infinity Fabric) to Socket 1's controller</td>
          <td><strong>~115 – 145 ns</strong> (~1.7x latency penalty!)</td>
          <td>Constrained by interconnect link bandwidth (UPI 16 GT/s or IF link saturation)</td>
          <td>Causes severe performance degradation if hypervisor schedules vCPU on Node 0 while allocating memory on Node 1</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-alert">
    <div class="callout-label"><i data-lucide="alert-triangle"></i> THE "NUMA PINNING" MANDATE IN VIRTUALIZATION</div>
    <div class="callout-body">
      When provisioning virtual machines running latency-sensitive databases (Microsoft SQL Server, Oracle RAC, SAP HANA), administrators must enforce <strong>vNUMA alignment</strong>. If a VM's assigned RAM exceeds the physical capacity of a single NUMA node, or if its vCPUs are scheduled across multiple sockets without NUMA topology awareness, the application incurs constant cross-socket UPI traversal penalties, slashing transactional throughput by up to <strong>40%</strong>.
    </div>
  </div>
</article>

<!-- ARTICLE 3: SERVER MEMORY SUBSYSTEMS & ECC ARCHITECTURE -->
<article class="doc-page" id="s1-ram">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Server Hardware • Article 03</span>
    <h2 class="section-title"><span class="sec-num">03</span> Server Memory Subsystems, ECC Architecture &amp; SECDED Mathematics</h2>
    <p class="lead-para">
      A single uncorrected bit-flip in server RAM can corrupt financial transactions, trigger operating system kernel panics, or silently alter cryptographic keys. Enterprise servers mandate Error-Correcting Code (ECC) registered memory architectures capable of autonomous hardware fault remediation.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Memory Module Topologies: UDIMM vs RDIMM vs LRDIMM</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Module Type</th>
          <th>Register / Buffer Architecture</th>
          <th>Bus Electrical Loading</th>
          <th>Max Capacity per Channel</th>
          <th>Typical Application</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>UDIMM (Unbuffered)</strong></td>
          <td>No registers; address/command lines connect directly from memory controller to DRAM chips</td>
          <td>High capacitance load; maximum 2 DIMMs per channel at reduced clock speeds</td>
          <td>32 GB</td>
          <td>Consumer PCs, entry-level micro-servers</td>
        </tr>
        <tr>
          <td><strong>RDIMM (Registered)</strong></td>
          <td>On-board hardware register buffers command and address lines; data lines remain unbuffered</td>
          <td>Electrical load on controller reduced by ~75%; allows higher clock frequency and stability</td>
          <td>64 GB – 128 GB</td>
          <td>Mainstream enterprise servers, virtualization hosts</td>
        </tr>
        <tr>
          <td><strong>LRDIMM (Load-Reduced)</strong></td>
          <td>Memory Buffer (iMB) buffers <strong>both</strong> command/address lines AND high-speed data lines</td>
          <td>Presents a single electrical load to memory controller; bypasses rank multiplication limits</td>
          <td>256 GB – 512 GB per DIMM</td>
          <td>Massive in-memory databases (SAP HANA, memcached clusters, AI training)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">2. SECDED Hamming Code Mathematics</h3>
  <p>
    Standard ECC memory employs an <strong>extended Hamming code with parity (SECDED: Single Error Correction, Double Error Detection)</strong>. For a 64-bit data word, ECC modules add 8 parity check bits (total 72-bit bus width):
  </p>
  <ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.8;">
    <li><strong>Bit Correction Formula:</strong> Minimum Hamming distance \(d_{\min} = 4\). This ensures that any single-bit alteration has a unique syndrome vector pointing directly to the erroneous bit position, allowing the memory controller to invert it back to the correct state on-the-fly without notifying the OS.</li>
    <li><strong>Double Error Detection:</strong> If two bits flip simultaneously due to cosmic ray alpha-particle ionization, the overall parity bit indicates an even number of errors, while the syndrome is non-zero. The memory controller flags an <strong>Uncorrectable Error (UCE)</strong> and immediately triggers a Non-Maskable Interrupt (NMI) / Machine Check Exception (MCE), halting the CPU to prevent silent data corruption.</li>
    <li><strong>Chipkill / Advanced ECC:</strong> Multi-bit error correction technology that scatters parity data across multiple independent DRAM chips. If an entire 4-bit or 8-bit memory chip fails catastrophically, the system continues running without downtime.</li>
  </ul>
</article>

<!-- ARTICLE 4: SERVER EXPANSION, NVME BACKPLANES & RISER CARDS -->
<article class="doc-page" id="s1-expansion">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Server Hardware • Article 04</span>
    <h2 class="section-title"><span class="sec-num">04</span> Server Expansion Busses, PCIe 5.0 Riser Architecture &amp; NVMe Backplanes</h2>
    <p class="lead-para">
      In 1U and 2U rack enclosures, horizontal space constraints prohibit plugging standard vertical PCIe expansion cards directly into the motherboard. Riser cards, PCIe retimers, and high-density U.2/U.3 backplanes solve mechanical and high-speed electrical routing challenges.
    </p>
  </header>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Subsystem</th>
          <th>Protocol / Form Factor</th>
          <th>Bandwidth / Throughput</th>
          <th>Signaling &amp; Cabling Architecture</th>
          <th>Enterprise Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>PCIe Riser Cards</strong></td>
          <td>PCIe Gen 4 / Gen 5 (x8, x16)</td>
          <td>PCIe 5.0 x16 = <strong>63.0 GB/s bidirectional</strong></td>
          <td>90-degree adapter boards; bifurcates x16 motherboard slot into dual x8 slots</td>
          <td>Housing full-height GPU accelerators, 100GbE NICs, and SAS RAID controllers in 2U chassis</td>
        </tr>
        <tr>
          <td><strong>OCP 3.0 NIC (Mezzanine)</strong></td>
          <td>Open Compute Project 3.0 SFF</td>
          <td>PCIe 4.0 x16 (25GbE / 100GbE)</td>
          <td>Hot-serviceable pull-tab card; bypasses PCIe slot usage; direct baseboard connector</td>
          <td>Standard datacenter networking; leaves primary PCIe slots open for accelerators</td>
        </tr>
        <tr>
          <td><strong>U.2 / U.3 NVMe Backplane</strong></td>
          <td>SFF-8639 / SFF-TA-1001 (Universal)</td>
          <td>4 lanes PCIe per drive (16 GB/s on Gen 4)</td>
          <td>Tri-Mode Backplane: dynamically accepts SAS-3 (12G), SATA (6G), or PCIe NVMe on same bay</td>
          <td>High-density all-flash storage tiers (24x NVMe drives in a 2U front bay)</td>
        </tr>
        <tr>
          <td><strong>SAS Host Bus Adapter (HBA)</strong></td>
          <td>SAS-3 12 Gbps / SAS-4 24 Gbps</td>
          <td>1200 MB/s per SAS lane (x8 wide port = 9.6 GB/s)</td>
          <td>Mini-SAS HD (SFF-8643) / SlimSAS internal cabling to storage backplane expanders</td>
          <td>Connecting bulk spinning disk JBOD enclosures (Software Defined Storage / Ceph / ZFS)</td>
        </tr>
      </tbody>
    </table>
  </div>
</article>

<!-- ARTICLE 5: ENTERPRISE POWER & THERMAL DYNAMICS -->
<article class="doc-page" id="s1-power-cooling">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Server Hardware • Article 05</span>
    <h2 class="section-title"><span class="sec-num">05</span> Enterprise Power Systems, Redundancy Configurations &amp; Thermal Management</h2>
    <p class="lead-para">
      Datacenter electrical infrastructure operates under strict High Availability SLAs. Power distribution units (PDUs), Common Redundant Power Supplies (CRPS), and hot/cold aisle thermal containment systems prevent catastrophic equipment failure and thermal throttling.
    </p>
  </header>

  <h3 style="margin-top: 1.5rem; color: var(--text-normal); font-size: 18px;">1. Power Redundancy Topologies: N, N+1, 2N</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Redundancy Model</th>
          <th>PSU Count &amp; Sizing</th>
          <th>Feed Architecture</th>
          <th>Fault Tolerance</th>
          <th>Datacenter Tier Alignment</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>N Configuration</strong></td>
          <td>Minimum PSUs required to power server (e.g. 1x 1100W PSU)</td>
          <td>Single utility feed / single PDU</td>
          <td><strong>Zero fault tolerance;</strong> PSU failure causes immediate server crash</td>
          <td>Tier I Datacenter / Non-critical dev</td>
        </tr>
        <tr>
          <td><strong>N+1 Redundancy</strong></td>
          <td>1 extra PSU beyond baseline (e.g., server needs 2000W; uses 3x 1000W PSUs)</td>
          <td>Load shared equally; if 1 PSU dies, remaining 2 absorb 100% load</td>
          <td>Survives any single PSU failure; cannot survive loss of an entire power feed</td>
          <td>Tier II Datacenter</td>
        </tr>
        <tr>
          <td><strong>2N (Concurrent Maintainability)</strong></td>
          <td>Double the required capacity (e.g. 2x 1600W PSUs for an 800W server load)</td>
          <td>PSU A connected to Grid Feed A (UPS A); PSU B connected to Grid Feed B (UPS B / Generator)</td>
          <td><strong>Full fault tolerance;</strong> survives loss of an entire electrical utility grid feed or UPS blowout</td>
          <td>Tier III &amp; Tier IV Mission-Critical</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="wind"></i> HOT-AISLE / COLD-AISLE AIRFLOW CONTAINMENT (ASHRAE A1–A4)</div>
    <div class="callout-body">
      Datacenters arrange server racks in alternating rows facing each other:
      <ul style="margin-left: 1.2rem; margin-top: 0.5rem; line-height: 1.8;">
        <li><strong>Cold Aisle:</strong> Server rack fronts face the cold aisle. Perforated raised floor tiles deliver chilled air (18°C – 27°C) directly into the server intake bezels.</li>
        <li><strong>Hot Aisle:</strong> Server rear exhaust fans expel hot air (35°C – 45°C) into the hot aisle, where ceiling plenums extract the thermal exhaust directly back to Computer Room Air Handlers (CRAH).</li>
        <li><strong>Containment Doors &amp; Blanking Panels:</strong> Physical barriers prevent heated exhaust air from recirculating into cold intakes. Missing blanking panels on empty rack slots cause localized hot spots, triggering server thermal throttling and PSU fan overspeed.</li>
      </ul>
    </div>
  </div>
</article>

<!-- UNIT 1 PRACTICE BANK: 30 MCQS -->
<article class="doc-page" id="practice-mcq-s1">
  <div class="page-header-meta">
    <span class="meta-tag">Server Administration • Unit 01</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreS1">Score: 0 / 30</span>
  </div>
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Assessment • Practice Bank</span>
    <h2 class="section-title"><span class="sec-num">Q1</span> Unit 1 Practice Bank: 30 Interactive Examination MCQs</h2>
    <p class="lead-para">
      Comprehensive assessment questions matching the rigor of CompTIA Server+ and Mid-Semester (MST) examinations. Test your knowledge on server form factors, NUMA architecture, ECC memory, PCIe risers, and power redundancy.
    </p>
  </header>

  <div class="callout callout-deep" style="margin-bottom: 2rem;">
    <div class="callout-label"><i data-lucide="award"></i> REAL-TIME SCORE ENGINE</div>
    <div class="callout-body">
      Select your answer for each question. Instant feedback will highlight correct answers in green and explanations will appear automatically.
    </div>
  </div>

  <!-- MCQ 1 -->
  <div class="mcq-card" data-unit="s1" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q1</span>
      <div class="mcq-question-text">What is the standard vertical height of a single rack unit (1U) in a standard 19-inch enterprise server rack according to EIA-310 standards?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 1.50 inches (38.10 mm)</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 1.75 inches (44.45 mm)</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 2.00 inches (50.80 mm)</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 2.25 inches (57.15 mm)</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B (1.75 inches / 44.45 mm).</strong> EIA-310 standards dictate that 1U equals exactly 1.75 inches. A standard 42U datacenter cabinet stands approximately 73.5 inches tall in usable internal mounting height.
    </div>
  </div>

  <!-- MCQ 2 -->
  <div class="mcq-card" data-unit="s1" data-correct="C">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q2</span>
      <div class="mcq-question-text">An administrator can access the web console of a Dell PowerEdge server's iDRAC even when the host operating system has experienced a kernel panic and the main CPU is halted. What architectural feature makes this possible?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The operating system kernel boots a secondary rescue kernel automatically in RAM.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The primary CPU reserves 1 core strictly for hypervisor management interrupts.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The Baseboard Management Controller (BMC) is an independent SoC powered by the standby power rail.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Wake-on-LAN activates the motherboard chipset to emulate an active host OS.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: C.</strong> The BMC (iDRAC/iLO) is an autonomous embedded ARM-based system-on-chip running an independent embedded Linux OS. It draws power from the standby electrical rail (+12VSB/+5VSB) and functions regardless of host OS or CPU state.
    </div>
  </div>

  <!-- MCQ 3 -->
  <div class="mcq-card" data-unit="s1" data-correct="D">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q3</span>
      <div class="mcq-question-text">In a dual-socket Intel Xeon server running a Non-Uniform Memory Access (NUMA) architecture, what occurs when a thread executing on CPU Socket 0 attempts to read memory pages mapped to physical DIMMs connected to CPU Socket 1?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The memory read is blocked and causes an immediate General Protection Fault.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The memory controller copies the page over SATA to local L3 cache first.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The operation executes with zero latency difference because all server memory is symmetric.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The read request traverses the Ultra Path Interconnect (UPI), incurring an additional 40–60 ns latency penalty.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: D.</strong> Remote NUMA access must traverse inter-socket interconnects (Intel UPI or AMD Infinity Fabric). This introduces an asymmetric latency penalty (~120ns vs ~70ns for local memory).
    </div>
  </div>

  <!-- MCQ 4 -->
  <div class="mcq-card" data-unit="s1" data-correct="B">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q4</span>
      <div class="mcq-question-text">What is the mathematical guarantee provided by SECDED (Single Error Correction, Double Error Detection) Hamming code in server ECC memory?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Corrects any 2-bit error and detects any 3-bit error simultaneously.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Corrects 1-bit errors autonomously in hardware and halts the CPU on 2-bit errors to prevent data corruption.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Detects parity errors only, requiring the OS kernel to re-read corrupted blocks from disk.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Scatters data across 4 memory channels so bit flips never occur physically.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: B.</strong> SECDED uses 8 check bits for 64 data bits (Hamming distance = 4). A single bit flip is corrected on-the-fly via syndrome decoding; a double bit flip triggers an uncorrectable MCE/NMI panic to avoid silent corruption.
    </div>
  </div>

  <!-- MCQ 5 -->
  <div class="mcq-card" data-unit="s1" data-correct="A">
    <div class="mcq-question-header">
      <span class="mcq-q-num">Q5</span>
      <div class="mcq-question-text">Why are Load-Reduced DIMMs (LRDIMMs) utilized instead of Registered DIMMs (RDIMMs) in extreme memory capacity server configurations (e.g., 2TB+ per socket)?</div>
    </div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> LRDIMMs buffer both command/address lines AND data lines, reducing the electrical load to a single rank equivalent.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> LRDIMMs eliminate ECC bits to achieve 25% faster raw clock speeds.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> LRDIMMs are unbuffered, allowing direct copper trace routing to CPU cache.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> LRDIMMs consume less than 1.0W of power, eliminating the need for server cooling fans.</div>
    </div>
    <div class="mcq-explanation">
      <strong>Correct Answer: A.</strong> RDIMMs only buffer command and address lines; data lines still load the bus directly. LRDIMMs use an Isolation Memory Buffer (iMB) to buffer data lines as well, presenting only one electrical load per DIMM.
    </div>
  </div>

  <!-- MCQs 6 to 30 concise cards -->
  <div class="mcq-card" data-unit="s1" data-correct="C">
    <div class="mcq-question-header"><span class="mcq-q-num">Q6</span><div class="mcq-question-text">Which power supply redundancy topology ensures concurrent maintainability, surviving the loss of an entire electrical utility feed or primary UPS system?</div></div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> N Configuration</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> N+1 Configuration</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 2N Configuration (Dual Independent Grid Feeds)</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Single-feed generator backup</div>
    </div>
    <div class="mcq-explanation"><strong>Correct Answer: C.</strong> In a 2N topology, each server has redundant PSUs fed by completely independent A and B power paths (separate transformers, switchgear, UPS systems, and PDUs).</div>
  </div>

  <div class="mcq-card" data-unit="s1" data-correct="B">
    <div class="mcq-question-header"><span class="mcq-q-num">Q7</span><div class="mcq-question-text">In a modern 2U server chassis, how is a full-height PCIe 5.0 x16 add-in card physically installed when the chassis vertical clearance is insufficient?</div></div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The card is mounted externally via a Thunderbolt cable.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A 90-degree PCIe Riser Card is inserted into the motherboard slot, orienting the card horizontally.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The bracket is bent to 45 degrees to clear the chassis lid.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The card is plugged directly into a USB-C header.</div>
    </div>
    <div class="mcq-explanation"><strong>Correct Answer: B.</strong> Riser cards redirect the vertical PCIe bus horizontally parallel to the motherboard plane, allowing full-height expansion cards to fit inside 2U envelopes.</div>
  </div>

  <div class="mcq-card" data-unit="s1" data-correct="A">
    <div class="mcq-question-header"><span class="mcq-q-num">Q8</span><div class="mcq-question-text">What is the primary function of empty blanking panels (filler panels) installed in unoccupied slots of a datacenter server rack?</div></div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Prevent hot exhaust air from recirculating back into the cold intake aisle.</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Protect datacenter staff from high-voltage electrical busbars.</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Improve structural earthquake rigidity of the rack frame.</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Provide reflective surfaces for biometric camera surveillance.</div>
    </div>
    <div class="mcq-explanation"><strong>Correct Answer: A.</strong> Unoccupied rack slots allow hot exhaust air to loop back into the cold aisle, raising server intake temperatures and causing thermal throttling. Blanking panels maintain laminar airflow separation.</div>
  </div>

  <div class="mcq-card" data-unit="s1" data-correct="D">
    <div class="mcq-question-header"><span class="mcq-q-num">Q9</span><div class="mcq-question-text">What physical interface standard allows a universal backplane to accept SAS-3, SATA-III, or PCIe NVMe drives interchangeably in the same drive bay?</div></div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> IDE / PATA 40-pin</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> SCSI SCA-2 80-pin</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Apple M.2 proprietary</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> SFF-TA-1001 (U.3) / SFF-8639 (U.2) Tri-Mode interface</div>
    </div>
    <div class="mcq-explanation"><strong>Correct Answer: D.</strong> The SFF-TA-1001 (U.3) standard unifies SAS, SATA, and NVMe signaling onto a single connector pinout managed by an intelligent Tri-Mode controller.</div>
  </div>

  <div class="mcq-card" data-unit="s1" data-correct="B">
    <div class="mcq-question-header"><span class="mcq-q-num">Q10</span><div class="mcq-question-text">According to ASHRAE thermal guidelines for Class A1 enterprise datacenters, what is the recommended server intake air temperature range?</div></div>
    <div class="mcq-options">
      <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 5°C to 12°C (41°F to 53.6°F)</div>
      <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 18°C to 27°C (64.4°F to 80.6°F)</div>
      <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 32°C to 45°C (89.6°F to 113°F)</div>
      <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Below 0°C to induce sub-ambient cooling</div>
    </div>
    <div class="mcq-explanation"><strong>Correct Answer: B.</strong> ASHRAE Class A1 datacenter specifications recommend an intake temperature of 18°C to 27°C with relative humidity between 40% and 60% to prevent electrostatic discharge (ESD) and condensation.</div>
  </div>

  <!-- Remaining MCQs 11 to 30 mapped accurately -->
  <div class="mcq-card" data-unit="s1" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q11</span><div class="mcq-question-text">Which Open Compute Project standard defines hot-serviceable modular mezzanine network cards without consuming standard PCIe expansion slots?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> AGP Pro</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ISA 16-bit</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> OCP NIC 3.0</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Mini-PCIe</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> OCP NIC 3.0 provides high-speed (25G/100G) modular networking with rear thumb-screw latching for easy replacement without chassis lid removal.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q12</span><div class="mcq-question-text">What occurs when a hot-swappable hard drive is removed from a live RAID 5 array in an enterprise chassis?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Backplane sensing pins detect physical disconnection, signal the RAID controller, and the array transitions to degraded mode without powering down.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The server immediately triggers a thermal shutdown to protect the spindle motor.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> All remaining drives lose data instantly due to electrical transient spikes.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The OS kernel crashes because hot-swap requires SCSI termination resistors to be manually closed.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Hot-swap SAS/SATA connectors have staggered pin lengths (ground pins make first/break last), allowing safe insertion and removal while the bus is fully energized.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q13</span><div class="mcq-question-text">What is the raw bidirectional bandwidth delivered by a single 16-lane (x16) PCIe 5.0 slot?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 8.0 GB/s</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 15.75 GB/s</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 31.5 GB/s</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> ~63.0 GB/s (128 GB/s bidirectional total)</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> PCIe 5.0 delivers 32 GT/s per lane. With 128b/130b encoding, a x16 slot yields ~3.94 GB/s per lane direction, or ~63.0 GB/s unconstrained unidirectional (~128 GB/s bidirectional).</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q14</span><div class="mcq-question-text">Which server component is responsible for stepping down high-voltage DC busbar power (e.g. 12V) directly to sub-volt precision levels required by CPU cores (~0.8V - 1.2V)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Common Redundant Power Supply (CRPS)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Voltage Regulator Modules (VRM) / Multiphase Buck Converters on the motherboard</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Baseboard Management Controller</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Supercapacitor backup pack</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Multiphase VRMs switch DC current at megahertz frequencies to deliver stable, high-amperage sub-volt power directly to modern multi-core processors.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q15</span><div class="mcq-question-text">What diagnostic technology allows enterprise servers to record the state of hardware registers and sensor telemetry in non-volatile memory immediately prior to a fatal crash?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> BIOS CMOS clear</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Syslog over UDP</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> System Event Log (SEL) / Black Box Crash Dump in the BMC</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Windows Event Viewer Application Log</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> The BMC maintains a persistent hardware System Event Log (SEL) and executes a black-box crash dump capture during fatal hardware interrupts (NMIs).</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q16</span><div class="mcq-question-text">Why do enterprise blade servers utilize midplanes instead of traditional internal ribbon/SAS cables?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The rigid midplane PCB provides impedance-matched traces for power, high-speed Ethernet, and PCIe fabrics directly between sleds and rear switch modules without cable clutter.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Midplanes are made of copper mesh that eliminates all radio frequency radiation.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Midplanes reduce the cost of the chassis to under $50.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Midplanes convert AC power directly to liquid nitrogen coolant.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Midplane printed circuit boards eliminate internal cable rat-nests, offering blind-mate connectors for hot-swapping compute sleds, power supplies, and network pass-through switches.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q17</span><div class="mcq-question-text">What is the electrical efficiency certification of a server power supply that achieves at least 96% efficiency at 50% load on 230V AC?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 80 Plus Bronze</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 80 Plus Gold</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 80 Plus Titanium</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Energy Star 1.0</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> 80 Plus Titanium is the highest standard, requiring 96% efficiency at 50% load and maintaining at least 90% efficiency even at light 10% load.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q18</span><div class="mcq-question-text">When configuring high-speed memory channels on an enterprise server, what is the impact of "Memory Interleaving"?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It forces all read requests to execute on Channel 0 first to conserve power.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It distributes sequential memory addresses across multiple memory channels simultaneously, multiplying throughput.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It disables ECC parity checks to allow higher clock multipliers.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It compresses RAM data before sending it to L1 cache.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Channel interleaving spreads consecutive memory addresses across distinct physical memory channels, allowing parallel reads and writes across multiple DIMMs.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q19</span><div class="mcq-question-text">What protocol standard has superseded IPMI for secure, JSON-formatted, RESTful out-of-band management of modern server infrastructure?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Telnet</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> SNMP v1</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> SOAP / XML</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> DMTF Redfish API</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> DMTF Redfish uses modern HTTPS, JSON schemas, and OData RESTful conventions, replacing insecure, complex binary IPMI 2.0 implementations.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q20</span><div class="mcq-question-text">Which memory technology allows replacing a failing DIMM in a live server without shutting down the operating system?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Memory Mirroring and Hot-Add / Hot-Replace RAM (supported by high-end mission-critical platforms)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Standard consumer DDR4</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> BIOS Overclocking Profile XMP</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> SATA DOM</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> High-end fault-tolerant servers (such as HPE Superdome or IBM Z) support hardware memory mirroring where active data is duplicated across memory channels, allowing online DIMM replacement.</div></div>

  <!-- MCQs 21 to 30 -->
  <div class="mcq-card" data-unit="s1" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q21</span><div class="mcq-question-text">What is the function of a Supercapacitor module connected to an enterprise hardware RAID controller's CacheVault / Flash-Backed Write Cache (FBWC)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Overclock the RAID controller processor to 5.0 GHz.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Provide emergency electrical power during a power failure to flush volatile DRAM cache contents into non-volatile NAND flash.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Suppress high-frequency audio noise from cooling fans.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Provide Wi-Fi connectivity to the storage enclosure.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Unlike legacy toxic NiMH batteries that degraded every 2 years, supercapacitors instantly discharge to copy dirty RAID cache blocks to on-board NAND flash during abrupt power loss.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q22</span><div class="mcq-question-text">Why must server chassis cooling fans be counter-rotating (two fan impellers spinning in opposite directions inside a single fan module)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> To generate an attractive acoustic musical tone in the datacenter.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> To generate electric current to recharge the CMOS battery.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> To straighten swirling airflow into linear high static-pressure streams, forcing air through dense heatsinks and drive cages.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> To create a vacuum chamber inside the server chassis.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Counter-rotating dual-rotor fan modules cancel rotational swirl, converting rotational energy into linear static pressure necessary to overcome the high resistance of dense server heatsinks.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q23</span><div class="mcq-question-text">In a server with 2 physical CPUs and 16 DIMM slots (8 per CPU), what happens if all 16 DIMMs are populated with 32GB sticks, but one CPU socket has bent pins in its memory controller socket?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The server will fail POST or only detect the 256GB connected to the healthy socket, logging a memory channel error.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The second CPU will automatically take over the failing CPU's memory traces via SATA.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The system boots with 512GB without error because memory traces are wired in parallel.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The power supply will explode due to high resistance.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> Memory traces connect point-to-point directly to specific CPU socket pins. Damaged pins on Socket 1 isolate its 8 DIMM slots, causing channel initialization failure during UEFI memory training.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q24</span><div class="mcq-question-text">What is the purpose of Intel Boot Guard and AMD Platform Secure Boot (PSB) in enterprise server processors?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Enforce automatic Windows updates.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Encrypt user passwords in Microsoft Excel.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Prevent users from installing Linux.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Establish a hardware Root of Trust by verifying the digital signature of the initial boot block before executing BIOS/UEFI firmware.</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> Hardware Root of Trust burns OEM public key hashes into one-time programmable CPU fuses, ensuring the processor will only execute cryptographically authentic UEFI firmware.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q25</span><div class="mcq-question-text">Which metric describes the total thermal energy a server cooling system must exhaust, expressed in Watts or British Thermal Units (BTU/hr)?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Volumetric Flow Rate (CFM)</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Thermal Design Power (TDP) / Heat Dissipation (1 Watt = 3.412 BTU/hr)</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Static Pressure in Pascals</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Revolutions Per Minute (RPM)</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> Heat dissipation in datacenters is directly proportional to electrical power consumption: 1 Watt of continuous electrical power produces 3.41214 BTUs of heat per hour.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q26</span><div class="mcq-question-text">Why are SAS (Serial Attached SCSI) drives preferred over SATA drives in enterprise mission-critical storage arrays?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> SAS drives are cheaper and use thinner copper wires.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> SAS drives can only be formatted with FAT32.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> SAS provides dual-port active/active failover paths, full-duplex signaling, and higher signal voltage tolerance.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> SATA drives do not support SMART monitoring.</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Dual-ported SAS drives connect simultaneously to two redundant RAID controllers or SAS expanders, eliminating single points of failure in enterprise SAN/JBOD fabrics.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="A"><div class="mcq-question-header"><span class="mcq-q-num">Q27</span><div class="mcq-question-text">What is the function of a Trusted Platform Module (TPM 2.0) chip soldered to a server motherboard?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Hardware-based security crypto-processor that securely stores cryptographic keys, platform measurement hashes (PCRs), and enables BitLocker/LUKS encryption.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Accelerates 3D graphics rendering in virtualized desktop infrastructure.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Regulates fan speed based on ambient room temperature.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Provides additional RAM cache for the hard disk controller.</div></div><div class="mcq-explanation"><strong>Correct Answer: A.</strong> TPM 2.0 provides tamper-resistant cryptographic key generation, hardware attestation via Platform Configuration Registers (PCRs), and sealed storage for full-disk encryption.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="D"><div class="mcq-question-header"><span class="mcq-q-num">Q28</span><div class="mcq-question-text">Which server chassis component allows hot-pluggable power supplies to slide directly into place and lock into high-current gold-plated terminal blades?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Motherboard ATX 24-pin harness</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Front bezel security key</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Optical drive bay</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Power Distribution Board (PDB) / Power Interposer Board (PIB)</div></div><div class="mcq-explanation"><strong>Correct Answer: D.</strong> The Power Interposer Board connects the blind-mate connectors of redundant CRPS modules to the server's main 12V busbar distribution system.</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="B"><div class="mcq-question-header"><span class="mcq-q-num">Q29</span><div class="mcq-question-text">What is the consequence of configuring memory modules with mismatched ranks, clock speeds, and voltages across channels on a multi-socket server?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The fastest DIMMs will automatically overclock the slower DIMMs.</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The memory controller downclocks all channels to the lowest common frequency and highest latency, or refuses to boot.</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The operating system dynamically allocates fast RAM to root processes and slow RAM to user processes.</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The CPU automatically disables its L3 cache.</div></div><div class="mcq-explanation"><strong>Correct Answer: B.</strong> The UEFI memory reference code (MRC) trains all memory buses to a single stable timing. Mismatches force all channels down to the lowest common denominator or cause post error codes (0x55).</div></div>

  <div class="mcq-card" data-unit="s1" data-correct="C"><div class="mcq-question-header"><span class="mcq-q-num">Q30</span><div class="mcq-question-text">Which remote console protocol allows an administrator to redirect the server's serial text console over an SSH connection through the BMC?</div></div><div class="mcq-options"><div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> RDP over TLS</div><div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> VNC over HTTP</div><div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Serial-over-LAN (SoL)</div><div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> NetBIOS over TCP/IP</div></div><div class="mcq-explanation"><strong>Correct Answer: C.</strong> Serial-over-LAN redirects the server's legacy UART serial COM port output over the IPMI management network, providing ultra-lightweight, out-of-band text terminal access.</div></div>

</article>

<!-- UNIT 1 SUBJECTIVE SHORT CONCEPTUAL Q&A (5M) -->
<article class="doc-page" id="practice-subj-short-s1">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Assessment • Conceptual Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q2</span> Conceptual Review Questions (5 Marks Each)</h2>
    <p class="lead-para">
      Five focused technical problems analyzing server form factors, NUMA memory node layout, ECC Hamming bit correction, out-of-band architecture, and power redundancy.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q1: Explain the functional role of the Baseboard Management Controller (BMC) and differentiate in-band vs out-of-band management.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> The Baseboard Management Controller (BMC) is an independent, low-power embedded processor (e.g., ASPEED AST2600) integrated onto the server motherboard that monitors physical sensors and controls system state.</p>
      <ul>
        <li><strong>In-Band Management:</strong> Relies on the primary host operating system, main network interface cards, and host CPU cycles (e.g., SSH, RDP, OS agent software). If the host OS crashes (BSOD/kernel panic), the network stack hangs, or the server powers down, in-band management becomes totally unreachable.</li>
        <li><strong>Out-of-Band (OOB) Management:</strong> Operates entirely outside the host OS boundary. Powered by the standby electrical rail (+5VSB/+12VSB) and connected to a dedicated management network interface, the BMC remains fully accessible 24/7. It provides Virtual KVM, remote power cycling (hard reset, soft power-off), virtual media ISO mounting, and firmware updates regardless of host OS health.</li>
      </ul>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q2: Diagram and explain the latency penalty incurred by remote NUMA node memory access in a dual-socket server.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> In Non-Uniform Memory Access (NUMA), each physical CPU socket owns a local memory controller and directly attached memory channels. When a core on Socket 0 accesses Socket 0's RAM, latency is ~65–80 ns. When it requests data from Socket 1's RAM, the request must traverse the point-to-point inter-socket fabric (Intel UPI or AMD Infinity Fabric), introducing queuing and routing delays that increase latency to ~120–145 ns (a ~1.7x to 2.0x performance penalty).</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q3: Differentiate Registered DIMMs (RDIMMs) from Load-Reduced DIMMs (LRDIMMs) in terms of electrical bus loading.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> RDIMMs incorporate a hardware register chip that buffers only the command, control, and address lines; the high-speed data lines connect directly between the DRAM chips and the memory controller. As multiple quad-rank RDIMMs are populated, the cumulative capacitive load on the data bus degrades signal integrity, forcing the controller to drop clock frequencies.</p>
      <p>LRDIMMs replace the register with an Isolation Memory Buffer (iMB) that buffers <strong>both</strong> address lines and data lines. The memory controller sees only a single electrical load per DIMM slot, enabling high-density configurations (e.g., 2TB+ RAM) at maximum rated speeds.</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q4: Explain how Hot-Aisle and Cold-Aisle containment systems optimize datacenter thermal management.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong> Servers ingest air through front bezels and exhaust it through the rear. In an uncontained room, hot exhaust air mixes with chilled supply air, raising average intake temperatures. Hot-Aisle / Cold-Aisle design arranges racks back-to-back and face-to-face. Cold air (18°C–27°C) is delivered via perforated tiles into contained cold aisles, while hot exhaust (35°C–45°C) is isolated in hot aisles and captured by ceiling plenum ducts, maximizing cooling efficiency and reducing PUE (Power Usage Effectiveness).</p>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">5 MARKS</div>
      <div class="subj-title">Q5: Contrast N, N+1, and 2N power redundancy topologies in mission-critical server deployments.</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Answer:</strong></p>
      <ul>
        <li><strong>N Topology:</strong> Employs exactly the minimum capacity required to power the system (e.g., 1x 1000W PSU). Single point of failure; zero fault tolerance.</li>
        <li><strong>N+1 Topology:</strong> Adds one redundant unit beyond baseline (e.g., 2x 1000W PSUs for a 900W load). Survives failure of a single PSU, but if the shared electrical feed or PDU fails, the server shuts down.</li>
        <li><strong>2N Topology:</strong> Doubles total infrastructure (2x 1000W PSUs connected to separate utility grids, transformers, and UPS systems). Survives total failure of an entire power feed or switchgear assembly, meeting Tier IV concurrent maintainability standards.</li>
      </ul>
    </div>
  </div>
</article>

<!-- UNIT 1 SUBJECTIVE LONG SCENARIOS (10M) -->
<article class="doc-page" id="practice-subj-long-s1">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Assessment • Scenario Analysis</span>
    <h2 class="section-title"><span class="sec-num">Q3</span> Architectural &amp; Triage Scenarios (10 Marks Each)</h2>
    <p class="lead-para">
      Enterprise datacenter engineering scenarios requiring hardware failure diagnosis, NUMA memory optimization, and thermal disaster recovery.
    </p>
  </header>

  <div class="subj-card revealed">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 1: Triaging Severe Database Latency on a Dual-Socket Virtualization Host</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A mission-critical SQL database running inside a VM on a dual-socket host (2x Intel Xeon Gold 6348, 28 cores each, 512GB RAM total, 256GB per socket) experiences a 45% drop in transaction processing throughput after being migrated from a smaller host. Analysis shows CPU utilization is only 35%, yet query wait times are elevated.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> DIAGNOSTIC ROOT CAUSE &amp; REMEDIATION PLAN</div>
        <div class="callout-body">
          <ol style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Root Cause Identification:</strong> The VM was provisioned with 40 vCPUs and 384GB of RAM. Because 384GB exceeds the physical capacity of Socket 0 (256GB), the hypervisor was forced to allocate 128GB from Socket 1's NUMA node. However, vNUMA was disabled in the VM configuration. The guest OS treated the memory as a uniform flat space, frequently scheduling database worker threads on Socket 0 cores while accessing pages mapped on Socket 1's controller. This resulted in constant UPI bus saturation and remote memory access latency penalties.</li>
            <li><strong>Remediation Step 1 (vNUMA Enablement):</strong> Enable virtual NUMA (vNUMA) in the hypervisor configuration, exposing the dual-socket physical topology directly to the guest OS.</li>
            <li><strong>Remediation Step 2 (Guest OS &amp; SQL Configuration):</strong> Configure SQL Server to enable NUMA node affinity, pinning database worker threads and buffer pool allocations to matching NUMA nodes.</li>
            <li><strong>Remediation Step 3 (Validation):</strong> Monitor Windows Performance Monitor counters: <code class="code-inline">NUMA Node Memory \ Remote Node Page Allocations / sec</code> should drop near zero, restoring baseline transactional throughput.</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 2: Root-Cause Analysis of Uncorrectable Memory Machine Check Exceptions (MCE)</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> A financial transaction server experiences intermittent kernel panics accompanied by Machine Check Exception (MCE) hardware halts. The BMC System Event Log (SEL) indicates multiple "Correctable ECC error rate exceeded" events on DIMM slot B2 over the preceding 72 hours before the fatal crash.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> ROOT-CAUSE ANALYSIS &amp; HARDWARE ACTION PLAN</div>
        <div class="callout-body">
          <p><strong>1. Failure Mechanism:</strong> Modern ECC memory corrects single-bit errors via SECDED Hamming codes. However, repeated single-bit errors on a specific DIMM indicate physical DRAM cell degradation or dielectric breakdown. When a second bit in the same 64-bit word fails simultaneously, the error transitions from correctable (1-bit) to uncorrectable (2-bit), triggering a fatal NMI/MCE panic to prevent corrupt data writes to storage.</p>
          <p><strong>2. Preventive Thresholds:</strong> Modern BMCs enforce Correctable Error Logging Thresholds (e.g. 10 errors per hour). When exceeded, the administrator should immediately trigger predictive failure alerts before an uncorrectable crash occurs.</p>
          <p><strong>3. Remediation:</strong> Take the server offline, inspect socket B2 for debris, replace the failing DIMM module, perform UEFI memory diagnostic training, and verify clear SEL logs.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 3: Designing a Fault-Tolerant 2N Power &amp; Cooling Infrastructure for a 10-Rack Cluster</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> Design the electrical and thermal infrastructure for a cluster of 10 server racks, each consuming 12 kW of critical IT load (total 120 kW IT load). Ensure zero downtime during scheduled transformer maintenance or CRAH fan failures.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="check-check"></i> ENGINEERING SPECIFICATION</div>
        <div class="callout-body">
          <ul style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Electrical Infrastructure:</strong> Implement true 2N power distribution. Feed A originates from Utility Substation 1 &rarr; Automatic Transfer Switch &rarr; Generator A &rarr; UPS A (160 kVA) &rarr; Floor PDU A &rarr; Rack PDU A. Feed B mirrors Feed A identically through independent switchgear. Each server is equipped with dual 1400W CRPS power supplies plugged into PDU A and PDU B respectively, operating at ~50% load under normal conditions.</li>
            <li><strong>Thermal Infrastructure:</strong> Total heat dissipation = \(120\text{ kW} \times 3,412.14 = \mathbf{409,457\text{ BTU/hr}}\) (\(\approx 34.1\text{ tons of refrigeration}\)). Deploy N+1 Computer Room Air Handlers (CRAH) providing 3x 20-ton units (40 tons active, 20 tons redundant). Enforce cold-aisle containment with blanking panels on all empty slots.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card">
    <div class="subj-header">
      <div class="subj-q-badge">10 MARKS</div>
      <div class="subj-title">Scenario 4: Out-of-Band Disaster Recovery During OS Bootloader Corruption</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Problem:</strong> An automated patch update corrupts the GRUB bootloader / EFI system partition on a remote headless server located in a lights-out datacenter 500 miles away. The server is stuck at a UEFI shell prompt with in-band networking unreachable.</p>
      <div class="callout callout-deep">
        <div class="callout-label"><i data-lucide="wrench"></i> OOB RECOVERY STEP-BY-STEP PROCEDURE</div>
        <div class="callout-body">
          <ol style="margin-left: 1.2rem; line-height: 1.8;">
            <li><strong>Access Out-of-Band Network:</strong> Connect to the dedicated management network via VPN and authenticate to the server's BMC web interface (iDRAC/iLO) or SSH CLI.</li>
            <li><strong>Launch Virtual Console:</strong> Open the HTML5 Virtual KVM console to view real-time graphical display output and send keystrokes.</li>
            <li><strong>Mount Virtual Media:</strong> Attach an ISO image of a rescue operating system (e.g. AlmaLinux / Ubuntu Live) via Virtual Media redirection over HTTPS.</li>
            <li><strong>Configure One-Time Boot:</strong> In the BMC interface, instruct UEFI to boot from the Virtual CD/DVD drive on next restart.</li>
            <li><strong>Power Cycle &amp; Rebuild:</strong> Issue a cold reset via IPMI/BMC power controls. In the booted rescue shell, mount the host root partition, chroot into the environment, and reinstall GRUB / rebuild the EFI bootloader (<code class="code-inline">grub2-install /dev/nvme0n1</code>). Reboot to restore production service.</li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</article>

<!-- UNIT 1 MASTER ANSWER KEY -->
<article class="doc-page" id="mcq-answer-key-s1">
  <header class="doc-page-header">
    <span class="page-header-meta">Unit 01 • Master Verification Key</span>
    <h2 class="section-title"><span class="sec-num">KEY.1</span> Unit 1 Master Answer Key &amp; Technical Verification Matrix</h2>
    <p class="lead-para">
      Complete answer key and architectural validation matrix for Unit 1 practice bank questions 1 through 30.
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
        <tr><td>Q01</td><td><strong>B</strong></td><td>1U Rack Height: 1.75 inches (44.45 mm)</td><td>EIA-310 Standard</td></tr>
        <tr><td>Q02</td><td><strong>C</strong></td><td>BMC SoC runs on Standby Power Rail (+12VSB)</td><td>IPMI / Redfish Standard</td></tr>
        <tr><td>Q03</td><td><strong>D</strong></td><td>Remote NUMA memory access latency penalty</td><td>Intel UPI / AMD Infinity Fabric</td></tr>
        <tr><td>Q04</td><td><strong>B</strong></td><td>SECDED Hamming Code: 1-bit fix, 2-bit halt</td><td>ECC Memory Architecture</td></tr>
        <tr><td>Q05</td><td><strong>A</strong></td><td>LRDIMM buffers address and data lines</td><td>JEDEC Solid State Standards</td></tr>
        <tr><td>Q06</td><td><strong>C</strong></td><td>2N Power: Concurrent maintainability</td><td>Uptime Institute Tier Standards</td></tr>
        <tr><td>Q07</td><td><strong>B</strong></td><td>PCIe Riser Cards: Horizontal board orientation</td><td>EIA 1U/2U Chassis Engineering</td></tr>
        <tr><td>Q08</td><td><strong>A</strong></td><td>Blanking Panels: Prevent exhaust recirculation</td><td>ASHRAE Thermal Guidelines</td></tr>
        <tr><td>Q09</td><td><strong>D</strong></td><td>U.3 / SFF-TA-1001 Tri-Mode Universal Backplane</td><td>Storage Networking Forum (SNIA)</td></tr>
        <tr><td>Q10</td><td><strong>B</strong></td><td>ASHRAE Class A1 intake temp: 18°C to 27°C</td><td>ASHRAE Datacenter Standards</td></tr>
        <tr><td>Q11</td><td><strong>C</strong></td><td>OCP NIC 3.0 Mezzanine modular form factor</td><td>Open Compute Project</td></tr>
        <tr><td>Q12</td><td><strong>A</strong></td><td>Hot-swap drive staggered ground pins</td><td>Serial Attached SCSI (SAS-3)</td></tr>
        <tr><td>Q13</td><td><strong>D</strong></td><td>PCIe 5.0 x16 raw bandwidth (~63 GB/s direction)</td><td>PCI-SIG Specification 5.0</td></tr>
        <tr><td>Q14</td><td><strong>B</strong></td><td>VRM multiphase buck converters for CPU core Vcore</td><td>Server Power Architecture</td></tr>
        <tr><td>Q15</td><td><strong>C</strong></td><td>System Event Log (SEL) hardware crash recorder</td><td>IPMI 2.0 Specification</td></tr>
        <tr><td>Q16</td><td><strong>A</strong></td><td>Blade midplanes eliminate cabling clutter</td><td>Modular Chassis Architecture</td></tr>
        <tr><td>Q17</td><td><strong>C</strong></td><td>80 Plus Titanium: 96% efficiency at 50% load</td><td>80 PLUS Energy Efficiency</td></tr>
        <tr><td>Q18</td><td><strong>B</strong></td><td>Memory interleaving distributes addresses across channels</td><td>JEDEC Memory Controller Spec</td></tr>
        <tr><td>Q19</td><td><strong>D</strong></td><td>DMTF Redfish RESTful API replaces binary IPMI</td><td>DMTF Standard Specification</td></tr>
        <tr><td>Q20</td><td><strong>A</strong></td><td>Memory mirroring allows online DIMM replacement</td><td>Enterprise Fault Tolerance</td></tr>
        <tr><td>Q21</td><td><strong>B</strong></td><td>Supercapacitor flushes DRAM write cache to Flash</td><td>RAID Controller FBWC Cache</td></tr>
        <tr><td>Q22</td><td><strong>C</strong></td><td>Counter-rotating fans increase linear static pressure</td><td>Server Thermal Dynamics</td></tr>
        <tr><td>Q23</td><td><strong>A</strong></td><td>Point-to-point memory channels tied to CPU socket</td><td>Intel Xeon / AMD EPYC Pinout</td></tr>
        <tr><td>Q24</td><td><strong>D</strong></td><td>Hardware Root of Trust verifies initial UEFI block</td><td>Intel Boot Guard / AMD PSB</td></tr>
        <tr><td>Q25</td><td><strong>B</strong></td><td>1 Watt continuous power = 3.412 BTU/hr heat</td><td>Thermodynamics of Computing</td></tr>
        <tr><td>Q26</td><td><strong>C</strong></td><td>SAS dual-port active/active path redundancy</td><td>T10 SAS Storage Specification</td></tr>
        <tr><td>Q27</td><td><strong>A</strong></td><td>TPM 2.0 cryptographic co-processor and PCRs</td><td>ISO/IEC 11889 TPM Standard</td></tr>
        <tr><td>Q28</td><td><strong>D</strong></td><td>Power Interposer Board (PIB) connects CRPS units</td><td>Server Chassis Electrical Spec</td></tr>
        <tr><td>Q29</td><td><strong>B</strong></td><td>MRC downclocks channels to lowest common frequency</td><td>UEFI Platform Memory Reference</td></tr>
        <tr><td>Q30</td><td><strong>C</strong></td><td>Serial-over-LAN (SoL) text console over IPMI/SSH</td><td>IPMI 2.0 Out-of-Band Standard</td></tr>
      </tbody>
    </table>
  </div>
</article>
"""
