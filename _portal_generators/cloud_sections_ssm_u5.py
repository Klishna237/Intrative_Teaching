# -*- coding: utf-8 -*-
"""
Cloud Administration (AWS) - Unit 5: Cloud Networking & Virtual Private Cloud (VPC)
Master Gold Standard Layout:
- c4-vpc: VPC CIDR Math, RFC 1918, The 5 Reserved IPs per Subnet & Multi-AZ Subnets
- c4-routing: Internet Gateways (IGW), NAT Gateways, Egress-Only IGW & Route Tables
- c4-security: Security Groups (Stateful) vs Network Access Control Lists (Stateless NACLs)
- c4-peering: VPC Peering, AWS Transit Gateway (Hub-and-Spoke) & AWS PrivateLink Endpoints
- c4-hybrid: Hybrid Connectivity: AWS Site-to-Site VPN vs AWS Direct Connect (DX)
- practice-mcq-c4: 30 MCQs with dynamic scoring
- practice-subj-short-c4: 5 Short Conceptual Sets
- practice-subj-long-c4: 4 Deep Analytical Scenarios
- mcq-answer-key-c4: Master Answer Key Table
"""

CLOUD_UNIT5_HTML = """
<!-- ==========================================================================
     UNIT 05: CLOUD NETWORKING & VIRTUAL PRIVATE CLOUD (VPC)
     ========================================================================== -->

<!-- Page 1: VPC Architecture & Reserved IPs -->
<article class="doc-page" id="c4-vpc">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">28.</span> Amazon Virtual Private Cloud (VPC) Architecture &amp; The 5 Reserved IPs
  </h2>

  <p class="lead-para">
    An Amazon VPC is a logically isolated software-defined virtual network dedicated to an AWS account. It mirrors a traditional physical corporate network, operating within an overlay network using encapsulation protocols executed directly on the AWS Nitro hardware fabric.
  </p>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="calculator"></i> Subnet Usable IP Math: The 5 Reserved IPs per Subnet</div>
    <p>
      In standard on-premises networking, only 2 addresses are subtracted from a subnet (Network ID and Directed Broadcast). <strong>In AWS VPC, exactly 5 IP addresses are reserved in every subnet and cannot be assigned to instances:</strong>
    </p>
    <ul>
      <li><strong>`.0` &ndash; Network Address:</strong> The base CIDR network identifier.</li>
      <li><strong>`.1` &ndash; VPC Local Router:</strong> Assigned to the default gateway router virtual interface.</li>
      <li><strong>`.2` &ndash; Amazon Route 53 DNS Resolver:</strong> The base of the VPC CIDR plus 2 (e.g. `10.0.0.2` in `10.0.0.0/16`), providing AmazonProvidedDNS.</li>
      <li><strong>`.3` &ndash; Future AWS Reservation:</strong> Reserved by AWS for future protocol extensions.</li>
      <li><strong>`.255` &ndash; Network Broadcast Address:</strong> Although AWS does not support broadcast routing, the top address is reserved to maintain standard TCP/IP compatibility.</li>
      <li><strong>Capacity Formula:</strong> For a \(/24\) subnet (\(2^8 = 256\text{ total}\)), usable instances = \(256 - 5 = \mathbf{251\text{ usable IP addresses}}\).</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: Gateways & Routing Topologies</span>
    <span>Unit 05 • Page 01</span>
  </div>
</article>

<!-- Page 2: Gateways & Routing -->
<article class="doc-page" id="c4-routing">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 02</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">29.</span> Internet Gateways (IGW), NAT Gateways &amp; Route Table Topologies
  </h2>

  <p class="lead-para">
    Traffic isolation between public-facing and internal database tiers is mediated by VPC Route Tables and managed gateway appliances.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Gateway Component</th>
          <th>Physical Placement</th>
          <th>High Availability Model</th>
          <th>Traffic Direction</th>
          <th>Cost Metric</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Internet Gateway (IGW)</strong></td>
          <td>Attached to VPC boundary</td>
          <td>Horizontally scaled, redundant, highly available managed service with zero bandwidth bottlenecks</td>
          <td>Bidirectional (Inbound and Outbound IPv4 &amp; IPv6)</td>
          <td><strong>Free</strong> (Zero hourly or data transfer fees)</td>
        </tr>
        <tr>
          <td><strong>NAT Gateway</strong></td>
          <td>Deployed inside a <strong>Public Subnet</strong></td>
          <td>Redundant within an AZ; <strong>must deploy 1 NAT Gateway per AZ</strong> for Multi-AZ fault tolerance!</td>
          <td>Outbound ONLY (Private instances initiate outbound internet requests; blocks inbound WAN probes)</td>
          <td>Hourly fee ($0.045/hr) + Per-GB data processing fees ($0.045/GB)</td>
        </tr>
        <tr>
          <td><strong>Egress-Only Internet Gateway (EIGW)</strong></td>
          <td>Attached to VPC boundary</td>
          <td>Horizontally scaled managed service</td>
          <td>Outbound ONLY for <strong>IPv6 traffic</strong> (IPv6 does not use NAT; EIGW prevents inbound connections)</td>
          <td><strong>Free</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> Routing Rule: What Makes a Subnet "Public" vs "Private"?</div>
    <p>
      In AWS, there is no physical switch setting that makes a subnet public or private. A subnet is defined as:
      <br>&bull; <strong>Public Subnet:</strong> Its associated Route Table contains an explicit default route pointing to the Internet Gateway: `0.0.0.0/0 &rarr; igw-xxxxxxxxx`.
      <br>&bull; <strong>Private Subnet:</strong> Its associated Route Table points default traffic to a NAT Gateway: `0.0.0.0/0 &rarr; nat-xxxxxxxxx` (or lacks an outbound default route entirely for isolated database tiers).
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Security Groups vs NACLs</span>
    <span>Unit 05 • Page 02</span>
  </div>
</article>

<!-- Page 3: Security Groups vs NACLs -->
<article class="doc-page" id="c4-security">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 03</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">30.</span> Security Groups (Stateful) vs Network Access Control Lists (Stateless NACLs)
  </h2>

  <p class="lead-para">
    AWS implements defense-in-depth security using two complementary firewall layers: instance-level virtual firewalls (Security Groups) and subnet-level boundary packet filters (NACLs).
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Feature Property</th>
          <th>Security Group (SG)</th>
          <th>Network Access Control List (NACL)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Operational Scope</strong></td>
          <td>Operates at the <strong>Instance / ENI Level</strong></td>
          <td>Operates at the <strong>Subnet Boundary Level</strong></td>
        </tr>
        <tr>
          <td><strong>Statefulness</strong></td>
          <td><strong style="color:var(--primary);">STATEFUL:</strong> Return traffic is automatically allowed regardless of outbound rules.</td>
          <td><strong style="color:var(--accent-rose);">STATELESS:</strong> Return traffic must be explicitly allowed by defining ephemeral port rules (ports 1024-65535)!</td>
        </tr>
        <tr>
          <td><strong>Rule Types Supported</strong></td>
          <td><strong>Allow rules ONLY</strong> (Cannot create explicit Deny rules)</td>
          <td>Supports both <strong>ALLOW and DENY rules</strong> (Ideal for blocking specific malicious IP addresses)</td>
        </tr>
        <tr>
          <td><strong>Rule Evaluation Order</strong></td>
          <td>All rules evaluated concurrently as a union before decision</td>
          <td>Rules processed in <strong>strict numerical order</strong> (Lowest rule number evaluated first; stops at first match)</td>
        </tr>
        <tr>
          <td><strong>Default Configuration</strong></td>
          <td>Default SG: Blocks all inbound; allows all outbound. Custom SG: Blocks all inbound and all outbound until rules added.</td>
          <td>Default NACL: Allows all inbound and outbound traffic (* rule). Custom NACL: Blocks all inbound and outbound traffic.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: VPC Peering & Transit Gateway</span>
    <span>Unit 05 • Page 03</span>
  </div>
</article>

<!-- Page 4: Peering, Transit Gateway & PrivateLink -->
<article class="doc-page" id="c4-peering">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 04</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">31.</span> VPC Peering, AWS Transit Gateway &amp; AWS PrivateLink Endpoints
  </h2>

  <p class="lead-para">
    Enterprise cloud footprints span hundreds of decentralized AWS accounts and VPCs requiring secure, low-latency, cross-network data communication without traversing the public Internet.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Interconnect Architecture</th>
          <th>Topology Model</th>
          <th>Transitive Routing Support</th>
          <th>Maximum Scale</th>
          <th>Primary Production Target</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>VPC Peering</strong></td>
          <td>Point-to-point mesh</td>
          <td><strong style="color:var(--accent-rose);">NON-TRANSITIVE:</strong> If VPC A peers with B, and B peers with C, A CANNOT talk to C through B!</td>
          <td>Scales poorly: \(N(N-1)/2\) links (100 VPCs require 4,950 peering links!)</td>
          <td>Simple point-to-point connections between 2 or 3 VPCs requiring maximum line-rate bandwidth</td>
        </tr>
        <tr>
          <td><strong>AWS Transit Gateway (TGW)</strong></td>
          <td>Hub-and-spoke star</td>
          <td><strong style="color:var(--primary);">FULLY TRANSITIVE:</strong> Routes centrally between thousands of VPCs, on-prem VPNs, and Direct Connect links.</td>
          <td>Scales to thousands of VPC attachments (50 Gbps burst per VPC attachment)</td>
          <td>Enterprise multi-account backbones, central egress firewall inspection VPCs</td>
        </tr>
        <tr>
          <td><strong>VPC Gateway Endpoints</strong></td>
          <td>Route Table prefix list target</td>
          <td>Free routing directly to <strong>Amazon S3</strong> and <strong>Amazon DynamoDB</strong></td>
          <td>VPC scope</td>
          <td>Connecting EC2 to S3/DynamoDB privately without NAT Gateway costs</td>
        </tr>
        <tr>
          <td><strong>VPC Interface Endpoints (PrivateLink)</strong></td>
          <td>Elastic Network Interface (ENI) with private IP inside your subnet</td>
          <td>Connects to 150+ AWS services or third-party SaaS providers via AWS PrivateLink</td>
          <td>Subnet scope</td>
          <td>Secure private API consumption keeping traffic entirely off public Internet</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Hybrid Connectivity (VPN vs Direct Connect)</span>
    <span>Unit 05 • Page 04</span>
  </div>
</article>

<!-- Page 5: Hybrid Connectivity -->
<article class="doc-page" id="c4-hybrid">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 05</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">32.</span> Hybrid Cloud Connectivity: AWS Site-to-Site VPN vs AWS Direct Connect (DX)
  </h2>

  <p class="lead-para">
    Bridging corporate on-premises datacenters to AWS infrastructure involves trade-offs between deployment velocity, bandwidth guarantees, encryption protocols, and operational expenditure.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Specification Metric</th>
          <th>AWS Site-to-Site VPN</th>
          <th>AWS Direct Connect (DX)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Underlying Transport Medium</strong></td>
          <td>Public Internet (Encrypted via IPsec tunnels)</td>
          <td>Dedicated private physical fiber optic cross-connect (Ethernet 802.1Q) bypassing the Internet entirely</td>
        </tr>
        <tr>
          <td><strong>Deployment Lead Time</strong></td>
          <td><strong>Minutes</strong> (Software configuration via Virtual Private Gateway or TGW)</td>
          <td><strong>Several weeks to months</strong> (Requires telecom carrier physical circuit installation)</td>
        </tr>
        <tr>
          <td><strong>Bandwidth Capacity</strong></td>
          <td>Up to 1.25 Gbps per IPsec tunnel (can aggregate with ECMP)</td>
          <td>Dedicated 1 Gbps, 10 Gbps, or 100 Gbps physical optical interfaces</td>
        </tr>
        <tr>
          <td><strong>Network Latency &amp; Jitter</strong></td>
          <td>Unpredictable (subject to public internet weather and ISP routing changes)</td>
          <td><strong>Highly deterministic, ultra-low latency</strong></td>
        </tr>
        <tr>
          <td><strong>Data Encryption</strong></td>
          <td>Encrypted natively by default using IPsec AES-256</td>
          <td>Unencrypted at Layer 2/3 natively (Must configure MACsec on 10/100G links or overlay IPsec for encryption)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 05 Practice MCQ Bank</span>
    <span>Unit 05 • Page 05</span>
  </div>
</article>

<!-- Page 6: Unit 5 Practice MCQ Bank (30 Questions) -->
<article class="doc-page" id="practice-mcq-c4">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreC4">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">33.</span> Unit 05 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Test your architectural knowledge of VPC CIDR math, routing configurations, stateful vs stateless firewalls, and hybrid enterprise transit hubs.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 01 • VPC Subnet IP Reservation</div>
      <div class="mcq-q">How many usable IP addresses are available for EC2 instances in an AWS VPC subnet created with a /28 prefix?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 16 addresses</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 11 addresses (16 total &minus; 5 AWS reserved)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 14 addresses (16 total &minus; 2 standard)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 8 addresses</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> A /28 subnet has 2^(32-28) = 16 total IPs. AWS reserves exactly 5 addresses (.0, .1, .2, .3, .255), leaving 16 - 5 = 11 usable IPs.
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="C4" data-correct="C">
      <div class="mcq-num">Question 02 • Security Group Statefulness</div>
      <div class="mcq-q">If an administrator adds an inbound rule allowing TCP port 443 into an EC2 Security Group, what outbound rule is required to allow the web server's responses back to the client?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> An outbound rule allowing TCP port 443</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> An outbound rule allowing ephemeral ports 1024-65535</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> No outbound rule is required because Security Groups are stateful; return traffic is automatically permitted</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> All outbound traffic must be denied first</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Security Groups are stateful. Any incoming connection permitted by an inbound rule automatically permits the return response regardless of outbound rules.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 03 • Blocking Specific IP Addresses</div>
      <div class="mcq-q">An enterprise detects a DDoS attack originating from a specific malicious IP address (`198.51.100.45`). Which VPC mechanism can be configured to explicitly DENY traffic from this IP address?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Network Access Control List (NACL) Inbound Deny Rule</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> EC2 Security Group Inbound Rule</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Route 53 Health Check</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Internet Gateway Deny Policy</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Security Groups support ALLOW rules only. To explicitly DENY an IP address, you must create a numbered DENY rule in the subnet's Network ACL.
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="C4" data-correct="D">
      <div class="mcq-num">Question 04 • VPC Peering Transitivity</div>
      <div class="mcq-q">VPC A has an active peering connection with VPC B. VPC B has an active peering connection with VPC C. Can instances in VPC A directly communicate with VPC C through VPC B?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Yes, if BGP is enabled</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Yes, all VPC peering connections are fully transitive by default</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Yes, but only for IPv6 traffic</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> No, VPC Peering does NOT support transitive routing; a direct peering link between A and C (or a Transit Gateway) is required</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> VPC peering is strictly non-transitive. Traffic cannot hop through an intermediate VPC. Direct peering or an AWS Transit Gateway is mandatory.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 05 • Gateway VPC Endpoints</div>
      <div class="mcq-q">Which two AWS services support free Gateway VPC Endpoints configured via Route Table prefix lists?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Amazon EC2 and Amazon RDS</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Amazon S3 and Amazon DynamoDB</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Lambda and Amazon SNS</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Amazon CloudFront and AWS Shield</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Gateway Endpoints exist exclusively for Amazon S3 and Amazon DynamoDB, routing traffic directly without incurring NAT Gateway hourly or data charges.
      </div>
    </div>

    <!-- Q6 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="C4" data-correct="C">
      <div class="mcq-num">Question 06 • NAT Gateway Placement</div>
      <div class="mcq-q">In which type of subnet must a managed AWS NAT Gateway be physically deployed to grant private instances access to the public Internet?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Inside a Private Subnet</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> In an Isolated Database Subnet</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Inside a Public Subnet with a route to an Internet Gateway and an associated Elastic IP</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Outside the VPC</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> NAT Gateways must reside in a public subnet (with a route to an IGW) and require an attached Elastic IP to perform outbound source translation.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 07 • DNS Hostname Resolution</div>
      <div class="mcq-q">Which reserved IP address inside the CIDR block `10.50.0.0/16` serves as the AmazonProvidedDNS resolver for instances inside the VPC?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 10.50.0.2</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 10.50.0.1</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 10.50.0.3</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 10.50.255.255</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> The Route 53 DNS resolver is always located at the base network address plus 2 (`10.50.0.2`), or at the link-local address `169.254.169.253`.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="D">
      <div class="mcq-num">Question 08 • Transit Gateway Scalability</div>
      <div class="mcq-q">What network topology does the AWS Transit Gateway implement to replace complex full-mesh VPC peering?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Token Ring</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Daisy Chain</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Dual counter-rotating fiber ring</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Centralized Hub-and-Spoke star topology</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Transit Gateway acts as a regional virtual cloud router in a hub-and-spoke star configuration, interconnecting thousands of VPCs and on-premises networks.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 09 • Stateless NACL Ephemeral Ports</div>
      <div class="mcq-q">Why must an administrator configure an outbound rule allowing ephemeral ports 1024-65535 in a Network ACL when web servers only listen on inbound port 80?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Because NACLs are stateful</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Because NACLs are stateless; when a client connects from a random high-numbered source port (e.g. 52140), the server's return response must be explicitly permitted outbound</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Ephemeral ports are required for power supply monitoring</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It is required by Windows Update</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> NACLs do not remember session state. Return traffic from web servers on port 80/443 is directed back to the client's ephemeral port, which must be allowed outbound.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="C">
      <div class="mcq-num">Question 10 • Direct Connect Encryption</div>
      <div class="mcq-q">Does an AWS Direct Connect (DX) physical fiber connection provide native data encryption by default?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Yes, all Direct Connect circuits are encrypted with AES-256 automatically</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Yes, using SSL certificates</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> No, Direct Connect is an unencrypted Layer 2/3 private link; organizations requiring in-flight encryption must enable MACsec or overlay an IPsec VPN tunnel</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Direct Connect cannot carry encrypted data</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Direct Connect provides dedicated private physical lines, but traffic is unencrypted plaintext unless combined with IEEE 802.1AE MACsec or an IPsec VPN overlay.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 11 • VPC Maximum CIDR Block Size</div>
      <div class="mcq-q">What is the largest (most IP addresses) and smallest permitted IPv4 CIDR block allocation for an Amazon VPC?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Largest: /16 (65,536 IPs) &bull; Smallest: /28 (16 IPs)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Largest: /8 &bull; Smallest: /32</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Largest: /24 &bull; Smallest: /30</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Any arbitrary prefix size is allowed</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> AWS VPC supports IPv4 CIDR blocks between /16 (65,536 addresses) and /28 (16 addresses). Larger /8 allocations are not permitted.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 12 • Egress-Only Internet Gateway</div>
      <div class="mcq-q">What is the primary operational role of an Egress-Only Internet Gateway (EIGW)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Translates private IPv4 to public IPv4</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Allows outbound IPv6 communication from VPC instances to the internet while preventing outside entities from initiating inbound connections to the instances</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Accelerates video uploads</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Encrypts S3 buckets</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Because every IPv6 address is globally routable (no NAT), an EIGW acts as a stateful egress filter allowing outbound traffic while blocking inbound connections.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="D">
      <div class="mcq-num">Question 13 • Interface VPC Endpoints (PrivateLink)</div>
      <div class="mcq-q">How does an Interface VPC Endpoint (powered by AWS PrivateLink) attach to your virtual private cloud?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By modifying the Internet Gateway routing table</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By installing software on each EC2 instance</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Via a public IP address allocated from the ISP</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It provisions an Elastic Network Interface (ENI) with a private IP address directly inside your designated subnet</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> PrivateLink provisions an ENI with a private IP in your subnet, allowing instances to connect privately to AWS services using private DNS.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="C">
      <div class="mcq-num">Question 14 • NAT Gateway High Availability</div>
      <div class="mcq-q">How should an enterprise architect NAT Gateways to ensure multi-AZ fault tolerance for private instances in 3 Availability Zones?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Deploy a single NAT Gateway in AZ-a; all 3 AZs route through it</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> NAT Gateways are automatically multi-AZ resilient across all zones</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Deploy 1 distinct NAT Gateway in each of the 3 Availability Zones, with each private subnet routing to its local AZ's NAT Gateway</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> NAT Gateways cannot be used in multi-AZ architectures</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> A NAT Gateway is AZ-bound. If the AZ hosting a single NAT Gateway fails, private subnets in all zones lose internet access. Multi-AZ resilience requires 1 NAT Gateway per AZ.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 15 • Route Table Longest Prefix Match</div>
      <div class="mcq-q">If a VPC Route Table has two overlapping routes: `10.0.0.0/16 &rarr; local` and `10.0.1.0/24 &rarr; tgw-12345`, how does the router forward a packet destined for `10.0.1.50`?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Forwards to `tgw-12345` because `/24` is a more specific route (Longest Prefix Match)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Forwards to `local` because `/16` is larger</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Drops the packet due to routing conflict</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Forwards 50% of packets to each route</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Standard IP routing uses Longest Prefix Match. The /24 route is more specific than /16, so packets destined for `10.0.1.50` follow the /24 route to `tgw-12345`.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 16 • VPC Flow Logs Target</div>
      <div class="mcq-q">Where can VPC Flow Logs be published for security network analysis and threat detection?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> AWS Artifact</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Directly to the administrator's email</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Local Windows Event Viewer only</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> VPC Flow Logs capture IP traffic metadata and publish directly to S3 buckets, CloudWatch Log Groups, or Kinesis Firehose for real-time SIEM ingestion.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="D">
      <div class="mcq-num">Question 17 • Flow Log Captured Fields</div>
      <div class="mcq-q">Which information is NOT captured by standard VPC Flow Logs?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Source and Destination IP addresses</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Source and Destination port numbers</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> ACCEPT or REJECT action status</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The actual deep packet payload (HTTP headers, user data, application payload content)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Flow logs capture metadata (IPs, ports, protocol, bytes, packets, accept/reject), but do NOT capture packet payload contents (Traffic Mirroring is required for deep inspection).
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="C">
      <div class="mcq-num">Question 18 • Site-to-Site VPN Redundancy</div>
      <div class="mcq-q">How many active IPsec tunnels are provisioned by default with every AWS Site-to-Site VPN connection?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Exactly 1 tunnel</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 4 tunnels</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Exactly 2 redundant tunnels terminating on distinct AWS endpoint endpoints</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 10 tunnels</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Every AWS Site-to-Site VPN connection automatically provisions two redundant tunnels for high availability, terminating on separate AWS data centers.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 19 • Direct Connect Gateway Purpose</div>
      <div class="mcq-q">What capability is unlocked by deploying an AWS Direct Connect Gateway?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Connects a single physical Direct Connect link to multiple VPCs across different AWS Regions globally</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Translates IPv4 into IPv6</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Provides free internet bandwidth to homes</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Replaces the need for routers</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> A Direct Connect Gateway enables a dedicated physical circuit to connect to VPCs in any commercial AWS Region worldwide (except China).
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 20 • Traffic Mirroring Use Case</div>
      <div class="mcq-q">What capability allows an enterprise security team to stream exact raw copies of all network packets entering and exiting an EC2 instance to a Zeek or Suricata IDS appliance?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> VPC Flow Logs</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> VPC Traffic Mirroring (encapsulated via VXLAN on UDP port 4789)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Shield Advanced</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Route 53 Traffic Flow</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> VPC Traffic Mirroring copies raw byte-level packet payloads directly from the Elastic Network Adapter (ENA) and tunnels them via VXLAN to security appliances for deep packet inspection.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="D">
      <div class="mcq-num">Question 21 • Security Group Referencing</div>
      <div class="mcq-q">Instead of specifying an IP CIDR block, what security best practice allows an EC2 Security Group on a backend database tier to allow traffic ONLY from instances belonging to the web application tier?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Allowing `0.0.0.0/0` with a password</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Hardcoding every web server's private IP</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Disabling the database firewall</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Referencing the Web Tier's Security Group ID (e.g. `sg-web12345`) directly in the database Security Group's inbound rule source</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Referencing a source Security Group ID dynamically authorizes any instance with that SG attached, eliminating fragile hardcoded IP address maintenance.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 22 • Bastion Host / Jump Box Role</div>
      <div class="mcq-q">What is the traditional architectural purpose of an EC2 Bastion Host (Jump Box)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Provides a single hardened, monitored public entry point to securely SSH/RDP into private subnet instances</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Speeds up database SQL queries</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Caches static media files</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Manages auto-scaling groups</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Bastion hosts sit in a public subnet, acting as a secure gateway for administrators to bridge into private subnets without exposing database ports to the Internet.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="C">
      <div class="mcq-num">Question 23 • Systems Manager Session Manager Advantage</div>
      <div class="mcq-q">Why is AWS Systems Manager Session Manager preferred over traditional SSH Bastion hosts?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Session Manager makes EC2 instances free</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Session Manager only works on Windows</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Allows secure command-line shell access via IAM without opening ANY inbound ports (port 22/3389) or managing SSH keys</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It requires a physical modem</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Session Manager tunnels shell traffic through an outbound agent connection over HTTPS (port 443), eliminating open inbound firewall ports and SSH key management.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 24 • Secondary VPC CIDR Blocks</div>
      <div class="mcq-q">What capability allows an organization that has exhausted the IP space of its primary `10.0.0.0/16` VPC to expand addressing without rebuilding the VPC?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> You must delete the VPC and recreate it</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Associating a Secondary IPv4 CIDR Block (e.g. `10.1.0.0/16` or `100.64.0.0/16`) to the existing VPC</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Turning on NAT Overload</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Subnetting the router IP</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> AWS allows adding up to 4 secondary IPv4 CIDR blocks to an existing VPC, allowing seamless subnet additions without disruption.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="D">
      <div class="mcq-num">Question 25 • NACL Numerical Processing Rule</div>
      <div class="mcq-q">A Network ACL has Rule 100: ALLOW TCP Port 80 from `0.0.0.0/0`, and Rule 50: DENY TCP Port 80 from `203.0.113.15`. If client `203.0.113.15` connects to Port 80, what happens?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Traffic is allowed because Rule 100 has a higher number</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Traffic is allowed because Allow overrides Deny</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Traffic is randomly dropped 50% of the time</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Traffic is DENIED because NACL rules are evaluated in strict numerical order; Rule 50 matches first and blocks the packet immediately</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> NACLs evaluate rules in numerical order (lowest to highest) and stop processing on the first match. Rule 50 executes before Rule 100, denying the connection.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 26 • AWS Global Accelerator</div>
      <div class="mcq-q">What is the functional difference between AWS Global Accelerator and Amazon CloudFront?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> CloudFront caches static HTTP content at edge locations; Global Accelerator provides static Anycast IPs to route non-HTTP (TCP/UDP) or uncached traffic directly into the AWS global backbone</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Both services are identical</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Global Accelerator only works in Japan</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> CloudFront does not use edge locations</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> CloudFront is a caching CDN for HTTP content. Global Accelerator proxies raw TCP/UDP traffic over static Anycast IP addresses directly into the AWS private backbone.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="C">
      <div class="mcq-num">Question 27 • Route 53 Private Hosted Zones</div>
      <div class="mcq-q">How does an Amazon Route 53 Private Hosted Zone resolve domain queries (e.g. `db.internal.corp`)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Exposes records to public internet DNS servers</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Sends email notifications to users</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Resolves DNS queries exclusively from within authorized VPCs associated with the private zone, completely hidden from the public Internet</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Requires a credit card per query</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Private Hosted Zones manage internal domain names accessible only from designated VPCs, keeping internal infrastructure hostnames confidential.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="B">
      <div class="mcq-num">Question 28 • Equal-Cost Multi-Path (ECMP)</div>
      <div class="mcq-q">How can an enterprise scale AWS Site-to-Site VPN bandwidth beyond the 1.25 Gbps limit of a single IPsec tunnel?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Compressing all data with WinRAR</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Terminating multiple VPN tunnels on an AWS Transit Gateway and enabling BGP Equal-Cost Multi-Path (ECMP) routing</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Upgrading the router power cable</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Switching to unencrypted Wi-Fi</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Transit Gateway supports BGP ECMP across multiple VPN tunnels, load-balancing traffic across tunnels to scale throughput into multiple gigabits.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="D">
      <div class="mcq-num">Question 29 • Default VPC Characteristics</div>
      <div class="mcq-q">What default configuration is automatically provisioned in a default AWS VPC in each Region?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> All subnets are private with no internet access</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Requires a Direct Connect connection</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Contains zero subnets</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> A /16 CIDR block (`172.31.0.0/16`), an attached Internet Gateway, and one public /20 subnet in every Availability Zone with auto-assign public IP enabled</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Default VPCs are designed for immediate onboarding: `172.31.0.0/16`, attached IGW, and pre-created public subnets in each AZ that assign public IPs automatically.
      </div>
    </div>

    <div class="mcq-card" data-unit="C4" data-correct="A">
      <div class="mcq-num">Question 30 • VPC Peering MTU Support</div>
      <div class="mcq-q">What is the maximum Transmission Unit (MTU) supported for traffic traversing a VPC Peering connection within the same AWS Region?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 9,001 bytes (Jumbo Frames)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 1,500 bytes standard MTU only</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 576 bytes</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 65,535 bytes</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Intra-region VPC peering supports 9,001-byte Jumbo Frames, drastically reducing packet processing overhead for large data transfers between EC2 instances.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 05 Conceptual Questions</span>
    <span>Unit 05 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 5 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-c4">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">34.</span> Unit 5 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted explanations of software-defined cloud networking, firewall statefulness, and hybrid transit routing.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Explain the architectural and mathematical reason why exactly 5 IP addresses are reserved in every AWS VPC subnet.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>In standard networking, only 2 addresses are reserved (Network ID and Broadcast). AWS VPC reserves exactly 5 addresses in every subnet:</p>
        <ul>
          <li><strong>`.0` (Network ID):</strong> Base CIDR network identifier.</li>
          <li><strong>`.1` (VPC Local Router):</strong> Default gateway IP virtual interface for routing off-subnet traffic.</li>
          <li><strong>`.2` (AmazonProvidedDNS):</strong> Internal recursive Route 53 DNS resolver endpoint (base + 2).</li>
          <li><strong>`.3` (Future AWS Reservation):</strong> Reserved by AWS for protocol enhancements.</li>
          <li><strong>`.255` (Broadcast Address):</strong> Reserved to preserve standard TCP/IP stack compatibility, even though AWS does not route layer 2 broadcasts.</li>
        </ul>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Contrast the stateful operational behavior of Security Groups with the stateless behavior of Network ACLs.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Security Groups (Stateful):</strong> Operate at the instance ENI level. Security Groups maintain a dynamic connection state table. When an inbound rule permits a packet, return traffic is automatically tracked and allowed outbound, regardless of outbound rules. They support ALLOW rules only.</p>
        <p><strong>Network ACLs (Stateless):</strong> Operate at the subnet boundary. NACLs do not track connection states. Inbound and outbound traffic are evaluated as completely independent, unrelated packets. If an inbound web request is allowed on port 80/443, the administrator <em>must explicitly configure an outbound rule allowing ephemeral ports (1024-65535)</em> for the response to leave the subnet! They evaluate rules in numerical order and support both ALLOW and DENY rules.</p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> What is non-transitive routing in VPC Peering, and how does AWS Transit Gateway eliminate this operational constraint?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Non-Transitive VPC Peering:</strong> If VPC A is peered with VPC B, and VPC B is peered with VPC C, traffic from VPC A cannot transit through VPC B to reach VPC C. Direct point-to-point peering requires a full mesh: \(N(N-1)/2\) peering links, which becomes unmanageable across hundreds of corporate VPCs.</p>
        <p><strong>AWS Transit Gateway (TGW):</strong> Functions as a centralized cloud router in a hub-and-spoke star topology. TGW supports fully transitive routing: VPCs attach to the TGW via Elastic Network Interfaces, and traffic routes seamlessly across any attached VPC, on-prem VPN, or Direct Connect connection through customizable route tables.</p>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> Contrast Gateway VPC Endpoints and Interface VPC Endpoints (AWS PrivateLink).</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Gateway Endpoints:</strong> Target entries configured directly in VPC Route Tables for Amazon S3 and Amazon DynamoDB. They are completely free of charge and do not consume IP addresses in your subnets.</p>
        <p><strong>Interface Endpoints (PrivateLink):</strong> Provision an Elastic Network Interface (ENI) with a private IP address directly inside your subnet. They support 150+ AWS services, third-party partner SaaS endpoints, and custom microservices. Billed on an hourly endpoint fee plus per-GB data processing fees.</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> When is AWS Direct Connect preferred over an AWS Site-to-Site VPN, and how can they be combined for maximum availability?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>When Direct Connect is Preferred:</strong> Direct Connect provides dedicated private physical optical fiber (1/10/100 Gbps) bypassing the public Internet. It is selected when workloads require deterministic, jitter-free low latency, heavy continuous multi-terabyte data transfers, or lower data egress fees.</p>
        <p><strong>High-Availability Architecture:</strong> The primary path routes over AWS Direct Connect. An AWS Site-to-Site VPN is configured as an <strong>automated failover backup link</strong> using BGP dynamic routing with AS-Path prepending. If a backhoe cuts the physical Direct Connect fiber, traffic automatically fails over to the IPsec VPN tunnel within seconds.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 05 Analytical Problems</span>
    <span>Unit 05 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 5 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-c4">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">35.</span> Unit 5 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Real-world architectural troubleshooting scenarios covering routing loops, asymmetrical firewall drops, and cross-account CIDR overlaps.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Network Outage Triage: Asymmetrical Packet Drop Triggered by Missing Ephemeral Port in Custom NACL</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A network security administrator creates a new custom Network ACL for a public web subnet. Inbound Rule 100 allows TCP Port 80, and Inbound Rule 110 allows TCP Port 443 from `0.0.0.0/0`. Outbound Rule 100 allows TCP Port 80 and 443 to `0.0.0.0/0`. Immediately after association, external web browsers report `ERR_CONNECTION_TIMED_OUT`. Pinging the web server succeeds.</p>
        <p><strong>Diagnostic &amp; Engineering Analysis:</strong></p>
        <ol>
          <li><strong>The Stateless Trap:</strong> Network ACLs are completely stateless. When a client browser connects to a web server on port 443, the client's operating system allocates a temporary random source port known as an <strong>ephemeral port</strong> (typically in the range of <strong>1024 to 65535</strong>).</li>
          <li><strong>The Failure Point:</strong> The server receives the SYN packet (Inbound port 443 is allowed). The server generates the SYN-ACK response packet: Source Port = 443, Destination Port = 52140. When the response hits the NACL, the NACL evaluates Outbound rules. The outbound rule <em>only allows ports 80 and 443</em>! Because port 52140 is not allowed, the response packet is silently dropped by the default `* DENY` rule!</li>
          <li><strong>Remediation:</strong> Add an Outbound NACL Rule: <strong>Rule 120 &ndash; ALLOW &ndash; TCP &ndash; Ports 1024-65535 &ndash; Destination: 0.0.0.0/0</strong>. Traffic immediately flows and websites load in milliseconds.</li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> M&A Cloud Integration: Resolving Overlapping CIDR Blocks (`10.0.0.0/16`) in Corporate Acquisition</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Engineering Challenge:</strong> Enterprise A (`10.0.0.0/16`) acquires Company B, whose entire AWS production environment is also configured as `10.0.0.0/16`. Both companies require secure, direct database communication between internal microservices. Standard VPC Peering fails with: `Overlapping CIDR block error`.</p>
        <p><strong>Architectural Solutions:</strong></p>
        <ul>
          <li><strong>Solution 1: AWS PrivateLink (Recommended):</strong> Company B creates a Network Load Balancer (NLB) in front of its database service and registers it as a <strong>VPC Endpoint Service</strong>. Enterprise A creates an Interface VPC Endpoint in its own VPC. Traffic routes over AWS PrivateLink using private IP addresses inside Enterprise A's subnet, completely bypassing the overlapping CIDR conflict with zero IP renumbering!</li>
          <li><strong>Solution 2: Secondary Non-Overlapping CIDR + Transit Gateway NAT:</strong> Enterprise A associates a secondary RFC 6598 carrier-grade NAT block (`100.64.0.0/16`) to its VPC. Subnets created in this secondary block connect through an AWS Transit Gateway configured with bidirectional 1:1 NAT, translating IP packets between the overlapping domains.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> High-Availability NAT Failure: Single-AZ NAT Gateway Outage Collapsing Multi-AZ Private Fleets</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A fin-tech company hosts its payment API across three Availability Zones (`us-east-1a`, `us-east-1b`, `us-east-1c`) in private subnets. To save $65/month, the team provisioned a single NAT Gateway in `us-east-1a`, routing outbound traffic from all three AZs through it. A localized utility transformer fire causes an outage in `us-east-1a`. Immediately, payment processing fails across 100% of servers in AZs `b` and `c`, even though instances in `b` and `c` are completely healthy!</p>
        <p><strong>Root Cause &amp; Architecture Hardening:</strong></p>
        <ul>
          <li><strong>The Architectural Flaw:</strong> While instances were distributed across 3 AZs, the outbound internet routing had a <strong>Single Point of Failure (SPOF)</strong> in `us-east-1a`. When the NAT Gateway died, private instances in `b` and `c` could not reach external payment gateways (Stripe, Visa), causing transactions to time out.</li>
          <li><strong>Multi-AZ NAT Architecture Mandate:</strong> Deploy <strong>one dedicated NAT Gateway per Availability Zone</strong> inside each public subnet. Configure the Route Table for Private Subnet A to route default traffic to NAT Gateway A; Private Subnet B routes to NAT Gateway B; Private Subnet C routes to NAT Gateway C. If an entire AZ facility collapses, remaining AZs retain unbroken local egress paths.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> Centralized Traffic Inspection: Designing an Egress Firewall Hub with AWS Transit Gateway</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>System Engineering Request:</strong> A multinational financial institution mandates that all outbound Internet traffic across 250 spoke VPCs must traverse a centralized inspection cluster of Palo Alto virtual firewalls for Deep Packet Inspection (DPI) and URL filtering before exiting to the web.</p>
        <p><strong>Transit Gateway Inspection Blueprint:</strong></p>
        <ul>
          <li>Deploy an <strong>AWS Transit Gateway (TGW)</strong> with Appliance Mode enabled on the security attachment.</li>
          <li>Create a centralized <strong>Inspection VPC</strong> hosting a Gateway Load Balancer (GLB) and an Auto Scaling fleet of virtual firewall appliances.</li>
          <li>Configure Route Tables in the 250 spoke VPCs: default route `0.0.0.0/0 &rarr; TGW`.</li>
          <li>The TGW routes all outbound traffic to the Inspection VPC. The Gateway Load Balancer encapsulates packets via Geneve (UDP 6081) and distributes them to healthy firewalls.</li>
          <li>After inspection, traffic exits through a centralized pool of NAT Gateways and Internet Gateways. Enabling <strong>TGW Appliance Mode</strong> ensures that symmetric bidirectional flows return to the exact same firewall node, preventing dropped TCP sessions.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 05 Master MCQ Answer Key</span>
    <span>Unit 05 • Page 08</span>
  </div>
</article>

<!-- Page 9: Master Answer Key Table -->
<article class="doc-page" id="mcq-answer-key-c4">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Master Answer Key • 30 Questions</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">36.</span> Unit 5 Master Answer Key Table & Verification Matrix
  </h2>

  <p class="lead-para">
    Complete verified answer keys and core learning objectives for all 30 multiple choice questions in Unit 5.
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
        <tr><td>01</td><td><strong style="color:var(--primary);">B</strong></td><td>/28 subnet usable IP capacity (16 total &minus; 5 AWS reserved = 11)</td><td>16</td><td><strong style="color:var(--primary);">B</strong></td><td>VPC Flow Logs destination targets (CloudWatch, S3, Kinesis)</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">C</strong></td><td>Security Group stateful connection tracking return traffic</td><td>17</td><td><strong style="color:var(--primary);">D</strong></td><td>Flow logs metadata capturing excluding packet payloads</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">A</strong></td><td>Network ACL inbound DENY rule for specific malicious IPs</td><td>18</td><td><strong style="color:var(--primary);">C</strong></td><td>AWS Site-to-Site VPN 2 redundant tunnels per connection</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">D</strong></td><td>VPC Peering strictly non-transitive routing constraint</td><td>19</td><td><strong style="color:var(--primary);">A</strong></td><td>Direct Connect Gateway multi-region global VPC routing</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">B</strong></td><td>Gateway VPC Endpoints exclusive to S3 and DynamoDB</td><td>20</td><td><strong style="color:var(--primary);">B</strong></td><td>VPC Traffic Mirroring raw packet capture via VXLAN UDP 4789</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">C</strong></td><td>NAT Gateway physical deployment in public subnet with EIP</td><td>21</td><td><strong style="color:var(--primary);">D</strong></td><td>Security Group referencing SG IDs dynamically</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">A</strong></td><td>Route 53 resolver IP allocation at base CIDR + 2 (10.50.0.2)</td><td>22</td><td><strong style="color:var(--primary);">A</strong></td><td>Bastion host single hardened entry point for private instances</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">D</strong></td><td>Transit Gateway centralized Hub-and-Spoke star topology</td><td>23</td><td><strong style="color:var(--primary);">C</strong></td><td>SSM Session Manager eliminating open inbound ports and SSH</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">B</strong></td><td>NACL stateless ephemeral port response rule requirement</td><td>24</td><td><strong style="color:var(--primary);">B</strong></td><td>Secondary IPv4 CIDR blocks expanding exhausted VPC space</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">C</strong></td><td>Direct Connect unencrypted layer 2/3 link requiring MACsec/IPsec</td><td>25</td><td><strong style="color:var(--primary);">D</strong></td><td>NACL numerical evaluation order (lowest rule executes first)</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">A</strong></td><td>VPC CIDR allocation limits (/16 maximum to /28 minimum)</td><td>26</td><td><strong style="color:var(--primary);">A</strong></td><td>AWS Global Accelerator Anycast IP routing non-HTTP traffic</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">B</strong></td><td>Egress-Only Internet Gateway outbound IPv6 filtering</td><td>27</td><td><strong style="color:var(--primary);">C</strong></td><td>Route 53 Private Hosted Zones resolving within VPC only</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">D</strong></td><td>Interface Endpoints provisioning ENIs with private IP addresses</td><td>28</td><td><strong style="color:var(--primary);">B</strong></td><td>BGP Equal-Cost Multi-Path scaling VPN beyond 1.25 Gbps</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">C</strong></td><td>Deploying 1 NAT Gateway per AZ for Multi-AZ fault tolerance</td><td>29</td><td><strong style="color:var(--primary);">D</strong></td><td>Default VPC configuration (172.31.0.0/16, IGW, public subnets)</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">A</strong></td><td>Route table Longest Prefix Match priority (/24 over /16)</td><td>30</td><td><strong style="color:var(--primary);">A</strong></td><td>Intra-region VPC Peering 9,001-byte Jumbo Frame support</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 05 Complete • Next: Unit 05 Cloud Databases & Big Data</span>
    <span>Unit 05 • Page 09</span>
  </div>
</article>
"""
