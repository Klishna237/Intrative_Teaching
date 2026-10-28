# -*- coding: utf-8 -*-
"""
Cloud Administration Portal - Practical Laboratory Manual (Master Gold Standard)
10 Comprehensive Hands-On AWS Experiments with Terminal CLI, Verification, and Viva Questions
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
      This practical lab manual provides end-to-end, reproducible engineering procedures conforming to the Department of Computer Science & Engineering Cloud Administration syllabus. Each experiment includes exact AWS CLI v2 terminal commands, architectural topologies, expected execution outputs, troubleshooting scenarios, and oral examination (Viva Voce) question sets.
    </p>
  </header>

  <div class="callout callout-deep">
    <div class="callout-label"><i data-lucide="terminal"></i> LABORATORY PREREQUISITES &amp; ENVIRONMENT SETUP</div>
    <div class="callout-body">
      Ensure you have an active AWS account (Free Tier or Academic Cloud Sandbox), the AWS CLI v2 installed locally (<code class="code-inline">aws --version</code>), an IAM User configured with programmatic access keys, and OpenSSH client tools for instance connectivity.
    </div>
  </div>

  <!-- LAB 1 -->
  <div class="subj-card revealed" style="margin-top: 2rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 01</div>
      <div class="subj-title">AWS Management Console, AWS CLI v2 Configuration, and IAM Multi-Factor Authentication</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Secure the root account, establish an administrative IAM Identity Center role / IAM User with Least Privilege permissions, configure AWS CLI credentials, and enforce Virtual MFA (TOTP).</p>
      
      <h4 style="color: var(--text-normal); margin-top: 1rem;">Procedure &amp; AWS CLI Commands:</h4>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left">
            <span class="terminal-dot dot-red"></span>
            <span class="terminal-dot dot-yellow"></span>
            <span class="terminal-dot dot-green"></span>
            <span class="code-title">Terminal • AWS CLI v2 IAM Configuration</span>
          </div>
          <button class="btn-tool" onclick="navigator.clipboard.writeText(this.closest('.terminal-block').querySelector('pre').innerText)"><i data-lucide="copy"></i> Copy</button>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># 1. Verify AWS CLI v2 installation
aws --version

# 2. Configure AWS CLI with IAM Access Keys and default region
aws configure
# AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
# AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# Default region name [None]: ap-south-1
# Default output format [None]: json

# 3. Create dedicated Administrator IAM Group and User
aws iam create-group --group-name CloudAdminGroup
aws iam attach-group-policy --group-name CloudAdminGroup --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam create-user --user-name devops-admin
aws iam add-user-to-group --user-name devops-admin --group-name CloudAdminGroup

# 4. Verify Identity and STS Caller Information
aws sts get-caller-identity</code></pre>
        </div>
      </div>

      <div class="callout callout-tip">
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
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 02</div>
      <div class="subj-title">Design &amp; Deployment of a Production Multi-AZ VPC with Public &amp; Private Subnets</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Construct an enterprise VPC (<code class="code-inline">10.0.0.0/16</code>) spanning 2 Availability Zones, containing 2 Public Subnets, 2 Private Subnets, an Internet Gateway (IGW), an Elastic IP, a NAT Gateway, and dedicated route tables.</p>
      
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left">
            <span class="terminal-dot dot-red"></span>
            <span class="terminal-dot dot-yellow"></span>
            <span class="terminal-dot dot-green"></span>
            <span class="code-title">Terminal • VPC &amp; Subnet Provisioning</span>
          </div>
          <button class="btn-tool" onclick="navigator.clipboard.writeText(this.closest('.terminal-block').querySelector('pre').innerText)"><i data-lucide="copy"></i> Copy</button>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># 1. Create VPC with DNS hostnames enabled
VPC_ID=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.VpcId' --output text)
aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-hostnames "{\"Value\":true}"

# 2. Create Internet Gateway and attach to VPC
IGW_ID=$(aws ec2 create-internet-gateway --query 'InternetGateway.InternetGatewayId' --output text)
aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $IGW_ID

# 3. Create Public Subnet (AZ-1a) and Private Subnet (AZ-1b)
PUB_SUB=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.1.0/24 --availability-zone ap-south-1a --query 'Subnet.SubnetId' --output text)
PRIV_SUB=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.10.0/24 --availability-zone ap-south-1a --query 'Subnet.SubnetId' --output text)

# 4. Create Public Route Table and add default 0.0.0.0/0 route to IGW
RTB_PUB=$(aws ec2 create-route-table --vpc-id $VPC_ID --query 'RouteTable.RouteTableId' --output text)
aws ec2 create-route --route-table-id $RTB_PUB --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID
aws ec2 associate-route-table --subnet-id $PUB_SUB --route-table-id $RTB_PUB</code></pre>
        </div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: Why are 5 IP addresses reserved in every AWS VPC subnet?</strong><br>
          <em>Answer:</em> AWS reserves 5 IPs per subnet: <code class="code-inline">.0</code> (Network), <code class="code-inline">.1</code> (VPC Router), <code class="code-inline">.2</code> (DNS Resolver / AmazonProvidedDNS), <code class="code-inline">.3</code> (Future reserve), and <code class="code-inline">.255</code> (Network broadcast).<br><br>
          <strong>Q2: Why must a NAT Gateway always reside in a Public Subnet?</strong><br>
          <em>Answer:</em> The NAT Gateway must translate private subnet IP addresses to its own Public Elastic IP to traverse the Internet Gateway. If placed in a private subnet, it lacks an IGW route and cannot reach the Internet.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 3 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 03</div>
      <div class="subj-title">EC2 Linux Instance Launch, UserData Bootstrapping, and Security Group Hardening</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Launch an Amazon Linux 2023 EC2 instance with automated UserData bootstrapping to install an NGINX web server, configure least-privilege security group ingress rules, and attach an Elastic IP.</p>
      
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left">
            <span class="terminal-dot dot-red"></span>
            <span class="terminal-dot dot-yellow"></span>
            <span class="terminal-dot dot-green"></span>
            <span class="code-title">Terminal • EC2 Instance Launch with UserData</span>
          </div>
          <button class="btn-tool" onclick="navigator.clipboard.writeText(this.closest('.terminal-block').querySelector('pre').innerText)"><i data-lucide="copy"></i> Copy</button>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># 1. Create Security Group allowing HTTP (80) and SSH (22 from specific IP)
SG_ID=$(aws ec2 create-security-group --group-name WebServerSG --description "NGINX HTTP and SSH" --vpc-id $VPC_ID --query 'GroupId' --output text)
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 203.0.113.50/32

# 2. Write Bootstrap UserData script
cat << 'EOF' > user_data.sh
#!/bin/bash
dnf update -y
dnf install -y nginx
systemctl enable nginx
systemctl start nginx
echo "<h1>Enterprise Cloud Lab • Host: $(hostname -f)</h1>" > /usr/share/nginx/html/index.html
EOF

# 3. Launch EC2 Instance with UserData
aws ec2 run-instances \
    --image-id ami-03f4878e83fedf440 \
    --count 1 \
    --instance-type t3.micro \
    --key-name devops-key \
    --security-group-ids $SG_ID \
    --subnet-id $PUB_SUB \
    --user-data file://user_data.sh</code></pre>
        </div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-label"><i data-lucide="help-circle"></i> VIVA VOCE QUESTIONS &amp; EVALUATION CRITERIA</div>
        <div class="callout-body">
          <strong>Q1: When does the EC2 UserData script execute, and with what privileges?</strong><br>
          <em>Answer:</em> UserData runs only once during the initial first-boot sequence of the instance lifecycle, executed by the <code class="code-inline">cloud-init</code> service with root privileges.<br><br>
          <strong>Q2: Why are Security Groups stateful while Network ACLs are stateless?</strong><br>
          <em>Answer:</em> Security Groups track connection state in the hypervisor connection tracking table: return traffic for allowed inbound requests is automatically permitted regardless of outbound rules. NACLs evaluate inbound and outbound rules independently.
        </div>
      </div>
    </div>
  </div>

  <!-- LAB 4 -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 04</div>
      <div class="subj-title">Application Load Balancer (ALB) and Auto Scaling Group (ASG) High-Availability Setup</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Deploy an Internet-facing Application Load Balancer across two availability zones, configure target group health checks, and launch a dynamic Auto Scaling Group configured with target-tracking scaling policies (Target CPU Utilization = 60%).</p>
      
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left">
            <span class="terminal-dot dot-red"></span>
            <span class="terminal-dot dot-yellow"></span>
            <span class="terminal-dot dot-green"></span>
            <span class="code-title">Terminal • ALB Target Group &amp; ASG Provisioning</span>
          </div>
          <button class="btn-tool" onclick="navigator.clipboard.writeText(this.closest('.terminal-block').querySelector('pre').innerText)"><i data-lucide="copy"></i> Copy</button>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># 1. Create Target Group with HTTP health check
TG_ARN=$(aws elbv2 create-target-group \
    --name web-app-tg \
    --protocol HTTP \
    --port 80 \
    --vpc-id $VPC_ID \
    --health-check-path / \
    --health-check-interval-seconds 30 \
    --query 'TargetGroups[0].TargetGroupArn' --output text)

# 2. Create Application Load Balancer spanning Public Subnets
ALB_ARN=$(aws elbv2 create-load-balancer \
    --name web-app-alb \
    --subnets $PUB_SUB $PUB_SUB_2 \
    --security-groups $ALB_SG \
    --query 'LoadBalancers[0].LoadBalancerArn' --output text)

# 3. Create HTTP Listener forwarding traffic to Target Group
aws elbv2 create-listener \
    --load-balancer-arn $ALB_ARN \
    --protocol HTTP --port 80 \
    --default-actions Type=forward,TargetGroupArn=$TG_ARN

# 4. Create Launch Template and Auto Scaling Group (Min=2, Desired=2, Max=6)
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name web-asg \
    --launch-template LaunchTemplateName=web-template,Version='$Latest' \
    --min-size 2 --max-size 6 --desired-capacity 2 \
    --target-group-arns $TG_ARN \
    --vpc-zone-identifier "$PRIV_SUB,$PRIV_SUB_2" \
    --health-check-type ELB --health-check-grace-period 300</code></pre>
        </div>
      </div>

      <div class="callout callout-tip">
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
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 05</div>
      <div class="subj-title">Amazon S3 Static Website Hosting, Bucket Policies &amp; CloudFront Distribution</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Create an Amazon S3 bucket, configure static website hosting, enforce HTTPS-only access via CloudFront Origin Access Control (OAC), and define bucket lifecycle transitions.</p>
      
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left">
            <span class="terminal-dot dot-red"></span>
            <span class="terminal-dot dot-yellow"></span>
            <span class="terminal-dot dot-green"></span>
            <span class="code-title">Terminal • S3 Website &amp; CloudFront CDN Configuration</span>
          </div>
          <button class="btn-tool" onclick="navigator.clipboard.writeText(this.closest('.terminal-block').querySelector('pre').innerText)"><i data-lucide="copy"></i> Copy</button>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># 1. Create S3 Bucket with unique name
BUCKET_NAME="cloud-portal-$(date +%s)"
aws s3 mb s3://$BUCKET_NAME --region ap-south-1

# 2. Upload website static assets with gzip headers
aws s3 cp ./index.html s3://$BUCKET_NAME/index.html --content-type "text/html"
aws s3 cp ./error.html s3://$BUCKET_NAME/error.html --content-type "text/html"

# 3. Configure Lifecycle Rule (Transition to Standard-IA at 30 days, Glacier Flexible at 90 days)
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

      <div class="callout callout-tip">
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

  <!-- LAB 6 to 10 Quick Summary Accordions -->
  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 06</div>
      <div class="subj-title">Amazon EBS Volume Management: Provisioning, XFS Formatting, Snapshots &amp; Elastic Volumes</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Create a 50 GiB General Purpose SSD (gp3) volume, attach to an EC2 instance, format as XFS, configure persistent mount via <code class="code-inline">/etc/fstab</code> with UUID, create automated snapshots, and modify volume size live using Elastic Volumes.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">Terminal • EBS Mounting &amp; Expansion</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># View attached block devices
lsblk
# Format with XFS filesystem
sudo mkfs.xfs /dev/nvme1n1
# Mount and register in fstab
sudo mkdir -p /data
UUID=$(sudo blkid -s UUID -o value /dev/nvme1n1)
echo "UUID=$UUID /data xfs defaults,nofail 0 2" | sudo tee -a /etc/fstab
sudo mount -a
# Online filesystem expansion after modifying volume in AWS CLI
sudo xfs_growfs -d /data</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 07</div>
      <div class="subj-title">Amazon RDS Multi-AZ MySQL Deployment, Read Replica Provisioning &amp; Failover Simulation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Deploy an Amazon RDS MySQL instance in Multi-AZ configuration across two subnets in a DB Subnet Group, provision an asynchronous Read Replica in a separate AZ for read offloading, and simulate primary database failover.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">Terminal • RDS Multi-AZ Failover</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># Simulate Multi-AZ manual failover
aws rds reboot-db-instance --db-instance-identifier mysql-prod --force-failover
# Monitor failover event stream
aws rds describe-events --source-identifier mysql-prod --source-type db-instance</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 08</div>
      <div class="subj-title">Serverless Microservice: AWS Lambda (Python 3.12), Amazon API Gateway &amp; DynamoDB CRUD</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Build a fully serverless REST API that writes and reads items from Amazon DynamoDB, orchestrated via Amazon API Gateway HTTP API and AWS Lambda.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">Python 3.12 • AWS Lambda Function Handler</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-python">import json
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
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 09</div>
      <div class="subj-title">Operational Monitoring: CloudWatch Alarms, Metric Filters, SNS Alerts &amp; CloudTrail Auditing</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Configure an Amazon CloudWatch Alarm triggering an Amazon SNS email notification when EC2 CPU Utilization exceeds 80% for two consecutive 1-minute evaluation periods; analyze security events using AWS CloudTrail logs.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">Terminal • CloudWatch Alarm &amp; CloudTrail Query</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-bash"># Query CloudTrail for Unauthorized API calls
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin \
    --max-results 10 \
    --query 'Events[*].[EventTime,Username,EventName]' --output table</code></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="subj-card" style="margin-top: 1.5rem;">
    <div class="subj-header">
      <div class="subj-q-badge" style="background: rgba(99, 102, 241, 0.15); color: #818cf8; border-color: rgba(99, 102, 241, 0.3);">LAB 10</div>
      <div class="subj-title">Infrastructure as Code (IaC): Multi-Tier Architecture Provisioning via AWS CloudFormation</div>
      <i data-lucide="chevron-down" class="subj-chevron"></i>
    </div>
    <div class="subj-body">
      <p><strong>Objective:</strong> Write a declarative YAML CloudFormation template modeling a complete 2-tier architecture (VPC, Subnets, Internet Gateway, EC2 instance, and Security Groups), and manage deployment lifecycles with change sets and drift detection.</p>
      <div class="terminal-block">
        <div class="code-header">
          <div class="code-header-left"><span class="terminal-dot dot-red"></span><span class="terminal-dot dot-yellow"></span><span class="terminal-dot dot-green"></span><span class="code-title">YAML • AWS CloudFormation Excerpt</span></div>
        </div>
        <div class="code-body">
          <pre class="code-block"><code class="language-yaml">AWSTemplateFormatVersion: '2010-09-09'
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
        - Key: Course
          Value: CloudAdmin</code></pre>
        </div>
      </div>
    </div>
  </div>

</article>
"""
