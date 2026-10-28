# -*- coding: utf-8 -*-
"""
Cloud Administration Portal - Practical Laboratory Manual (Master Gold Standard)
10 Comprehensive Hands-On AWS Experiments with Terminal CLI, Verification, and Viva Questions
Exact layout, classes, and styling matching IT Fundamentals and Server Administration portals.
"""

CLOUD_LABS_HTML = r"""
<!-- ===================================================================
     HANDS-ON LABORATORY MANUAL: 10 ENTERPRISE AWS PRACTICALS
     =================================================================== -->
<article class="doc-page" id="cloud-labs-manual">
  <header class="doc-page-header">
    <span class="page-header-meta">Curriculum Lab Manual • Hands-On Enterprise Practicals</span>
    <h2 class="section-title"><span class="sec-num">LAB.1</span> Enterprise AWS Laboratory Manual: 10 Rigorous Hands-on Practicals</h2>
    <p class="lead-para">
      This practical lab manual provides end-to-end, reproducible engineering procedures conforming to the Department of Computer Science &amp; Engineering Cloud Administration syllabus. Each experiment includes exact AWS CLI v2 terminal commands, architectural topologies, apparatus &amp; prerequisites, expected execution outputs, troubleshooting scenarios, and oral examination (Viva Voce) question sets.
    </p>
  </header>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="terminal"></i> LABORATORY PREREQUISITES &amp; ENVIRONMENT SETUP</div>
    <div class="callout-body">
      Ensure you have an active AWS account (Free Tier or Academic Cloud Sandbox), the AWS CLI v2 installed locally (<code>aws --version</code>), an IAM User configured with programmatic access keys, and OpenSSH client tools for instance connectivity.
    </div>
  </div>

  <!-- LAB 1 -->
  <div class="subj-card revealed" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 01</div>
      <div class="subj-title">AWS Management Console, AWS CLI v2 Configuration, and IAM Multi-Factor Authentication</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Secure the root account, establish an administrative IAM Identity Center role / IAM User with Least Privilege permissions, configure AWS CLI credentials, and enforce Virtual MFA (TOTP).</p>
      <p><strong>Apparatus &amp; Tools:</strong> Workstation with AWS CLI v2 installed, modern web browser, authenticator app (Google Authenticator / Authy), and administrative terminal access.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • AWS CLI v2 IAM Configuration</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Verify AWS CLI v2 installation</span>
aws --version

<span class="code-comment"># 2. Configure AWS CLI with IAM Access Keys and default region</span>
aws configure
<span class="code-comment"># AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE</span>
<span class="code-comment"># AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY</span>
<span class="code-comment"># Default region name [None]: ap-south-1</span>
<span class="code-comment"># Default output format [None]: json</span>

<span class="code-comment"># 3. Create dedicated Administrator IAM Group and User</span>
aws iam create-group --group-name CloudAdminGroup
aws iam attach-group-policy --group-name CloudAdminGroup --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam create-user --user-name devops-admin
aws iam add-user-to-group --user-name devops-admin --group-name CloudAdminGroup

<span class="code-comment"># 4. Verify Identity and STS Caller Information</span>
aws sts get-caller-identity</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Command <code>aws sts get-caller-identity</code> returns a JSON document displaying <code>UserId</code>, <code>Account</code> ID (12-digit AWS account number), and <code>Arn: "arn:aws:iam::123456789012:user/devops-admin"</code> confirming successful IAM authentication without root exposure.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why should root account credentials never be used for daily administrative tasks?</strong><br>
          <em>Answer:</em> The root account possesses unrestricted, omnipotent privileges that cannot be constrained by IAM policies. Compromise of root credentials leads to total account loss and severe financial exploitation.<br><br>
          <strong>Q2: What is the difference between IAM Roles and IAM Users?</strong><br>
          <em>Answer:</em> IAM Users represent persistent individual human identities with long-term credentials (passwords/access keys), whereas IAM Roles are assumed temporarily by users or services to obtain short-term STS credentials (tokens expiring within 15 mins to 12 hours).
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 2 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 02</div>
      <div class="subj-title">Design &amp; Deployment of a Production Multi-AZ VPC with Public &amp; Private Subnets</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Construct an enterprise VPC (<code>10.0.0.0/16</code>) spanning 2 Availability Zones, containing 2 Public Subnets, 2 Private Subnets, an Internet Gateway (IGW), an Elastic IP, a NAT Gateway, and dedicated route tables.</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, bash/zsh shell with <code>jq</code> utility installed, and CIDR subnet calculation chart.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • VPC &amp; Subnet Provisioning</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create VPC with DNS hostnames enabled</span>
VPC_ID=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.VpcId' --output text)
aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-hostnames "{\"Value\":true}"

<span class="code-comment"># 2. Create Internet Gateway and attach to VPC</span>
IGW_ID=$(aws ec2 create-internet-gateway --query 'InternetGateway.InternetGatewayId' --output text)
aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $IGW_ID

<span class="code-comment"># 3. Create Public Subnet (AZ-1a) and Private Subnet (AZ-1b)</span>
PUB_SUB=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.1.0/24 --availability-zone ap-south-1a --query 'Subnet.SubnetId' --output text)
PRIV_SUB=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.10.0/24 --availability-zone ap-south-1a --query 'Subnet.SubnetId' --output text)

<span class="code-comment"># 4. Create Public Route Table and add default 0.0.0.0/0 route to IGW</span>
RTB_PUB=$(aws ec2 create-route-table --vpc-id $VPC_ID --query 'RouteTable.RouteTableId' --output text)
aws ec2 create-route --route-table-id $RTB_PUB --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID
aws ec2 associate-route-table --subnet-id $PUB_SUB --route-table-id $RTB_PUB</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Execute <code>aws ec2 describe-route-tables --route-table-id $RTB_PUB</code>. The route table confirms state <code>"active"</code> with two routes: local <code>10.0.0.0/16</code> and default route <code>0.0.0.0/0</code> pointing directly to <code>igw-xxxxxxxx</code>.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why are 5 IP addresses reserved in every AWS VPC subnet?</strong><br>
          <em>Answer:</em> AWS reserves 5 IPs per subnet: <code>.0</code> (Network ID), <code>.1</code> (VPC Router), <code>.2</code> (DNS Resolver / AmazonProvidedDNS), <code>.3</code> (Future reserve), and <code>.255</code> (Network broadcast).<br><br>
          <strong>Q2: Why must a NAT Gateway always reside in a Public Subnet?</strong><br>
          <em>Answer:</em> The NAT Gateway must translate private subnet IP addresses to its own Public Elastic IP to traverse the Internet Gateway. If placed in a private subnet, it lacks an IGW route and cannot reach the Internet.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 3 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 03</div>
      <div class="subj-title">EC2 Linux Instance Launch, UserData Bootstrapping, and Security Group Hardening</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Launch an Amazon Linux 2023 EC2 instance with automated UserData bootstrapping to install an NGINX web server, configure least-privilege security group ingress rules, and attach an Elastic IP.</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, OpenSSH keypair (<code>ec2-key.pem</code>), curl HTTP client, and security group firewall rule sheet.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • EC2 Instance Launch with UserData</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create Web Security Group allowing inbound HTTP (80) and restricted SSH (22)</span>
SG_ID=$(aws ec2 create-security-group --group-name WebSecurityGroup --description "Allow HTTP and SSH" --vpc-id $VPC_ID --query 'GroupId' --output text)
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 203.0.113.50/32

<span class="code-comment"># 2. Base64 encode UserData bootstrap script for NGINX</span>
cat << 'EOF' > userdata.sh
#!/bin/bash
dnf update -y
dnf install -y nginx
echo "<h1>Production Cloud Web Server • Instance $(hostname -f)</h1>" > /usr/share/nginx/html/index.html
systemctl enable --now nginx
EOF

<span class="code-comment"># 3. Launch EC2 instance (t3.micro) in Public Subnet</span>
INSTANCE_ID=$(aws ec2 run-instances \
    --image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64 \
    --instance-type t3.micro \
    --key-name CloudAdminKey \
    --security-group-ids $SG_ID \
    --subnet-id $PUB_SUB \
    --user-data file://userdata.sh \
    --query 'Instances[0].InstanceId' --output text)

<span class="code-comment"># 4. Wait for running state and fetch public IP</span>
aws ec2 wait instance-running --instance-ids $INSTANCE_ID
PUB_IP=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
curl -I http://$PUB_IP</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          The <code>curl -I</code> query returns <code>HTTP/1.1 200 OK</code>, <code>Server: nginx</code>, confirming that cloud-init parsed the UserData payload, configured systemd daemon units, and bound port 80 successfully on the public IP.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the key operational difference between Security Groups and Network ACLs (NACLs)?</strong><br>
          <em>Answer:</em> Security Groups operate at the instance/ENI level, are stateful (inbound allows return outbound automatically), and only support ALLOW rules. NACLs operate at the subnet boundary, are stateless, and evaluate ordered ALLOW and DENY rules.<br><br>
          <strong>Q2: When does an EC2 UserData script execute in the VM lifecycle?</strong><br>
          <em>Answer:</em> UserData scripts execute only once during the very first boot cycle (under root privileges) unless cloud-init is explicitly configured to rerun on subsequent reboots.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 4 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 04</div>
      <div class="subj-title">Application Load Balancer (ALB) and Auto Scaling Group (ASG) High-Availability Setup</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Deploy an Internet-facing Application Load Balancer across two availability zones, configure target group health checks, and launch a dynamic Auto Scaling Group configured with target-tracking scaling policies (Target CPU Utilization = 60%).</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, ApacheBench (<code>ab</code>) stress testing tool, and Multi-AZ VPC deployment from Lab 02.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • ALB Target Group &amp; ASG Provisioning</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create Target Group with HTTP health check</span>
TG_ARN=$(aws elbv2 create-target-group \
    --name web-app-tg \
    --protocol HTTP \
    --port 80 \
    --vpc-id $VPC_ID \
    --health-check-path / \
    --health-check-interval-seconds 30 \
    --query 'TargetGroups[0].TargetGroupArn' --output text)

<span class="code-comment"># 2. Create Application Load Balancer spanning Public Subnets</span>
ALB_ARN=$(aws elbv2 create-load-balancer \
    --name web-app-alb \
    --subnets $PUB_SUB $PUB_SUB_2 \
    --security-groups $ALB_SG \
    --query 'LoadBalancers[0].LoadBalancerArn' --output text)

<span class="code-comment"># 3. Create HTTP Listener forwarding traffic to Target Group</span>
aws elbv2 create-listener \
    --load-balancer-arn $ALB_ARN \
    --protocol HTTP --port 80 \
    --default-actions Type=forward,TargetGroupArn=$TG_ARN

<span class="code-comment"># 4. Create Launch Template and Auto Scaling Group (Min=2, Desired=2, Max=6)</span>
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name web-asg \
    --launch-template LaunchTemplateName=web-template,Version='$Latest' \
    --min-size 2 --max-size 6 --desired-capacity 2 \
    --target-group-arns $TG_ARN \
    --vpc-zone-identifier "$PRIV_SUB,$PRIV_SUB_2" \
    --health-check-type ELB --health-check-grace-period 300</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Run <code>aws elbv2 describe-target-health --target-group-arn $TG_ARN</code>. Both backend EC2 instances register state <code>"healthy"</code>, and sending 1,000 HTTP requests via <code>curl</code> across the ALB DNS name displays alternating instance hostnames verifying round-robin distribution.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What happens when an ASG instance fails an ELB health check?</strong><br>
          <em>Answer:</em> The load balancer stops routing traffic to the unhealthy target. The Auto Scaling Group marks the instance unhealthy, terminates it, and launches a replacement instance to maintain desired capacity.<br><br>
          <strong>Q2: Why is health check grace period necessary in an ASG?</strong><br>
          <em>Answer:</em> It provides a buffer window (e.g., 300 seconds) allowing newly launched instances to complete bootstrapping, install software, and start services before health check evaluations begin, preventing premature termination.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 5 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 05</div>
      <div class="subj-title">Amazon S3 Static Website Hosting, Bucket Policies &amp; CloudFront Distribution</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Create an Amazon S3 bucket, configure static website hosting, enforce HTTPS-only access via CloudFront Origin Access Control (OAC), and define bucket lifecycle transitions.</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, static HTML/CSS web assets, and Amazon CloudFront CDN console.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • S3 Website &amp; CloudFront CDN Configuration</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create S3 Bucket with unique name</span>
BUCKET_NAME="cloud-portal-$(date +%s)"
aws s3 mb s3://$BUCKET_NAME --region ap-south-1

<span class="code-comment"># 2. Upload website static assets with gzip headers</span>
aws s3 cp ./index.html s3://$BUCKET_NAME/index.html --content-type "text/html"
aws s3 cp ./error.html s3://$BUCKET_NAME/error.html --content-type "text/html"

<span class="code-comment"># 3. Configure Lifecycle Rule (Transition to Standard-IA at 30 days, Glacier Flexible at 90 days)</span>
cat << 'EOF' > lifecycle.json
{
  "Rules": [
    {
      "ID": "ArchiveLogs",
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Transitions": [
        { "Days": 30, "StorageClass": "STANDARD_IA" },
        { "Days": 90, "StorageClass": "GLACIER" }
      ],
      "Expiration": { "Days": 365 }
    }
  ]
}
EOF
aws s3api put-bucket-lifecycle-configuration --bucket $BUCKET_NAME --lifecycle-configuration file://lifecycle.json</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Verify via <code>aws s3api get-bucket-lifecycle-configuration --bucket $BUCKET_NAME</code>. Output confirms rule <code>ArchiveLogs</code> is active with two transition stages and object expiration set at 365 days.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why is CloudFront Origin Access Control (OAC) preferred over public S3 buckets?</strong><br>
          <em>Answer:</em> OAC ensures the S3 bucket remains entirely private: users cannot bypass CloudFront edge security, WAF filtering, or caching, preventing direct origin scraping and unauthorized bandwidth consumption.<br><br>
          <strong>Q2: What is the minimum billable object size and duration for S3 Standard-IA?</strong><br>
          <em>Answer:</em> S3 Standard-IA imposes a minimum billable size of 128 KB and a minimum retention duration of 30 days. Objects smaller or deleted earlier incur penalty charges.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 6 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 06</div>
      <div class="subj-title">Amazon EBS Volume Management: Provisioning, XFS Formatting, Snapshots &amp; Elastic Volumes</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Create a 50 GiB General Purpose SSD (gp3) volume, attach to an EC2 instance, format as XFS, configure persistent mount via <code>/etc/fstab</code> with UUID, create automated snapshots, and modify volume size live using Elastic Volumes.</p>
      <p><strong>Apparatus &amp; Tools:</strong> Running EC2 Linux instance, AWS CLI v2, Linux utilities (<code>lsblk</code>, <code>mkfs.xfs</code>, <code>blkid</code>, <code>xfs_growfs</code>).</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • EBS Mounting &amp; Expansion</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. View attached block devices</span>
lsblk

<span class="code-comment"># 2. Format new secondary volume with high-performance XFS</span>
sudo mkfs.xfs /dev/nvme1n1

<span class="code-comment"># 3. Mount and register in fstab using permanent UUID</span>
sudo mkdir -p /data
UUID=$(sudo blkid -s UUID -o value /dev/nvme1n1)
echo "UUID=$UUID /data xfs defaults,nofail 0 2" | sudo tee -a /etc/fstab
sudo mount -a

<span class="code-comment"># 4. Online filesystem expansion after modifying volume size in AWS CLI</span>
sudo xfs_growfs -d /data</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Command <code>df -h /data</code> reports the full mounted capacity (e.g. <code>50G</code> or expanded <code>100G</code>) with filesystem type <code>xfs</code>. A simulated reboot confirms persistent remounting without boot hangs thanks to the <code>nofail</code> flag.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the benefit of EBS Elastic Volumes?</strong><br>
          <em>Answer:</em> Elastic Volumes permit live modifications to EBS capacity, IOPS, and volume types (e.g. gp2 to gp3) on-the-fly without detaching the disk or rebooting the running instance.<br><br>
          <strong>Q2: Why must you use UUID instead of device names (/dev/xvdf) in /etc/fstab?</strong><br>
          <em>Answer:</em> In modern Nitro instances, NVMe drive device nodes can be assigned dynamically during boot, causing traditional drive letters to shift. The filesystem UUID remains completely static across all reboot cycles.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 7 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 07</div>
      <div class="subj-title">Amazon RDS Multi-AZ MySQL Deployment, Read Replica Provisioning &amp; Failover Simulation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Deploy an Amazon RDS MySQL instance in Multi-AZ configuration across two subnets in a DB Subnet Group, provision an asynchronous Read Replica in a separate AZ for read offloading, and simulate primary database failover.</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, MySQL Client CLI (<code>mysql</code>), and DB Subnet Group across 2 Availability Zones.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • RDS Multi-AZ Failover</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Provision Multi-AZ MySQL 8.0 Database Instance</span>
aws rds create-db-instance \
    --db-instance-identifier mysql-prod \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --master-username admin \
    --master-user-password "ProdDBPass2026!" \
    --allocated-storage 20 \
    --multi-az \
    --db-subnet-group-name db-subnet-grp

<span class="code-comment"># 2. Simulate Multi-AZ manual failover to standby replica</span>
aws rds reboot-db-instance --db-instance-identifier mysql-prod --force-failover

<span class="code-comment"># 3. Monitor failover event stream in real-time</span>
aws rds describe-events --source-identifier mysql-prod --source-type db-instance</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Event stream displays <code>"Multi-AZ instance failover started"</code> followed by <code>"Multi-AZ instance failover completed"</code>. The CNAME record for <code>mysql-prod.xxxxxx.ap-south-1.rds.amazonaws.com</code> automatically flips to the new primary IP in under 60 seconds with zero data loss.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: How does replication differ between Multi-AZ RDS and Read Replicas?</strong><br>
          <em>Answer:</em> Multi-AZ uses synchronous physical block-level replication to a standby instance strictly for high availability/disaster recovery. Read Replicas use asynchronous logical replication to separate database instances to serve read traffic and queries.<br><br>
          <strong>Q2: Can client applications query the standby replica in a standard Multi-AZ RDS configuration?</strong><br>
          <em>Answer:</em> No. In standard Multi-AZ, the standby instance does not accept client connections and does not have an independent DNS endpoint. It only activates upon failover.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 8 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 08</div>
      <div class="subj-title">Serverless Microservice: AWS Lambda (Python 3.12), Amazon API Gateway &amp; DynamoDB CRUD</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Build a fully serverless REST API that writes and reads items from Amazon DynamoDB, orchestrated via Amazon API Gateway HTTP API and AWS Lambda.</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, Python 3.12 runtime, Boto3 SDK, and Postman or cURL for REST API payload verification.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS Lambda Code:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Python 3.12 • AWS Lambda Function Handler</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># Serverless Python Lambda handler interacting with DynamoDB table</span>
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRegistry')

def lambda_handler(event, context):
    http_method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')
    
    if http_method == 'POST':
        body = json.loads(event.get('body', '{}'))
        table.put_item(Item={'student_id': body['id'], 'name': body['name'], 'course': body['course']})
        return {'statusCode': 201, 'body': json.dumps({'message': 'Record persisted successfully'})}
    elif http_method == 'GET':
        response = table.scan(Limit=50)
        return {'statusCode': 200, 'body': json.dumps(response.get('Items', []))}
    
    return {'statusCode': 400, 'body': 'Unsupported HTTP Method'}</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Testing via <code>curl -X POST -d '{"id":"CSE101","name":"Alice","course":"Cloud"}' $API_URL/students</code> returns HTTP 201 <code>{"message": "Record persisted successfully"}</code>, and querying the DynamoDB table confirms the new item attributes.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is a Lambda "Cold Start" and how can it be mitigated?</strong><br>
          <em>Answer:</em> A cold start occurs when an invocation requires downloading code, initializing the execution runtime environment, and running setup code. It can be mitigated using Provisioned Concurrency, lighter deployment packages, or smaller memory profiles.<br><br>
          <strong>Q2: What is the maximum execution duration for an individual AWS Lambda invocation?</strong><br>
          <em>Answer:</em> 900 seconds (15 minutes). Workloads exceeding this threshold should be transitioned to AWS Fargate (ECS/EKS) or orchestrated via AWS Step Functions.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 9 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 09</div>
      <div class="subj-title">Operational Monitoring: CloudWatch Alarms, Metric Filters, SNS Alerts &amp; CloudTrail Auditing</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure an Amazon CloudWatch Alarm triggering an Amazon SNS email notification when EC2 CPU Utilization exceeds 80% for two consecutive 1-minute evaluation periods; analyze security events using AWS CloudTrail logs.</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, Amazon CloudWatch, Amazon SNS topic subscription, and AWS CloudTrail event stream.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> Terminal • CloudWatch Alarm &amp; CloudTrail Query</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Create SNS Topic and subscribe administrator email</span>
SNS_ARN=$(aws sns create-topic --name HighCpuAlertTopic --query 'TopicArn' --output text)
aws sns subscribe --topic-arn $SNS_ARN --protocol email --notification-endpoint admin@corp.contoso.com

<span class="code-comment"># 2. Put Metric Alarm for EC2 CPU Utilization > 80%</span>
aws cloudwatch put-metric-alarm \
    --alarm-name "High-CPU-Utilization" \
    --metric-name CPUUtilization \
    --namespace AWS/EC2 \
    --statistic Average \
    --period 60 \
    --threshold 80 \
    --comparison-operator GreaterThanThreshold \
    --dimensions Name=InstanceId,Value=$INSTANCE_ID \
    --evaluation-periods 2 \
    --alarm-actions $SNS_ARN

<span class="code-comment"># 3. Query CloudTrail for unauthorized or console login events</span>
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin \
    --max-results 10 \
    --query 'Events[*].[EventTime,Username,EventName]' --output table</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Simulating CPU load via <code>stress --cpu 4 --timeout 180s</code> shifts the CloudWatch Alarm state from <code>OK</code> to <code>ALARM</code>. An automated notification email arrives with the exact metric value, timestamp, and instance identifier.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is the core difference between CloudWatch and CloudTrail?</strong><br>
          <em>Answer:</em> CloudWatch monitors performance telemetry, metrics (CPU, RAM, disk I/O), application logs, and triggers automated alerts. CloudTrail audits management plane API calls, tracking <em>who</em> made <em>what</em> API call, from <em>which IP</em>, and at <em>what time</em>.<br><br>
          <strong>Q2: Why does EC2 memory utilization require the unified CloudWatch Agent?</strong><br>
          <em>Answer:</em> The hypervisor cannot inspect guest OS internal virtual memory allocation without violating privacy boundaries. RAM telemetry requires an in-guest OS agent collecting OS-level performance counters.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 10 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(6, 182, 212, 0.15); color: #22d3ee; border-color: rgba(6, 182, 212, 0.3);">LAB 10</div>
      <div class="subj-title">Infrastructure as Code (IaC): Multi-Tier Architecture Provisioning via AWS CloudFormation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Write a declarative YAML CloudFormation template modeling a complete 2-tier architecture (VPC, Subnets, Internet Gateway, EC2 instance, and Security Groups), and manage deployment lifecycles with change sets and drift detection.</p>
      <p><strong>Apparatus &amp; Tools:</strong> AWS CLI v2, YAML syntax linter (<code>cfn-lint</code>), and CloudFormation template designer.</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CloudFormation Commands:</h4>
      <div class="terminal-block full-width-module">
        <div class="terminal-header">
          <div class="terminal-header-left">
            <span class="term-dot dot-red"></span>
            <span class="term-dot dot-yellow"></span>
            <span class="term-dot dot-green"></span>
            <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> YAML &amp; CLI • AWS CloudFormation Stack Provisioning</span>
          </div>
          <div class="terminal-actions">
            <button class="btn-term-action btn-toggle-comments" title="Show / Hide Comments"><i data-lucide="eye" style="width:12px;height:12px;"></i> <span>Comments</span></button>
            <button class="btn-term-action btn-copy-code" title="Copy Command Code"><i data-lucide="copy" style="width:12px;height:12px;"></i> <span>Copy</span></button>
          </div>
        </div>
        <div class="terminal-body">
          <pre class="code-pre"><code><span class="code-comment"># 1. Author Declarative YAML CloudFormation Template</span>
cat << 'EOF' > vpc-stack.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Enterprise Production 2-Tier VPC Stack'
Resources:
  ProductionVPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      CidrBlock: '10.50.0.0/16'
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Environment
          Value: Production
EOF

<span class="code-comment"># 2. Deploy CloudFormation Stack via CLI</span>
aws cloudformation create-stack \
    --stack-name ProductionInfrastructureStack \
    --template-body file://vpc-stack.yaml \
    --tags Key=Owner,Value=DevOpsAdmin

<span class="code-comment"># 3. Wait for complete stack deployment and verify resources</span>
aws cloudformation wait stack-create-complete --stack-name ProductionInfrastructureStack
aws cloudformation describe-stack-resources --stack-name ProductionInfrastructureStack</code></pre>
        </div>
      </div>

      <div class="callout callout-key" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="check-circle-2"></i> VERIFICATION &amp; EXPECTED OUTPUT</div>
        <div class="callout-body">
          Output confirms <code>"StackStatus": "CREATE_COMPLETE"</code>. Executing <code>aws cloudformation detect-stack-drift --stack-name ProductionInfrastructureStack</code> yields <code>"StackDriftStatus": "IN_SYNC"</code>, proving that physical resources match the declarative template specification.
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top: 1rem;">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: What is Stack Drift in CloudFormation and how is it detected?</strong><br>
          <em>Answer:</em> Stack drift occurs when infrastructure configurations are modified outside of CloudFormation (e.g. through the AWS Console or manual CLI). CloudFormation drift detection compares current live resource properties with the expected template configuration.<br><br>
          <strong>Q2: What is the function of CloudFormation Change Sets?</strong><br>
          <em>Answer:</em> Change Sets allow engineers to preview how proposed stack updates will impact running resources (e.g., whether an update will perform an in-place modification or require destructive resource recreation) prior to execution.
        </div>
      </div>
    </div>
  </div>

</article>
"""
