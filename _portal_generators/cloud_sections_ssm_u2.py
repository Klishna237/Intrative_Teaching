# -*- coding: utf-8 -*-
"""
Cloud Administration (AWS) - Unit 2: Cloud Compute & Virtualization
Master Gold Standard Layout:
- c2-ec2: EC2 Instance Families, Naming Conventions, vCPUs & NUMA
- c2-pricing: EC2 Purchasing Options: On-Demand, Spot, Reserved & Savings Plans
- c2-nitro: The AWS Nitro System Architecture (Nitro Cards, Hypervisor & Security Chip)
- c2-scaling: Elastic Load Balancing (ALB vs NLB vs GLB) & Auto Scaling Groups (ASG)
- c2-serverless: AWS Lambda, Firecracker MicroVMs & Serverless Event-Driven Runtimes
- practice-mcq-c2: 30 MCQs with dynamic scoring
- practice-subj-short-c2: 5 Short Conceptual Sets
- practice-subj-long-c2: 4 Deep Analytical Scenarios
- mcq-answer-key-c2: Master Answer Key Table
"""

CLOUD_UNIT2_HTML = """
<!-- ==========================================================================
     UNIT 02: CLOUD COMPUTE & VIRTUALIZATION
     ========================================================================== -->

<!-- Page 1: EC2 Instance Families -->
<article class="doc-page" id="c2-ec2">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 02 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">10.</span> Amazon EC2 Instance Families, vCPU Threading &amp; Silicon Architecture
  </h2>

  <p class="lead-para">
    Amazon Elastic Compute Cloud (Amazon EC2) provides secure, resizable compute capacity in the cloud. Physical host hardware is partitioned into virtual machine instances categorized by optimized silicon ratios balancing compute cores, physical memory, network bandwidth, and local NVMe storage.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Instance Family</th>
          <th>Representative Types</th>
          <th>vCPU-to-RAM Ratio</th>
          <th>Underlying Hardware Silicon</th>
          <th>Optimized Production Workloads</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>General Purpose (M/T)</strong></td>
          <td>`m7i`, `m7g`, `t4g`</td>
          <td>1 vCPU : 4 GiB RAM</td>
          <td>Intel Xeon Platinum 8488C / AWS Graviton3</td>
          <td>Corporate web servers, microservice backends, small-to-medium databases</td>
        </tr>
        <tr>
          <td><strong>Compute Optimized (C)</strong></td>
          <td>`c7i`, `c7g`</td>
          <td>1 vCPU : 2 GiB RAM</td>
          <td>High-frequency 3.8 GHz all-core turbo silicon</td>
          <td>Batch processing, scientific modeling, video encoding, gaming server hosting</td>
        </tr>
        <tr>
          <td><strong>Memory Optimized (R/X)</strong></td>
          <td>`r7i`, `r7g`, `x2gd`</td>
          <td>1 vCPU : 8 GiB RAM (up to 32 GiB in X2)</td>
          <td>Multi-terabyte DDR5 RAM topologies</td>
          <td>In-memory caches (Redis/Memcached), SAP HANA, large relational databases</td>
        </tr>
        <tr>
          <td><strong>Storage Optimized (I/D)</strong></td>
          <td>`i4i`, `d3`</td>
          <td>Dense local NVMe SSDs (up to 30 TB raw)</td>
          <td>Direct-attached PCIe 4.0 AWS Nitro SSDs</td>
          <td>NoSQL databases (Cassandra, MongoDB, Elasticsearch/OpenSearch), Kafka brokers</td>
        </tr>
        <tr>
          <td><strong>Accelerated Compute (G/P)</strong></td>
          <td>`p5`, `g5`</td>
          <td>Up to 8 NVIDIA H100 GPUs (640GB VRAM)</td>
          <td>PCIe Gen 5 with 3.2 Tbps GPUDirect RDMA</td>
          <td>Large Language Model (LLM) training, generative AI, 3D graphics rendering</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="cpu"></i> Silicon Architecture: What Exactly is a vCPU?</div>
    <p>
      On x86 Intel and AMD platforms, <strong>1 vCPU equals 1 hardware execution thread (Hyper-Thread)</strong> on a physical multi-core CPU. A physical core with Simultaneous Multithreading (SMT) provides 2 vCPUs. For example, a `c7i.2xlarge` instance provides 8 vCPUs, which maps to 4 physical hyper-threaded CPU cores. On ARM-based AWS Graviton3/4 processors, SMT is disabled; therefore, <strong>1 vCPU represents an entire dedicated physical CPU core</strong>, delivering deterministic performance with zero inter-thread L1 cache eviction contention!
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: EC2 Purchasing Options & Economics</span>
    <span>Unit 02 • Page 01</span>
  </div>
</article>

<!-- Page 2: Purchasing Options -->
<article class="doc-page" id="c2-pricing">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 02 • Page 02</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">11.</span> Amazon EC2 Purchasing Models: On-Demand, Spot, Reserved &amp; Savings Plans
  </h2>

  <p class="lead-para">
    AWS provides flexible purchasing models allowing systems architects to optimize compute expenditure based on workload predictability, interruption tolerance, and multi-year financial commitments.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Purchasing Option</th>
          <th>Discount vs On-Demand</th>
          <th>Commitment Term</th>
          <th>Interruption Risk</th>
          <th>Ideal Workload Profile</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>On-Demand</strong></td>
          <td>0% (Baseline list price)</td>
          <td>None (Per-second billing, 1-minute minimum)</td>
          <td>Zero interruption risk (Dedicated until stopped)</td>
          <td>Short-term, unpredictable workloads, software development, proof-of-concept testing</td>
        </tr>
        <tr>
          <td><strong>Spot Instances</strong></td>
          <td><strong>Up to 90% discount</strong></td>
          <td>None (Purchases spare AWS compute capacity)</td>
          <td>High (AWS issues a <strong>2-minute termination notice</strong> via EC2 metadata if capacity needed)</td>
          <td>Fault-tolerant batch jobs, stateless container tasks, big data Hadoop/Spark processing, rendering</td>
        </tr>
        <tr>
          <td><strong>Compute Savings Plans</strong></td>
          <td>Up to 66% discount</td>
          <td>1-year or 3-year commitment ($/hour spend)</td>
          <td>Zero interruption risk</td>
          <td>Steady-state production baseline workloads; automatically applies across EC2, Fargate, and Lambda</td>
        </tr>
        <tr>
          <td><strong>EC2 Instance Savings Plans</strong></td>
          <td>Up to 72% discount</td>
          <td>1-year or 3-year commitment (Specific family &amp; region)</td>
          <td>Zero interruption risk</td>
          <td>Stable production database nodes with fixed instance family requirements (e.g. `m7i` in `us-east-1`)</td>
        </tr>
        <tr>
          <td><strong>Dedicated Hosts</strong></td>
          <td>Premium over On-Demand</td>
          <td>On-Demand or 1/3-year Reservation</td>
          <td>Zero interruption risk</td>
          <td>Strict regulatory hardware compliance and bringing socket-bound proprietary software licenses (BYOL)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: The AWS Nitro System Architecture</span>
    <span>Unit 02 • Page 02</span>
  </div>
</article>

<!-- Page 3: AWS Nitro System -->
<article class="doc-page" id="c2-nitro">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 02 • Page 03</span>
    <span class="meta-tag">Bloom's: Understand / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">12.</span> The AWS Nitro System: PCIe Hardware Offload, Hypervisor &amp; Security Chip
  </h2>

  <p class="lead-para">
    The AWS Nitro System represents a complete re-architecture of traditional datacenter server hardware virtualization, offloading networking, local storage, remote storage, and security monitoring onto dedicated custom hardware accelerator cards.
  </p>

  <div class="diagram-container">
    <div class="diagram-title">The Modular AWS Nitro Architecture</div>
    <div class="arch-stack-visual">
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">HOST PHYSICAL SILICON (Intel Xeon / AMD EPYC / AWS Graviton)</span>
        <div class="tier-desc">Nearly 100% of CPU cores &amp; DRAM allocated to customer VMs • Stripped Nitro Microvisor manages core thread scheduling &amp; memory mapping • Zero Dom0 management VM overhead</div>
      </div>
      <div style="text-align: center; color: var(--primary); font-weight: 800; font-family: var(--font-mono); font-size: 11px;">
        &Updownarrow; Dedicated High-Speed Internal PCIe Bus Interconnects &Updownarrow;
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">CUSTOM HARDWARE NITRO ACCELERATOR CARDS</span>
        <div class="tier-desc">
          &bull; <strong>Nitro Card for VPC:</strong> ASIC accelerates Elastic Network Adapter (ENA), encapsulating VPC packets at 100 Gbps line-rate.<br>
          &bull; <strong>Nitro Card for EBS:</strong> NVMe controller connects to remote EBS storage volumes with transparent hardware encryption.<br>
          &bull; <strong>Nitro Card for Local Storage:</strong> Manages local PCIe NVMe SSD scratch drives with hardware wear-leveling.<br>
          &bull; <strong>Nitro Security Chip:</strong> Cryptographically traps and validates firmware boots, establishing hardware Root of Trust.
        </div>
      </div>
    </div>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="shield-check"></i> Security Architecture: The Zero-Operator-Access Model</div>
    <p>
      Traditional cloud virtualization relied on an administrative operating system (Dom0) where datacenter operators could SSH into the host machine to inspect processes. The AWS Nitro System <strong>completely eliminates Dom0 and all interactive shells</strong>. There is no operator login, no root password, and no mechanism for an Amazon employee to access host memory, read customer RAM, or intercept guest CPU registers. Security is cryptographically enforced in hardware by the Nitro Security Chip.
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Elastic Load Balancing & Auto Scaling</span>
    <span>Unit 02 • Page 03</span>
  </div>
</article>

<!-- Page 4: ELB & ASG -->
<article class="doc-page" id="c2-scaling">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 02 • Page 04</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">13.</span> Elastic Load Balancing (ALB vs NLB vs GLB) &amp; Auto Scaling Groups (ASG)
  </h2>

  <p class="lead-para">
    High-availability distributed cloud systems distribute incoming application traffic across redundant compute fleets while dynamically modulating instance counts based on real-time load telemetry.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Load Balancer Type</th>
          <th>OSI Layer</th>
          <th>Routing Decision Protocol</th>
          <th>Latency Performance</th>
          <th>Primary Production Target</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Application Load Balancer (ALB)</strong></td>
          <td>Layer 7 (Application)</td>
          <td>Inspects HTTP/HTTPS headers, hostnames, query strings, and URL path rules (e.g. `/api/*` &rarr; API Target Group; `/images/*` &rarr; Static Target Group)</td>
          <td>Low (~5-15 milliseconds)</td>
          <td>Microservice web applications, REST APIs, containerized Docker/ECS workloads, gRPC</td>
        </tr>
        <tr>
          <td><strong>Network Load Balancer (NLB)</strong></td>
          <td>Layer 4 (Transport)</td>
          <td>Inspects TCP, UDP, and TLS sockets without touching application payloads; provides static Elastic IP per AZ</td>
          <td><strong>Ultra-low (Sub-millisecond)</strong></td>
          <td>Gaming backends, high-frequency financial trading, streaming video, handling millions of requests/second</td>
        </tr>
        <tr>
          <td><strong>Gateway Load Balancer (GLB)</strong></td>
          <td>Layer 3 (Network) + Layer 4</td>
          <td>Geneve encapsulation (Port 6081) routes packets through 3rd-party virtual appliances</td>
          <td>Low (Line rate)</td>
          <td>Fleet scaling of third-party firewalls (Palo Alto, Fortinet), IDS/IPS appliances, and deep packet inspection</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> Auto Scaling Mechanics: Target Tracking vs Step Scaling</div>
    <p>
      An Auto Scaling Group (ASG) maintains application availability by enforcing Minimum, Maximum, and Desired capacity limits:
    </p>
    <ul>
      <li><strong>Target Tracking Scaling:</strong> Maintains a specific metric threshold (e.g. `Average CPU Utilization = 60%`). If CPU hits 75%, ASG automatically provisions new instances; if CPU drops to 30%, it terminates surplus instances smoothly.</li>
      <li><strong>Health Check Grace Period:</strong> When a new instance launches, it requires time to boot the OS, start application runtimes, and warm caches. The grace period (default 300 seconds) prevents the load balancer from terminating an instance prematurely before it can pass health checks.</li>
      <li><strong>Cooldown Period (Default 300s):</strong> Pauses scaling actions following a scale-out event, preventing aggressive thrashing (over-scaling) while newly added instances initialize.</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: Serverless Computing & AWS Lambda</span>
    <span>Unit 02 • Page 04</span>
  </div>
</article>

<!-- Page 5: Serverless & Lambda -->
<article class="doc-page" id="c2-serverless">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 02 • Page 05</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">14.</span> Serverless Computing: AWS Lambda, Firecracker MicroVMs &amp; Event-Driven Architecture
  </h2>

  <p class="lead-para">
    Serverless computing abstracts server provisioning, operating system maintenance, and capacity capacity management completely. Application code executes strictly in response to discrete triggers, with billing calculated in 1-millisecond increments.
  </p>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="zap"></i> Silicon Architecture: How Firecracker MicroVMs Boot in 5 Milliseconds</div>
    <p>
      Legacy virtual machines (such as QEMU) emulated complex legacy PC hardware (floppy drives, IDE controllers, PCI buses), requiring 30 to 60 seconds to boot. To make serverless scalable, AWS built <strong>Firecracker</strong>—an open-source Virtual Machine Monitor (VMM) written in Rust utilizing the Linux Kernel-based Virtual Machine (KVM):
    </p>
    <ul>
      <li><strong>Stripped Device Model:</strong> Firecracker strips away all legacy PC hardware emulations, providing only a minimal serial console, a block device, a network device, and a hardware cryptographic TRNG.</li>
      <li><strong>Blazing Fast Boot Time:</strong> A Firecracker MicroVM boots a guest Linux kernel in <strong>under 5 milliseconds</strong> while consuming only <strong>5 MiB of RAM</strong>!</li>
      <li><strong>Multi-Tenant Security:</strong> Unlike Docker containers which share the host kernel (where a single kernel privilege escalation compromises all tenants), each Lambda function executes inside its own hardware-isolated Firecracker MicroVM with dedicated CPU non-root isolation and seccomp-bpf system call filters.</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 02 Practice MCQ Bank</span>
    <span>Unit 02 • Page 05</span>
  </div>
</article>

<!-- Page 6: Unit 2 Practice MCQ Bank (30 Questions) -->
<article class="doc-page" id="practice-mcq-c2">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 02</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreC2">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">15.</span> Unit 02 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Test your mastery of EC2 instance types, purchasing models, the AWS Nitro System, Elastic Load Balancing, and serverless Lambda architectures.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 01 • EC2 Family Selection</div>
      <div class="mcq-q">Which EC2 instance family should be selected for high-performance in-memory caching databases like Redis that require massive RAM per core?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Compute Optimized (C7i)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Memory Optimized (R7i / X2gd)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Storage Optimized (D3)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Accelerated Compute (G5)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The R and X families provide high RAM-to-vCPU ratios (1:8 to 1:32) specifically engineered for in-memory databases and large memory caches.
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 02 • Spot Interruption Notice</div>
      <div class="mcq-q">How much advance warning does AWS issue via Amazon EC2 instance metadata before reclaiming a Spot Instance due to capacity demands?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Exactly 2 minutes</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 15 minutes</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 1 hour</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 24 hours</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> When AWS reclaims Spot capacity, it sends an EC2 Spot Instance Interruption Notice 2 minutes prior to termination, allowing instances to save state or drain connections.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="C2" data-correct="C">
      <div class="mcq-num">Question 03 • Nitro VPC Offload</div>
      <div class="mcq-q">Which component of the AWS Nitro System encapsulates VPC network packets (Geneve/VXLAN) directly in hardware at 100 Gbps line rate?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Nitro Security Chip</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Nitro Card for EBS</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Nitro Card for VPC</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The host CPU BIOS</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> The Nitro Card for VPC contains a dedicated ASIC that offloads all software-defined networking, security group enforcement, and encapsulation from the host CPU.
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="C2" data-correct="D">
      <div class="mcq-num">Question 04 • ALB Path-Based Routing</div>
      <div class="mcq-q">An application requires routing incoming requests containing the URL path `/orders/*` to one target group and `/users/*` to another. Which load balancer is required?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Network Load Balancer (NLB)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Classic Load Balancer (CLB)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Gateway Load Balancer (GLB)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Application Load Balancer (ALB)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The Application Load Balancer operates at Layer 7 and inspects HTTP/HTTPS headers and URL paths to perform content-based and path-based routing.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 05 • Firecracker MicroVMs</div>
      <div class="mcq-q">What technology allows AWS Lambda to achieve sub-10 millisecond execution container startup while maintaining hardware-isolated hypervisor security?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Docker Swarm</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Firecracker MicroVMs running on Linux KVM</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> VMware vSphere</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Microsoft Hyper-V</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Firecracker is AWS's open-source Rust-based VMM that boots stripped Linux kernels in &lt;5 ms with 5 MiB memory footprint per microVM.
      </div>
    </div>

    <!-- Q6 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 06 • Graviton vCPU Mapping</div>
      <div class="mcq-q">How does a vCPU on an ARM-based AWS Graviton3 processor differ architecturally from an x86 Intel/AMD vCPU?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 1 Graviton vCPU represents a complete dedicated physical CPU core (no SMT sharing)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Graviton vCPUs can only run 32-bit software</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Graviton vCPUs share physical cores with 4 other tenants</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Graviton vCPUs do not have L1 cache</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Graviton disables SMT. Each vCPU is a full physical core, eliminating noisy neighbor cache thrashing.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="C">
      <div class="mcq-num">Question 07 • Lambda Maximum Execution Duration</div>
      <div class="mcq-q">What is the absolute maximum execution timeout limit for a single invocation of an AWS Lambda function?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 1 minute</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 5 minutes</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 15 minutes (900 seconds)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Unlimited duration</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> AWS Lambda functions have a hard 15-minute maximum runtime limit. Longer-running batch tasks must run on AWS Fargate, ECS, or EC2.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="D">
      <div class="mcq-num">Question 08 • Network Load Balancer IP</div>
      <div class="mcq-q">What unique network capability distinguishes the Network Load Balancer (NLB) from the Application Load Balancer (ALB)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> NLB can read HTTP cookie values</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> NLB is free of charge</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> NLB converts IPv6 to IPv4 automatically</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> NLB provides a static, fixed Elastic IP address per Availability Zone and can handle millions of requests/second at ultra-low latency</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> NLB operates at Layer 4, providing static IPs that allow client corporate firewalls to whitelist fixed IP addresses, unlike ALB which uses dynamic DNS names.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 09 • ASG Cooldown Period</div>
      <div class="mcq-q">What is the functional objective of an Auto Scaling Group Cooldown Period (default 300 seconds)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Allows the physical server fans to cool down</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Prevents the ASG from launching or terminating additional instances before previously added instances stabilize and handle traffic</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Shuts down all servers at midnight</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Delays billing charges for 5 minutes</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The cooldown period pauses auto-scaling activities to allow newly launched instances to begin handling traffic and prevent over-compensation.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 10 • Compute Savings Plans Flexibility</div>
      <div class="mcq-q">How does a Compute Savings Plan differ in flexibility from an EC2 Instance Savings Plan?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Compute Savings Plans apply discounts automatically regardless of instance family, size, OS, region, or compute service (EC2, Fargate, Lambda)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Compute Savings Plans only work in Ireland</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Compute Savings Plans do not require a monetary commitment</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Instance Savings Plans are non-binding</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Compute Savings Plans provide the highest flexibility, applying discounts even if an architecture migrates from Intel EC2 to Graviton or Fargate containers.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="C">
      <div class="mcq-num">Question 11 • Nitro Security Chip</div>
      <div class="mcq-q">What primary security function is performed by the dedicated AWS Nitro Security Chip on physical motherboard hardware?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Encrypting Wi-Fi signals in the office</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Blocking spam emails from the server</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Trapping and cryptographically validating all firmware flash updates, preventing unauthorized firmware injection into server hardware</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Mining Bitcoin during idle server hours</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> The Nitro Security Chip controls physical access to motherboard flash memory, validating cryptographically signed firmware to prevent rootkits.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="D">
      <div class="mcq-num">Question 12 • Gateway Load Balancer Protocol</div>
      <div class="mcq-q">Which tunneling encapsulation protocol does the AWS Gateway Load Balancer (GLB) use to route raw packets to third-party security inspection appliances on UDP Port 6081?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> IPsec</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> GRE</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> OpenVPN</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Geneve (Generic Network Virtualization Encapsulation)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> GLB encapsulates IP packets using Geneve protocol on UDP port 6081, preserving original packet headers for deep inspection by virtual firewalls.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 13 • EC2 Hibernation Mechanism</div>
      <div class="mcq-q">When an administrator hibernates an Amazon EC2 instance, where does the operating system save its volatile RAM contents?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> In an S3 Glacier archive</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Dumped into an encrypted file on the root Amazon EBS volume</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Stored inside the CPU L3 cache</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Transferred to the administrator's desktop PC</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> EC2 Hibernation writes RAM state directly to the encrypted root EBS volume, allowing instant resume with applications in their exact pre-hibernation state.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 14 • Lambda Resource Sizing</div>
      <div class="mcq-q">In AWS Lambda, how does an engineer scale the CPU processing power and network bandwidth allocated to a serverless function?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By increasing the configured Memory allocation (CPU scales linearly in proportion to RAM, up to 6 vCPUs at 10,240 MB)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By selecting an EC2 instance family in the Lambda settings</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By rewriting the code in C++</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> CPU power cannot be adjusted in Lambda</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Lambda does not provide direct CPU knobs; allocating more memory (128 MB to 10,240 MB) allocates proportionally more CPU shares and network throughput.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="C">
      <div class="mcq-num">Question 15 • EC2 Placement Groups</div>
      <div class="mcq-q">Which EC2 Placement Group strategy packs instances closely together inside a single Availability Zone to achieve the lowest possible network latency and highest packet-per-second performance?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Spread Placement Group</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Partition Placement Group</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Cluster Placement Group</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Multi-AZ Placement Group</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Cluster placement groups place instances physically close together on the same switch fabric inside one AZ, delivering 100 Gbps low-latency interconnects for HPC.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="D">
      <div class="mcq-num">Question 16 • Spread Placement Group</div>
      <div class="mcq-q">When should an enterprise deploy a Spread Placement Group for Amazon EC2?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> To save money on Spot instances</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> To download files faster from the web</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> To run machine learning clusters</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> For a small number of critical instances (e.g. redundant database primary/standby) that must strictly reside on distinct physical server racks with independent power and networking</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Spread placement groups place each instance on distinct physical hardware racks (maximum 7 instances per AZ), protecting against physical hardware rack failures.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 17 • Dedicated Instances vs Dedicated Hosts</div>
      <div class="mcq-q">What core capability is provided by an EC2 Dedicated Host that is NOT available on standard Dedicated Instances?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Dedicated Hosts provide free EBS storage</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Full visibility and socket/core socket-level control of the physical server to satisfy Bring-Your-Own-License (BYOL) software agreements</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Dedicated Hosts can be physically moved to your house</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Dedicated Hosts do not require power</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Dedicated Hosts give direct visibility into physical socket and core counts, required by vendors (like Microsoft or Oracle) for per-core licensing compliance.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 18 • ASG Target Tracking Policy</div>
      <div class="mcq-q">Which Auto Scaling policy functions analogous to a home air conditioning thermostat, automatically modulating capacity to hold a metric at a set point?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Target Tracking Scaling Policy</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Scheduled Scaling Policy</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Step Scaling Policy</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Manual Capacity Override</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Target Tracking dynamically increases or decreases capacity to keep the target metric (e.g. 50% CPU or 1000 requests per target) at the specified goal.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="C">
      <div class="mcq-num">Question 19 • Instance Metadata Service v2</div>
      <div class="mcq-q">Why does AWS mandate IMDSv2 (Instance Metadata Service Version 2) over legacy IMDSv1 on modern EC2 deployments?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> IMDSv2 downloads metadata faster</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> IMDSv2 allows instances to bypass the hypervisor</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> IMDSv2 requires a session-oriented PUT request with a token header, neutralizing Server-Side Request Forgery (SSRF) attacks that stole IAM credentials</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> IMDSv1 was limited to 10 instances</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> IMDSv2 requires fetching a session token via an HTTP PUT with `X-aws-ec2-metadata-token-ttl-seconds`, blocking SSRF vulnerabilities from dumping IAM role keys.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="D">
      <div class="mcq-num">Question 20 • Elastic Network Adapter (ENA)</div>
      <div class="mcq-q">What performance enhancement is provided by AWS Enhanced Networking using the Elastic Network Adapter (ENA)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Automatic translation of English web pages</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Doubling the size of hard drives</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Connecting instances without an IP address</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Single Root I/O Virtualization (SR-IOV) bypassing the hypervisor to achieve up to 100+ Gbps throughput and higher packets-per-second with minimal CPU overhead</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> ENA utilizes SR-IOV to provide direct access to physical PCIe network interfaces, slashing latency and delivering predictable multi-gigabit throughput.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 21 • Lambda Concurrency Model</div>
      <div class="mcq-q">What happens when incoming request invocations to an AWS Lambda function exceed its configured Provisioned Concurrency limit?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Standard on-demand scaling spins up fresh execution environments, which may experience an initial "cold start" latency spike</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> All excess requests are immediately dropped and deleted</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The AWS account is permanently suspended</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The function code is automatically recompiled in Python</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Requests exceeding provisioned concurrency spill over to standard on-demand initialization, incurring cold start latency while new microVMs boot.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 22 • Cross-Zone Load Balancing</div>
      <div class="mcq-q">How does Cross-Zone Load Balancing improve application resilience across an unevenly distributed backend fleet?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It copies all databases to London automatically</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It distributes incoming client traffic evenly across all registered backend targets across all enabled Availability Zones, regardless of how many instances exist in each zone</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It stops instances from failing</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It makes load balancers invisible</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Without cross-zone balancing, each load balancer node distributes traffic only to instances in its local AZ (overloading AZs with fewer instances). Cross-zone routes 50/50 across all targets.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="C">
      <div class="mcq-num">Question 23 • T-Series Burstable CPU Credits</div>
      <div class="mcq-q">How do EC2 burstable general-purpose instances (e.g. `t4g.micro`, `t3.medium`) manage temporary CPU spikes above their baseline?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> They shut down when CPU reaches 100%</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> They install extra physical fans</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> They accumulate CPU Credits during idle hours below baseline and spend those credits to burst up to 100% CPU utilization when traffic arrives</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> They ask other instances for permission to burst</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> T-series instances earn CPU credits when running below their baseline utilization and consume credits to burst to full compute speed during traffic spikes.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="D">
      <div class="mcq-num">Question 24 • Serverless Ephemeral Storage</div>
      <div class="mcq-q">What is the maximum configurable ephemeral `/tmp` storage capacity available to an AWS Lambda function execution environment?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 512 MB only</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 2,048 MB</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 5,120 MB</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 10,240 MB (10 GiB)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Lambda provides configurable ephemeral `/tmp` scratch disk space ranging from 512 MB up to 10,240 MB (10 GiB) for processing large video or machine learning files.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 25 • ALB Connection Draining / Deregistration Delay</div>
      <div class="mcq-q">What does Deregistration Delay (Connection Draining) do when an EC2 instance is being removed from an Application Load Balancer target group?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Stops sending new requests to the instance while allowing in-flight active HTTP requests to complete cleanly before terminating</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Instantly severs all open TCP sockets</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Deletes the instance AMI image</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Reboots the instance into safe mode</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Deregistration delay (default 300 seconds) gives active client connections time to finish completing requests, preventing broken HTTP 502/504 errors during scale-in.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 26 • Spot Fleet Allocation Strategy</div>
      <div class="mcq-q">Which Spot Fleet allocation strategy launches instances across the Spot pools with the lowest historical interruption rate?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Lowest Price strategy</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Capacity-Optimized strategy</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Diversified strategy</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Price-Capacity-Optimized strategy</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> `capacity-optimized` inspects real-time spare capacity telemetry across pools, allocating from pools with the deepest capacity to minimize interruption risk.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="C">
      <div class="mcq-num">Question 27 • Dedicated Host BYOL Compliance</div>
      <div class="mcq-q">Why does Microsoft Windows Server licensing with Software Assurance often require Amazon EC2 Dedicated Hosts rather than multi-tenant EC2?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Multi-tenant EC2 cannot boot Windows</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> AWS charges double for Windows on shared hardware</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Traditional enterprise licensing rules mandate tracking physical core and physical processor socket allocations to specific designated physical hardware</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Dedicated Hosts eliminate the need for Windows licenses</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Proprietary enterprise licenses require tracking physical processor sockets and cores, which is only supported when instances are bound to an EC2 Dedicated Host.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="D">
      <div class="mcq-num">Question 28 • Lambda Cold Starts</div>
      <div class="mcq-q">What architectural mitigation completely eliminates "cold start" latency spikes for latency-sensitive AWS Lambda microservices?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Increasing the function timeout to 15 minutes</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Compressing the code into a `.zip` archive</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Running the function on an EC2 t2.micro instance</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Enabling Provisioned Concurrency, which pre-initializes and warms dedicated execution environments in advance</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Provisioned Concurrency maintains pre-warmed execution microVMs ready to respond immediately in double-digit milliseconds, eliminating runtime initialization cold starts.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="A">
      <div class="mcq-num">Question 29 • Serverless Container Engine</div>
      <div class="mcq-q">Which AWS serverless compute service allows teams to execute Docker containers without managing, provisioning, or patching underlying EC2 virtual machines?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> AWS Fargate (via Amazon ECS or Amazon EKS)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Amazon LightSail</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Elastic Beanstalk (Single Instance)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Amazon CloudFront</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and EKS, removing the need to manage EC2 cluster infrastructure.
      </div>
    </div>

    <div class="mcq-card" data-unit="C2" data-correct="B">
      <div class="mcq-num">Question 30 • ALB SNI Support</div>
      <div class="mcq-q">What capability allows a single Application Load Balancer (ALB) to host multiple secure websites (e.g. `api.example.com` and `shop.example.com`) each using distinct SSL/TLS certificates on the same listener port 443?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Port Address Translation</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Server Name Indication (SNI / RFC 6066)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Route 53 Geolocation</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Dual-stack IPv6</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> SNI allows the client to specify the target hostname during the TLS handshake before certificates are exchanged, allowing one ALB listener to bind multiple distinct TLS certs.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 02 Conceptual Questions</span>
    <span>Unit 02 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 2 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-c2">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 02</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">16.</span> Unit 2 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted architectural comparisons of compute virtualization, hardware offload engines, and load balancing mechanics.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Contrast Application Load Balancers (ALB) and Network Load Balancers (NLB) regarding OSI layer, routing criteria, and latency profiles.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>ALB (Layer 7):</strong> Inspects HTTP/HTTPS application payloads. Routes traffic based on host headers, URL paths (e.g. `/api` vs `/checkout`), query parameters, and HTTP methods. Terminates TLS and supports Server Name Indication (SNI). Latency is ~5-15 ms due to deep packet inspection.</p>
        <p><strong>NLB (Layer 4):</strong> Operates strictly at the Transport layer (TCP/UDP). Does not touch application payloads. Capable of processing tens of millions of requests per second with sub-millisecond latency. Provides static Elastic IPs per AZ and supports client IP preservation without modifying HTTP headers, making it ideal for gaming, trading, and non-HTTP protocols.</p>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Explain how the AWS Nitro System completely removes the performance and security overhead of the legacy Xen Dom0 management VM.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>In legacy cloud architectures (Xen), a privileged management virtual machine (Dom0) executed alongside customer guest VMs, consuming up to 30% of host CPU and memory to handle networking encapsulation, disk I/O virtualization, and telemetry monitoring.</p>
        <p>The AWS Nitro System physically offloads these responsibilities onto dedicated PCIe ASIC cards (Nitro Card for VPC, Nitro Card for EBS, Nitro Security Chip). The host CPU no longer runs Dom0 or heavy virtualization daemons; it runs a stripped-down microvisor that merely allocates memory and schedules CPU threads. This delivers nearly 100% of host silicon to customer instances and eliminates hypervisor jitter.</p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> Detail the operational lifecycle of an EC2 Spot Instance termination: notification, state draining, and re-allocation strategies.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>When demand for On-Demand capacity surges, AWS reclaims spare Spot compute capacity. The process follows a strict 2-minute timeline:</p>
        <ol>
          <li><strong>2-Minute Warning:</strong> AWS issues an EC2 Spot Instance Interruption Notice accessible via instance metadata (`http://169.254.169.254/latest/meta-data/spot/instance-action`) and Amazon EventBridge.</li>
          <li><strong>Graceful Draining:</strong> Workload agents intercept the event, deregister the instance from load balancers, finish active in-flight requests, and flush state or checkpoint data to Amazon S3 or DynamoDB.</li>
          <li><strong>Mitigation Strategy:</strong> Deploy Spot Fleets using the `price-capacity-optimized` allocation strategy across multiple instance families and multiple AZs to ensure auto-replacement occurs in healthy pools.</li>
        </ol>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> How does AWS Firecracker achieve microVM isolation in under 5 milliseconds compared to standard Docker container runtimes?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>Standard Docker containers provide process-level isolation sharing the host Linux kernel. If a container executes a malicious kernel exploit (e.g. dirty COW), all sibling containers on the host can be breached.</p>
        <p>Firecracker is a lightweight Virtual Machine Monitor written in Rust that creates full hardware-isolated virtual machines using Linux KVM. Firecracker strips all legacy PC peripheral emulations (USB, ACPI, IDE), leaving only a minimal serial port, virtio block, and virtio net device. This minimal device model boots a full Linux kernel in &lt;5 ms inside a hardware VMX non-root sandbox with 5 MiB memory footprint, combining the security of hardware virtualization with the speed of containers.</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> Differentiate Cluster, Spread, and Partition EC2 Placement Groups from an infrastructure reliability perspective.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Cluster:</strong> Packs instances close together inside a single Availability Zone on the same network spine. Delivers high throughput (100 Gbps) and ultra-low latency for HPC and big data clusters, but carries higher risk (AZ failure impacts all nodes).</p>
        <p><strong>Spread:</strong> Strictly places each instance on a separate physical server rack with distinct power and network sources (maximum 7 instances per AZ). Used for mission-critical replicated pairs (e.g. primary/standby SQL databases).</p>
        <p><strong>Partition:</strong> Divides the placement group into logical partitions; instances in one partition do not share hardware racks with other partitions. Tailored for distributed topologies like Apache Cassandra, Kafka, and HDFS.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 02 Analytical Problems</span>
    <span>Unit 02 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 2 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-c2">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 02</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">17.</span> Unit 2 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Real-world architectural failure analyses, capacity scaling incidents, and serverless cold start mitigation scenarios.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Capacity Scaling Collapse: Auto Scaling Thrashing &amp; Broken Health Checks During Black Friday Surge</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> At 12:01 AM on Black Friday, an e-commerce platform's traffic surges by 1,200%. The Auto Scaling Group launches 50 new EC2 instances. However, within 4 minutes, the ALB marks all newly launched instances as `Unhealthy`, terminating them. The ASG launches 50 more instances, which are also terminated immediately. The site collapses into continuous HTTP 504 Gateway Timeout errors.</p>
        <p><strong>Root Cause Analysis &amp; Resolution:</strong></p>
        <ol>
          <li><strong>The Health Check Grace Period Flaw:</strong> The ASG had its <em>Health Check Grace Period</em> configured to the default 60 seconds. However, during container boot, Java runtime compilation, and database cache pre-warming, the application took <strong>180 seconds to become operational</strong>. The ALB probed the health check endpoint at second 70, received connection refused, marked the instance `Unhealthy`, and triggered an immediate ASG termination loop!</li>
          <li><strong>Remediation 1:</strong> Increase the Health Check Grace Period to <strong>300 seconds</strong>, ensuring newly provisioned instances have adequate runway to initialize caches before health checks begin evaluating.</li>
          <li><strong>Remediation 2:</strong> Implement <strong>Warm Pools</strong> in the Auto Scaling Group. Warm pools maintain a pool of pre-initialized instances in a `Stopped` or `Running` state, cutting scale-out times from 4 minutes down to 30 seconds.</li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> Serverless Cold Start Optimization: Eliminating 4-Second Tail Latency in Java Lambda APIs</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Engineering Challenge:</strong> A mobile banking app migrates its backend to AWS Lambda with an Application Load Balancer. While 95% of API requests execute in 25 milliseconds, the p99 tail latency spikes to <strong>4.2 seconds</strong>, causing mobile users to experience frozen screens during payment authentication.</p>
        <p><strong>Technical Analysis &amp; Architectural Fix:</strong></p>
        <ul>
          <li><strong>Cold Start Decomposition:</strong> Profiling with AWS X-Ray reveals that the 4.2-second delay consists of:
            <br>&bull; Firecracker MicroVM boot: ~15 ms
            <br>&bull; VPC Elastic Network Interface (ENI) attachment: ~20 ms
            <br>&bull; <strong>Java Virtual Machine (JVM) initialization &amp; Spring Boot dependency injection: 4,100 ms!</strong>
          </li>
          <li><strong>Architectural Solutions:</strong>
            <br>1. <strong>AWS Lambda SnapStart:</strong> Enables SnapStart for Java. When the code is deployed, Lambda initializes the JVM, loads all Spring Boot classes, takes an encrypted snapshot of the memory and disk state, and caches it. Subsequent cold starts restore directly from the cached memory snapshot in under <strong>180 milliseconds</strong>!
            <br>2. <strong>Provisioned Concurrency:</strong> Pre-warm 20 execution environments during market trading hours to eliminate cold starts entirely.
          </li>
        </ul>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> Spot Fleet Resiliency: Architecting Fault-Tolerant Genomic Sequencing at 80% Cost Reduction</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>System Engineering Request:</strong> A bio-informatics lab processes 10,000 human genome samples monthly. Running the pipeline on On-Demand `c6i.8xlarge` instances costs $45,000/month. The engineering team wants to transition the pipeline to Spot Instances to reduce costs below $12,000/month without risking job loss from Spot terminations.</p>
        <p><strong>Architectural Blueprint:</strong></p>
        <ul>
          <li><strong>Stateless Worker Architecture:</strong> Containerize the genomic analysis pipeline and deploy onto Amazon EKS with Karpenter auto-scaling.</li>
          <li><strong>Spot Fleet Diversification:</strong> Instead of requesting only `c6i.8xlarge`, configure Karpenter to select from <strong>16 distinct instance families and generations</strong> across multiple AZs (`c5.8xlarge`, `c5a.8xlarge`, `c6i.8xlarge`, `c6a.8xlarge`, `m6i.8xlarge`). By diversifying across 16 pools, an interruption in one pool impacts less than 6% of the fleet.</li>
          <li><strong>Micro-Checkpointing with S3:</strong> The analysis algorithm writes checkpoints to Amazon S3 every 3 minutes. When an instance receives the 2-minute Spot Interruption Notice via EventBridge, the worker flushes the active step progress to S3 and gracefully exits. A replacement Spot node spins up and resumes processing from the checkpoint with zero data loss.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> SSRF Credential Theft Mitigation: Enforcing IMDSv2 Across Enterprise EC2 Fleets</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Security Audit Finding:</strong> A penetration tester discovers a Server-Side Request Forgery (SSRF) vulnerability in an internal enterprise web application. By exploiting the parameter `https://app.corp/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/AppRole`, the tester extracts temporary AWS STS access keys, secret keys, and session tokens, compromising the entire AWS cloud account.</p>
        <p><strong>Cryptographic Root Cause &amp; Remediation:</strong></p>
        <ul>
          <li><strong>Vulnerability of IMDSv1:</strong> Legacy IMDSv1 allowed simple HTTP GET requests without headers. Any SSRF flaw that tricks an application into making an outbound HTTP request can effortlessly dump IAM credentials from `169.254.169.254`.</li>
          <li><strong>The IMDSv2 Defense:</strong> Enforce IMDSv2 (`HttpTokens=required`). IMDSv2 mandates a two-step session exchange:
            <br>&bull; Step 1: Send HTTP PUT with header `X-aws-ec2-metadata-token-ttl-seconds: 21600` to retrieve a signed session token.
            <br>&bull; Step 2: Pass token in header `X-aws-ec2-metadata-token` for data requests.
            <br>Standard SSRF vulnerabilities cannot construct arbitrary HTTP PUT requests with custom headers, neutralizing the attack vector completely.</li>
          <li><strong>Automated Enforcement:</strong> Deploy an AWS Service Control Policy (SCP) that denies launching any EC2 instance unless `ec2:MetadataHttpTokens` is set to `required`.</li>
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
<article class="doc-page" id="mcq-answer-key-c2">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 02</span>
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
        <tr><td>01</td><td><strong style="color:var(--primary);">B</strong></td><td>Memory Optimized instance selection for in-memory databases</td><td>16</td><td><strong style="color:var(--primary);">D</strong></td><td>Spread placement group hardware rack isolation</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">A</strong></td><td>Spot Instance 2-minute interruption notice mechanism</td><td>17</td><td><strong style="color:var(--primary);">B</strong></td><td>Dedicated Hosts physical socket control for BYOL software</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">C</strong></td><td>Nitro Card for VPC hardware network encapsulation offload</td><td>18</td><td><strong style="color:var(--primary);">A</strong></td><td>Target Tracking Auto Scaling Policy thermostat mechanism</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">D</strong></td><td>ALB Layer 7 URL path-based routing capability</td><td>19</td><td><strong style="color:var(--primary);">C</strong></td><td>IMDSv2 tokenized PUT headers neutralizing SSRF attacks</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">B</strong></td><td>Firecracker MicroVMs &lt;5ms boot on Linux KVM</td><td>20</td><td><strong style="color:var(--primary);">D</strong></td><td>Elastic Network Adapter (ENA) SR-IOV enhanced networking</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">A</strong></td><td>Graviton vCPU representing dedicated physical CPU core</td><td>21</td><td><strong style="color:var(--primary);">A</strong></td><td>Lambda on-demand cold start spillover behavior</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">C</strong></td><td>AWS Lambda 15-minute maximum execution timeout limit</td><td>22</td><td><strong style="color:var(--primary);">B</strong></td><td>Cross-Zone Load Balancing distributing traffic evenly</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">D</strong></td><td>NLB static Elastic IP allocation per Availability Zone</td><td>23</td><td><strong style="color:var(--primary);">C</strong></td><td>T-series burstable CPU credit accumulation and consumption</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">B</strong></td><td>ASG cooldown period preventing scaling thrashing</td><td>24</td><td><strong style="color:var(--primary);">D</strong></td><td>Lambda ephemeral /tmp scratch disk capacity (up to 10 GiB)</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">A</strong></td><td>Compute Savings Plans multi-service automatic flexibility</td><td>25</td><td><strong style="color:var(--primary);">A</strong></td><td>ALB deregistration delay / connection draining clean completion</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">C</strong></td><td>Nitro Security Chip cryptographically validating firmware</td><td>26</td><td><strong style="color:var(--primary);">B</strong></td><td>Spot Fleet capacity-optimized allocation strategy</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">D</strong></td><td>Gateway Load Balancer Geneve UDP port 6081 encapsulation</td><td>27</td><td><strong style="color:var(--primary);">C</strong></td><td>Microsoft enterprise licensing socket-bound tracking</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">B</strong></td><td>EC2 hibernation dumping volatile RAM to encrypted root EBS</td><td>28</td><td><strong style="color:var(--primary);">D</strong></td><td>Provisioned Concurrency eliminating Lambda cold starts</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">A</strong></td><td>Lambda CPU scaling proportionally with allocated memory</td><td>29</td><td><strong style="color:var(--primary);">A</strong></td><td>AWS Fargate serverless container compute engine</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">C</strong></td><td>Cluster placement group high-throughput low-latency packing</td><td>30</td><td><strong style="color:var(--primary);">B</strong></td><td>Server Name Indication (SNI) multi-certificate binding</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 02 Complete • Next: Unit 03 Cloud Storage & CDN</span>
    <span>Unit 02 • Page 09</span>
  </div>
</article>
"""
