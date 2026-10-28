# -*- coding: utf-8 -*-
"""
Cloud Administration (AWS) - Unit 5: Cloud Databases & Big Data Analytics
Master Gold Standard Layout:
- c5-rds: Amazon RDS Multi-AZ Synchronous Replication vs Read Replicas
- c5-aurora: Amazon Aurora Distributed Architecture (4-of-6 Quorum, Serverless v2)
- c5-dynamo: Amazon DynamoDB (Consistent Hashing, RCUs/WCUs, Global Tables)
- c5-cache: Amazon ElastiCache (Redis vs Memcached) & In-Memory Strategies
- c5-bigdata: Amazon Redshift Columnar MPP, Athena & AWS Glue Data Catalog
- practice-mcq-c5: 30 MCQs with dynamic scoring
- practice-subj-short-c5: 5 Short Conceptual Sets
- practice-subj-long-c5: 4 Deep Analytical Scenarios
- mcq-answer-key-c5: Master Answer Key Table
"""

CLOUD_UNIT5_HTML = """
<!-- ==========================================================================
     UNIT 05: CLOUD DATABASES & BIG DATA ANALYTICS
     ========================================================================== -->

<!-- Page 1: Amazon RDS Overview -->
<article class="doc-page" id="c5-rds">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">37.</span> Amazon Relational Database Service (RDS): Multi-AZ vs Read Replicas
  </h2>

  <p class="lead-para">
    Amazon RDS automates the administrative overhead of relational database deployment, operating system patching, storage scaling, automated backup retention, and disaster failover across PostgreSQL, MySQL, MariaDB, Oracle, and Microsoft SQL Server engines.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Architectural Property</th>
          <th>RDS Multi-AZ Deployment</th>
          <th>RDS Read Replicas</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Primary Operational Goal</strong></td>
          <td><strong style="color:var(--primary);">High Availability &amp; Disaster Recovery</strong> (Zero data loss SLA)</td>
          <td><strong style="color:var(--accent-purple);">Read Scalability &amp; Query Offloading</strong> (OLAP reporting)</td>
        </tr>
        <tr>
          <td><strong>Replication Mechanism</strong></td>
          <td><strong>Synchronous Physical Block-Level Replication</strong> (Committed to standby storage before write returns OK)</td>
          <td><strong>Asynchronous Logical Engine Replication</strong> (Subject to replication lag of milliseconds to seconds)</td>
        </tr>
        <tr>
          <td><strong>Active Database Endpoints</strong></td>
          <td><strong>Single DNS Endpoint:</strong> Traffic routes strictly to Primary; Standby is warm but passive and cannot receive reads.</td>
          <td><strong>Independent DNS Endpoints:</strong> Applications can directly query each replica independently (up to 15 replicas).</td>
        </tr>
        <tr>
          <td><strong>Failover Behavior</strong></td>
          <td><strong>Automatic DNS CNAME failover</strong> flips to Standby in 60-120 seconds with zero data loss (RPO = 0).</td>
          <td>Manual or scripted promotion to standalone database; breaks replication relationship.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Amazon Aurora Distributed Quorum</span>
    <span>Unit 05 • Page 01</span>
  </div>
</article>

<!-- Page 2: Amazon Aurora -->
<article class="doc-page" id="c5-aurora">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 02</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">38.</span> Amazon Aurora Distributed Architecture, 4-of-6 Storage Quorum &amp; Serverless v2
  </h2>

  <p class="lead-para">
    Amazon Aurora completely reimagines relational database architecture for the cloud by cleanly decoupling the SQL processing compute tier from the underlying distributed storage subsystem.
  </p>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="layers"></i> Distributed Storage Physics: The 4-of-6 Quorum Model</div>
    <p>
      In traditional databases, the database engine writes full dirty pages, doublewrite buffers, and WAL logs to disk. <strong>Aurora writes only redo log records over the network to a shared, cluster-wide distributed storage fleet:</strong>
    </p>
    <ul>
      <li><strong>6-Way Mirroring Across 3 AZs:</strong> Every 10 GB segment of database volume is replicated 6 times across 3 distinct Availability Zones (2 copies per AZ).</li>
      <li><strong>Write Quorum (4-of-6):</strong> A transaction is committed and acknowledged to the client as soon as <strong>4 out of the 6 storage nodes</strong> acknowledge persisting the redo log. An entire Availability Zone can physically disappear, plus one additional storage node can crash, and Aurora continues writing with zero data loss!</li>
      <li><strong>Read Quorum (3-of-6):</strong> Reads require agreement from only 3 nodes. The compute head reads directly from local storage nodes; background peer-to-peer gossip algorithms repair lagging nodes asynchronously without compute intervention.</li>
      <li><strong>15 Millisecond Read Replicas:</strong> Because all compute instances mount the exact same shared virtual storage volume, Aurora Read Replicas do not replicate disk blocks. Replica lag is typically <strong>under 15 milliseconds</strong>!</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: Amazon DynamoDB NoSQL Architecture</span>
    <span>Unit 05 • Page 02</span>
  </div>
</article>

<!-- Page 3: Amazon DynamoDB -->
<article class="doc-page" id="c5-dynamo">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 03</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">39.</span> Amazon DynamoDB: Consistent Hashing, Primary Keys &amp; Global Tables
  </h2>

  <p class="lead-para">
    Amazon DynamoDB is a fully managed, serverless, key-value and document NoSQL database engineered to deliver single-digit millisecond latency at any scale, supporting workloads processing trillions of requests per day.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Architectural Component</th>
          <th>Implementation Mechanics</th>
          <th>Operational Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Partition Key (Hash Key)</strong></td>
          <td>Input attribute is passed to an internal MD5-based cryptographic hash function to determine the exact physical storage partition holding the item.</td>
          <td>Requires high-cardinality keys (e.g. `user_id`, `uuid`) to prevent <em>hot partitions</em> where one node is overloaded.</td>
        </tr>
        <tr>
          <td><strong>Sort Key (Range Key)</strong></td>
          <td>Stores items sharing the same Partition Key in sorted physical order on disk (e.g. `timestamp`, `event_id`).</td>
          <td>Enables rich range queries (`begins_with`, `between`, `&gt;`, `&lt;`) within a single partition.</td>
        </tr>
        <tr>
          <td><strong>Global Secondary Index (GSI)</strong></td>
          <td>Creates an entirely new Partition Key and optional Sort Key; asynchronously replicates data from the base table.</td>
          <td>Can be created and deleted dynamically at any time; queries span the entire table.</td>
        </tr>
        <tr>
          <td><strong>Local Secondary Index (LSI)</strong></td>
          <td>Shares the base table's Partition Key, but specifies a different Sort Key.</td>
          <td><strong>Must be created at table creation time!</strong> Cannot be added or removed later; capped at 10 GB per partition key.</td>
        </tr>
        <tr>
          <td><strong>DynamoDB Global Tables</strong></td>
          <td>Multi-region, multi-active fully managed replication based on DynamoDB Streams.</td>
          <td>Delivers local single-digit millisecond read/write latency globally with automatic conflict resolution using Last-Writer-Wins.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: In-Memory Caching (ElastiCache)</span>
    <span>Unit 05 • Page 03</span>
  </div>
</article>

<!-- Page 4: Amazon ElastiCache -->
<article class="doc-page" id="c5-cache">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 04</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">40.</span> In-Memory Caching: Amazon ElastiCache (Redis OSS vs Memcached)
  </h2>

  <p class="lead-para">
    In-memory caching layers mitigate database bottlenecks by storing frequently queried database rows, user session tokens, and computed results in volatile high-speed DRAM, accelerating response times to sub-millisecond levels.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Feature Capability</th>
          <th>Amazon ElastiCache for Redis</th>
          <th>Amazon ElastiCache for Memcached</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Data Structures Supported</strong></td>
          <td>Rich native types: Strings, Hashes, Lists, Sets, Sorted Sets, Bitmaps, HyperLogLogs, Geospatial indexes</td>
          <td>Simple Key-Value strings only</td>
        </tr>
        <tr>
          <td><strong>Data Persistence</strong></td>
          <td>Supports AOF (Append-Only File) and RDB (point-in-time disk snapshots) to Amazon S3</td>
          <td>None (Purely volatile in-memory; restart flushes all data)</td>
        </tr>
        <tr>
          <td><strong>Replication &amp; Multi-AZ</strong></td>
          <td>Multi-AZ with automatic failover across read replicas</td>
          <td>Zero replication (Sharded stateless nodes)</td>
        </tr>
        <tr>
          <td><strong>Pub/Sub &amp; Streams</strong></td>
          <td>Native Pub/Sub messaging and streaming primitives</td>
          <td>None</td>
        </tr>
        <tr>
          <td><strong>Multi-Threading Architecture</strong></td>
          <td>Single-threaded core event loop (optimized for sub-millisecond execution)</td>
          <td>Multi-threaded (Scales efficiently across large multi-core CPU instances)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Big Data & Analytics (Redshift, Athena)</span>
    <span>Unit 05 • Page 04</span>
  </div>
</article>

<!-- Page 5: Redshift & Big Data -->
<article class="doc-page" id="c5-bigdata">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 05 • Page 05</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">41.</span> Big Data Analytics: Amazon Redshift Columnar MPP, Athena &amp; AWS Glue
  </h2>

  <p class="lead-para">
    Petabyte-scale analytical querying requires specialized columnar storage formatting and Massively Parallel Processing (MPP) architectures to aggregate billions of rows without locking transactional databases.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Analytics Service</th>
          <th>Query Engine Architecture</th>
          <th>Data Storage Location</th>
          <th>Primary Analytical Target</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Amazon Redshift</strong></td>
          <td>Massively Parallel Processing (MPP) cluster with Leader Node coordinating distributed Compute Nodes; columnar disk compression</td>
          <td>Managed local NVMe cache + Redshift Managed Storage (RMS) on S3</td>
          <td>Complex enterprise data warehousing, business intelligence reporting, continuous SQL analytics</td>
        </tr>
        <tr>
          <td><strong>Amazon Athena</strong></td>
          <td>Serverless interactive query service powered by open-source Presto and Trino; billed per TB scanned</td>
          <td>Directly queries raw files (Parquet, ORC, JSON, CSV) residing in Amazon S3 buckets</td>
          <td>Ad-hoc log investigation, CloudTrail/VPC Flow log security auditing, serverless data lake querying</td>
        </tr>
        <tr>
          <td><strong>AWS Glue</strong></td>
          <td>Serverless ETL (Extract, Transform, Load) service running Apache Spark + Central Data Catalog</td>
          <td>Discovers and catalogs metadata schemas across S3, RDS, and DynamoDB</td>
          <td>Building automated data pipelines, schema crawlers, and preparing data for analytical consumption</td>
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
<article class="doc-page" id="practice-mcq-c5">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreC5">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">42.</span> Unit 05 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Test your mastery of relational multi-AZ engines, Amazon Aurora distributed quorums, DynamoDB consistent hashing, and big data analytical pipelines.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 01 • RDS Multi-AZ Replication Mode</div>
      <div class="mcq-q">What replication mechanism is utilized between the primary database and the standby database in an Amazon RDS Multi-AZ deployment?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Asynchronous logical SQL statement replication</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Synchronous physical block-level storage replication</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Daily snapshot restores</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> S3 cross-region copy</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> RDS Multi-AZ uses synchronous physical block-level replication, guaranteeing that writes are persisted on standby storage before returning success (RPO = 0).
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 02 • Aurora Storage Quorum</div>
      <div class="mcq-q">How many storage copies does Amazon Aurora maintain across how many Availability Zones, and how many copies are required for a write quorum?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 2 copies across 2 AZs (2-of-2 write quorum)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 3 copies across 3 AZs (2-of-3 write quorum)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 6 copies across 3 AZs (4-of-6 write quorum; 3-of-6 read quorum)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 10 copies across 5 AZs (5-of-10 write quorum)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Aurora replicates every 10GB segment 6 times across 3 AZs. A write commits as soon as 4 of the 6 nodes acknowledge persisting the redo log.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="C5" data-correct="A">
      <div class="mcq-num">Question 03 • DynamoDB Consistent Hashing</div>
      <div class="mcq-q">What does Amazon DynamoDB use to determine which physical storage partition will store an item?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> A cryptographic hash function applied to the item's Partition Key</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The date and time the item was uploaded</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The physical size of the JSON document</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Random selection across server hard drives</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> DynamoDB hashes the Partition Key value (using an internal MD5-derived hash), directing the item to the specific partition holding that hash range.
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="C5" data-correct="D">
      <div class="mcq-num">Question 04 • ElastiCache Redis Feature Set</div>
      <div class="mcq-q">Which capability is supported by Amazon ElastiCache for Redis that is NOT supported by Memcached?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> In-memory caching of strings</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Sub-millisecond latency</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> VPC security group isolation</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Complex data structures (Lists, Sets, Sorted Sets), disk persistence (RDB/AOF), and Multi-AZ automatic failover</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Redis provides rich data structures, disk persistence snapshots, and automated Multi-AZ failover. Memcached is a pure volatile multi-threaded memory buffer.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 05 • Columnar Storage Advantage</div>
      <div class="mcq-q">Why does Amazon Redshift's columnar storage architecture execute analytical aggregate queries (such as `SUM(revenue)`) orders of magnitude faster than row-based databases?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Redshift does not use computer memory</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It only reads the specific requested column off disk, skipping all other columns and achieving massive compression on uniform data types</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It deletes old rows automatically</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It requires users to write queries in Java</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Row-oriented databases must read every column of every row into memory. Columnar databases read only the target column, minimizing disk I/O drastically.
      </div>
    </div>

    <!-- Q6 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 06 • DynamoDB Strongly Consistent Reads</div>
      <div class="mcq-q">How does requesting a Strongly Consistent Read impact Read Capacity Unit (RCU) consumption in Amazon DynamoDB for a 4KB item?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Consumes 0.5 RCUs</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Consumes 4 RCUs</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Consumes 1 full RCU (compared to 0.5 RCU for Eventually Consistent Read)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Strongly consistent reads are free</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> An Eventually Consistent Read costs 0.5 RCU per 4KB. A Strongly Consistent Read queries two nodes to guarantee the latest data, consuming 1 full RCU per 4KB.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="A">
      <div class="mcq-num">Question 07 • RDS Read Replica Scaling</div>
      <div class="mcq-q">How many read replicas can be provisioned for a single Amazon RDS PostgreSQL database instance?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Up to 15 read replicas</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Exactly 1 read replica</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 50 read replicas</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Unlimited replicas</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Amazon RDS supports up to 15 read replicas per primary DB instance (and Aurora supports up to 15 Aurora replicas across the shared storage cluster).
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="D">
      <div class="mcq-num">Question 08 • DynamoDB Local Secondary Index Constraint</div>
      <div class="mcq-q">What is the critical architectural constraint when creating a Local Secondary Index (LSI) on an Amazon DynamoDB table?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> LSIs cannot be used on tables larger than 1 MB</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> LSIs only work on Tuesdays</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> LSIs require an EC2 instance to run</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> An LSI can ONLY be defined at the exact moment the table is created; it can never be added, modified, or dropped later</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> LSIs must be defined at initial table creation time. Global Secondary Indexes (GSIs), by contrast, can be added and removed dynamically at any time.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 09 • Amazon Athena Pricing Model</div>
      <div class="mcq-q">How is an enterprise billed when executing interactive SQL queries against S3 data using Amazon Athena?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Billed based on the number of rows returned in the result</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Billed per Terabyte (TB) of data scanned by the query ($5.00 per TB scanned)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Fixed monthly server maintenance charge</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Billed per second of query runtime</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Athena charges $5.00 per TB of data scanned. Converting raw JSON/CSV files into columnar Apache Parquet format cuts costs by 90% by reducing scanned bytes.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 10 • Aurora Serverless v2 Scaling Unit</div>
      <div class="mcq-q">What unit of scaling does Amazon Aurora Serverless v2 use to scale compute capacity dynamically in sub-second intervals?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> vCPUs</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Gigabytes</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Aurora Capacity Units (ACUs), where 1 ACU provides approximately 2 GiB of memory and corresponding compute</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> EC2 credits</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Aurora Serverless v2 scales up and down instantly in fine-grained increments of 0.5 ACUs (each ACU = ~2 GiB RAM + CPU/networking).
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="A">
      <div class="mcq-num">Question 11 • DynamoDB Hot Partition Trap</div>
      <div class="mcq-q">Which attribute choice would cause a catastrophic "hot partition" bottleneck in a high-throughput Amazon DynamoDB table?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Using a low-cardinality status field like `status` with values "active" or "inactive" as the Partition Key</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Using a randomly generated UUID4 as the Partition Key</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Using a composite key of `CustomerId` and `Timestamp`</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Using device MAC addresses</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Partition keys require high cardinality. If a low-cardinality key like "active" is used, all 100,000 writes/sec hash to the same physical node, exceeding partition throughput limits.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="D">
      <div class="mcq-num">Question 12 • AWS Glue Data Catalog Role</div>
      <div class="mcq-q">What is the primary role of the AWS Glue Data Catalog in a serverless data lake architecture?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> It acts as a hard drive for EC2 instances</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> It sends billing invoices to accounting</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It installs MySQL on physical servers</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Acts as a central persistent metadata repository (Apache Hive compatible) storing table schemas, partition definitions, and data types across S3 data lakes</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The Glue Data Catalog stores schema metadata, allowing query engines (Athena, Redshift Spectrum, EMR) to query flat S3 files as structured relational tables.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 13 • Lazy Loading (Cache-Aside) Strategy</div>
      <div class="mcq-q">In a Lazy Loading (Cache-Aside) caching architecture, what happens when an application requests data that is NOT present in the cache (Cache Miss)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The application crashes</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The application queries the primary database, writes the returned data into the cache for future requests, and returns the data to the user</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> The cache automatically generates fake data</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The database reboots</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> In Cache-Aside, the app checks the cache. On a miss, it reads from the primary database, populates the cache with a TTL, and returns the result.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 14 • DynamoDB Streams Ingestion</div>
      <div class="mcq-q">What capability is unlocked by enabling Amazon DynamoDB Streams on a table?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Video streaming to YouTube</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Automatic table deletion</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> An ordered 24-hour log of item-level modifications (INSERT, MODIFY, REMOVE) that can trigger AWS Lambda functions in real time</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Converting NoSQL data into Microsoft Excel files</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> DynamoDB Streams emits real-time changelogs of item updates, powering event-driven architectures, replication, and search index synchronization via Lambda.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="A">
      <div class="mcq-num">Question 15 • Redshift Leader Node Responsibility</div>
      <div class="mcq-q">In an Amazon Redshift cluster, what is the role of the Leader Node?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Coordinates client SQL connections, parses queries, develops execution plans, and aggregates results returned by parallel Compute Nodes</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Stores 100% of the customer database data</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Powers the datacenter air conditioning</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Reboots failed EC2 instances</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> The Leader Node receives queries from SQL clients, compiles optimized execution code, and coordinates parallel execution across compute slice nodes.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="D">
      <div class="mcq-num">Question 16 • DynamoDB On-Demand vs Provisioned Capacity</div>
      <div class="mcq-q">When should an architect select DynamoDB On-Demand Capacity mode instead of Provisioned Capacity?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> When traffic is 100% predictable 24/7</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> When running Oracle database engines</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> To reduce network cable costs</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> When application traffic is completely unknown, spiky, or has unpredictable idle periods where paying for idle capacity is wasteful</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> On-Demand mode accommodates unpredictable traffic surges instantly, charging purely per read/write request with zero capacity planning.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 17 • Write-Through Caching Trade-off</div>
      <div class="mcq-q">What is the primary drawback of implementing a Write-Through caching strategy?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Data is always stale</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Increased write latency because data must be written to both the cache and the primary database before the write is acknowledged</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> It only works with PHP code</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> It requires disabling SSL</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Write-Through ensures cache freshness by writing to cache and DB simultaneously, but incurs a write latency penalty and caches data that may never be read.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 18 • Amazon RDS Automated Backups</div>
      <div class="mcq-q">What is the maximum backup retention period configurable for Amazon RDS Automated Backups?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 7 days</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 14 days</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 35 days</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 365 days</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> RDS automated point-in-time backups support a maximum retention period of 35 days. Manual DB snapshots can be retained indefinitely.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="A">
      <div class="mcq-num">Question 19 • Redshift Spectrum Capability</div>
      <div class="mcq-q">What unique analytics capability is enabled by Amazon Redshift Spectrum?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Directly querying exabytes of unstructured/semi-structured data residing in Amazon S3 without loading it into Redshift cluster disk tables</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Providing free Wi-Fi to offices</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Streaming video to mobile phones</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Automatically repairing broken fiber cables</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Redshift Spectrum allows standard Redshift SQL queries to join local cluster tables with massive exabyte-scale S3 data lakes without data ingestion.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="D">
      <div class="mcq-num">Question 20 • DynamoDB Global Tables Conflict Resolution</div>
      <div class="mcq-q">How does Amazon DynamoDB Global Tables resolve concurrent write conflicts occurring in two different AWS Regions simultaneously?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Deletes both items to be safe</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Asks the user to vote on the correct version</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Pauses database operations for 1 hour</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Employs a Last-Writer-Wins reconciliation strategy based on timestamp ordering</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Global Tables performs multi-region multi-active replication using a deterministic Last-Writer-Wins protocol to reconcile concurrent updates.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 21 • Aurora Global Database Latency</div>
      <div class="mcq-q">What is the typical cross-region replication latency achieved by an Amazon Aurora Global Database?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 15 to 30 minutes</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Under 1 second (typically &lt;200 milliseconds) with zero performance impact on the primary cluster</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Exactly zero nanoseconds</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> 24 hours</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Aurora Global Database replicates storage redo logs directly across regions using the AWS private backbone, achieving typical sub-second replication latency.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 22 • DynamoDB Time to Live (TTL)</div>
      <div class="mcq-q">What does enabling Time to Live (TTL) on an Amazon DynamoDB table accomplish?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Speeds up query execution times</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Encrypts data with a rotating password</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Automatically deletes expired items based on a designated epoch timestamp attribute without consuming provisioned write throughput</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Powers down the database at night</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> TTL defines an expiration timestamp; DynamoDB's background processes delete expired items within 48 hours for free without consuming WCUs.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="A">
      <div class="mcq-num">Question 23 • Amazon DocumentDB Compatibility</div>
      <div class="mcq-q">Which popular open-source NoSQL document database API is natively emulated by Amazon DocumentDB?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> MongoDB (BSON document model)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Apache Cassandra</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Neo4j Graph DB</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Couchbase</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Amazon DocumentDB provides a managed, scalable document database engine that is fully compatible with MongoDB drivers and tools.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="D">
      <div class="mcq-num">Question 24 • Amazon Keyspaces Compatibility</div>
      <div class="mcq-q">Which wide-column distributed database technology is managed serverlessly by Amazon Keyspaces?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> MySQL</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Oracle PL/SQL</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Redis</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Apache Cassandra (CQL API)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Amazon Keyspaces is a scalable, highly available serverless database service compatible with the Apache Cassandra CQL API.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 25 • Amazon OpenSearch Service Use Case</div>
      <div class="mcq-q">What is the optimal production application for Amazon OpenSearch Service (formerly Elasticsearch)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Storing raw video files</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Full-text search indexing, application log analytics, and interactive SIEM dashboards (OpenSearch Dashboards / Kibana)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Running financial accounting payroll</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Compiling Java source code</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> OpenSearch provides distributed full-text search, fuzzy matching, and log analytics with interactive dashboard visualizations.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 26 • Aurora Peer-to-Peer Storage Repair</div>
      <div class="mcq-q">How does Amazon Aurora repair corrupted or missing data segments on an individual storage node?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By asking the database administrator to restore an S3 backup</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By rebooting the primary compute instance</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Storage nodes continuously exchange gossip protocols; lagging nodes identify missing log records and reconstruct blocks directly from peer storage nodes without impacting compute performance</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> By deleting the corrupted table</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Aurora's storage tier is self-healing: background gossip protocols detect and rebuild corrupted segments from surviving nodes without consuming compute CPU.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="A">
      <div class="mcq-num">Question 27 • DynamoDB Accelerator (DAX)</div>
      <div class="mcq-q">What latency enhancement is delivered by deploying Amazon DynamoDB Accelerator (DAX) in front of a DynamoDB table?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Slashes read latency from single-digit milliseconds down to microsecond response times (&lt;1 ms)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Makes database writes free</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Converts JSON into XML</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Backs up data to floppy disk</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> DAX is a fully managed in-memory cache for DynamoDB that delivers microsecond response times for read-heavy workloads at scale.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="D">
      <div class="mcq-num">Question 28 • Amazon Neptune Graph Model</div>
      <div class="mcq-q">Which database engine should be selected for high-speed relationship graph analysis (fraud rings, social networks, knowledge graphs)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Amazon RDS MySQL</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Amazon Redshift</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Amazon DynamoDB</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Amazon Neptune (supporting Property Graph / Apache TinkerPop Gremlin and W3C RDF / SPARQL)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Amazon Neptune is a specialized graph database engine optimized for navigating billions of interconnected relationships with millisecond latency.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="B">
      <div class="mcq-num">Question 29 • RDS Storage Auto Scaling</div>
      <div class="mcq-q">How does Amazon RDS Storage Auto Scaling prevent databases from running out of disk space?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Deletes old customer records automatically</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Automatically detects when free disk space falls below 10% and provisions additional EBS storage on-the-fly with zero application downtime</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Compresses images into smaller files</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Shuts down the database server to prevent write errors</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Storage Auto Scaling monitors free disk space and automatically expands storage capacity up to a configured threshold with zero downtime.
      </div>
    </div>

    <div class="mcq-card" data-unit="C5" data-correct="C">
      <div class="mcq-num">Question 30 • DynamoDB Write Capacity Units (WCU)</div>
      <div class="mcq-q">How much data write capacity does exactly 1 Write Capacity Unit (WCU) represent in Amazon DynamoDB?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> 1 write per second for an item up to 4 KB in size</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> 100 writes per minute</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> 1 write per second for an item up to 1 KB in size</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Unlimited writes for 1 hour</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> In DynamoDB, 1 WCU represents one write per second for an item up to 1 KB in size. Writing a 2.5 KB item consumes 3 WCUs.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 05 Conceptual Questions</span>
    <span>Unit 05 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 5 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-c5">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">43.</span> Unit 5 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted explanations of database replication mechanics, distributed consensus quorums, and NoSQL partitioning.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Detail the architectural differences between an Amazon RDS Multi-AZ Standby and an Amazon RDS Read Replica.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Multi-AZ Standby:</strong> Synchronous physical block-level replication strictly for disaster recovery. Does not possess an independent endpoint and cannot serve read traffic. Provides automatic failover via DNS CNAME update in 60-120 seconds with zero data loss (RPO = 0).</p>
        <p><strong>Read Replica:</strong> Asynchronous logical engine replication intended for read scaling and reporting. Has its own distinct DNS endpoint and can serve read queries (up to 15 replicas). Subject to replication lag; if promoted to a standalone database, failover is manual and may incur data loss.</p>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Explain the 4-of-6 storage write quorum mechanism in Amazon Aurora and how it survives Availability Zone failures.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>Aurora replicates every 10 GB storage segment 6 ways across 3 Availability Zones (2 copies per AZ). Instead of full-page writes, compute heads transmit lightweight redo log streams.</p>
        <p>A write transaction is committed as soon as <strong>4 of the 6 storage nodes</strong> acknowledge persisting the log. If an entire Availability Zone is completely destroyed (losing 2 copies), 4 copies remain healthy, allowing Aurora to maintain continuous read and write availability without interruption. Even if a third node fails concurrently (losing 3 of 6), Aurora retains read availability (3-of-6 quorum) and rebuilds missing copies via peer-to-peer gossip.</p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> What is consistent hashing in Amazon DynamoDB, and why does poor Partition Key selection result in throttling?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>DynamoDB hashes the Partition Key value using an internal cryptographic hash function to assign items to physical storage partitions. Each partition is allocated a slice of the table's total provisioned RCU/WCU capacity (up to 1,000 WCUs and 3,000 RCUs per partition).</p>
        <p>If an application uses a low-cardinality key (e.g. `country = "US"`), all incoming traffic hashes to the same single physical partition ("hot partition"). When requests exceed that partition's 1,000 WCU limit, DynamoDB throttles requests (`ProvisionedThroughputExceededException`), even if the overall table capacity is 90% idle!</p>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> Contrast Amazon ElastiCache for Redis and Amazon ElastiCache for Memcached from a feature and operational standpoint.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Redis:</strong> Supports rich in-memory data structures (Hashes, Sorted Sets, Lists, Bitmaps), disk persistence (RDB snapshots to S3, AOF), Pub/Sub messaging, geospatial queries, and Multi-AZ replication with automatic failover. Single-threaded execution core.</p>
        <p><strong>Memcached:</strong> Simple, high-throughput in-memory key-value cache. Entirely volatile with zero persistence or replication. Multi-threaded architecture that scales horizontally across large multi-core CPU instances. Ideal for caching simple HTML fragments and JSON strings.</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> How does Amazon Redshift's Massively Parallel Processing (MPP) architecture execute analytical queries across petabyte datasets?</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>A Redshift cluster consists of a <strong>Leader Node</strong> and multiple <strong>Compute Nodes</strong>. The Leader Node parses incoming SQL queries, compiles optimized C++ execution code, and distributes query execution slices across compute nodes.</p>
        <p>Each compute node has dedicated CPU, memory, and columnar storage slices. Data is distributed across nodes using distribution styles (`KEY`, `ALL`, `EVEN`). When a query executes, all compute nodes process their local columnar data slices simultaneously in parallel, streaming intermediate aggregates back to the Leader Node to produce the final result in seconds.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 05 Analytical Problems</span>
    <span>Unit 05 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 5 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-c5">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">44.</span> Unit 5 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Real-world architectural failure analyses, database failovers, and partition bottleneck remediation scenarios.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Database Failover Triage: Stale DNS Caching Causing 15-Minute Outage Following RDS Multi-AZ Failover</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> An Amazon RDS PostgreSQL database in `us-east-1a` suffers a hardware host failure. AWS automatically initiates a Multi-AZ failover, successfully promoting the standby in `us-east-1b` in 75 seconds. However, web application servers continue attempting to connect to the dead IP address in `us-east-1a` for over 15 minutes, causing thousands of database connection failures!</p>
        <p><strong>Root Cause Analysis &amp; Resolution:</strong></p>
        <ol>
          <li><strong>The JVM DNS Caching Trap:</strong> When RDS performs a failover, it flips the canonical DNS CNAME record (e.g. `prod-db.xxxx.us-east-1.rds.amazonaws.com`) to point to the new standby's IP address. AWS sets the Route 53 DNS Time-to-Live (TTL) to <strong>5 seconds</strong>.</li>
          <li><strong>The Java Network Address Cache Flaw:</strong> By default, the Java Virtual Machine (JVM) caches DNS lookups <em>forever</em> (`networkaddress.cache.ttl = -1`) to protect against DNS spoofing. Even though Route 53 updated the DNS mapping within seconds, the Java application servers never queried DNS again, stubbornly attempting to connect to the dead IP address!</li>
          <li><strong>Remediation:</strong> Modify the JVM security configuration (`java.security` or runtime parameter):
            <br><code>networkaddress.cache.ttl = 5</code>
            <br>This forces the JVM to obey the 5-second TTL, ensuring application connection pools seamlessly reconnect to the promoted database within seconds of an RDS failover.
          </li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> NoSQL Partition Hot-Spotting: Resolving IoT Fleet Throttling in Amazon DynamoDB</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A smart meter IoT network with 500,000 devices transmits telemetry readings every minute. The DynamoDB table has 10,000 WCUs provisioned. The table schema uses `Date` (e.g. `2026-10-27`) as the Partition Key and `DeviceID` as the Sort Key. During peak morning hours, devices experience heavy `ProvisionedThroughputExceededException` throttles, even though CloudWatch reports total consumed WCUs never exceed 1,500 WCUs (15% utilization)!</p>
        <p><strong>Root Cause &amp; Sharding Solution:</strong></p>
        <ul>
          <li><strong>The Hot Partition Bottleneck:</strong> Because all 500,000 devices send readings on the same calendar day, all 10,000 writes/second hash to the <strong>exact same single physical storage partition</strong>! A single DynamoDB partition is strictly capped at 1,000 WCUs. The remaining 9,000 provisioned WCUs allocated across other idle partitions are completely wasted.</li>
          <li><strong>Architectural Fix 1 (Inverted Key Hierarchy):</strong> Swap the primary key design: make `DeviceID` the Partition Key and `Timestamp` the Sort Key. Because 500,000 distinct device IDs exist, writes distribute evenly across hundreds of physical partitions, scaling throughput linearly.</li>
          <li><strong>Architectural Fix 2 (Write Sharding / Salt Suffix):</strong> If querying by date is strictly mandatory, append a randomized calculated suffix (e.g. `2026-10-27_0` through `2026-10-27_19`) to distribute the date across 20 distinct partition hash buckets.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> Cost &amp; Performance Optimization: Athena Data Lake Query Tuning with Apache Parquet</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Engineering Challenge:</strong> A cybersecurity operations center stores 100 TB of raw JSON firewall logs monthly in Amazon S3. Security analysts execute 50 Athena queries daily to hunt for indicators of compromise (IOCs). Monthly Athena query costs exceed $12,500/month (50 queries &times; 100 TB &times; $5/TB = $25,000/month!). Queries take 4 minutes to return results.</p>
        <p><strong>Data Pipeline Optimization Blueprint:</strong></p>
        <ul>
          <li><strong>Step 1: Convert to Apache Parquet (Columnar):</strong> Deploy an AWS Glue ETL job that compresses and transforms raw JSON logs into columnar Apache Parquet format using Snappy compression.</li>
          <li><strong>Step 2: Hive Partitioning:</strong> Partition S3 storage paths by date: `s3://logs/year=2026/month=10/day=27/`.</li>
          <li><strong>Performance Impact:</strong>
            <br>&bull; Columnar filtering allows Athena to read only the target `source_ip` and `dest_port` columns, skipping 95% of data.
            <br>&bull; Partition pruning scans only the specific target day instead of the entire 100 TB monthly dataset.
            <br>&bull; Data scanned per query plummets from 100 TB down to <strong>50 GB</strong>!
            <br>&bull; Query time drops from 4 minutes down to <strong>3 seconds</strong>, and monthly query cost drops from $12,500 down to <strong>$37.50/month (99.7% cost reduction!)</strong>.
          </li>
        </ul>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> In-Memory Cache Thundering Herd: Cache Stampede Mitigation in High-Traffic News Portal</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A breaking news portal caches its homepage article data in Amazon ElastiCache for Redis with a 15-minute TTL. At 10:15 AM, the cache key expires. Within 500 milliseconds, 50,000 concurrent web requests experience a cache miss and simultaneously query the backend Amazon Aurora database, triggering a massive CPU spike (100%), exhausting database connection pools, and knocking the site offline.</p>
        <p><strong>Cache Stampede (Thundering Herd) Mitigation Strategies:</strong></p>
        <ul>
          <li><strong>1. Mutual Exclusion Locks (Distributed Mutex):</strong> When a cache miss occurs, the first application worker thread acquires an atomic lock in Redis (`SET lock_key true NX EX 10`). Only that single thread is permitted to query the database and update the cache. All other 49,999 threads wait or serve stale cached content until the key is repopulated.</li>
          <li><strong>2. Probabilistic Early Expiration (XFetch Algorithm):</strong> Instead of waiting for hard expiration, application threads probabilistically refresh the cache entry a few seconds <em>before</em> the TTL expires, based on compute time and read frequency. Background refresh ensures the key is never allowed to expire in production.</li>
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
<article class="doc-page" id="mcq-answer-key-c5">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 05</span>
    <span class="meta-tag">Master Answer Key • 30 Questions</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">45.</span> Unit 5 Master Answer Key Table & Verification Matrix
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
        <tr><td>01</td><td><strong style="color:var(--primary);">B</strong></td><td>RDS Multi-AZ synchronous physical block-level replication</td><td>16</td><td><strong style="color:var(--primary);">D</strong></td><td>DynamoDB On-Demand capacity for spiky unpredictable traffic</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">C</strong></td><td>Aurora 6-way storage mirroring (4-of-6 write quorum)</td><td>17</td><td><strong style="color:var(--primary);">B</strong></td><td>Write-Through caching increased write latency trade-off</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">A</strong></td><td>DynamoDB Partition Key cryptographic hashing algorithm</td><td>18</td><td><strong style="color:var(--primary);">C</strong></td><td>RDS automated backup maximum retention period (35 days)</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">D</strong></td><td>ElastiCache Redis rich data structures and disk persistence</td><td>19</td><td><strong style="color:var(--primary);">A</strong></td><td>Redshift Spectrum direct SQL querying of S3 data lakes</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">B</strong></td><td>Columnar storage reading only requested columns off disk</td><td>20</td><td><strong style="color:var(--primary);">D</strong></td><td>DynamoDB Global Tables Last-Writer-Wins conflict resolution</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">C</strong></td><td>DynamoDB Strongly Consistent Read consuming 1 full RCU</td><td>21</td><td><strong style="color:var(--primary);">B</strong></td><td>Aurora Global Database sub-second cross-region replication</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">A</strong></td><td>RDS Read Replica scaling limit (Up to 15 read replicas)</td><td>22</td><td><strong style="color:var(--primary);">C</strong></td><td>DynamoDB TTL automated expiration without consuming WCUs</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">D</strong></td><td>Local Secondary Index creation strictly at table creation time</td><td>23</td><td><strong style="color:var(--primary);">A</strong></td><td>Amazon DocumentDB native MongoDB API emulation</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">B</strong></td><td>Amazon Athena billing model ($5.00 per TB scanned)</td><td>24</td><td><strong style="color:var(--primary);">D</strong></td><td>Amazon Keyspaces managed Apache Cassandra CQL service</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">C</strong></td><td>Aurora Serverless v2 fine-grained scaling in ACU increments</td><td>25</td><td><strong style="color:var(--primary);">B</strong></td><td>OpenSearch full-text search and log analytics indexing</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">A</strong></td><td>Low-cardinality status partition key causing hot partitions</td><td>26</td><td><strong style="color:var(--primary);">C</strong></td><td>Aurora peer-to-peer storage gossip self-healing repair</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">D</strong></td><td>AWS Glue Data Catalog persistent Apache Hive metadata store</td><td>27</td><td><strong style="color:var(--primary);">A</strong></td><td>DynamoDB Accelerator (DAX) microsecond in-memory response</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">B</strong></td><td>Cache-Aside lazy loading on cache miss querying DB</td><td>28</td><td><strong style="color:var(--primary);">D</strong></td><td>Amazon Neptune graph database for relationship analytics</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">C</strong></td><td>DynamoDB Streams real-time 24-hour change log triggers</td><td>29</td><td><strong style="color:var(--primary);">B</strong></td><td>RDS Storage Auto Scaling expanding disk with zero downtime</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">A</strong></td><td>Redshift Leader Node query compilation and coordination</td><td>30</td><td><strong style="color:var(--primary);">C</strong></td><td>1 Write Capacity Unit representing 1 write/sec up to 1 KB</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 05 Complete • Next: Unit 06 Cloud Security & Governance</span>
    <span>Unit 05 • Page 09</span>
  </div>
</article>
"""
