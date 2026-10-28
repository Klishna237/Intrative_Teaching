# CSC205: Cloud Administration (AWS) — Master University Knowledge Portal

> **Department of Computer Science & Engineering**  
> **Course Code:** CSC205 • **Domain:** Cyber Security & Cloud Architecture  
> **Format:** 100% Self-Contained Offline Single-Page Academic Publication (Master Gold Standard)

---

## 🌟 Executive Overview

The **Cloud Administration (AWS) Knowledge Portal** is an enterprise-grade academic master reference designed to the rigorous publication standards of the external gold-standard benchmark (`CSC104: IT Fundamentals`). It encapsulates the complete curriculum of AWS Cloud Administration with unmatched technical depth, register- and silicon-level execution traces, structured comparison matrices, 180 interactive MCQs with instant feedback and scoring engines, subjective analysis questions, 10 fully verified hands-on laboratory manuals, interactive engineering calculators, and an embedded AWS CLI v2 terminal sandbox.

---

## 📊 Portal Metrics & Blueprint

| Metric | Measurement | Description |
| :--- | :--- | :--- |
| **Total Artifact Size** | **549.5 KB** | 100% Self-contained single-page web application (`index.html`) |
| **Source Code Scale** | **9,022 Lines** | Clean, semantic, validated HTML5 / CSS3 / ES6 |
| **Curricular Units** | **6 Core + 4 Specialized** | Units 1 to 6, Packet Trace, Lab Manual, Simulators, Exam Bank |
| **Technical Articles** | **30 Core Deep-Dives** | Comprehensive theoretical and practical architecture coverage |
| **Practice Bank (MCQs)** | **180 Questions** | 30 MCQs per unit with scoring engine & master answer keys |
| **Subjective Problems** | **69 Card Scenarios** | 30 Conceptual (5M) & 24 Scenarios (10M) + MST & Final papers |
| **Laboratory Practicals** | **10 Full Experiments** | Production CLI v2 commands, expected outputs & Viva Voce questions |
| **Interactive Simulators** | **4 Calculators + CLI** | Subnet CIDR, Aurora Quorum, S3 Cost, EBS Sizer & CloudShell |

---

## 🗂️ Curricular Structure & Syllabus Alignment

### Unit 01: Cloud Computing Concepts & Global Infrastructure
- **c1-concepts:** Cloud Delivery Models (NIST SP 800-145: IaaS vs PaaS vs SaaS vs FaaS, On-demand Self-Service, Broad Network Access, Resource Pooling, Rapid Elasticity, Measured Service).
- **c1-virt:** Virtualization Mechanics (Type-1 Bare Metal vs Type-2 Hosted Hypervisors, Hardware-Assisted Virtualization Intel VT-x / AMD-V, Over-Subscription, Containerization Namespaces & Cgroups).
- **c1-infra:** AWS Global Physical Infrastructure (Regions, Edge POPs, Availability Zones, Fault Domains, Subsea Cables, Metro Fiber Ring DWDM).
- **c1-shared:** AWS Shared Responsibility Model (Security "OF" the Cloud vs Security "IN" the Cloud, EC2 vs S3 vs Lambda matrix).
- **c1-econ:** Cloud Economics & TCO Analysis (Capex vs Opex, Total Cost of Ownership Math, 5 Migration R's: Rehost, Replatform, Repurchase, Refactor, Retain).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 02: Cloud Compute & Modern Virtualization
- **c2-ec2:** Amazon EC2 Instance Architectures (General Purpose, Compute, Memory, Storage Optimized, vCPU Hyperthreading vs Core Allocation).
- **c2-pricing:** EC2 Pricing Models & Financial Engineering (On-Demand, Reserved Instances 1yr/3yr, Compute & EC2 Savings Plans, Spot Bidding & Interruption Notices).
- **c2-nitro:** AWS Nitro System Deep Architecture (Offloading Hypervisor overhead to PCIe ASICs: Nitro Card for VPC, Nitro Card for EBS, Nitro Security Chip, SR-IOV ENA Direct Memory Access).
- **c2-scaling:** High Availability Scaling (Application Load Balancer Layer-7 routing, Target Groups, Health Checks, Auto Scaling Step & Target Tracking policies).
- **c2-serverless:** Serverless Compute Paradigms (AWS Lambda MicroVM Firecracker virtualization, Cold Starts, Concurrency, API Gateway HTTP vs REST).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 03: Cloud Storage Architectures & Content Delivery
- **c3-s3:** Amazon S3 Architecture (Object Flat Namespace, 11 9's Durability Math, Storage Classes: Standard, Standard-IA, OneZone-IA, Glacier Flexible, Glacier Deep Archive).
- **c3-s3deep:** S3 Advanced Storage Management (Multipart Upload & 5MB chunks, Bucket Policies, SSE-S3 vs SSE-KMS, Cross-Region Replication CRR).
- **c3-ebs:** Amazon EBS Block Storage (gp3 Baseline 3000 IOPS / 125 MB/s, io2 Block Express 256,000 IOPS, Volume Striping, NVMe attachment).
- **c3-efs:** Amazon EFS & Distributed File Systems (NFSv4.1, POSIX file locking, Multi-AZ concurrent mounting, Max I/O vs General Purpose modes).
- **c3-cdn:** Amazon CloudFront CDN (Anycast Edge BGP, TLS 1.3 0-RTT Termination, Origin Shield, Cache-Control headers, Invalidation propagation).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 04: Software-Defined Networking & VPC Architecture
- **c4-vpc:** Amazon VPC Topology & CIDR Subnetting (RFC 1918 private CIDR, Subnet sizing /16 to /28, The 5 AWS Reserved IP Addresses).
- **c4-routing:** Routing Infrastructure (Internet Gateway IGW 1:1 NAT, Elastic IPs, NAT Gateway in Public Subnets, Private Route Tables).
- **c4-security:** Micro-Segmentation & Firewalls (Security Groups stateful hypervisor tracking vs Network ACLs stateless 16-bit evaluation).
- **c4-peering:** Inter-VPC Connectivity (VPC Peering non-transitive limitations vs AWS Transit Gateway TGW hub-and-spoke star routing).
- **c4-hybrid:** Hybrid Cloud Networking (AWS Direct Connect DX 802.1q VLAN trunking, IPsec Site-to-Site VPN failover, Route 53 Resolver).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 05: Managed Database Services & Big Data Analytics
- **c5-rds:** Amazon RDS & High Availability (Synchronous Multi-AZ standby replica EBS block mirroring, automated DNS CNAME failover, Asynchronous Read Replicas).
- **c5-aurora:** Amazon Aurora Distributed Storage Engine ("The Log is the Database", 6-way storage replication across 3 AZs, 4/6 Write Quorum, 3/6 Read Quorum).
- **c5-dynamo:** Amazon DynamoDB NoSQL Architecture (Partition Keys, Hash Rings, Local & Global Secondary Indexes, RCU & WCU calculation math).
- **c5-cache:** Distributed In-Memory Caching (Amazon ElastiCache: Redis Cluster sharding vs Memcached multithreaded key-value caching).
- **c5-bigdata:** Big Data Analytics Ecosystem (Amazon Redshift columnar petabyte warehousing, Amazon EMR Spark/Hadoop, Serverless Athena Presto querying).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 06: Enterprise Cloud Security, Governance & Well-Architected
- **c6-iam:** AWS Identity & Access Management (Explicit Deny evaluation logic, Condition Keys, Temporary STS token credentials, Least Privilege).
- **c6-kms:** Cryptographic Envelope Encryption (AWS KMS Customer Managed Keys, GenerateDataKey API, Plaintext vs Ciphertext Data Keys).
- **c6-monitoring:** Observability & Audit Logging (Amazon CloudWatch Metrics & Alarms, AWS CloudTrail non-repudiation audit trails, EventBridge).
- **c6-defense:** Perimeter Security & Threat Detection (AWS Shield Standard & Advanced DDoS, AWS WAF rate limiting, Amazon GuardDuty VPC Flow Log machine learning).
- **c6-waf-framework:** AWS Well-Architected Framework (6 Architectural Pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability).
- **Assessments:** 30 MCQs, 5 Conceptual Q&As, 4 Architectural Scenarios, Master Answer Key.

### Unit 07: Special Architectural Deep Trace
- **cloud-trace-packet:** End-to-End Silicon, Fiber & Protocol Packet Trace tracking an HTTP request from client smartphone &rarr; Route 53 Anycast DNS &rarr; CloudFront POP &rarr; AWS Global Backbone &rarr; Transit Gateway &rarr; ALB Target Group &rarr; EC2 Nitro Hypervisor DMA &rarr; Aurora 4/6 Quorum Storage Commit (29.2 ms total latency budget).

### Unit 08: Hands-On Enterprise Laboratory Manual
- Complete step-by-step guides for 10 university practicals with AWS CLI v2 terminal commands, architectures, and Viva Voce examination questions.

### Unit 09: Engineering Simulators & Live AWS CLI Sandbox
- Interactive client-side tools: Subnet CIDR Calculator, Aurora Quorum Node Toggle visualizer, S3 Cost Break-Even calculator, EBS GP3 baseline inspector, and an embedded interactive AWS CLI v2 terminal sandbox with realistic mock command dispatch.

### Unit 10: Master Comprehensive Examination Bank
- Mid-Semester Tests (MST-1 & MST-2) and End-Semester Final Examination papers mapped directly to Course Outcomes (CO1–CO5) and Bloom's Revised Taxonomy levels.

---

## 🚀 How to Access & Deploy

1. **Local Offline Access**: Open `d:\CU - Teach\Cloud_Administration_Portal\index.html` in any modern web browser (Chrome, Edge, Firefox, Safari). Zero Internet connectivity or web server required.
2. **Search Shortcut**: Press `Ctrl + K` or `/` to launch the interactive instant keyword search.
3. **Table of Contents**: Press `Ctrl + B` or click the menu icon in the top left to toggle the collapsible course navigator.
4. **Theme Customization**: Toggle between Light, Sepia, and Dark themes using the header theme switcher dots.
