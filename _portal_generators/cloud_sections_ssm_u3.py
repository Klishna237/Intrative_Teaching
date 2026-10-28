# -*- coding: utf-8 -*-
"""
Cloud Administration (AWS) - Unit 3: Cloud Storage & Content Delivery
Master Gold Standard Layout:
- c3-s3: Amazon S3 Storage Classes, 11 9's Durability & Bucket Policies
- c3-s3deep: S3 Multipart Uploads, Lifecycle Rules, Versioning & S3 Object Lock
- c3-ebs: Amazon EBS Volume Types (gp3 vs io2 Block Express vs st1/sc1) & Snapshots
- c3-efs: Amazon EFS (Distributed NFS) vs Amazon FSx (Lustre / Windows / NetApp)
- c3-cdn: Amazon CloudFront Global CDN, Edge Caching & AWS Storage Gateway
- practice-mcq-c3: 30 MCQs with dynamic scoring
- practice-subj-short-c3: 5 Short Conceptual Sets
- practice-subj-long-c3: 4 Deep Analytical Scenarios
- mcq-answer-key-c3: Master Answer Key Table
"""

CLOUD_UNIT3_HTML = """
<!-- ==========================================================================
     UNIT 03: CLOUD STORAGE & CONTENT DELIVERY
     ========================================================================== -->

<!-- Page 1: Amazon S3 Overview -->
<article class="doc-page" id="c3-s3">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 03 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">19.</span> Amazon S3 Object Storage Architecture, 11 9's Durability &amp; Storage Classes
  </h2>

  <p class="lead-para">
    Amazon Simple Storage Service (Amazon S3) is an exabyte-scale, distributed object store offering industry-leading data availability, security, and performance. Unlike traditional filesystem block stores that organize data into hierarchical directory trees, S3 stores data as flat objects identified by unique keys within globally unique buckets.
  </p>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="shield"></i> The Mathematical Physics of 11 9's Durability (99.999999999%)</div>
    <p>
      Amazon S3 is engineered to deliver <strong>99.999999999% durability</strong>. If an enterprise stores 10,000,000 objects in Amazon S3 Standard, you can on average expect to lose a single object once every 10,000 years!
      <br><br>
      <strong>How AWS Achieves This:</strong> Every object written to S3 Standard is synchronously written across a minimum of <strong>three physically separated Availability Zones</strong> before an HTTP 200 OK write acknowledgment is returned. Each AZ maintains independent erasure-coded storage node arrays capable of surviving concurrent multiple-device failures without data loss.
    </p>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>S3 Storage Class</th>
          <th>Designed Durability</th>
          <th>Availability SLA</th>
          <th>Minimum Storage Duration</th>
          <th>Retrieval Time &amp; Cost Trade-off</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>S3 Standard</strong></td>
          <td>99.999999999% (11 9's)</td>
          <td>99.99% (Multi-AZ)</td>
          <td>None</td>
          <td>Milliseconds retrieval; highest storage cost; zero retrieval fees</td>
        </tr>
        <tr>
          <td><strong>S3 Intelligent-Tiering</strong></td>
          <td>99.999999999% (11 9's)</td>
          <td>99.9% (Multi-AZ)</td>
          <td>None</td>
          <td>Automatically moves objects between Frequent, Infrequent, and Archive tiers based on access patterns; zero retrieval fees</td>
        </tr>
        <tr>
          <td><strong>S3 Standard-IA (Infrequent Access)</strong></td>
          <td>99.999999999% (11 9's)</td>
          <td>99.9% (Multi-AZ)</td>
          <td>30 days</td>
          <td>Milliseconds retrieval; lower monthly storage fee; per-GB data retrieval charge</td>
        </tr>
        <tr>
          <td><strong>S3 One Zone-IA</strong></td>
          <td>99.999999999% (11 9's)</td>
          <td>99.5% (Single AZ only!)</td>
          <td>30 days</td>
          <td>Stored in a single AZ; 20% cheaper than Standard-IA; destroyed if the AZ facility is physically lost</td>
        </tr>
        <tr>
          <td><strong>S3 Glacier Instant Retrieval</strong></td>
          <td>99.999999999% (11 9's)</td>
          <td>99.9% (Multi-AZ)</td>
          <td>90 days</td>
          <td>Milliseconds retrieval for rarely accessed medical images or archival news assets</td>
        </tr>
        <tr>
          <td><strong>S3 Glacier Flexible Retrieval</strong></td>
          <td>99.999999999% (11 9's)</td>
          <td>99.99% (Multi-AZ)</td>
          <td>90 days</td>
          <td>Expedited (1-5 min), Standard (3-5 hours), Bulk (5-12 hours); low cost</td>
        </tr>
        <tr>
          <td><strong>S3 Glacier Deep Archive</strong></td>
          <td>99.999999999% (11 9's)</td>
          <td>99.99% (Multi-AZ)</td>
          <td>180 days</td>
          <td>Standard (12 hours), Bulk (48 hours); lowest cost storage in the cloud (~$0.00099/GB/month)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: S3 Multipart, Versioning & Object Lock</span>
    <span>Unit 03 • Page 01</span>
  </div>
</article>

<!-- Page 2: S3 Multipart & Versioning -->
<article class="doc-page" id="c3-s3deep">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 03 • Page 02</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">20.</span> S3 Multipart Uploads, Lifecycle Rules, Versioning &amp; Object Lock
  </h2>

  <p class="lead-para">
    Managing petabyte-scale object lifecycles requires programmatic automation to optimize storage costs, ensure immutable regulatory compliance, and accelerate network ingest of massive multi-gigabyte payloads.
  </p>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> Engineering Mechanics: The S3 Multipart Upload Architecture</div>
    <p>
      For any object exceeding <strong>100 MB</strong> (and mandated for objects &gt; 5 GB up to the 5 TB single-object ceiling), engineers must utilize the S3 Multipart Upload API:
    </p>
    <ul>
      <li><strong>Parallel Transmission:</strong> The client chunks the file into parts (from 5 MB to 5 GB each). Parts 1 through \(N\) are transmitted concurrently over independent TCP streams, saturating available network bandwidth.</li>
      <li><strong>Fault Tolerance &amp; Resiliency:</strong> If Part 42 experiences a network timeout or packet corruption, only that single 10 MB chunk is retried rather than restarting the entire 500 GB upload!</li>
      <li><strong>ETag Mathematical Verification:</strong> Standard S3 objects have an ETag equal to the hex MD5 checksum of the file. In a multipart upload, the ETag represents the <em>MD5 hash of the concatenated binary MD5 hashes of each individual part</em>, suffixed by the part count (e.g. `d41d8cd98f00b204e9800998ecf8427e-45`).</li>
    </ul>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Governance Feature</th>
          <th>Operational Logic</th>
          <th>Regulatory &amp; Security Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>S3 Versioning</strong></td>
          <td>Preserves previous iterations of an object on every write or delete. A `DELETE` operation simply places a <strong>Delete Marker</strong>; previous versions remain recoverable.</td>
          <td>Protects against accidental administrative deletions and malicious overwrite attempts.</td>
        </tr>
        <tr>
          <td><strong>S3 Object Lock (WORM)</strong></td>
          <td>Enforces Write-Once-Read-Many storage in <em>Compliance Mode</em> or <em>Governance Mode</em>. Compliance Mode prevents even the root AWS account from deleting the object until retention expires!</td>
          <td>Mandatory for financial SEC Rule 17a-4, FINRA, and healthcare HIPAA immutable record-keeping.</td>
        </tr>
        <tr>
          <td><strong>S3 Lifecycle Policies</strong></td>
          <td>Automates cascading transitions: e.g. Day 0: S3 Standard &rarr; Day 30: S3 Standard-IA &rarr; Day 90: S3 Glacier &rarr; Day 365: Expire/Delete.</td>
          <td>Reduces storage expenditure by up to 80% without manual administrative intervention.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Amazon EBS Volume Types & Performance</span>
    <span>Unit 03 • Page 02</span>
  </div>
</article>

<!-- Page 3: Amazon EBS -->
<article class="doc-page" id="c3-ebs">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 03 • Page 03</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">21.</span> Amazon Elastic Block Store (EBS): Volume Architectures, IOPS &amp; Snapshots
  </h2>

  <p class="lead-para">
    Amazon EBS provides persistent, raw, unformatted block-level storage volumes designed for attachment to a single EC2 instance (or multiple via Multi-Attach) within the same Availability Zone, behaving physically like an enterprise Storage Area Network (SAN).
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>EBS Volume Type</th>
          <th>Volume API Code</th>
          <th>Baseline Performance</th>
          <th>Max IOPS / Max Throughput</th>
          <th>Primary Production Workloads</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>General Purpose SSD</strong></td>
          <td>`gp3`</td>
          <td>3,000 IOPS &amp; 125 MB/s included free with base storage</td>
          <td>16,000 IOPS / 1,000 MB/s (Decoupled from storage capacity!)</td>
          <td>Default root boot volumes, virtual desktops, corporate web servers, dev/test</td>
        </tr>
        <tr>
          <td><strong>Provisioned IOPS SSD</strong></td>
          <td>`io2 Block Express`</td>
          <td>Up to 1,000 IOPS per GiB provisioned</td>
          <td><strong>256,000 IOPS / 4,000 MB/s (&lt;0.2 ms sub-millisecond latency)</strong></td>
          <td>Mission-critical enterprise I/O: Oracle, SAP HANA, Microsoft SQL Server, PostgreSQL</td>
        </tr>
        <tr>
          <td><strong>Throughput Optimized HDD</strong></td>
          <td>`st1`</td>
          <td>Sequential streaming magnetic media</td>
          <td>500 IOPS / 500 MB/s</td>
          <td>Large sequential streaming data warehouses, Hadoop/Spark big data, Kafka logs</td>
        </tr>
        <tr>
          <td><strong>Cold HDD</strong></td>
          <td>`sc1`</td>
          <td>Lowest-cost magnetic block media</td>
          <td>250 IOPS / 250 MB/s</td>
          <td>Infrequently accessed sequential file archives</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="cpu"></i> Silicon Architecture: Decoupled IOPS on gp3 vs gp2</div>
    <p>
      Legacy `gp2` volumes tied IOPS directly to storage capacity at a fixed 3 IOPS/GiB ratio. To achieve 3,000 IOPS, a customer was forced to purchase 1,000 GiB of storage even if they only needed 50 GiB!
      <br><br>
      The modern **`gp3` architecture decouples IOPS and throughput from volume size**. An engineer can provision a compact 30 GiB root disk and independently scale throughput to 500 MB/s and 12,000 IOPS without buying unneeded storage, slashing AWS monthly EBS spend by 20% to 40%.
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Distributed Filesystems: EFS vs FSx</span>
    <span>Unit 03 • Page 03</span>
  </div>
</article>

<!-- Page 4: EFS vs FSx -->
<article class="doc-page" id="c3-efs">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 03 • Page 04</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">22.</span> Distributed Shared Filesystems: Amazon EFS vs Amazon FSx
  </h2>

  <p class="lead-para">
    Unlike block storage (which mounts to a single host), shared network filesystems enable hundreds or thousands of compute instances to mount and concurrently read/write to a unified file tree over standard networking protocols.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Service</th>
          <th>Protocol</th>
          <th>Underlying OS Affinity</th>
          <th>Multi-AZ Architecture</th>
          <th>Typical Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Amazon EFS</strong></td>
          <td>NFSv4.0 / NFSv4.1</td>
          <td>Linux POSIX filesystems</td>
          <td>Native synchronous Multi-AZ durability; scales automatically to petabytes</td>
          <td>Web content management (WordPress), container shared persistent storage (ECS/EKS), DevOps home dirs</td>
        </tr>
        <tr>
          <td><strong>Amazon FSx for Windows</strong></td>
          <td>SMB (Server Message Block)</td>
          <td>Microsoft Windows Server</td>
          <td>Supports Multi-AZ deployment with Active Directory integration</td>
          <td>Enterprise Windows file shares, IIS web farms, SharePoint, CAD applications</td>
        </tr>
        <tr>
          <td><strong>Amazon FSx for Lustre</strong></td>
          <td>Lustre parallel POSIX</td>
          <td>Linux High Performance Computing</td>
          <td>Sub-millisecond parallel access; links directly to Amazon S3 buckets</td>
          <td>Machine learning model training, seismic analysis, financial risk modeling</td>
        </tr>
        <tr>
          <td><strong>Amazon FSx for NetApp ONTAP</strong></td>
          <td>NFS, SMB, iSCSI</td>
          <td>Multi-protocol enterprise</td>
          <td>Multi-AZ with ONTAP SnapMirror</td>
          <td>Migrating on-premises NetApp storage arrays into AWS without changing operational scripts</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: CloudFront Global CDN & Storage Gateway</span>
    <span>Unit 03 • Page 04</span>
  </div>
</article>

<!-- Page 5: CloudFront & Storage Gateway -->
<article class="doc-page" id="c3-cdn">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 03 • Page 05</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">23.</span> Amazon CloudFront Global CDN, Edge Caching &amp; AWS Storage Gateway
  </h2>

  <p class="lead-para">
    Content Delivery Networks accelerate asset delivery by caching copies of data at physical Points of Presence (PoPs) located geographically adjacent to end-users, shielding backend origin servers from crushing traffic loads.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Storage Gateway Type</th>
          <th>On-Premises Interface</th>
          <th>AWS Cloud Backend</th>
          <th>Primary Operational Problem Solved</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>S3 File Gateway</strong></td>
          <td>NFS / SMB network share</td>
          <td>Amazon S3 buckets (Standard, IA, Glacier)</td>
          <td>Seamless on-premises file storage backup to cloud; files appear as native local files while residing in S3.</td>
        </tr>
        <tr>
          <td><strong>Volume Gateway (Stored)</strong></td>
          <td>iSCSI block volume</td>
          <td>Primary data on-prem; asynchronous snapshot backups to Amazon S3</td>
          <td>Low-latency local access for on-prem applications requiring local storage with offsite cloud DR.</td>
        </tr>
        <tr>
          <td><strong>Volume Gateway (Cached)</strong></td>
          <td>iSCSI block volume</td>
          <td>Primary data in Amazon S3; frequently accessed data cached locally</td>
          <td>Substantially reduces on-premises storage footprint by keeping only working set locally.</td>
        </tr>
        <tr>
          <td><strong>Tape Gateway (VTL)</strong></td>
          <td>iSCSI Virtual Tape Library</td>
          <td>Amazon S3 and S3 Glacier Flexible / Deep Archive</td>
          <td>Completely replaces physical robotic magnetic tape libraries without altering legacy backup software (Veeam, Commvault).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 03 Practice MCQ Bank</span>
    <span>Unit 03 • Page 05</span>
  </div>
</article>

<!-- Page 6: Unit 3 Practice MCQ Bank (30 Questions) -->
<article class="doc-page" id="practice-mcq-c3">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 03</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreC3">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">24.</span> Unit 03 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Test your mastery of S3 storage classes, multipart uploads, EBS block performance, distributed filesystems, and global content delivery.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="C3" data-correct="C">
      <div class="mcq-num">Question 01 • S3 Durability Rating</div>
      <div class="mcq-q">What is the designed data durability percentage of the Amazon S3 Standard storage class across multiple Availability Zones?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 99.9%</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 99.99%</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 99.999999999% (11 9's)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 100%</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Amazon S3 Standard is architected to provide eleven 9's of durability by synchronously storing data across at least three independent AZs.
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 02 • S3 Lowest Cost Archive</div>
      <div class="mcq-q">Which S3 storage class provides the absolute lowest cost per gigabyte-month for compliance data that is accessed once every few years with a 12-hour retrieval window?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> S3 Glacier Deep Archive</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> S3 Standard-IA</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> S3 Glacier Instant Retrieval</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> S3 One Zone-IA</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> S3 Glacier Deep Archive costs ~$0.00099/GB/month, making it the cheapest cloud storage option for multi-year regulatory records.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="C3" data-correct="D">
      <div class="mcq-num">Question 03 • S3 Multipart Upload Threshold</div>
      <div class="mcq-q">At what file size threshold does AWS mandate the use of the S3 Multipart Upload API, and at what size is it strongly recommended?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Mandated at 10 MB; recommended at 1 MB</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Mandated at 50 GB; recommended at 10 GB</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Mandated at 100 GB; recommended at 500 MB</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Mandated for single files &gt; 5 GB; strongly recommended for files &gt; 100 MB</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Single PUT operations are capped at 5 GB. Files above 5 GB must use Multipart Upload, while files &gt; 100 MB benefit heavily from parallel uploading.
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 04 • EBS gp3 Baseline IOPS</div>
      <div class="mcq-q">What baseline performance is included free of charge with every Amazon EBS General Purpose SSD (gp3) volume regardless of size?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 100 IOPS and 10 MB/s</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 3,000 IOPS and 125 MB/s throughput</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 10,000 IOPS and 500 MB/s</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 256,000 IOPS and 4,000 MB/s</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> `gp3` provides 3,000 baseline IOPS and 125 MB/s throughput included with the base storage cost, with decoupled scaling up to 16,000 IOPS.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 05 • EFS Multi-AZ Mounting</div>
      <div class="mcq-q">Which shared file storage service allows thousands of Linux EC2 instances across multiple Availability Zones to concurrently mount a unified POSIX filesystem via NFSv4?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Amazon Elastic File System (Amazon EFS)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Amazon EBS gp3</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Storage Gateway VTL</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Amazon S3 Glacier</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Amazon EFS is a managed serverless NFS filesystem that synchronously stores data across multiple AZs and supports massive concurrent Linux client mounts.
      </div>
    </div>

    <!-- Q6 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="C3" data-correct="C">
      <div class="mcq-num">Question 06 • EBS io2 Block Express Performance</div>
      <div class="mcq-q">What is the maximum provisioned IOPS capacity supported by an Amazon EBS io2 Block Express volume?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 16,000 IOPS</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 64,000 IOPS</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 256,000 IOPS (with 4,000 MB/s throughput)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 1,000,000 IOPS</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> `io2 Block Express` volumes deliver SAN-grade performance up to 256,000 IOPS, 4,000 MB/s throughput, and sub-millisecond latency for mission-critical enterprise databases.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 07 • S3 Intelligent-Tiering Monitoring</div>
      <div class="mcq-q">What is the primary operational advantage of using S3 Intelligent-Tiering for workloads with unpredictable access patterns?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It converts files to PDF automatically</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It automatically shifts objects between access tiers based on usage without operational overhead or data retrieval fees</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It provides free compute servers</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It deletes old files after 24 hours</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Intelligent-Tiering monitors access patterns and moves objects between Frequent, Infrequent, and Archive tiers with zero performance impact and zero retrieval charges.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="D">
      <div class="mcq-num">Question 08 • S3 Object Lock Compliance Mode</div>
      <div class="mcq-q">What happens when an object in Amazon S3 is placed in S3 Object Lock Compliance Mode?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It can be deleted if the AWS root user signs in with MFA</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> AWS support can unlock the file upon written request</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It is encrypted with a password sent by email</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The object cannot be overwritten or deleted by ANY user (including the AWS account root user) until the retention period expires</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Compliance Mode strictly prevents any user, including root, from deleting the object or altering retention settings during the retention window to satisfy SEC Rule 17a-4.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 09 • FSx for Lustre Application</div>
      <div class="mcq-q">Which shared file service is engineered specifically to feed data into machine learning, financial analytics, and seismic modeling HPC clusters with sub-millisecond parallel throughput?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Amazon FSx for Lustre</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Amazon EFS Standard</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Storage Gateway Tape Gateway</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Amazon S3 Glacier Deep Archive</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> FSx for Lustre is a parallel filesystem that scales to hundreds of gigabytes per second and millions of IOPS, linking directly to S3 data lakes for compute jobs.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 10 • S3 Versioning Delete Marker</div>
      <div class="mcq-q">When an administrator deletes an object from a versioning-enabled S3 bucket without specifying a Version ID, what occurs?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The object and all its history are permanently expunged</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> S3 inserts a Delete Marker as the current version; previous versions remain intact and can be restored</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> S3 returns an HTTP 403 Forbidden error</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The bucket is automatically placed in read-only mode</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> S3 inserts a Delete Marker. The object disappears from standard listings, but removing the Delete Marker restores the previous version cleanly.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="C">
      <div class="mcq-num">Question 11 • Tape Gateway Modernization</div>
      <div class="mcq-q">Which AWS Storage Gateway configuration replaces physical magnetic tape robotics with an iSCSI Virtual Tape Library (VTL) backed by S3 and Glacier?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> File Gateway</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Volume Gateway Cached</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Tape Gateway</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Volume Gateway Stored</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Tape Gateway exposes a standard iSCSI VTL to on-premises backup software (like Veeam or Backup Exec), eliminating tape logistics while archiving to Glacier.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="D">
      <div class="mcq-num">Question 12 • EBS Snapshot Consistency</div>
      <div class="mcq-q">How does Amazon EBS store point-in-time snapshot backups in Amazon S3?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By copying the entire volume from start to finish every time</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> In an uncompressed `.zip` file on an EC2 instance</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By converting block data into text strings</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Incrementally, saving only the specific 512KB disk blocks that changed since the previous snapshot was captured</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> EBS snapshots are incremental: only changed blocks are written to S3, reducing storage consumption while maintaining full-volume point-in-time restorable images.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 13 • S3 One Zone-IA Risk</div>
      <div class="mcq-q">What is the critical engineering risk when selecting S3 One Zone-IA over S3 Standard-IA?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Data is stored in only one physical Availability Zone; if that AZ suffers physical destruction, data cannot be recovered</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> S3 One Zone-IA takes 5 hours to retrieve files</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> S3 One Zone-IA cannot be encrypted</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> S3 One Zone-IA limits file sizes to 1 MB</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> One Zone-IA saves 20% on storage by foregoing Multi-AZ replication. It is suitable only for easily reproducible data (like image thumbnails), not primary backups.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 14 • EBS Instance Store Contrast</div>
      <div class="mcq-q">What distinguishing characteristic separates an EC2 Instance Store volume from an Amazon EBS volume?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Instance Store volumes are stored on magnetic tape</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Instance Store volumes are ephemeral NVMe SSDs physically attached to the host server; all data is lost if the instance is stopped or terminated</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Instance Store volumes can be detached and attached to other instances</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Instance Store volumes are slower than EBS</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Instance Store provides ultra-high IOPS local storage, but is ephemeral: data does not survive instance stop/termination events. EBS is network-attached and persistent.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="C">
      <div class="mcq-num">Question 15 • CloudFront Origin Shield</div>
      <div class="mcq-q">What is the purpose of enabling Amazon CloudFront Origin Shield?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Encrypts web pages with user passwords</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Translates website code to WebAssembly</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Acts as a centralized caching layer that consolidates cache misses from hundreds of global edge locations, minimizing requests to the origin backend</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Blocks all traffic from outside the United States</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Origin Shield adds a designated centralized regional caching layer, reducing origin load by up to 99% during traffic spikes.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="D">
      <div class="mcq-num">Question 16 • S3 Transfer Acceleration</div>
      <div class="mcq-q">How does Amazon S3 Transfer Acceleration accelerate file uploads from global clients to an S3 bucket in a distant region?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By compressing all files using Gzip</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By converting TCP traffic into UDP packets</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By skipping file checksum validation</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Clients upload to the nearest AWS Edge Location via Anycast BGP; data then travels over the optimized private AWS global fiber backbone to the target S3 bucket</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> S3 Transfer Acceleration routes uploads into the closest AWS Edge Location, routing across Amazon's private dark fiber backbone to bypass public internet congestion.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 17 • S3 Glacier Retrieval Speeds</div>
      <div class="mcq-q">Which retrieval tier allows an engineer to retrieve emergency data from Amazon S3 Glacier Flexible Retrieval within 1 to 5 minutes?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Expedited Retrieval</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Standard Retrieval</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Bulk Retrieval</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Instant Retrieval</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Expedited Retrieval delivers Glacier Flexible objects in 1-5 minutes for urgent operational recoveries (Standard takes 3-5 hours; Bulk takes 5-12 hours).
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 18 • EBS Multi-Attach Limitation</div>
      <div class="mcq-q">What filesystem requirement is mandatory when mounting an EBS volume to multiple EC2 instances concurrently using EBS Multi-Attach?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Standard NTFS filesystem</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> A cluster-aware filesystem (e.g. GFS2 or OCFS2) to prevent concurrent write corruption</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> FAT32 filesystem</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> ext4 without journaling</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Standard filesystems (ext4/NTFS) are not cluster-aware; multiple hosts writing concurrently will corrupt metadata. Multi-Attach requires cluster filesystems like GFS2.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="C">
      <div class="mcq-num">Question 19 • S3 Replication Architecture</div>
      <div class="mcq-q">What prerequisite must be enabled on BOTH source and destination Amazon S3 buckets before configuring Cross-Region Replication (CRR)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> S3 Transfer Acceleration</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> S3 Object Lock</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> S3 Versioning</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> S3 Static Website Hosting</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> S3 Cross-Region and Same-Region Replication require S3 Versioning to be explicitly enabled on both source and destination buckets to track version states.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="D">
      <div class="mcq-num">Question 20 • S3 Maximum Single Object Size</div>
      <div class="mcq-q">What is the absolute maximum file size of a single object stored in Amazon S3?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 5 GB</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 100 GB</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 1 TB</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 5 TB (Terabytes)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The maximum size of an individual object in S3 is 5 TB (uploaded via Multipart Upload). The maximum size in a single PUT operation is 5 GB.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 21 • FSx for Windows Active Directory</div>
      <div class="mcq-q">How does Amazon FSx for Windows File Server integrate with enterprise security infrastructure?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Integrates natively with Microsoft Active Directory to enforce Windows NTFS ACLs, DFS Namespaces, and SMB protocol access</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Uses Linux PAM passwords</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Requires users to authenticate via SMS</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Bypasses all security policies</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> FSx for Windows integrates with AWS Managed Microsoft AD or on-premises AD domains, supporting standard Windows NTFS permissions and SMB encryption.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 22 • CloudFront Signed URLs vs Cookies</div>
      <div class="mcq-q">When should an architect select CloudFront Signed Cookies rather than Signed URLs to restrict access to paid streaming media?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> When streaming to smart watches</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> When providing access to multiple restricted files (e.g. an entire HLS video stream with hundreds of `.ts` segments) without modifying individual URL links</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> When caching HTML files</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Signed Cookies are obsolete</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Signed URLs work well for single download links. Signed Cookies grant access to an entire directory of streaming chunks (HLS/DASH) without rewriting video manifests.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="C">
      <div class="mcq-num">Question 23 • S3 Event Notifications</div>
      <div class="mcq-q">Which target destinations can receive automated event notifications when a new object is created (`s3:ObjectCreated:*`) in an S3 bucket?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> EC2 BIOS registers</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Windows Event Log only</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Amazon SNS topics, Amazon SQS queues, AWS Lambda functions, and Amazon EventBridge</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Local desktop printer</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> S3 Event Notifications publish object events directly to SNS, SQS, Lambda, or EventBridge to trigger automated serverless processing pipelines.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="D">
      <div class="mcq-num">Question 24 • EBS Volume Encryption</div>
      <div class="mcq-q">When an Amazon EBS volume is encrypted using AWS KMS, what data is protected?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Data at rest inside the volume only</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Data in transit between the volume and the EC2 instance only</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> All snapshots created from the volume only</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Data at rest, data in flight between host and volume, all disk snapshots, and all volumes created from those snapshots</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> EBS encryption transparently protects data at rest, data moving across PCIe to the Nitro Card, all snapshots, and all derivative volumes.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 25 • S3 Batch Operations</div>
      <div class="mcq-q">Which AWS feature enables executing large-scale batch tasks (such as copying billions of objects, replacing metadata tags, or altering ACLs) across exabytes of S3 data?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> S3 Batch Operations</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> S3 Simple Upload</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Snowball</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> EC2 Auto Scaling</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> S3 Batch Operations executes bulk actions across billions of objects specified in an S3 inventory list with automated progress tracking and completion reports.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 26 • S3 Access Points</div>
      <div class="mcq-q">How do S3 Access Points simplify access governance for large shared data lakes with hundreds of distinct application teams?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By turning S3 into a relational SQL database</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By creating unique DNS hostnames with dedicated IAM policies tailored to specific applications or VPCs instead of managing a single monolithic bucket policy</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By doubling data download speeds</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Access points make passwords unnecessary</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> S3 Access Points decompose complex thousands-line bucket policies into modular, application-specific endpoints with distinct IAM and network restrictions.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="C">
      <div class="mcq-num">Question 27 • EFS Storage Tiers</div>
      <div class="mcq-q">What feature automatically transitions files in Amazon EFS that haven't been accessed for 30 days to an Infrequent Access storage tier to reduce costs by 92%?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> EFS Snapshots</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> EFS Replication</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> EFS Lifecycle Management</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> EFS Elastic Throughput</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> EFS Lifecycle Management transparently migrates cold files to the EFS Infrequent Access tier while retaining seamless POSIX file access for users.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="D">
      <div class="mcq-num">Question 28 • CloudFront Geo-Restriction</div>
      <div class="mcq-q">How can a media streaming company prevent users located outside approved distribution countries from accessing licensed content via CloudFront?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By deleting the S3 bucket</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By changing the domain name weekly</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By asking users to self-report their location</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Using CloudFront Geographic Restriction (Geo-Blocking) with an Allowlist or Blocklist based on client IP GeoIP location lookup</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> CloudFront evaluates the client IP against a GeoIP database at the edge, returning an HTTP 403 Forbidden to unauthorized geographic locations.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="A">
      <div class="mcq-num">Question 29 • EBS Fast Snapshot Restore (FSR)</div>
      <div class="mcq-q">What performance problem does EBS Fast Snapshot Restore (FSR) eliminate when restoring new EBS volumes from S3 snapshots?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Eliminates the initial I/O latency penalty ("lazy loading") by pre-warming all volume blocks into the storage tier immediately</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Prevents the volume from being deleted</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Doubles the size of the hard drive for free</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Converts HDD volumes to SSD</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Standard restored EBS volumes lazy-load blocks from S3 upon first read, incurring high latency. FSR pre-warms all blocks, delivering full IOPS immediately.
      </div>
    </div>

    <div class="mcq-card" data-unit="C3" data-correct="B">
      <div class="mcq-num">Question 30 • S3 Strong Read-After-Write Consistency</div>
      <div class="mcq-q">As of December 2020, what consistency model does Amazon S3 guarantee for PUT and DELETE requests of objects across all AWS Regions?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Eventual consistency (requiring seconds for changes to propagate)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Strong Read-After-Write Consistency for all PUTs, LISTs, and DELETEs</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Causal consistency only</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Inconsistent reads unless cache is flushed</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> S3 delivers strong read-after-write consistency automatically with zero performance penalty. Immediately after a successful write, any read returns the latest object.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 03 Conceptual Questions</span>
    <span>Unit 03 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 3 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-c3">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 03</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">25.</span> Unit 3 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted explanations of object vs block storage, multi-part parallel ingestion, and distributed filesystem semantics.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Contrast Object Storage (Amazon S3) and Block Storage (Amazon EBS) regarding addressing, update mechanics, and operational targets.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Object Storage (S3):</strong> Treats data as complete, indivisible objects referenced by a URL key within a flat namespace. Supports rich customizable metadata. Modifying a single byte requires rewriting the <em>entire object</em>. Scales infinitely to exabytes and is accessed over HTTP/HTTPS REST APIs.</p>
        <p><strong>Block Storage (EBS):</strong> Divides storage into raw 512-byte or 4KB sectors (blocks) without metadata. Operating systems format volumes with native filesystems (NTFS/ext4) and can alter individual bytes directly with sub-millisecond random I/O latency. Bound to a single instance in a specific AZ; ideal for transactional database engines and OS root drives.</p>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Explain how S3 Multipart Upload achieves high throughput and network resiliency for multi-gigabyte video files.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Parallelization:</strong> S3 Multipart Upload chunks large files into parts (5 MB to 5 GB each). Instead of serial upload over a single TCP connection, client workers upload dozens of chunks concurrently over parallel sockets, saturating high-bandwidth connections.</p>
        <p><strong>Failure Isolation:</strong> Over unstable long-haul networks, single-stream uploads frequently drop at 98%, forcing a full restart. With Multipart Upload, if a single chunk fails due to packet loss, only that specific chunk is retried. S3 verifies individual chunk MD5 hashes, reassembles the file into a unified object, and generates a composite multipart ETag.</p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> Detail the operational difference between S3 Object Lock Compliance Mode and Governance Mode.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Governance Mode:</strong> Protects objects from accidental deletion by standard users. However, users granted the special `s3:BypassGovernanceRetention` IAM permission can alter retention periods or delete versions if authorized.</p>
        <p><strong>Compliance Mode:</strong> Enforces strict Write-Once-Read-Many (WORM) immutability. <strong>No user in the organization, including the AWS Account Root User, can delete the object or decrease its retention period until time expires</strong>. AWS Support cannot bypass it. Mandated for legal and financial compliance (SEC Rule 17a-4).</p>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> How does Amazon EBS gp3 decouple IOPS and throughput from volume capacity, and why is this financially advantageous over gp2?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>Under legacy `gp2`, IOPS were locked to size at 3 IOPS per GiB. A database requiring 3,000 IOPS forced the customer to provision a 1,000 GiB volume, resulting in massive wasted spend on unneeded storage capacity.</p>
        <p>Under `gp3`, every volume receives 3,000 IOPS and 125 MB/s baseline throughput for free. If higher performance is needed, administrators can independently provision up to 16,000 IOPS and 1,000 MB/s on a small 50 GiB disk. This decoupling allows precise workload tailoring and cuts average EBS monthly costs by up to 20-40%.</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> Contrast Amazon EFS and Amazon FSx for Lustre regarding protocol, architecture, and optimal computing workloads.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Amazon EFS:</strong> Serverless NFSv4 filesystem built for general-purpose Linux workloads. Synchronously replicates across multiple Availability Zones, offering high durability and automatic growth to petabytes. Ideal for web content management (WordPress), developer home directories, and container shared storage.</p>
        <p><strong>Amazon FSx for Lustre:</strong> High-performance parallel filesystem designed for compute-heavy batch workloads. Provides sub-millisecond latencies, hundreds of gigabytes/second throughput, and millions of IOPS. Links directly to S3 data lakes to ingest datasets for High-Performance Computing (HPC), machine learning training, and financial simulations.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 03 Analytical Problems</span>
    <span>Unit 03 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 3 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-c3">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 03</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">26.</span> Unit 3 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Complex enterprise storage incident triage, S3 bucket leak remediation, and high-performance EBS volume optimization scenarios.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Storage Incident Triage: Lazy-Loading Latency Spike on Newly Restored 10TB EBS Database Volume</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> During a disaster recovery drill, a systems team restores a 10TB production PostgreSQL database from an EBS snapshot onto a brand-new `gp3` volume. When launching the database, query latencies spike to 3,500 milliseconds (normally 4 ms), database connections pool and time out, and disk queue depth exceeds 200 despite provisioning 12,000 IOPS.</p>
        <p><strong>Root Cause Analysis &amp; Resolution:</strong></p>
        <ol>
          <li><strong>The Lazy-Loading (Hydration) Penalty:</strong> EBS snapshots are stored in Amazon S3. When an EBS volume is created from a snapshot, storage blocks are <em>not</em> pre-copied to the physical SAN drives; instead, metadata pointers are created instantly. When the database reads a disk block for the first time, the block must be pulled over the network from S3 ("lazy loading"), causing an initial 50-100 ms latency spike per block!</li>
          <li><strong>Immediate Manual Pre-Warming:</strong> To force block hydration immediately without waiting for database queries to hit cold blocks, execute a raw sequential read across the entire volume in Linux:
            <br><code>sudo dd if=/dev/xvdf of=/dev/null bs=1M status=progress</code>
            <br>This forces the hypervisor to fetch every block from S3 immediately.
          </li>
          <li><strong>Architectural Permanent Fix:</strong> Enable <strong>EBS Fast Snapshot Restore (FSR)</strong> on critical database snapshots. FSR pre-warms all volume blocks into the EBS storage tier in advance, eliminating the hydration penalty completely and delivering 100% full provisioned IOPS from the very first second of restoration.</li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> Security Incident Response: Remediating an Actively Leaking Public S3 Data Lake</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A threat intelligence monitoring vendor alerts an enterprise that sensitive customer financial PDF statements stored in an S3 bucket (`corp-finance-datalake`) are being actively downloaded by unauthorized external IP addresses via direct web links.</p>
        <p><strong>Emergency Incident Response Protocol:</strong></p>
        <ul>
          <li><strong>Step 1: Immediate Blast Radius Containment:</strong> Open AWS Management Console &rarr; S3 &rarr; <em>Block Public Access (account settings)</em>. Toggle <strong>Block all public access</strong> ON at the account level. This immediately overrides all permissive bucket policies, object ACLs, and bucket ACLs, severing all external public downloads in under 3 seconds.</li>
          <li><strong>Step 2: Root Cause Investigation:</strong> Inspect bucket policy: an engineer had pasted an overly permissive policy granting `Principal: "*"` on `Action: "s3:GetObject"`. In addition, multiple objects had public-read ACLs stamped during programmatic SDK uploads.</li>
          <li><strong>Step 3: Enforce S3 Object Ownership:</strong> Set Object Ownership to <strong>Bucket owner enforced</strong>. This permanently disables Access Control Lists (ACLs) entirely, making IAM and Bucket Policies the exclusive authority over access permissions.</li>
          <li><strong>Step 4: Threat Forensics via CloudTrail &amp; Athena:</strong> Query CloudTrail Data Events in Amazon Athena to extract all external IP addresses that executed `s3:GetObject` over the preceding 30 days to quantify exfiltration scope and notify regulatory bodies.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> Lifecycle Cost Optimization: Designing an Archival Architecture for a 50-Petabyte Medical Imaging Archive</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>System Engineering Request:</strong> A national healthcare network generates 2 Petabytes of MRI and CT scan DICOM images monthly (total current storage: 50 PB). Raw S3 Standard storage costs $1,150,000/month ($0.023/GB). Access pattern analysis reveals: 90% of accesses occur in the first 30 days; 9% occur between days 31-90; beyond 90 days, retrieval occurs only during legal malpractice audits (average 2 retrievals/year).</p>
        <p><strong>Optimized Lifecycle Architecture:</strong></p>
        <ul>
          <li><strong>Day 0 to 30 (S3 Standard):</strong> Active diagnosis window. Sub-second immediate retrieval across multiple AZs. Cost: $0.023/GB.</li>
          <li><strong>Day 31 to 90 (S3 Standard-IA):</strong> Follow-up appointments. Transition via Lifecycle rule: cost drops to $0.0125/GB (45% reduction).</li>
          <li><strong>Day 91+ (S3 Glacier Deep Archive):</strong> Medical legal retention mandate (7 years). Transition to Deep Archive: cost drops to <strong>$0.00099/GB/month (95.7% reduction!)</strong>.</li>
          <li><strong>Financial Impact:</strong> Monthly storage bill for 50 PB drops from $1,150,000/month down to approximately <strong>$65,000/month</strong>, achieving over $13,000,000 in annual cloud infrastructure savings.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> Legacy Modernization: Transitioning an On-Premises SAN to Amazon FSx for NetApp ONTAP</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Engineering Challenge:</strong> An enterprise datacenter contract expires in 6 months. Their core applications rely heavily on specialized NetApp storage features: SMB/NFS multi-protocol access, volume cloning (FlexClone), block deduplication, and automated snapshots (NetApp SnapMirror). Migrating to standard S3 or EBS would require completely rewriting application storage code.</p>
        <p><strong>Solution Architecture:</strong></p>
        <ul>
          <li>Deploy <strong>Amazon FSx for NetApp ONTAP</strong> in a Multi-AZ deployment.</li>
          <li>Establish a continuous data replication pipeline from on-premises NetApp arrays to FSx ONTAP using native <strong>NetApp SnapMirror</strong> over an AWS Direct Connect link.</li>
          <li>Because FSx for NetApp ONTAP exposes identical ONTAP APIs, applications mount cloud file shares using standard NFS and SMB protocols with zero code changes.</li>
          <li>Enable automatic tiering: inactive snapshot blocks transparently shift to the low-cost capacity pool tier, slashing cloud storage costs while preserving sub-millisecond primary SSD performance.</li>
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
<article class="doc-page" id="mcq-answer-key-c3">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 03</span>
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
        <tr><td>01</td><td><strong style="color:var(--primary);">C</strong></td><td>S3 Standard eleven 9's durability rating (99.999999999%)</td><td>16</td><td><strong style="color:var(--primary);">D</strong></td><td>S3 Transfer Acceleration edge ingress via Anycast</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">A</strong></td><td>S3 Glacier Deep Archive lowest cost archival tier</td><td>17</td><td><strong style="color:var(--primary);">A</strong></td><td>Glacier Expedited retrieval delivery within 1-5 minutes</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">D</strong></td><td>Multipart Upload mandated &gt;5GB and recommended &gt;100MB</td><td>18</td><td><strong style="color:var(--primary);">B</strong></td><td>EBS Multi-Attach cluster filesystem (GFS2) requirement</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">B</strong></td><td>EBS gp3 baseline performance (3,000 IOPS &amp; 125 MB/s)</td><td>19</td><td><strong style="color:var(--primary);">C</strong></td><td>S3 Versioning requirement on source and destination for CRR</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">A</strong></td><td>Amazon EFS concurrent Multi-AZ POSIX NFS mounting</td><td>20</td><td><strong style="color:var(--primary);">D</strong></td><td>S3 maximum individual object size limit (5 Terabytes)</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">C</strong></td><td>EBS io2 Block Express max IOPS limit (256,000 IOPS)</td><td>21</td><td><strong style="color:var(--primary);">A</strong></td><td>FSx for Windows native Active Directory &amp; SMB integration</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">B</strong></td><td>S3 Intelligent-Tiering automatic tier shifting without fees</td><td>22</td><td><strong style="color:var(--primary);">B</strong></td><td>CloudFront Signed Cookies for multiple streaming files</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">D</strong></td><td>S3 Object Lock Compliance Mode WORM root immunity</td><td>23</td><td><strong style="color:var(--primary);">C</strong></td><td>S3 Event Notifications destinations (SNS, SQS, Lambda)</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">A</strong></td><td>Amazon FSx for Lustre sub-millisecond parallel HPC</td><td>24</td><td><strong style="color:var(--primary);">D</strong></td><td>EBS encryption protecting rest, in-transit, and snapshots</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">B</strong></td><td>S3 Versioning Delete Marker insertion behavior</td><td>25</td><td><strong style="color:var(--primary);">A</strong></td><td>S3 Batch Operations large-scale multi-object actions</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">C</strong></td><td>Tape Gateway replacing physical VTL magnetic tape libraries</td><td>26</td><td><strong style="color:var(--primary);">B</strong></td><td>S3 Access Points modular application-specific endpoints</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">D</strong></td><td>EBS snapshot incremental 512KB changed block storage</td><td>27</td><td><strong style="color:var(--primary);">C</strong></td><td>EFS Lifecycle Management transitioning cold files to IA</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">A</strong></td><td>S3 One Zone-IA single-facility failure data loss risk</td><td>28</td><td><strong style="color:var(--primary);">D</strong></td><td>CloudFront Geo-Restriction GeoIP access filtering</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">B</strong></td><td>EC2 Instance Store local NVMe ephemeral volatility</td><td>29</td><td><strong style="color:var(--primary);">A</strong></td><td>Fast Snapshot Restore eliminating lazy-loading hydration lag</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">C</strong></td><td>CloudFront Origin Shield consolidating edge cache misses</td><td>30</td><td><strong style="color:var(--primary);">B</strong></td><td>S3 Strong Read-After-Write Consistency across all regions</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 03 Complete • Next: Unit 04 Cloud Networking & VPC</span>
    <span>Unit 03 • Page 09</span>
  </div>
</article>
"""
