# -*- coding: utf-8 -*-
"""
Unit 2: Computer Networking Topologies & Protocols
In-depth Engineering Standard style:
- Article it2-topologies: Physical & Logical Network Topologies
- Article it2-cables: Physical Media: Cat5e-Cat8, Fiber Optic & T568A/B Pinning
- Article it2-switching: Layer 2 Switching, MAC Learning & Collision/Broadcast Domains
- Article it2-encapsulation: OSI 7-Layer vs TCP/IP 4-Layer Packet Encapsulation Trace
- Article it2-subnetting: IPv4 CIDR Subnetting Math, RFC 1918 & IPv6 SLAAC
- Article practice-mcq-u2-net: Unit 2 Self-Testing Bank: 30 Multiple Choice Questions
- Article practice-subj-short-u2-net: Short Conceptual Questions (5 Sets)
- Article practice-subj-long-u2-net: Analytical & Scenario Problems (4 Sets)
- Article mcq-answer-key-u2-net: Master Answer Key Table
"""

IT_UNIT2_HTML = """
<!-- ==========================================================================
     UNIT 02: COMPUTER NETWORKING TOPOLOGIES & PROTOCOLS
     ========================================================================== -->

<!-- Page 1: Topologies -->
<article class="doc-page" id="it2-topologies">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 02 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">10.</span> Physical vs Logical Network Topologies & High-Availability Meshing
  </h2>

  <p class="lead-para">
    A network topology defines the geometric arrangement and signaling paths connecting communicating nodes. Physical topology governs physical cable layouts and patch panel drops, whereas logical topology dictates the signaling mechanism and data transmission paths mediated by Layer 2 Media Access Control protocols.
  </p>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="network"></i> Full Mesh Interconnect Mathematical Formula</div>
    <p>
      For any fully meshed network comprising \(N\) nodes, the total number of physical point-to-point links required is:
      $$\text{Total Physical Links} = \frac{N(N - 1)}{2}$$
      <strong>Scalability Analysis:</strong>
      <br>&bull; 5 core switches require \((5 \times 4) / 2 = \mathbf{10\text{ links}}\).
      <br>&bull; 20 datacenter spine-leaf switches require \((20 \times 19) / 2 = \mathbf{190\text{ physical fiber runs}}\)! (Demonstrating why Partial Mesh or Spine-and-Leaf Clos topologies are deployed in hyperscale facilities).
    </p>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Topology Type</th>
          <th>Physical Cabling Layout</th>
          <th>Logical Data Flow</th>
          <th>Single Point of Failure (SPOF)</th>
          <th>Fault Tolerance Rating</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Physical Star / Logical Bus</strong></td>
          <td>Cables radiate from central hub to endpoints</td>
          <td>Shared broadcast bus; collisions occur across all ports</td>
          <td>Central legacy multiport repeater hub</td>
          <td>Low (Hub failure halts all communication)</td>
        </tr>
        <tr>
          <td><strong>Physical Star / Logical Star</strong></td>
          <td>Cables connect to intelligent Layer 2 switch</td>
          <td>Dedicated microsegmentation; point-to-point frame forwarding</td>
          <td>Central switch backplane / supervisor engine</td>
          <td>Moderate (Switch failure halts local VLAN)</td>
        </tr>
        <tr>
          <td><strong>Physical Ring</strong></td>
          <td>Closed loop; each node connects to two neighbors</td>
          <td>Token passing (FDDI / Token Ring) or dual counter-rotating rings</td>
          <td>Single cable break if lacking counter-rotating redundancy</td>
          <td>Moderate (High if dual counter-rotating fiber ring like SONET)</td>
        </tr>
        <tr>
          <td><strong>Full Mesh</strong></td>
          <td>Dedicated point-to-point link between every node pair</td>
          <td>Direct transmission with dynamic rerouting around link drops</td>
          <td>None (Zero single points of failure)</td>
          <td>Maximum (Mission-critical core backbones)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="cpu"></i> Silicon & Protocol Mechanics: Spanning Tree Protocol (IEEE 802.1D / 802.1w RSTP)</div>
    <p>
      When redundant Ethernet links are introduced to eliminate single points of failure in switched networks, they inadvertently create physical loops. Because Layer 2 Ethernet frame headers lack a Time-to-Live (TTL) hop decrement field, broadcast frames (such as ARP requests) circulate perpetually, creating a catastrophic <strong>broadcast storm</strong> that consumes 100% of switch backplane bandwidth within milliseconds. The Spanning Tree Protocol prevents this by exchanging Bridge Protocol Data Units (BPDUs), electing a Root Bridge based on lowest Bridge ID (Priority + MAC address), calculating lowest root path cost, and dynamically transitioning redundant switch ports into a <strong>Blocking / Discarding</strong> state. Upon link failure, RSTP recalculates topology in under 1 second to unblock backup paths.
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Structured Cabling & T568A/B Pinning</span>
    <span>Unit 02 • Page 01</span>
  </div>
</article>

<!-- Page 2: Structured Cabling & T568A/B -->
<article class="doc-page" id="it2-cables">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 02 • Page 02</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">11.</span> Structured Cabling, Twisted-Pair Categories (Cat5e&ndash;Cat8) & T568A/B Pinouts
  </h2>

  <p class="lead-para">
    Unshielded Twisted Pair (UTP) copper cabling utilizes differential signaling across four balanced wire pairs to cancel out electromagnetic interference (EMI) and crosstalk. Industry standards defined by TIA/EIA govern maximum link distances, shielding architectures, and RJ-45 modular termination pinouts.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Category</th>
          <th>Max Frequency</th>
          <th>Max Data Rate</th>
          <th>Max Certified Distance</th>
          <th>Shielding Standard & Construction</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cat 5e</strong></td>
          <td>100 MHz</td>
          <td>1 Gbps (1000BASE-T)</td>
          <td>100 meters (328 feet)</td>
          <td>UTP (Unshielded Twisted Pair)</td>
        </tr>
        <tr>
          <td><strong>Cat 6</strong></td>
          <td>250 MHz</td>
          <td>10 Gbps (10GBASE-T)</td>
          <td>55 meters (10 Gbps) / 100 m (1 Gbps)</td>
          <td>UTP / STP (Internal plastic spline separates pairs)</td>
        </tr>
        <tr>
          <td><strong>Cat 6a</strong></td>
          <td>500 MHz</td>
          <td>10 Gbps (10GBASE-T)</td>
          <td>100 meters (328 feet)</td>
          <td>STP / S/FTP (Eliminates alien crosstalk up to 100m)</td>
        </tr>
        <tr>
          <td><strong>Cat 8</strong></td>
          <td>2,000 MHz (2 GHz)</td>
          <td>40 Gbps (40GBASE-T)</td>
          <td>30 meters (98 feet)</td>
          <td>S/FTP (Individual foil pairs + overall braid for datacenter top-of-rack)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="git-commit"></i> TIA/EIA T568A vs T568B RJ-45 Pinout Color Standards</div>
    <p>
      Both standards terminate 8 conductors (4 pairs). <strong>T568B</strong> is the enterprise corporate standard in North America; <strong>T568A</strong> is mandated for US Federal / military installations:
    </p>
    <ul>
      <li><strong>T568B (Standard Corporate):</strong> Pin 1: White/Orange &bull; Pin 2: Orange &bull; Pin 3: White/Green &bull; Pin 4: Blue &bull; Pin 5: White/Blue &bull; Pin 6: Green &bull; Pin 7: White/Brown &bull; Pin 8: Brown</li>
      <li><strong>T568A (Government / Residential):</strong> Pin 1: White/Green &bull; Pin 2: Green &bull; Pin 3: White/Orange &bull; Pin 4: Blue &bull; Pin 5: White/Blue &bull; Pin 6: Orange &bull; Pin 7: White/Brown &bull; Pin 8: Brown</li>
      <li><strong>Straight-Through Cable:</strong> Identical standard on both ends (T568B to T568B). Connects unlike devices (PC to Switch, Switch to Router).</li>
      <li><strong>Crossover Cable:</strong> T568A on one end, T568B on the other. Swaps Pair 2 (Orange) and Pair 3 (Green) to connect like devices (Switch to Switch, PC to PC) without Auto-MDIX.</li>
    </ul>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> Physics of Twisted Pair: Differential Signaling & Twist Ratios</div>
    <p>
      Twisted pair cabling does not send signals relative to chassis ground; instead, it utilizes <strong>differential signaling</strong> where one wire carries \(+V\) and the partner wire carries \(-V\). When external electromagnetic noise strikes the cable, both wires receive identical interference. The receiver subtracts the two signals: \((+V + \text{Noise}) - (-V + \text{Noise}) = 2V\). The noise cancels out completely (Common-Mode Rejection Ratio / CMRR). To prevent Near-End Crosstalk (NEXT) between neighboring pairs, each of the four pairs is wound at a <em>different physical twist pitch</em> (e.g. 3 turns per inch on Orange vs 4.5 turns per inch on Green). Untwisting pairs more than 0.5 inches during RJ-45 crimping destroys this noise cancellation and causes severe frame CRC dropouts.
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Layer 2 Switching & Domains</span>
    <span>Unit 02 • Page 02</span>
  </div>
</article>

<!-- Page 3: Layer 2 Switching -->
<article class="doc-page" id="it2-switching">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 02 • Page 03</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">12.</span> Layer 2 Ethernet Switching, MAC Learning & Domain Boundaries
  </h2>

  <p class="lead-para">
    An Ethernet switch is a multiport Layer 2 bridging device that inspects hardware Media Access Control (MAC) addresses to dynamically microsegment traffic into independent collision domains, operating at line rate via dedicated Application-Specific Integrated Circuits (ASICs).
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Device Type</th>
          <th>OSI Layer</th>
          <th>Collision Domains</th>
          <th>Broadcast Domains</th>
          <th>Forwarding Logic Mechanism</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Legacy Hub</strong></td>
          <td>Layer 1 (Physical)</td>
          <td>Exactly 1 shared across all ports</td>
          <td>Exactly 1 shared across all ports</td>
          <td>Blind electrical repeater; regenerates bits out every port</td>
        </tr>
        <tr>
          <td><strong>Ethernet Switch</strong></td>
          <td>Layer 2 (Data Link)</td>
          <td><strong>1 per physical port</strong> (Microsegmentation)</td>
          <td>1 per VLAN (Defaults to 1 across all ports)</td>
          <td>Hardware MAC Address Table (CAM Table) lookup</td>
        </tr>
        <tr>
          <td><strong>IP Router</strong></td>
          <td>Layer 3 (Network)</td>
          <td>1 per physical port</td>
          <td><strong>1 per interface</strong> (Breaks broadcast domains)</td>
          <td>IP Routing Table lookup (Longest Prefix Match)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="cpu"></i> Silicon Architecture: The 3-Step MAC Learning Algorithm</div>
    <p>
      Inside every modern switch sits Content-Addressable Memory (CAM). When an Ethernet frame enters physical Port 3 with Source MAC `00:1A:2B:3C:4D:5E` and Destination MAC `AA:BB:CC:DD:EE:FF`:
    </p>
    <ol>
      <li><strong>Learn:</strong> The ASIC inspects the <em>Source MAC address</em>. If not in the CAM table, it writes `00:1A:2B:3C:4D:5E &rarr; Port 3` with a 300-second aging timer. If it exists, the timer is refreshed.</li>
      <li><strong>Lookup:</strong> The ASIC inspects the <em>Destination MAC address</em>. If `AA:BB:CC:DD:EE:FF` is matched in CAM on Port 7, the frame is switched directly to Port 7 with zero latency.</li>
      <li><strong>Flood (Unknown Unicast / Broadcast):</strong> If the Destination MAC is not present in CAM (or is the broadcast address `FF:FF:FF:FF:FF:FF`), the frame is flooded out <strong>every active port except the ingress port (Port 3)</strong>. Once the destination node responds, its location is learned, and future frames are unicast.</li>
    </ol>
  </div>

  <div class="page-footer-meta">
    <span>Next: OSI 7-Layer vs TCP/IP Encapsulation</span>
    <span>Unit 02 • Page 03</span>
  </div>
</article>

<!-- Page 4: Encapsulation -->
<article class="doc-page" id="it2-encapsulation">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 02 • Page 04</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">13.</span> OSI 7-Layer Reference Model vs TCP/IP: The End-to-End Encapsulation Story
  </h2>

  <p class="lead-para">
    Data communication relies on layered architectural models that isolate hardware-specific transmission details from high-level application logic. As data descends the protocol stack on the transmitting host, each layer wraps the payload in a protocol-specific header containing addressing and flow-control metadata.
  </p>

  <div class="diagram-container">
    <div class="diagram-title">The End-to-End Encapsulation Pipeline</div>
    <div class="arch-stack-visual">
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">LAYER 7/6/5 • APPLICATION / PRESENTATION / SESSION</span>
        <div class="tier-desc">Raw Data Payload: HTTP GET /index.html • TLS 1.3 Encryption • User Session State</div>
      </div>
      <div style="text-align: center; color: var(--primary); font-weight: 800; font-family: var(--font-mono); font-size: 11px;">
        &Downarrow; Transport Layer Encapsulation (Adds TCP Header: Source Port 54120, Dest Port 443, SEQ#, ACK#) &Downarrow;
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">LAYER 4 • TRANSPORT (PDU = SEGMENT)</span>
        <div class="tier-desc">TCP Segment Header (20 Bytes): Window Size, Checksum, SYN/ACK Flags • End-to-End Reliability</div>
      </div>
      <div style="text-align: center; color: var(--primary); font-weight: 800; font-family: var(--font-mono); font-size: 11px;">
        &Downarrow; Network Layer Encapsulation (Adds IP Header: Source IP 192.168.1.50, Dest IP 93.184.216.34, TTL=64) &Downarrow;
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">LAYER 3 • NETWORK (PDU = PACKET)</span>
        <div class="tier-desc">IPv4/IPv6 Packet Header (20/40 Bytes): Logical Addressing, Fragmentation Flags, Protocol (TCP=6)</div>
      </div>
      <div style="text-align: center; color: var(--primary); font-weight: 800; font-family: var(--font-mono); font-size: 11px;">
        &Downarrow; Data Link Layer Encapsulation (Adds Ethernet Header: Source MAC, Next-Hop MAC, EtherType=0x0800 &amp; Trailer FCS) &Downarrow;
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">LAYER 2 • DATA LINK (PDU = FRAME)</span>
        <div class="tier-desc">Ethernet Frame Header (14 Bytes) + Frame Check Sequence / CRC-32 Trailer (4 Bytes) • Hop-by-Hop Delivery</div>
      </div>
    </div>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> Execution Trace: Why the Destination MAC Changes at Every Hop While IP Stays Constant</div>
    <p>
      When your workstation sends a packet to a remote web server on the Internet (`93.184.216.34`):
    </p>
    <ul>
      <li><strong>IP Destination:</strong> Remains fixed at `93.184.216.34` from source to destination across the entire global Internet.</li>
      <li><strong>MAC Destination:</strong> Your computer does <em>not</em> know the MAC address of Google or Cloudflare. Your OS checks its routing table, determines the destination IP is off-subnet, and uses ARP (Address Resolution Protocol) to resolve the MAC address of its <strong>Default Gateway (Local Router)</strong>!</li>
      <li><strong>Hop Transition:</strong> When the local router receives the Ethernet frame, it strips the Layer 2 header (decapsulation), checks the IP destination, consults its BGP/OSPF routing table, rewrites a brand-new Layer 2 frame containing its own egress MAC as source and the next-hop ISP router as destination, and transmits it. Layer 2 changes at every single physical hop; Layer 3 endures end-to-end!</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: IPv4 Subnetting & CIDR Math</span>
    <span>Unit 02 • Page 04</span>
  </div>
</article>

<!-- Page 5: Subnetting -->
<article class="doc-page" id="it2-subnetting">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 02 • Page 05</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">14.</span> IPv4 CIDR Subnetting Math, Private RFC 1918 & IPv6 SLAAC
  </h2>

  <p class="lead-para">
    An IPv4 address comprises 32 contiguous binary bits grouped into four 8-bit octets. Classless Inter-Domain Routing (CIDR) replaced rigid legacy Class A/B/C boundaries by defining an arbitrary bit prefix denoting the network portion, with remaining host bits determining local addressing capacity.
  </p>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="calculator"></i> Mathematical Subnetting Formulas</div>
    <p>
      For any IPv4 network with prefix length \(/n\):
      <br>&bull; <strong>Host Bits \((H)\):</strong> \(H = 32 - n\)
      <br>&bull; <strong>Total IP Addresses:</strong> \(2^H = 2^{32 - n}\)
      <br>&bull; <strong>Usable Host Addresses:</strong> \(2^H - 2 = 2^{32 - n} - 2\)
      <br>&bull; <em>Why Subtract 2?</em> The first address where all host bits are binary `0` is reserved as the <strong>Network ID</strong>; the last address where all host bits are binary `1` is reserved as the <strong>Directed Broadcast Address</strong>.
    </p>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>CIDR Prefix</th>
          <th>Dotted Decimal Subnet Mask</th>
          <th>Total Addresses</th>
          <th>Usable Host Capacity</th>
          <th>Typical Corporate Deployment Role</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>/24</strong></td>
          <td>255.255.255.0</td>
          <td>256</td>
          <td>254 usable hosts</td>
          <td>Standard department VLAN, corporate office floor</td>
        </tr>
        <tr>
          <td><strong>/26</strong></td>
          <td>255.255.255.192</td>
          <td>64</td>
          <td>62 usable hosts</td>
          <td>Server DMZ subnet, executive secure management</td>
        </tr>
        <tr>
          <td><strong>/28</strong></td>
          <td>255.255.255.240</td>
          <td>16</td>
          <td>14 usable hosts</td>
          <td>Database server cluster, hardware appliance pool</td>
        </tr>
        <tr>
          <td><strong>/30</strong></td>
          <td>255.255.255.252</td>
          <td>4</td>
          <td>2 usable hosts</td>
          <td>Point-to-point router serial WAN links</td>
        </tr>
        <tr>
          <td><strong>/32</strong></td>
          <td>255.255.255.255</td>
          <td>1</td>
          <td>1 host (Host Route)</td>
          <td>Router loopback interface, VPN single host route</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="shield"></i> RFC 1918 Private Address Allocations (Non-Routable on Public Internet)</div>
    <p>
      To prevent exhaustion of the 4.29 billion IPv4 address space, IANA reserved three private address ranges:
    </p>
    <ul>
      <li><strong>Class A Private:</strong> `10.0.0.0/8` (`10.0.0.0` to `10.255.255.255`, 16.7 million addresses) &mdash; Large multinational enterprise backbones.</li>
      <li><strong>Class B Private:</strong> `172.16.0.0/12` (`172.16.0.0` to `172.31.255.255`, 1.04 million addresses) &mdash; University campuses, regional datacenters.</li>
      <li><strong>Class C Private:</strong> `192.168.0.0/16` (`192.168.0.0` to `192.168.255.255`, 65,536 addresses) &mdash; SOHO routers and home consumer LANs.</li>
      <li><strong>APIPA (Automatic Private IP Addressing):</strong> `169.254.0.0/16` &mdash; Assigned automatically by OS when DHCP server fails to respond. Demonstrates link-local Layer 2 connectivity but cannot route to Internet!</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 02 Practice MCQ Bank</span>
    <span>Unit 02 • Page 05</span>
  </div>
</article>

<!-- Page 6: Unit 2 Practice MCQ Bank (30 Questions) -->
<article class="doc-page" id="practice-mcq-u2-net">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 02</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreU2Net">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">15.</span> Unit 02 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Validate your understanding of network topologies, cable pinning, switching mechanics, protocol encapsulation, and subnetting math.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 01 • Full Mesh Scalability</div>
      <div class="mcq-q">How many physical point-to-point links are required to connect 8 core switches in a full mesh topology?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 16 links</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 56 links</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 28 links</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 64 links</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Formula: N(N - 1) / 2 = 8(7) / 2 = 56 / 2 = 28 physical links.
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 02 • Cat 6 Distance Limit</div>
      <div class="mcq-q">What is the maximum certified cable run distance for Cat 6 cabling operating at 10 Gbps (10GBASE-T)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 100 meters</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 55 meters</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 30 meters</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 15 meters</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Cat 6 supports 10 Gbps up to 55 meters in standard environments (or 37m under alien crosstalk). Cat 6a is required for 10 Gbps up to the full 100-meter standard distance.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="2Net" data-correct="A">
      <div class="mcq-num">Question 03 • T568B Pinout Standard</div>
      <div class="mcq-q">In the TIA/EIA T568B wiring standard, which color conductor connects to Pin 1 of the RJ-45 plug?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> White / Orange</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> White / Green</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Solid Green</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> White / Blue</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> T568B starts with Pair 2: Pin 1 is White/Orange, Pin 2 is Orange. (T568A starts with White/Green on Pin 1).
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="2Net" data-correct="D">
      <div class="mcq-num">Question 04 • Switching Forwarding Engine</div>
      <div class="mcq-q">When an Ethernet switch receives a frame destined for an unknown unicast MAC address, how does it process the frame?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Drops the frame immediately</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Sends an ICMP Destination Unreachable packet to the sender</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Stores the frame in flash memory until reboot</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Floods the frame out all active switch ports within the VLAN except the ingress port</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> An unknown unicast frame triggers switch flooding out all ports except the arrival port. When the destination host replies, the switch learns its port location in the CAM table.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 05 • Usable Hosts Calculation</div>
      <div class="mcq-q">How many usable host IP addresses are available in a /27 subnet?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 32 hosts</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 30 hosts</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 62 hosts</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 14 hosts</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Host bits H = 32 - 27 = 5. Total addresses = 2^5 = 32. Usable hosts = 32 - 2 (Network ID and Broadcast) = 30.
      </div>
    </div>

    <!-- Q6 -->
    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 06 • Collision Domains</div>
      <div class="mcq-q">A 24-port unmanaged Ethernet switch with all 24 ports actively connected to host PCs contains how many collision domains?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Exactly 1 collision domain</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 2 collision domains</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 24 collision domains</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 0 collision domains</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Each physical port on a switch represents an independent collision domain (microsegmentation). A 24-port switch provides 24 distinct collision domains.
      </div>
    </div>

    <!-- Q7 -->
    <div class="mcq-card" data-unit="2Net" data-correct="A">
      <div class="mcq-num">Question 07 • APIPA Subnet</div>
      <div class="mcq-q">If a workstation displays an IP address of 169.254.88.12, what does this symptom signify?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The DHCP server failed to respond and the OS assigned an APIPA link-local address</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The computer is connected to a public cloud ISP</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The network interface card is permanently damaged</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> DNS resolution is malfunctioning</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> `169.254.0.0/16` is the IANA APIPA address block automatically assigned when DHCP DORA negotiation times out.
      </div>
    </div>

    <!-- Q8 -->
    <div class="mcq-card" data-unit="2Net" data-correct="D">
      <div class="mcq-num">Question 08 • Spanning Tree Purpose</div>
      <div class="mcq-q">What critical network disaster does Spanning Tree Protocol (STP / IEEE 802.1D) prevent in redundant switched LANs?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Unauthorized Wi-Fi logins</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> IP address duplication</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> High CPU temperatures in routers</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Layer 2 broadcast storms caused by physical switching loops</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Ethernet frames lack a TTL hop count. Redundant switch links without STP create looping broadcast storms that crash switches within seconds.
      </div>
    </div>

    <!-- Q9 -->
    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 09 • OSI Protocol Data Units</div>
      <div class="mcq-q">What is the formal Protocol Data Unit (PDU) at Layer 3 (Network Layer) of the OSI model?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Frame</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Packet</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Segment</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Bit</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Layer 4 PDU is a Segment/Datagram; Layer 3 is a Packet; Layer 2 is a Frame; Layer 1 is Bits.
      </div>
    </div>

    <!-- Q10 -->
    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 10 • Point-to-Point WAN Subnet</div>
      <div class="mcq-q">Which subnet mask prefix conserves maximum IPv4 address space for a point-to-point router serial WAN link?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> /28 (255.255.255.240)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> /29 (255.255.255.248)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> /30 (255.255.255.252)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> /24 (255.255.255.0)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> A /30 subnet contains 4 total IPs: 1 network ID, 2 usable host IPs (one for each router interface), and 1 broadcast IP, leaving zero wasted addresses.
      </div>
    </div>

    <!-- Q11 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="2Net" data-correct="A">
      <div class="mcq-num">Question 11 • Subnet Broadcast Address</div>
      <div class="mcq-q">What is the directed broadcast address for the subnet containing host IP 192.168.10.65 with a /26 prefix?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 192.168.10.127</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 192.168.10.255</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 192.168.10.64</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 192.168.10.128</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> For /26, block size = 2^(32-26) = 64. Subnets are: .0, .64, .128, .192. Host .65 falls in the .64 subnet (Network ID: .64, Broadcast: .127).
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 12 • Address Resolution Protocol</div>
      <div class="mcq-q">What is the exact functional objective of the Address Resolution Protocol (ARP)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Resolves human-readable domain names to IPv4 addresses</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Maps a known Layer 3 IPv4 address to its corresponding physical Layer 2 MAC address</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Encrypts Ethernet frames on the local wire</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Assigns gateway addresses automatically to client devices</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> ARP operates between Layer 2 and Layer 3, broadcasting "Who has IP X.X.X.X? Tell IP Y.Y.Y.Y" to discover the destination hardware MAC address.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 13 • Fiber Optic Modes</div>
      <div class="mcq-q">Why is Single-Mode Fiber (SMF) selected over Multi-Mode Fiber (MMF) for long-distance telecommunications backbones?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Single-mode fiber is much cheaper to terminate than copper</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Single-mode fiber uses LED light sources rather than lasers</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Its microscopic 9-micron core allows a single ray of laser light to travel with virtually zero modal dispersion over 40+ kilometers</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Single-mode fiber can carry high-voltage electrical current</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Single-mode fiber has a tiny ~9 &mu;m glass core that prevents modal dispersion (light bouncing at different angles), enabling distances up to 40-100 km. MMF has a larger 50-62.5 &mu;m core limited to ~550m.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="D">
      <div class="mcq-num">Question 14 • Broadcast Domains</div>
      <div class="mcq-q">Which networking device is required to divide a single physical local area network into multiple broadcast domains?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Unmanaged Layer 2 Switch</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Cat 6a Patch Panel</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Multiport Active Repeater Hub</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Layer 3 Router (or Layer 3 Managed Switch with VLAN routing)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Routers drop broadcast frames by default, creating a distinct broadcast domain boundary on each interface.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="A">
      <div class="mcq-num">Question 15 • Crossover Cable Pinout</div>
      <div class="mcq-q">Which two wire pairs are physically transposed between T568A and T568B to construct an Ethernet crossover cable?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Pair 2 (Orange) and Pair 3 (Green)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Pair 1 (Blue) and Pair 4 (Brown)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Pair 2 (Orange) and Pair 4 (Brown)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Pair 1 (Blue) and Pair 3 (Green)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> T568A uses Green on Pins 1 & 2 and Orange on Pins 3 & 6; T568B swaps them (Orange on 1 & 2, Green on 3 & 6), transposing transmit (Tx) and receive (Rx) pairs.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 16 • RFC 1918 Class B Range</div>
      <div class="mcq-q">What is the exact private address range defined by RFC 1918 for Class B networks?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 10.0.0.0 to 10.255.255.255</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 172.16.0.0 to 172.31.255.255 (/12 prefix)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 192.168.0.0 to 192.168.255.255</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 169.254.0.0 to 169.254.255.255</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The Class B private block is `172.16.0.0/12`, providing 16 contiguous /16 networks (`172.16.0.0` through `172.31.255.255`).
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 17 • Ethernet Framing Overhead</div>
      <div class="mcq-q">Which field in an Ethernet frame trailer allows the receiving network card to detect corrupted bits?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Preamble</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> EtherType</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Frame Check Sequence (FCS / CRC-32)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Start Frame Delimiter (SFD)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> The 4-byte Frame Check Sequence (FCS) contains a Cyclic Redundancy Check (CRC-32) hash. If the calculated hash fails to match the received hash, the frame is silently discarded.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="D">
      <div class="mcq-num">Question 18 • Transport Layer Protocols</div>
      <div class="mcq-q">Which Transport Layer protocol should be chosen for real-time VoIP voice packets where low latency is critical and dropped packets cannot be retransmitted?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Transmission Control Protocol (TCP)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Internet Control Message Protocol (ICMP)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Address Resolution Protocol (ARP)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> User Datagram Protocol (UDP)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> UDP provides connectionless, best-effort delivery with zero handshake overhead and no retransmission delays, making it ideal for streaming audio/video and DNS queries.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="A">
      <div class="mcq-num">Question 19 • Auto-MDIX Technology</div>
      <div class="mcq-q">What does Auto-MDIX (Medium Dependent Interface Crossover) do on modern network switches?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Automatically detects and configures whether straight-through or crossover pinout is needed</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Upgrades Cat 5e cables to Cat 6a speeds</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Powers switches without needing an AC electrical cord</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Disables Wi-Fi interference automatically</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Auto-MDIX eliminates the need for manual crossover cables by electronically swapping the Tx and Rx pairs inside the switch physical layer (PHY) transceiver.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 20 • IPv6 Address Length</div>
      <div class="mcq-q">How many total bits constitute an IPv6 address compared to a 32-bit IPv4 address?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 64 bits</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 128 bits (represented as 8 groups of 4 hexadecimal digits)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 256 bits</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 512 bits</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> IPv6 expands the address space to 128 bits (yielding 3.4 &times; 10^38 addresses), formatted as 8 hex hextets separated by colons.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 21 • VLAN Tagging Standard</div>
      <div class="mcq-q">Which IEEE standard inserts a 4-byte VLAN identification tag into the Ethernet frame header on trunk links?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> IEEE 802.3ad</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> IEEE 802.11ax</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> IEEE 802.1Q</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> IEEE 802.15.1</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> IEEE 802.1Q defines industry-standard frame tagging on trunk links, adding a 12-bit VLAN ID (allowing 4,096 VLANs) and 3-bit CoS priority bits.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="D">
      <div class="mcq-num">Question 22 • Cat 8 Deployment Focus</div>
      <div class="mcq-q">What is the certified operating distance of Cat 8 cabling running at 40 Gbps?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 100 meters</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 55 meters</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 10 kilometers</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 30 meters (98 feet)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Cat 8 operates at 2,000 MHz (2 GHz) to deliver 25GBASE-T and 40GBASE-T, but is physically restricted to a 30-meter channel intended for datacenter Top-of-Rack switch-to-server interconnects.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="A">
      <div class="mcq-num">Question 23 • Default Gateway Function</div>
      <div class="mcq-q">Why does a host computer forward IP packets to its configured Default Gateway?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The host performs a bitwise AND on the destination IP with its subnet mask and determines the target is on a remote network</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The host's ARP table has reached full capacity</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The Default Gateway acts as the primary web browser cache</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The host requires permission to transmit Wi-Fi packets</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> When the bitwise AND calculation reveals that the destination IP's network ID differs from the host's own local subnet, the host forwards the packet to the Default Gateway's MAC address.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 24 • Fiber Cable Connectors</div>
      <div class="mcq-q">Which compact fiber optic connector uses a push-pull latching mechanism and is standard on modern SFP+ transceiver modules?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ST (Straight Tip bayonet connector)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> LC (Lucent Connector)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> BNC connector</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> F-Type coaxial connector</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The LC (Lucent Connector) has a small 1.25 mm ferrule with a RJ-45 style push-pull latch, making it the industry standard for high-density enterprise switch transceivers (SFP/SFP+).
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 25 • Classless Inter-Domain Routing</div>
      <div class="mcq-q">What major limitation of legacy classful IPv4 addressing did CIDR (RFC 1519) solve in 1993?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It allowed copper cables to transmit without electrical shielding</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It introduced encryption into the IP header</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It eliminated rigid /8, /16, and /24 class boundaries, curbing rapid IP exhaustion and global routing table explosion via route summarization</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It made DNS servers unnecessary</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> CIDR enabled Variable Length Subnet Masking (VLSM) and route aggregation (supernetting), preventing catastrophic waste where a company needing 300 hosts was forced to consume a whole /16 (65,536 IPs).
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="D">
      <div class="mcq-num">Question 26 • TCP 3-Way Handshake</div>
      <div class="mcq-q">In what strict order are TCP control flags exchanged to establish a reliable connection?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> ACK &rarr; SYN &rarr; FIN</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> FIN &rarr; FIN-ACK &rarr; RST</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> SYN &rarr; ACK &rarr; SYN-ACK</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> SYN &rarr; SYN-ACK &rarr; ACK</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Host A sends SYN (synchronize initial sequence number); Host B replies with SYN-ACK; Host A completes with ACK. Both sequence spaces are synchronized.
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="A">
      <div class="mcq-num">Question 27 • Power over Ethernet Standard</div>
      <div class="mcq-q">What is the maximum DC electrical power delivered at the switch port by the PoE+ (IEEE 802.3at) standard?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 30.0 Watts (yielding ~25.5W at the powered device after cable loss)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 15.4 Watts</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 60.0 Watts</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 100.0 Watts</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> 802.3at (PoE+) provides 30W from the switch port (25.5W at the device), sufficient for PTZ IP security cameras and multi-radio Wi-Fi 6 access points. (802.3af was 15.4W; 802.3bt PoE++ is 60W/90W).
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="B">
      <div class="mcq-num">Question 28 • IPv6 SLAAC Mechanism</div>
      <div class="mcq-q">How does an IPv6 client automatically configure its global unicast address without requiring a stateful DHCPv6 server?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By running an ARP broadcast across the LAN</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Via SLAAC (Stateless Address Autoconfiguration) using ICMPv6 Router Solicitation and Router Advertisement packets</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By copying the MAC address of the default gateway</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> By querying the local DNS server directly on port 53</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Under SLAAC, the host sends an ICMPv6 Router Solicitation (RS); the local router responds with a Router Advertisement (RA) containing the /64 network prefix. The client appends its own 64-bit interface ID (EUI-64 or randomized).
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="C">
      <div class="mcq-num">Question 29 • Time-to-Live Operation</div>
      <div class="mcq-q">What happens to an IPv4 packet when its Time-to-Live (TTL) field is decremented to zero by an intermediate router?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The packet is forwarded immediately to the destination</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The router re-encapsulates the packet into an IPv6 header</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The router discards the packet and sends an ICMP Type 11 (Time Exceeded) message to the source IP</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The router stores the packet in NVRAM for 24 hours</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Every router decrements the TTL by 1. When TTL hits 0, the packet is dropped to prevent routing loops, and an ICMP Type 11 message is returned (the fundamental mechanism used by `traceroute`!).
      </div>
    </div>

    <div class="mcq-card" data-unit="2Net" data-correct="D">
      <div class="mcq-num">Question 30 • Loopback Address Block</div>
      <div class="mcq-q">Which complete IPv4 address block is reserved by IANA for internal host software loopback testing?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 192.168.1.0/24</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 10.0.0.0/8</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 169.254.0.0/16</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 127.0.0.0/8 (including 127.0.0.1)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The entire `127.0.0.0/8` block (16.7 million IPs) is reserved for host loopback. Packets sent to this block never exit the local TCP/IP stack or hit the physical network interface.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 02 Conceptual Questions</span>
    <span>Unit 02 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 2 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-u2-net">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 02</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">16.</span> Unit 2 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted explanations of core networking protocols, domain boundaries, and cable construction standards.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Contrast Collision Domains and Broadcast Domains, detailing how switches and routers impact each.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Collision Domain:</strong> A physical network segment where data packets can collide with one another if two transmitters broadcast simultaneously (governed by CSMA/CD). A legacy hub has only <em>1 shared collision domain</em> across all ports. A switch microsegments the network: <em>each physical switch port is its own separate collision domain</em>, completely eliminating half-duplex collisions in full-duplex operation.</p>
        <p><strong>Broadcast Domain:</strong> The scope of nodes that receive an Ethernet broadcast frame (destination MAC `FF:FF:FF:FF:FF:FF`). A standard Layer 2 switch forwards broadcasts out every port; thus, an unmanaged switch is <em>1 single broadcast domain</em>. A Layer 3 router drops broadcasts by default: <em>each router interface terminates and creates a new broadcast domain</em>.</p>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Explain the physical purpose of the plastic center spine (spline) inside Cat 6 cabling and how pair twist pitches combat crosstalk.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Plastic Spline:</strong> Operating at 250 MHz (compared to 100 MHz in Cat 5e) makes signals highly vulnerable to <em>Near-End Crosstalk (NEXT)</em> between adjacent pairs inside the same jacket. The cross-shaped polyethylene spline physically separates the four pairs, maintaining a precise, uniform spatial distance throughout the cable length.</p>
        <p><strong>Varying Twist Pitches:</strong> Each of the four wire pairs is twisted at a deliberately different rate (e.g. Blue pair has 3.8 twists/inch; Green pair has 4.5 twists/inch). If pairs had identical twist rates, their magnetic fields would align periodically along the run, inducing electromagnetic noise. Staggering twist rates ensures magnetic fields remain out of phase, maximizing Common-Mode Rejection.</p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> Walk through the exact Address Resolution Protocol (ARP) resolution process when Host A communicates with Host B on the same local subnet.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>Host A (`192.168.1.10`) wants to send an IP packet to Host B (`192.168.1.20`), but its local ARP cache contains no entry for Host B:</p>
        <ol>
          <li><strong>ARP Request Broadcast:</strong> Host A generates an ARP Request frame with Source MAC = Host A's MAC, Destination MAC = `FF:FF:FF:FF:FF:FF` (Layer 2 broadcast). Inside the ARP payload: "Who has IP 192.168.1.20? Tell 192.168.1.10."</li>
          <li><strong>Switch Flooding:</strong> The local switch floods the broadcast frame out all ports.</li>
          <li><strong>Host Evaluation:</strong> Every host on the subnet receives the frame. Hosts with other IPs discard it. Host B matches its own IP.</li>
          <li><strong>ARP Reply Unicast:</strong> Host B records Host A's mapping in its ARP cache and transmits an ARP Reply unicast directly to Host A's MAC: "192.168.1.20 is at MAC 00:AA:22:33:44:55."</li>
          <li><strong>Packet Transmission:</strong> Host A caches the entry and encapsulates its pending IP packet inside an Ethernet frame addressed to Host B's newly discovered MAC.</li>
        </ol>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> Why can IPv6 function without traditional broadcast addressing, and what protocol mechanism replaces ARP in IPv6?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>IPv6 completely eliminated the concept of broadcast addressing (`FF:FF:FF:FF:FF:FF` or subnet broadcast) because broadcasting interrupts every single CPU on the local wire to process unrequested frames, causing severe battery drain on mobile devices and wasting switch fabric capacity.</p>
        <p>In IPv6, broadcasting is replaced by <strong>Multicast</strong> and <strong>Neighbor Discovery Protocol (NDP / RFC 4861)</strong> running over ICMPv6. To resolve an IPv6 address to a link-layer MAC address, a host transmits a <em>Neighbor Solicitation (NS)</em> to a narrow <strong>Solicited-Node Multicast Address</strong> (`FF02::1:FFxx:xxxx`). Only the specific host whose last 24 bits match the multicast group listens and replies with a <em>Neighbor Advertisement (NA)</em>. All other uninvolved nodes ignore the packet at the hardware NIC level!</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> Perform a complete subnet breakdown for the IP address 172.16.45.130/28: find the Subnet Mask, Network ID, Broadcast ID, Usable Host Range, and Total Usable Hosts.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Step-by-Step Subnetting Calculation:</strong></p>
        <ul>
          <li><strong>Prefix Length:</strong> /28 means 28 network bits and 4 host bits (\(32 - 28 = 4\)).</li>
          <li><strong>Subnet Mask:</strong> In the 4th octet, 4 bits on = \(128 + 64 + 32 + 16 = 240\). Full mask: <strong>255.255.255.240</strong>.</li>
          <li><strong>Block Size (Magic Number):</strong> \(256 - 240 = \mathbf{16}\) (or \(2^4 = 16\)). Subnets in the 4th octet increment by 16: .0, .16, .32, .48, .64, .80, .96, .112, .128, .144...</li>
          <li><strong>Locate IP .130:</strong> Falls between 128 and 144.
            <br>&bull; <strong>Network ID:</strong> <strong>172.16.45.128</strong>
            <br>&bull; <strong>Broadcast ID:</strong> The number before the next subnet (144 - 1): <strong>172.16.45.143</strong>
            <br>&bull; <strong>Usable Host Range:</strong> <strong>172.16.45.129 to 172.16.45.142</strong>
            <br>&bull; <strong>Usable Hosts Capacity:</strong> \(2^4 - 2 = 16 - 2 = \mathbf{14\text{ usable hosts}}\).</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 02 Analytical Problems</span>
    <span>Unit 02 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 2 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-u2-net">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 02</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">17.</span> Unit 2 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Complex enterprise network engineering challenges covering routing convergence, STP failures, subnet reallocation, and cable plant troubleshooting.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Network Outage Triage: Broadcast Storm Collapse Triggered by Novice Patch Cord Loop in Conference Room</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> At 10:15 AM, the entire corporate headquarters LAN suffers catastrophic degradation. IP phones reboot simultaneously, workstations lose access to file servers, and switch management LEDs across all distribution racks flash rapidly in unison. The network monitoring dashboard reports 100% switch backplane utilization with millions of broadcast frames per second.</p>
        <p><strong>Engineering Analysis & Root Cause:</strong></p>
        <ol>
          <li><strong>The Physical Trigger:</strong> An employee in a conference room plugged both ends of a standard RJ-45 patch cable into two adjacent wall jacks. Both jacks were wired back to the same access layer switch stack, creating a physical Layer 2 copper loop.</li>
          <li><strong>Why the Storm Occurs:</strong> When any node on that VLAN emitted a broadcast (e.g. an ARP query or DHCP discover), the switch flooded the frame out Port 1. The frame entered the patch cord, arrived at Port 2, and the switch immediately flooded it back out Port 1 and all other ports! Because Ethernet headers lack a TTL decrement counter, each frame duplicates exponentially, saturating the switch CAM table and backplane in seconds.</li>
          <li><strong>Why STP Failed to Stop It:</strong> The network administrator had enabled `portfast` on edge access ports to allow fast DHCP address acquisition for client PCs, but <em>failed to enable BPDU Guard</em> (`spanning-tree bpduguard enable`). Without BPDU Guard, when the loop generated BPDUs, the PortFast port ignored them rather than immediately transitioning into an `err-disable` shutdown state.</li>
          <li><strong>Remediation:</strong> Immediately unplug the offending patch cord. Globally enforce `spanning-tree portfast bpduguard default` on all edge access ports and configure Storm Control (`storm-control broadcast level 1.0`) to drop broadcast traffic if it exceeds 1% of port bandwidth.</li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> Subnetting Architecture: Designing an Optimal VLSM Address Scheme for a 4-Branch Enterprise</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Design Brief:</strong> An organization is allocated the private network block `192.168.100.0/24`. They mandate an optimal Variable Length Subnet Mask (VLSM) allocation to satisfy the following requirements with zero overlapping addresses and room for growth:</p>
        <ul>
          <li><strong>Sales Department:</strong> 100 host workstations</li>
          <li><strong>Engineering Department:</strong> 50 host workstations</li>
          <li><strong>Server Farm DMZ:</strong> 25 host servers</li>
          <li><strong>WAN Link 1:</strong> Point-to-point connection between HQ and Branch Router (2 IP addresses)</li>
          <li><strong>WAN Link 2:</strong> Point-to-point connection between HQ and DR Site (2 IP addresses)</li>
        </ul>
        <p><strong>VLSM Allocation Plan (Ordered by Largest Subnet First):</strong></p>
        <ol>
          <li><strong>Sales (Need 100 hosts):</strong> Nearest power of 2: \(2^7 - 2 = 126\) hosts. Requires 7 host bits &rarr; Prefix: <strong>/25</strong> (Mask: `255.255.255.128`).
            <br>&bull; Network ID: `192.168.100.0/25` &bull; Usable Range: `.1` to `.126` &bull; Broadcast: `.127`.</li>
          <li><strong>Engineering (Need 50 hosts):</strong> Next available IP: `192.168.100.128`. Nearest power of 2: \(2^6 - 2 = 62\) hosts. Requires 6 host bits &rarr; Prefix: <strong>/26</strong> (Mask: `255.255.255.192`).
            <br>&bull; Network ID: `192.168.100.128/26` &bull; Usable Range: `.129` to `.190` &bull; Broadcast: `.191`.</li>
          <li><strong>Server Farm DMZ (Need 25 hosts):</strong> Next available IP: `192.168.100.192`. Nearest power of 2: \(2^5 - 2 = 30\) hosts. Requires 5 host bits &rarr; Prefix: <strong>/27</strong> (Mask: `255.255.255.224`).
            <br>&bull; Network ID: `192.168.100.192/27` &bull; Usable Range: `.193` to `.222` &bull; Broadcast: `.223`.</li>
          <li><strong>WAN Link 1 (Need 2 hosts):</strong> Next available IP: `192.168.100.224`. Prefix: <strong>/30</strong> (Mask: `255.255.255.252`).
            <br>&bull; Network ID: `192.168.100.224/30` &bull; Usable IPs: `.225` and `.226` &bull; Broadcast: `.227`.</li>
          <li><strong>WAN Link 2 (Need 2 hosts):</strong> Next available IP: `192.168.100.228`. Prefix: <strong>/30</strong> (Mask: `255.255.255.252`).
            <br>&bull; Network ID: `192.168.100.228/30` &bull; Usable IPs: `.229` and `.230` &bull; Broadcast: `.231`.</li>
          <li><strong>Remaining Unallocated Pool:</strong> `192.168.100.232` to `.255` (24 IP addresses preserved for future subnets!).</li>
        </ol>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> Physical Cable Plant Diagnosis: Excessive FCS Errors and Duplex Mismatches on a 90-Meter Run</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A newly installed workstation located in an annex building connected via a 90-meter Cat 5e horizontal cable run experiences extreme network sluggishness. Pinging the local gateway shows 20% packet loss, and file copies stall. Running `show interface gigabitethernet 0/12` on the Cisco access switch reveals thousands of <strong>Late Collisions</strong> and <strong>FCS-Err (CRC checksum)</strong> increments, with port operating at 100 Mbps Half-Duplex.</p>
        <p><strong>Diagnostic Protocol & Resolution:</strong></p>
        <ul>
          <li><strong>Root Cause 1: Duplex Mismatch:</strong> The switch port had its speed and duplex hardcoded to `100 Full`, but the workstation NIC was set to `Auto-Negotiate`. Under IEEE 802.3u standards, if one side does not negotiate, the auto-negotiating side defaults to <em>Half-Duplex</em> for backward compatibility! The workstation expects CSMA/CD collisions while the switch transmits simultaneously, generating continuous collisions and FCS frame discards. Setting both sides to `Auto` resolves the duplex mismatch.</li>
          <li><strong>Root Cause 2: Excessive Pair Untwisting at Patch Panel:</strong> A Time-Domain Reflectometer (TDR) and cable certifier test reveals that during termination on the 110-punchdown block, the field technician untwisted the copper pairs by approximately 1.5 inches. At 90 meters (near the 100m maximum limit), this excessive untwist eliminates Common-Mode Rejection, allowing high electromagnetic noise from adjacent fluorescent light ballasts to corrupt data bits. Re-terminating with less than 0.5 inches of untwist restores zero-loss 1000BASE-T gigabit speeds.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> Packet Encapsulation & Routing: Resolving Off-Subnet Host Communication via Proxy ARP vs Default Gateway</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>System Engineering Request:</strong> A network engineer misconfigures a Linux server with an incorrect subnet mask: IP `192.168.1.50/16` (Mask `255.255.0.0`), while the rest of the subnet and the router use `192.168.1.50/24` (Mask `255.255.255.0`). The default gateway is `192.168.1.1`.</p>
        <p><strong>Behavioral Trace:</strong></p>
        <ul>
          <li><strong>Local Communication (to 192.168.1.75):</strong> Works perfectly. Both /16 and /24 bitwise AND calculations conclude that `192.168.1.75` is on the local network; standard ARP resolves the destination MAC.</li>
          <li><strong>Remote Communication (to 192.168.2.100):</strong> Fails completely! Because the server has a /16 mask, its local TCP/IP stack calculates that `192.168.2.100` is on its <em>local subnet</em> (`192.168.0.0/16`). Therefore, instead of forwarding the packet to the Default Gateway (`192.168.1.1`), the server broadcasts an ARP Request: "Who has 192.168.2.100?".</li>
          <li><strong>The Proxy ARP Trap:</strong> If the Cisco router has `ip proxy-arp` enabled, the router will intercept the ARP broadcast and reply with its own MAC address, masking the configuration error. However, if Proxy ARP is disabled (as security baselines require to prevent spoofing), no device replies, the ARP request times out, and the server reports "Destination Host Unreachable"! Correcting the mask to `/24` immediately directs remote traffic to the gateway.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 02 Master MCQ Answer Key</span>
    <span>Unit 02 • Page 08</span>
  </div>
</article>

<!-- Page 9: Master Answer Key Table -->
<article class="doc-page" id="mcq-answer-key-u2-net">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • Unit 02</span>
    <span class="meta-tag">Master Answer Key • 30 Questions</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">18.</span> Unit 2 Master Answer Key Table & Verification Matrix
  </h2>

  <p class="lead-para">
    Complete verified answer keys and core learning objectives for all 30 multiple choice questions in Unit 2.
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
        <tr><td>01</td><td><strong style="color:var(--primary);">C</strong></td><td>Full Mesh point-to-point link formula (N(N-1)/2 = 28)</td><td>16</td><td><strong style="color:var(--primary);">B</strong></td><td>RFC 1918 Class B private allocation (172.16.0.0/12)</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">B</strong></td><td>Cat 6 maximum distance at 10 Gbps (55 meters)</td><td>17</td><td><strong style="color:var(--primary);">C</strong></td><td>Ethernet Frame Check Sequence (FCS/CRC-32) trailer</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">A</strong></td><td>T568B Pin 1 color standard (White/Orange)</td><td>18</td><td><strong style="color:var(--primary);">D</strong></td><td>UDP protocol selection for real-time low-latency traffic</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">D</strong></td><td>Switch unknown unicast frame flooding behavior</td><td>19</td><td><strong style="color:var(--primary);">A</strong></td><td>Auto-MDIX automatic TX/RX pair crossover detection</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">B</strong></td><td>/27 usable host capacity calculation (2^5 - 2 = 30)</td><td>20</td><td><strong style="color:var(--primary);">B</strong></td><td>IPv6 128-bit address representation</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">C</strong></td><td>Switch per-port collision domain microsegmentation (24)</td><td>21</td><td><strong style="color:var(--primary);">C</strong></td><td>IEEE 802.1Q 4-byte VLAN frame tagging standard</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">A</strong></td><td>APIPA 169.254.0.0/16 DHCP timeout auto-assignment</td><td>22</td><td><strong style="color:var(--primary);">D</strong></td><td>Cat 8 40 Gbps certified distance limit (30 meters)</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">D</strong></td><td>Spanning Tree Protocol (STP) loop & storm prevention</td><td>23</td><td><strong style="color:var(--primary);">A</strong></td><td>Default Gateway routing for off-subnet IP destinations</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">B</strong></td><td>OSI Layer 3 Protocol Data Unit (Packet)</td><td>24</td><td><strong style="color:var(--primary);">B</strong></td><td>LC (Lucent Connector) small-form-factor fiber connector</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">C</strong></td><td>Point-to-point serial WAN link prefix (/30)</td><td>25</td><td><strong style="color:var(--primary);">C</strong></td><td>CIDR classless addressing & route aggregation benefits</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">A</strong></td><td>Subnet directed broadcast address calculation (.127)</td><td>26</td><td><strong style="color:var(--primary);">D</strong></td><td>TCP 3-way handshake flag order (SYN &rarr; SYN-ACK &rarr; ACK)</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">B</strong></td><td>Address Resolution Protocol (ARP) IP-to-MAC mapping</td><td>27</td><td><strong style="color:var(--primary);">A</strong></td><td>PoE+ IEEE 802.3at maximum port wattage (30.0 Watts)</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">C</strong></td><td>Single-Mode Fiber (SMF) 9&mu;m core & low modal dispersion</td><td>28</td><td><strong style="color:var(--primary);">B</strong></td><td>IPv6 SLAAC Router Solicitation / Advertisement autoconfig</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">D</strong></td><td>Layer 3 Routers dividing broadcast domains</td><td>29</td><td><strong style="color:var(--primary);">C</strong></td><td>IPv4 TTL decrement to zero (ICMP Type 11 Time Exceeded)</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">A</strong></td><td>Crossover cable pair transposition (Pair 2 and Pair 3)</td><td>30</td><td><strong style="color:var(--primary);">D</strong></td><td>IANA Loopback address reservation (127.0.0.0/8)</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 02 Complete • Next: Unit 03 Mobile & Peripherals</span>
    <span>Unit 02 • Page 09</span>
  </div>
</article>
"""
