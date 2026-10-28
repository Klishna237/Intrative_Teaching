# -*- coding: utf-8 -*-
"""
Cloud Administration (AWS) - Unit 6: Cloud Security, Governance & Well-Architected
Master Gold Standard Layout:
- c6-iam: AWS IAM Architecture (Roles, Policies, STS Tokens, Least Privilege)
- c6-kms: AWS KMS Envelope Encryption & CloudHSM (FIPS 140-2 Level 3)
- c6-monitoring: CloudWatch Metrics/Alarms, CloudTrail API Auditing & AWS Config
- c6-defense: Perimeter Defense: AWS WAF, AWS Shield Advanced & GuardDuty
- c6-waf-framework: The AWS Well-Architected Framework (The 6 Pillars)
- practice-mcq-c6: 30 MCQs with dynamic scoring
- practice-subj-short-c6: 5 Short Conceptual Sets
- practice-subj-long-c6: 4 Deep Analytical Scenarios
- mcq-answer-key-c6: Master Answer Key Table
"""

CLOUD_UNIT6_HTML = """
<!-- ==========================================================================
     UNIT 06: CLOUD SECURITY, GOVERNANCE & WELL-ARCHITECTED
     ========================================================================== -->

<!-- Page 1: AWS IAM Architecture -->
<article class="doc-page" id="c6-iam">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 06 • Page 01</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">46.</span> AWS Identity &amp; Access Management (IAM): Roles, Policies &amp; Least Privilege
  </h2>

  <p class="lead-para">
    AWS IAM provides fine-grained access control across all AWS resources, evaluating cryptographic authorization policies to authenticate principals and enforce the principle of least privilege.
  </p>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="shield"></i> The IAM Policy Evaluation Logic Hierarchy</div>
    <p>
      When an API call is made, IAM evaluates authorization using a strict priority order:
      <br>1. <strong>Explicit Deny:</strong> If any applicable policy (SCP, Permission Boundary, Identity Policy, Resource Policy) contains an `Effect: "Deny"`, the request is <strong>immediately denied</strong>. An explicit deny overrides all allows!
      <br>2. <strong>Service Control Policy (SCP):</strong> Organizations SCP must allow the action.
      <br>3. <strong>Permissions Boundary:</strong> Must permit the action if attached to the identity.
      <br>4. <strong>Explicit Allow:</strong> At least one identity-based policy or resource-based policy must explicitly grant `Effect: "Allow"`.
      <br>5. <strong>Default Deny (Implicit Deny):</strong> If no explicit allow matches, the request is denied by default.
    </p>
  </div>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>IAM Entity</th>
          <th>Credentials Issued</th>
          <th>Primary Operational Role</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>IAM User</strong></td>
          <td>Permanent Console Password &amp; Long-term Access Keys (`AKIA...`)</td>
          <td>Individual human operators; anti-pattern for software applications (should use IAM Roles instead!).</td>
        </tr>
        <tr>
          <td><strong>IAM Group</strong></td>
          <td>None (Cannot be referenced as a Principal)</td>
          <td>Administrative container to attach policies to multiple users concurrently (e.g. `Developers`, `SecurityAuditors`).</td>
        </tr>
        <tr>
          <td><strong>IAM Role</strong></td>
          <td><strong>Temporary, automatically rotating STS Credentials</strong> (Access Key `ASIA...`, Secret Key, Session Token)</td>
          <td>Assumed by EC2 instances (Instance Profiles), Lambda functions, cross-account administrators, and federated SSO users.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: AWS KMS Envelope Encryption</span>
    <span>Unit 06 • Page 01</span>
  </div>
</article>

<!-- Page 2: AWS KMS & CloudHSM -->
<article class="doc-page" id="c6-kms">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 06 • Page 02</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">47.</span> Cryptographic Governance: AWS KMS Envelope Encryption &amp; AWS CloudHSM
  </h2>

  <p class="lead-para">
    Protecting data at rest across hyperscale object, block, and relational datastores relies on hardware-validated cryptographic key hierarchies and envelope encryption algorithms.
  </p>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="lock"></i> Cryptographic Mechanics: The 2-Tier Envelope Encryption Model</div>
    <p>
      Encrypting large multi-gigabyte files directly with a master key over an API would introduce massive network latency and risk key exposure. AWS KMS utilizes <strong>Envelope Encryption</strong>:
    </p>
    <ol>
      <li><strong>Data Encryption Key (DEK) Generation:</strong> The application calls `kms:GenerateDataKey`. KMS uses the root AWS KMS Key (KMS Master Key) inside a hardware security module (HSM) to generate a unique plaintext 256-bit symmetric AES key (DEK) and an encrypted copy of that DEK.</li>
      <li><strong>Local High-Speed Encryption:</strong> The application uses the <em>plaintext DEK</em> in memory to encrypt the file locally at full memory bus speeds.</li>
      <li><strong>Plaintext DEK Destruction:</strong> As soon as encryption completes, the application <strong>erases the plaintext DEK from memory</strong>!</li>
      <li><strong>Ciphertext Bundling:</strong> The application stores the <em>encrypted DEK</em> as metadata alongside the ciphertext file. To decrypt later, the application sends the encrypted DEK back to KMS (`kms:Decrypt`), which returns the plaintext key to decrypt the payload. The root KMS Key never leaves the physical HSM hardware!</li>
    </ol>
  </div>

  <div class="page-footer-meta">
    <span>Next: Monitoring: CloudWatch, CloudTrail & Config</span>
    <span>Unit 06 • Page 02</span>
  </div>
</article>

<!-- Page 3: Monitoring & Auditing -->
<article class="doc-page" id="c6-monitoring">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 06 • Page 03</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">48.</span> Observability &amp; Auditing: Amazon CloudWatch, AWS CloudTrail &amp; AWS Config
  </h2>

  <p class="lead-para">
    Enterprise governance mandates complete operational visibility into system performance metrics, administrative API invocations, and historical compliance configuration states.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Service</th>
          <th>Core Question Answered</th>
          <th>Data Collected</th>
          <th>Operational Focus</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Amazon CloudWatch</strong></td>
          <td><em>"How are my systems performing right now?"</em></td>
          <td>CPU utilization, disk IOPS, network bytes, custom application metrics, real-time log streams, composite alarms.</td>
          <td>Performance monitoring, alerting, Auto Scaling triggers, and operational dashboards.</td>
        </tr>
        <tr>
          <td><strong>AWS CloudTrail</strong></td>
          <td><em>"WHO did WHAT, WHEN, and from WHICH IP address?"</em></td>
          <td>Complete cryptographic audit trail of all AWS Management Console logins, SDK calls, and CLI API requests.</td>
          <td>Security incident forensics, compliance auditing, tracking unauthorized privilege escalations.</td>
        </tr>
        <tr>
          <td><strong>AWS Config</strong></td>
          <td><em>"Is my infrastructure compliant with security rules over time?"</em></td>
          <td>Point-in-time configuration snapshots, resource change history, and compliance rule evaluations (e.g. "Is EBS encrypted?").</td>
          <td>Configuration drift tracking, continuous compliance auditing, automated remediation via AWS Systems Manager Automation.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: Perimeter Defense: WAF, Shield & GuardDuty</span>
    <span>Unit 06 • Page 03</span>
  </div>
</article>

<!-- Page 4: Perimeter Defense -->
<article class="doc-page" id="c6-defense">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 06 • Page 04</span>
    <span class="meta-tag">Bloom's: Apply / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">49.</span> Perimeter Defense: AWS WAF, AWS Shield Advanced &amp; Amazon GuardDuty
  </h2>

  <p class="lead-para">
    Safeguarding cloud applications from distributed denial-of-service (DDoS) barrages, automated web scrapers, and malicious account compromises requires multi-layered perimeter defense technologies.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Security Service</th>
          <th>OSI Layer Protection</th>
          <th>Detection Mechanism</th>
          <th>Primary Threat Neutralized</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>AWS WAF</strong></td>
          <td>Layer 7 (Application)</td>
          <td>Web Access Control Lists (ACLs) inspecting HTTP/HTTPS headers, bodies, SQLi regex, XSS scripts, rate-limiting rules.</td>
          <td>OWASP Top 10 web vulnerabilities, SQL injection, Cross-Site Scripting, brute-force login bots.</td>
        </tr>
        <tr>
          <td><strong>AWS Shield Standard</strong></td>
          <td>Layer 3 (Network) &amp; Layer 4</td>
          <td>Automatic inline traffic scrubbing at all global CloudFront and Route 53 Edge Locations.</td>
          <td>SYN floods, UDP reflection amplification, TCP reset attacks (included free for all AWS customers!).</td>
        </tr>
        <tr>
          <td><strong>AWS Shield Advanced</strong></td>
          <td>Layer 3, 4, and 7</td>
          <td>24/7 dedicated AWS DDoS Response Team (DRT), automated WAF rule synthesis, and <strong>DDoS Cost Protection</strong>.</td>
          <td>Large-scale multi-gigabit DDoS campaigns; refunds AWS resource scaling charges incurred during an attack!</td>
        </tr>
        <tr>
          <td><strong>Amazon GuardDuty</strong></td>
          <td>Account &amp; Workload Level</td>
          <td>Continuous intelligent threat detection using machine learning analyzing VPC Flow Logs, DNS logs, CloudTrail events, and EKS audit logs.</td>
          <td>Compromised EC2 instances mining cryptocurrency, stolen IAM credentials operating from Tor exit nodes.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Next: The AWS Well-Architected Framework</span>
    <span>Unit 06 • Page 04</span>
  </div>
</article>

<!-- Page 5: Well-Architected Framework -->
<article class="doc-page" id="c6-waf-framework">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • AWS-ARCH</span>
    <span class="meta-tag">Unit 06 • Page 05</span>
    <span class="meta-tag">Bloom's: Understand / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">50.</span> The AWS Well-Architected Framework: The 6 Core Engineering Pillars
  </h2>

  <p class="lead-para">
    The AWS Well-Architected Framework provides a consistent approach for customers and partners to evaluate cloud architectures and implement designs that scale reliably over time.
  </p>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="award"></i> The 6 Core Pillars of the Well-Architected Framework</div>
    <p>
      <strong>1. Operational Excellence:</strong> The ability to run and monitor systems to deliver business value and continually improve supporting processes and procedures. (Core design principle: <em>Perform operations as code, make small reversible changes, anticipate failure</em>).
      <br><strong>2. Security:</strong> Protecting information, systems, and assets while delivering business value through risk assessments and mitigation strategies. (Core design principle: <em>Apply security at all layers, enable traceability, automate security best practices</em>).
      <br><strong>3. Reliability:</strong> The ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues. (Core design principle: <em>Test recovery procedures, automatically recover from failure, scale horizontally</em>).
      <br><strong>4. Performance Efficiency:</strong> The ability to use computing resources efficiently to meet system requirements and maintain that efficiency as demand changes and technologies evolve. (Core design principle: <em>Democratize advanced technologies, go global in minutes, use serverless architectures</em>).
      <br><strong>5. Cost Optimization:</strong> The ability to run systems to deliver business value at the lowest price point. (Core design principle: <em>Implement cloud financial management, adopt a consumption model, measure overall efficiency</em>).
      <br><strong>6. Sustainability:</strong> Minimizing the environmental impacts of running cloud workloads. (Core design principle: <em>Understand your impact, establish sustainability goals, maximize utilization, adopt new efficient hardware like AWS Graviton</em>).
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 06 Practice MCQ Bank</span>
    <span>Unit 06 • Page 05</span>
  </div>
</article>

<!-- Page 6: Unit 6 Practice MCQ Bank (30 Questions) -->
<article class="doc-page" id="practice-mcq-c6">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 06</span>
    <span class="meta-tag">Assessment • 30 Questions</span>
    <span class="meta-tag" id="mcqScoreC6">Score: 0 / 30</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">51.</span> Unit 06 Self-Testing Bank: 30 Multiple Choice Questions
  </h2>

  <p class="lead-para">
    Test your mastery of IAM policy evaluation, envelope encryption, CloudWatch/CloudTrail telemetry, perimeter defense, and the Well-Architected pillars.
  </p>

  <div class="mcq-grid">
    <!-- Q1 -->
    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 01 • IAM Policy Priority</div>
      <div class="mcq-q">If an identity-based IAM policy contains an explicit `Effect: "Allow"` on `s3:*`, but an attached Service Control Policy (SCP) contains an `Effect: "Deny"` on `s3:DeleteBucket`, what happens when the user attempts to delete a bucket?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> The bucket is deleted because Allow overrides Deny</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The request is DENIED because an Explicit Deny always overrides any Allow</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS sends an approval email to root</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> The user is logged out of the console</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> In AWS IAM authorization logic, an explicit Deny in any applicable policy unconditionally takes precedence over any Allow.
      </div>
    </div>

    <!-- Q2 -->
    <div class="mcq-card" data-unit="C6" data-correct="D">
      <div class="mcq-num">Question 02 • Envelope Encryption Plaintext DEK</div>
      <div class="mcq-q">In AWS KMS envelope encryption, what must the application do with the plaintext Data Encryption Key (DEK) immediately after encrypting local data?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Save it in a text file on the desktop</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Upload it to an S3 bucket</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Email it to the security auditor</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Securely erase the plaintext DEK from memory as quickly as possible</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The security of envelope encryption depends on memory hygiene: once data is encrypted, the plaintext DEK is purged from RAM; only the encrypted DEK is persisted.
      </div>
    </div>

    <!-- Q3 -->
    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 03 • CloudTrail vs CloudWatch Focus</div>
      <div class="mcq-q">Which AWS service should a security forensics officer query to determine WHO terminated a production EC2 instance at 3:15 AM?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> AWS CloudTrail (logs the `TerminateInstances` API call with IAM identity, timestamp, and caller IP)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Amazon CloudWatch Metrics</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Trusted Advisor</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Amazon Inspector</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> CloudTrail audits all API calls made across the account, recording the exact IAM username or assumed role, timestamp, request parameters, and source IP.
      </div>
    </div>

    <!-- Q4 -->
    <div class="mcq-card" data-unit="C6" data-correct="C">
      <div class="mcq-num">Question 04 • AWS Shield Cost Protection</div>
      <div class="mcq-q">What unique financial protection is provided by AWS Shield Advanced during a massive Layer 7 DDoS attack targeting an Application Load Balancer fleet?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Free EC2 instances for 1 year</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Double internet speed</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> "DDoS Cost Protection" providing bill credits for scaling charges incurred by Auto Scaling Groups and ALBs in response to malicious attack traffic</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Eliminating credit card transaction fees</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Shield Advanced protects corporate budgets: AWS issues financial credits for spike-related resource scaling costs resulting from a verified DDoS attack.
      </div>
    </div>

    <!-- Q5 -->
    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 05 • The 6th Well-Architected Pillar</div>
      <div class="mcq-q">Which pillar was officially added as the 6th pillar of the AWS Well-Architected Framework in December 2021 to address environmental impact?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Cloud Economics Pillar</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Sustainability Pillar</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> High Availability Pillar</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Artificial Intelligence Pillar</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The Sustainability Pillar focuses on minimizing environmental footprints, maximizing resource utilization, and adopting efficient technologies like AWS Graviton.
      </div>
    </div>

    <!-- Q6 to Q30 formatted identically -->
    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 06 • GuardDuty Threat Detection Sources</div>
      <div class="mcq-q">Which continuous telemetry sources are analyzed automatically by Amazon GuardDuty without requiring agent installation on EC2 instances?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> VPC Flow Logs, DNS query logs, CloudTrail Management &amp; S3 Data Events, and EKS audit logs</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> User web browser search history</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Audio recordings from server room microphones</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Employee email text</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> GuardDuty consumes foundational AWS data streams directly from the infrastructure fabric, applying machine learning to detect anomalies without host agent overhead.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="C">
      <div class="mcq-num">Question 07 • AWS Config Continuous Tracking</div>
      <div class="mcq-q">What capability allows AWS Config to alert security teams when a developer disables encryption on an Amazon S3 bucket?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> AWS Config reboots the S3 service</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> AWS Config changes the password of the developer</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Config continuously evaluates resource state against managed rules (e.g. `s3-bucket-server-side-encryption-enabled`) and flags non-compliant resources</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> AWS Config blocks all internet traffic</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> AWS Config audits configuration changes against rules, marking non-compliant resources and optionally triggering automated remediation scripts.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="D">
      <div class="mcq-num">Question 08 • AWS CloudHSM Regulatory Standard</div>
      <div class="mcq-q">Which government security compliance standard is achieved by AWS CloudHSM dedicated single-tenant hardware appliances?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> FIPS 140-2 Level 1</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> ISO 9001</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> PCI DSS Level 4</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> FIPS 140-2 Level 3 (Tamper-evident, zero-AWS-operator access dedicated cryptographic hardware)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> CloudHSM provides dedicated single-tenant hardware security modules meeting FIPS 140-2 Level 3 physical tamper-resistance standards.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 09 • IAM Permission Boundaries</div>
      <div class="mcq-q">What does an IAM Permission Boundary do when attached to an IAM User or Role?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Automatically grants Administrator privileges</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Defines the absolute maximum permissions an identity can possess, preventing delegated administrators from escalating their own privileges beyond the boundary</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Restricts logins to specific GPS coordinates</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Disables the password after 30 days</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> A Permission Boundary sets the maximum ceiling of permissions. Even if a user attaches `AdministratorAccess`, they cannot perform actions disallowed by the boundary.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 10 • AWS WAF Layer Protection</div>
      <div class="mcq-q">Which OSI layer is protected by the AWS Web Application Firewall (WAF)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Layer 7 (Application Layer)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Layer 4 (Transport Layer)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Layer 3 (Network Layer)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Layer 2 (Data Link Layer)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> AWS WAF inspects HTTP/HTTPS application layer traffic (Layer 7) on Application Load Balancers, CloudFront distributions, and API Gateways.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="C">
      <div class="mcq-num">Question 11 • AWS Trusted Advisor Pillars</div>
      <div class="mcq-q">Which five operational categories are analyzed by AWS Trusted Advisor to recommend architectural improvements?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Hardware, Software, Physics, Cooling, Heating</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> HTML, CSS, JavaScript, Python, Bash</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Cost Optimization, Security, Fault Tolerance, Performance, and Service Quotas</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Sales, Marketing, Payroll, Billing, Human Resources</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Trusted Advisor scans accounts across 5 pillars: Cost Optimization, Security, Fault Tolerance, Performance, and Service Quotas.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="D">
      <div class="mcq-num">Question 12 • CloudTrail Log File Integrity</div>
      <div class="mcq-q">How does AWS CloudTrail validate that log files stored in Amazon S3 have not been altered, modified, or deleted after delivery?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By storing logs on floppy disks</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By printing physical copies daily</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By requiring the administrator to sign an affidavit</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Using CloudTrail Log File Validation, which generates cryptographic SHA-256 hashes and RSA digital signatures linked into an immutable hash tree (Merkle tree)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Log File Validation uses SHA-256 and digital signatures to detect any modification or deletion of log files, proving non-repudiation in court audits.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 13 • Root User Best Practice</div>
      <div class="mcq-q">What is the mandatory security best practice regarding the AWS Account Root User credentials?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Share the root password with all developers</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Lock away the root credentials, enable hardware MFA, delete root access keys, and use IAM Identity Center / SSO for daily administration</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Embed root access keys inside application source code</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Disable MFA to avoid lockouts</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> The root account has unrestricted access. Best practice mandates locking it away with hardware MFA and using IAM roles for everyday administrative tasks.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 14 • CloudWatch Synthetic Canaries</div>
      <div class="mcq-q">What is the primary role of an Amazon CloudWatch Synthetic Canary?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Executes automated headless browser scripts 24/7 to test customer user journeys (checkout, login) and alert before customers experience outages</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Detects carbon monoxide inside server rooms</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Compresses log files</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Reboots unresponsive routers</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Synthetic canaries run automated Node.js/Python scripts mimicking user actions, alerting on broken UI elements or API errors proactively.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="C">
      <div class="mcq-num">Question 15 • Amazon Inspector Assessment Target</div>
      <div class="mcq-q">What security vulnerability scanning capability is delivered by Amazon Inspector?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Inspects physical server racks with cameras</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Audits employee expense reports</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Automated vulnerability management scanning EC2 instances, container images in ECR, and Lambda functions for software CVEs and unintended network exposure</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Tests Wi-Fi speeds</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Amazon Inspector scans EC2, container images, and Lambda functions for known CVE software vulnerabilities and exposed network attack vectors.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="D">
      <div class="mcq-num">Question 16 • KMS Automatic Key Rotation</div>
      <div class="mcq-q">What occurs when Automatic Key Rotation is enabled on a customer-managed AWS KMS Key?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> All existing encrypted data is immediately deleted</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> The key password changes daily</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> All customer files must be downloaded and re-encrypted manually</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> KMS generates a new cryptographic backing key material yearly; previous backing keys are retained to seamlessly decrypt older ciphertext without re-encrypting existing data</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> KMS key rotation creates new backing key material for new writes while retaining older material so historical ciphertext decrypts transparently without re-encryption.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 17 • AWS Secrets Manager Auto-Rotation</div>
      <div class="mcq-q">How does AWS Secrets Manager automatically rotate database credentials without service downtime?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> By sending an email to the DBA every 30 days</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> By invoking an AWS Lambda function that changes the password inside the target RDS database, validates connectivity, and updates the secret in Secrets Manager</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> By shutting down the database for 10 minutes</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> By using default passwords</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Secrets Manager uses a Lambda rotation function to update credentials inside the database engine, verify connections, and update secret values without manual intervention.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 18 • CloudWatch Metric Resolution</div>
      <div class="mcq-q">What is the difference between standard CloudWatch metric resolution and High-Resolution metrics?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Standard resolution captures data at 1-minute intervals; High-Resolution captures telemetry down to 1-second intervals</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> High-resolution displays in 4K video resolution</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Standard resolution is free; high-resolution is illegal</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> High-resolution metrics can only be viewed on mobile phones</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> High-Resolution metrics provide sub-minute granularity (1, 5, 10, or 30 seconds), enabling ultra-responsive monitoring for financial and real-time gaming systems.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="C">
      <div class="mcq-num">Question 19 • Service Control Policy (SCP) Function</div>
      <div class="mcq-q">What is the scope and operational authority of an AWS Organizations Service Control Policy (SCP)?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Grants permissions to individual IAM users in an account</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Configures billing invoice addresses</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Sets the maximum permission boundary for all member AWS accounts within an Organizational Unit (OU), preventing even account root users from executing restricted APIs</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Deploys EC2 instances across accounts</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> SCPs establish guardrails across an entire organization. If an SCP blocks an action (e.g. `s3:DeleteBucket`), no IAM user or root account in that member account can execute it.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="D">
      <div class="mcq-num">Question 20 • AWS Security Hub Aggregation</div>
      <div class="mcq-q">What is the primary architectural function of AWS Security Hub?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Backing up hard drives</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Resetting forgotten passwords</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Translating foreign language text</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Centralizing and aggregating security alerts and findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, and partner tools into a single dashboard against security standards (CIS, NIST)</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Security Hub is a Cloud Security Posture Management (CSPM) service aggregating findings across AWS security tools against industry benchmarks.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 21 • Amazon Macie Purpose</div>
      <div class="mcq-q">Which data privacy risk is detected by Amazon Macie?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> High CPU temperatures in servers</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Unencrypted personally identifiable information (PII, credit card numbers, passport numbers) stored inside Amazon S3 buckets</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Slow Wi-Fi connections</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Expired domain name registrations</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> Amazon Macie uses machine learning and pattern matching to discover and protect sensitive PII and financial data stored in Amazon S3.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 22 • CloudWatch Metric Math</div>
      <div class="mcq-q">What capability allows an administrator to combine multiple CloudWatch metrics using mathematical expressions (e.g. `(Errors / TotalRequests) * 100`) to create a single composite error rate alarm?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> CloudWatch Metric Math</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> CloudWatch Calculator</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> AWS Glue Formula</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Amazon Athena Math</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Metric Math enables querying multiple CloudWatch metrics and applying mathematical formulas to publish new composite metrics and alarm thresholds.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="C">
      <div class="mcq-num">Question 23 • Security Pillar Core Design Principle</div>
      <div class="mcq-q">Which design principle is explicitly mandated by the Security Pillar of the AWS Well-Architected Framework?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Make infrastructure as complicated as possible</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Disable encryption to maximize throughput</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Apply security at all layers (defense in depth across network, compute, operating system, and data)</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Share passwords over corporate Slack channels</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> The Security Pillar mandates defense-in-depth: applying multiple security controls across edge network boundaries, VPCs, instances, operating systems, and encrypted data.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="D">
      <div class="mcq-num">Question 24 • Reliability Pillar Design Principle</div>
      <div class="mcq-q">Which architectural tenet represents a foundational principle of the Reliability Pillar in the Well-Architected Framework?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Build single monolithic servers with massive CPUs</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Never test disaster recovery plans</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Rely on human engineers to manually restart failed servers</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Automatically recover from failure by monitoring KPIs, triggering automated healing actions, and replacing failed nodes gracefully</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> The Reliability Pillar mandates building systems that anticipate failure, automatically healing and replacing degraded components without manual human intervention.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 25 • Cost Optimization Pillar Consumption Model</div>
      <div class="mcq-q">Under the Cost Optimization Pillar, what does "Adopt a consumption model" mean?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Buying as many servers as possible upfront</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Paying only for the computing resources that are actively consumed, and scaling resources up and down to match real-time business demand</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Consuming 100% of CPU at all times</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Eating lunch during cloud deployments</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> A consumption model aligns costs directly with demand, avoiding over-provisioned idle capacity by leveraging elasticity and serverless architectures.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 26 • Operational Excellence Operations as Code</div>
      <div class="mcq-q">What design principle of the Operational Excellence Pillar ensures infrastructure changes are repeatable, audited, and easily rolled back?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Perform operations as code (Infrastructure as Code via AWS CloudFormation or Terraform)</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Manually click buttons in the web console</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Deploy code changes directly to production on Friday evening</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Disable version control systems</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Performing operations as code allows entire multi-tier environments to be defined in declarative code, version-controlled, tested, and rolled back deterministically.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="C">
      <div class="mcq-num">Question 27 • Performance Efficiency Serverless Principle</div>
      <div class="mcq-q">How does adopting serverless architectures support the Performance Efficiency Pillar?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Serverless eliminates the need for computer programming</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Serverless makes all databases relational</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Removes the operational burden of managing physical servers, allowing systems to scale elastically from zero to tens of thousands of concurrent requests automatically</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Serverless allows instances to run without internet</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: C.</strong> Serverless architectures abstract host management and scale instantaneously with demand, optimizing compute efficiency and resource utilization.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="D">
      <div class="mcq-num">Question 28 • AWS Audit Manager Capability</div>
      <div class="mcq-q">What is the primary function of AWS Audit Manager?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Listening to audio calls with customers</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Auditing employee payroll taxes</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Testing network cable continuity</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Continuously and automatically collecting evidence of compliance with regulatory standards (HIPAA, GDPR, PCI DSS) to produce audit-ready assessment reports</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: D.</strong> Audit Manager automates evidence collection, mapping AWS resource configurations directly to industry compliance frameworks to simplify audit preparation.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="B">
      <div class="mcq-num">Question 29 • IAM Access Analyzer Mathematical Proof</div>
      <div class="mcq-q">What mathematical technology powers AWS IAM Access Analyzer to identify resource policies granting public or cross-account access?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Simple keyword text search</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Automated Reasoning (formal mathematical logic proofs verifying all possible access paths)</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Random guessing algorithms</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Quantum entanglement</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: B.</strong> IAM Access Analyzer uses automated reasoning (formal logic proofs) to mathematically prove whether a resource policy allows unintended public or cross-account access.
      </div>
    </div>

    <div class="mcq-card" data-unit="C6" data-correct="A">
      <div class="mcq-num">Question 30 • Sustainability Pillar Hardware Adoption</div>
      <div class="mcq-q">How does migrating workloads to AWS Graviton3 processors support the Sustainability Pillar of the Well-Architected Framework?</div>
      <div class="mcq-options">
        <div class="mcq-option" data-opt="A"><span class="opt-letter">A</span> Graviton3 processors deliver up to 60% lower energy consumption for the same performance compared to comparable x86 EC2 instances</div>
        <div class="mcq-option" data-opt="B"><span class="opt-letter">B</span> Graviton processors are made of recycled cardboard</div>
        <div class="mcq-option" data-opt="C"><span class="opt-letter">C</span> Graviton instances can only run during daytime solar hours</div>
        <div class="mcq-option" data-opt="D"><span class="opt-letter">D</span> Graviton processors do not use electricity</div>
      </div>
      <div class="mcq-explanation">
        <strong>Correct: A.</strong> Custom ARM-based Graviton3 processors achieve superior compute performance per watt, cutting electrical consumption and carbon footprints by up to 60%.
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Unit 06 Complete • Next: End-to-End Silicon & Fiber Trace</span>
    <span>Unit 06 • Page 06</span>
  </div>
</article>

<!-- Page 7: Unit 6 Conceptual Questions (5 Sets) -->
<article class="doc-page" id="practice-subj-short-c6">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 06</span>
    <span class="meta-tag">Conceptual Q&A • 5 Sets</span>
    <span class="meta-tag">Exam Weightage: 5 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">52.</span> Unit 6 Short Conceptual Questions (5 High-Yield Sets)
  </h2>

  <p class="lead-para">
    Targeted explanations of cryptographic envelope encryption, IAM evaluation algorithms, and perimeter defense layers.
  </p>

  <div class="subj-grid">
    <!-- Q1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q1</span> Explain the step-by-step cryptographic workflow of AWS KMS Envelope Encryption.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>1. The application requests a data key from KMS: `GenerateDataKey(KMSKeyId)`.
          <br>2. KMS uses the hardware-protected KMS Master Key inside the HSM to generate a plaintext Data Encryption Key (DEK) and an encrypted copy of that DEK.
          <br>3. KMS returns both the plaintext DEK and the encrypted DEK to the client over TLS.
          <br>4. The application uses the plaintext DEK to encrypt data locally using AES-GCM at memory bus speeds.
          <br>5. <strong>The application immediately zeroes out the plaintext DEK from RAM.</strong>
          <br>6. The encrypted DEK is stored as metadata alongside the ciphertext. To decrypt later, the encrypted DEK is sent to KMS (`kms:Decrypt`), which returns the plaintext key to decrypt the payload.
        </p>
      </div>
    </div>

    <!-- Q2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q2</span> Detail the complete IAM policy evaluation logic: Explicit Deny, SCPs, Permission Boundaries, and Explicit Allow.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p>Every authorization decision begins with a <strong>Default Deny</strong>. The evaluation engine applies the following order:
          <br>&bull; <strong>1. Explicit Deny:</strong> If any policy (Identity, Resource, SCP, Boundary) contains an explicit Deny, the request is immediately denied.
          <br>&bull; <strong>2. Organizations SCP:</strong> If the account belongs to an AWS Organization, the Service Control Policy must permit the action.
          <br>&bull; <strong>3. Permission Boundary:</strong> If attached, the boundary must allow the action.
          <br>&bull; <strong>4. Session Policy:</strong> If assuming a temporary STS role, session policies must allow the action.
          <br>&bull; <strong>5. Explicit Allow:</strong> An identity-based policy or resource policy must explicitly permit the action. If all checks pass, the decision is <strong>Allow</strong>; otherwise, it defaults to <strong>Deny</strong>.
        </p>
      </div>
    </div>

    <!-- Q3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q3</span> Contrast Amazon CloudWatch and AWS CloudTrail from an architectural and operational perspective.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Amazon CloudWatch:</strong> System performance and telemetry monitoring service. Collects numeric metrics (CPU, disk IOPS, network bytes) and text log streams. Evaluates alarms to trigger operational actions (Auto Scaling, SNS notifications, EC2 reboot). Focus: <em>"How are my resources performing?"</em></p>
        <p><strong>AWS CloudTrail:</strong> Governance and compliance audit trail service. Records cryptographic event records of every administrative and programmatic API call made in the account. Captures the exact IAM identity, timestamp, source IP address, user agent, and request parameters. Focus: <em>"Who modified my cloud resources, when, and from where?"</em></p>
      </div>
    </div>

    <!-- Q4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q4</span> Differentiate AWS WAF and AWS Shield regarding OSI layer protection and threat models.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>AWS WAF (Layer 7):</strong> Web Application Firewall inspecting application payloads (HTTP/HTTPS). Filters SQL Injection, Cross-Site Scripting (XSS), rate-limits brute-force login attempts, and blocks malicious web crawlers. Deployed on ALBs, CloudFront, and API Gateways.</p>
        <p><strong>AWS Shield (Layer 3 &amp; 4):</strong> Distributed Denial of Service (DDoS) protection. Shield Standard is automatically active on all edge endpoints, scrubbing SYN floods, UDP reflection, and DNS amplification attacks. Shield Advanced provides 24/7 access to the DDoS Response Team, automated Layer 7 mitigations, and financial cost protection against scaling charges.</p>
      </div>
    </div>

    <!-- Q5 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Q5</span> State the 6 Pillars of the AWS Well-Architected Framework and explain the core objective of the Sustainability Pillar.</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>The 6 Pillars:</strong> Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.</p>
        <p><strong>Sustainability Pillar Objective:</strong> Focuses on minimizing the environmental and carbon impact of running cloud workloads. Core practices include understanding energy consumption footprints, establishing reduction targets, maximizing resource utilization to eliminate idle compute waste, and adopting energy-efficient silicon such as AWS Graviton processors.</p>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 06 Analytical Problems</span>
    <span>Unit 06 • Page 07</span>
  </div>
</article>

<!-- Page 8: Unit 6 Analytical & Scenario Problems (4 Sets) -->
<article class="doc-page" id="practice-subj-long-c6">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 06</span>
    <span class="meta-tag">Analytical Scenarios • 4 Sets</span>
    <span class="meta-tag">Exam Weightage: 10 Marks</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">53.</span> Unit 6 Deep Analytical & Scenario Problems (4 Sets)
  </h2>

  <p class="lead-para">
    Real-world security breach investigations, privilege escalation exploits, and enterprise multi-account compliance audits.
  </p>

  <div class="subj-grid">
    <!-- Problem 1 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 01</span> Privilege Escalation Forensics: Investigating Unauthorized Administrator Creation via `iam:PassRole`</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> A disgruntled junior software developer with limited EC2 developer permissions successfully elevates their privileges to full AWS Administrator, modifies production database tables, and exfiltrates proprietary code.</p>
        <p><strong>Forensic Analysis &amp; Attack Vector:</strong></p>
        <ol>
          <li><strong>The IAM Policy Flaw:</strong> The developer's IAM policy permitted `ec2:RunInstances` and `iam:PassRole` with resource `*`. The policy lacked a restriction specifying which roles could be passed.</li>
          <li><strong>The Exploitation Path:</strong> The developer discovered an existing highly privileged IAM Role (`AdminServerRole`) containing `AdministratorAccess`. The developer executed `aws ec2 run-instances` with `--iam-instance-profile AdminServerRole` and embedded a user-data bash script that created a new backdoor IAM user with full administrative privileges!</li>
          <li><strong>Remediation:</strong>
            <br>&bull; Enforce the principle of least privilege: strictly scope `iam:PassRole` to only specific approved instance profile ARNs.
            <br>&bull; Attach an <strong>IAM Permission Boundary</strong> to all developer roles preventing them from creating or assuming any identity that exceeds developer-level permissions.
            <br>&bull; Implement AWS Config rule `iam-user-unused-credentials-check` and enable Amazon GuardDuty to alert instantly on suspicious IAM role assumptions from newly launched instances.
          </li>
        </ol>
      </div>
    </div>

    <!-- Problem 2 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 02</span> Ransomware Extortion Defense: S3 Object Lock &amp; CloudTrail Merkle Tree Non-Repudiation</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Incident Description:</strong> An attacker breaches corporate credentials and attempts to wipe out all financial transaction archives stored in an S3 bucket (`fin-archives`) while demanding $5,000,000 in Bitcoin.</p>
        <p><strong>Security Architecture Defense Evaluation:</strong></p>
        <ul>
          <li><strong>S3 Object Lock (Compliance Mode):</strong> The bucket had S3 Object Lock enabled in <strong>Compliance Mode</strong> with a 7-year retention period. When the attacker executed `aws s3 rm s3://fin-archives --recursive`, the API returned `AccessDenied`. In Compliance Mode, <em>even the AWS Account Root User is physically blocked from deleting objects or reducing retention</em>. The archives remained 100% intact.</li>
          <li><strong>CloudTrail Log Integrity:</strong> The attacker attempted to cover their tracks by deleting CloudTrail log files from the audit bucket. However, <strong>CloudTrail Log File Validation</strong> was active. Forensic auditors ran `aws cloudtrail validate-logs`, which mathematically proved using SHA-256 Merkle tree hashing that log files had been tampered with and restored authentic records from a read-only secondary compliance account.</li>
        </ul>
      </div>
    </div>

    <!-- Problem 3 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 03</span> Multi-Account Governance: Enforcing Data Residency via AWS Organizations Service Control Policies (SCPs)</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>Regulatory Mandate:</strong> Under the European Union General Data Protection Regulation (GDPR), a multinational bank mandates that all customer data and compute workloads must strictly reside inside EU AWS Regions (`eu-west-1`, `eu-central-1`). Creating resources in any non-EU Region (e.g. `us-east-1`, `ap-south-1`) is a severe legal violation incurring multi-million euro fines.</p>
        <p><strong>SCP Policy Implementation:</strong></p>
        <ul>
          <li>Attach the following Service Control Policy (SCP) at the root of the AWS Organization:</li>
        </ul>
        <div class="terminal-block">
          <div class="terminal-header">
            <div class="terminal-header-left">
              <span class="term-dot dot-red"></span>
              <span class="term-dot dot-yellow"></span>
              <span class="term-dot dot-green"></span>
              <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> AWS Organizations SCP • Region Guardrail</span>
            </div>
            <div class="terminal-actions">
              <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
            </div>
          </div>
          <pre class="code-pre"><code>{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAllOutsideEU",
      "Effect": "Deny",
      "NotAction": [
        "iam:*",
        "organizations:*",
        "route53:*",
        "cloudfront:*",
        "support:*",
        "kms:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": [
            "eu-west-1",
            "eu-central-1"
          ]
        }
      }
    }
  ]
}</code></pre>
        </div>
        <p><strong>Operational Impact:</strong> Even if a developer possesses full Administrator privileges inside a member account, any attempt to launch EC2, create S3 buckets, or provision RDS instances outside the approved EU regions is instantaneously rejected with `AccessDenied` by the AWS Nitro control plane.</p>
      </div>
    </div>

    <!-- Problem 4 -->
    <div class="subj-card">
      <div class="subj-header">
        <div class="subj-q"><span class="badge-sub">Scenario 04</span> Automated Configuration Drift Remediation: Auto-Remediating Unencrypted EBS Volumes via AWS Config &amp; SSM</div>
        <i data-lucide="chevron-down" class="subj-chevron"></i>
      </div>
      <div class="subj-body">
        <p><strong>System Engineering Request:</strong> Corporate infosec policy mandates that 100% of all Amazon EBS volumes must be encrypted with AWS KMS. The engineering team requires an automated solution that immediately detects and terminates any unencrypted volume launched by developers.</p>
        <p><strong>Event-Driven Remediation Architecture:</strong></p>
        <ol>
          <li><strong>Continuous Compliance Rule:</strong> Enable the AWS Config managed rule `encrypted-volumes`.</li>
          <li><strong>EventBridge Integration:</strong> When AWS Config detects an unencrypted volume, it transitions the resource state to `NON_COMPLIANT` and emits an event to Amazon EventBridge.</li>
          <li><strong>Automated Remediation Action:</strong> EventBridge triggers an <strong>AWS Systems Manager (SSM) Automation Runbook</strong>:
            <br>&bull; Step 1: Takes an immediate point-in-time snapshot of the non-compliant volume.
            <br>&bull; Step 2: Creates an encrypted copy of the snapshot using the corporate KMS customer-managed key.
            <br>&bull; Step 3: Detaches and terminates the unencrypted volume.
            <br>&bull; Step 4: Attaches the newly encrypted volume to the host EC2 instance and posts an incident alert to the Slack security operations channel.
          </li>
        </ol>
      </div>
    </div>
  </div>

  <div class="page-footer-meta">
    <span>Next: Unit 06 Master MCQ Answer Key</span>
    <span>Unit 06 • Page 08</span>
  </div>
</article>

<!-- Page 9: Master Answer Key Table -->
<article class="doc-page" id="mcq-answer-key-c6">
  <div class="page-header-meta">
    <span class="meta-tag">Cloud Administration • Unit 06</span>
    <span class="meta-tag">Master Answer Key • 30 Questions</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">54.</span> Unit 6 Master Answer Key Table &amp; Verification Matrix
  </h2>

  <p class="lead-para">
    Complete verified answer keys and core learning objectives for all 30 multiple choice questions in Unit 6.
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
        <tr><td>01</td><td><strong style="color:var(--primary);">B</strong></td><td>Explicit Deny unconditionally overriding any Allow</td><td>16</td><td><strong style="color:var(--primary);">D</strong></td><td>KMS automatic key rotation retaining historical backing keys</td></tr>
        <tr><td>02</td><td><strong style="color:var(--primary);">D</strong></td><td>Plaintext DEK memory zeroing in envelope encryption</td><td>17</td><td><strong style="color:var(--primary);">B</strong></td><td>Secrets Manager automated credential rotation via Lambda</td></tr>
        <tr><td>03</td><td><strong style="color:var(--primary);">A</strong></td><td>CloudTrail auditing API calls with IAM identity &amp; caller IP</td><td>18</td><td><strong style="color:var(--primary);">A</strong></td><td>High-Resolution CloudWatch metrics capturing down to 1s</td></tr>
        <tr><td>04</td><td><strong style="color:var(--primary);">C</strong></td><td>AWS Shield Advanced DDoS cost protection bill credits</td><td>19</td><td><strong style="color:var(--primary);">C</strong></td><td>Service Control Policy (SCP) maximum permission guardrail</td></tr>
        <tr><td>05</td><td><strong style="color:var(--primary);">B</strong></td><td>Sustainability Pillar focusing on environmental footprint</td><td>20</td><td><strong style="color:var(--primary);">D</strong></td><td>AWS Security Hub aggregating findings across services</td></tr>
        <tr><td>06</td><td><strong style="color:var(--primary);">A</strong></td><td>GuardDuty intelligent threat detection telemetry sources</td><td>21</td><td><strong style="color:var(--primary);">B</strong></td><td>Amazon Macie machine learning PII discovery in S3</td></tr>
        <tr><td>07</td><td><strong style="color:var(--primary);">C</strong></td><td>AWS Config continuous compliance rule evaluation</td><td>22</td><td><strong style="color:var(--primary);">A</strong></td><td>CloudWatch Metric Math composite alarm expressions</td></tr>
        <tr><td>08</td><td><strong style="color:var(--primary);">D</strong></td><td>AWS CloudHSM FIPS 140-2 Level 3 tamper-resistant hardware</td><td>23</td><td><strong style="color:var(--primary);">C</strong></td><td>Security Pillar applying defense in depth across all layers</td></tr>
        <tr><td>09</td><td><strong style="color:var(--primary);">B</strong></td><td>IAM Permission Boundary setting maximum privilege ceiling</td><td>24</td><td><strong style="color:var(--primary);">D</strong></td><td>Reliability Pillar automatically recovering from failure</td></tr>
        <tr><td>10</td><td><strong style="color:var(--primary);">A</strong></td><td>AWS WAF Layer 7 application layer HTTP/HTTPS inspection</td><td>25</td><td><strong style="color:var(--primary);">B</strong></td><td>Cost Optimization Pillar adopting a consumption model</td></tr>
        <tr><td>11</td><td><strong style="color:var(--primary);">C</strong></td><td>AWS Trusted Advisor 5 operational analysis pillars</td><td>26</td><td><strong style="color:var(--primary);">A</strong></td><td>Operational Excellence performing operations as code</td></tr>
        <tr><td>12</td><td><strong style="color:var(--primary);">D</strong></td><td>CloudTrail Log File Validation SHA-256 Merkle tree hashing</td><td>27</td><td><strong style="color:var(--primary);">C</strong></td><td>Performance Efficiency adopting serverless architectures</td></tr>
        <tr><td>13</td><td><strong style="color:var(--primary);">B</strong></td><td>Root account hardening with hardware MFA and locked credentials</td><td>28</td><td><strong style="color:var(--primary);">D</strong></td><td>AWS Audit Manager automated compliance evidence collection</td></tr>
        <tr><td>14</td><td><strong style="color:var(--primary);">A</strong></td><td>CloudWatch Synthetic canaries headless browser monitoring</td><td>29</td><td><strong style="color:var(--primary);">B</strong></td><td>IAM Access Analyzer automated reasoning formal logic proofs</td></tr>
        <tr><td>15</td><td><strong style="color:var(--primary);">C</strong></td><td>Amazon Inspector automated CVE vulnerability scanning</td><td>30</td><td><strong style="color:var(--primary);">A</strong></td><td>AWS Graviton3 processors 60% lower energy consumption</td></tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 06 Complete • Next: End-to-End Silicon & Fiber Trace</span>
    <span>Unit 06 • Page 09</span>
  </div>
</article>
"""
