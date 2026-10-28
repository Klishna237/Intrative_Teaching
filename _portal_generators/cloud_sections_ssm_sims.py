# -*- coding: utf-8 -*-
"""
Cloud Administration Portal - Interactive Engineering Calculators & AWS CLI Sandbox
Master Gold Standard
"""

CLOUD_SIMS_HTML = r"""
<!-- ===================================================================
     INTERACTIVE ENGINEERING TOOLS & MASTER AWS CLI TERMINAL SANDBOX
     =================================================================== -->
<article class="doc-page" id="cloud-simulators-tools">
  <header class="doc-page-header">
    <span class="page-header-meta">Engineering Utilities • Interactive Cloud Simulators</span>
    <h2 class="section-title"><span class="sec-num">SIM.1</span> Interactive Cloud Engineering Calculators &amp; Live AWS CLI Sandbox</h2>
    <p class="lead-para">
      Perform real-time calculations for subnet sizing, EBS IOPS baseline provisioning, Aurora storage quorum fault tolerance, and execute live commands in an embedded interactive AWS CLI v2 terminal emulator.
    </p>
  </header>

  <!-- GRID OF CALCULATORS -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
    
    <!-- 1. VPC CIDR CALCULATOR -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="network"></i> AWS VPC Subnet CIDR Calculator
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 1rem;">
        Calculates total vs usable host capacity, accounting for the 5 AWS reserved IP addresses.
      </p>
      <div style="display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem;">
        <input type="text" id="cidrInput" value="10.0.1.0/24" style="background: var(--bg-page); border: 1px solid var(--border-subtle); color: var(--text-normal); font-family: var(--font-mono); font-size: 13px; padding: 0.4rem 0.6rem; border-radius: 4px; flex: 1;">
        <button class="btn-tool" onclick="calculateCidr()" style="padding: 0.4rem 0.8rem; background: var(--primary); color: #fff; font-weight: 600;">Calculate</button>
      </div>
      <div id="cidrResult" style="font-family: var(--font-mono); font-size: 11px; line-height: 1.6; color: var(--text-muted); background: var(--bg-code); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-subtle);">
        • Total Addresses: 256<br>
        • Usable EC2 Hosts: <strong style="color:var(--primary);">251</strong> (256 - 5 reserved)<br>
        • Reserved: .0 (Net), .1 (Router), .2 (DNS), .3 (Future), .255 (Bcast)<br>
        • Netmask: 255.255.255.0
      </div>
    </div>

    <!-- 2. AURORA QUORUM VISUALIZER -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="database"></i> Amazon Aurora 4/6 Quorum Simulator
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 0.75rem;">
        Toggle storage node health across 3 Availability Zones to test Write &amp; Read Quorum durability:
      </p>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem; margin-bottom: 1rem; text-align: center;">
        <div style="background: var(--bg-page); padding: 0.4rem; border-radius: 4px; border: 1px solid var(--border-subtle);">
          <div style="font-size: 10px; font-weight: bold; color: var(--text-muted);">AZ-1a</div>
          <button id="qnode1" onclick="toggleQuorumNode(1)" style="margin: 2px; padding: 2px 6px; font-size: 10px; background: #22c55e; color: white; border-radius: 3px; border: none; cursor: pointer;">Node 1</button>
          <button id="qnode2" onclick="toggleQuorumNode(2)" style="margin: 2px; padding: 2px 6px; font-size: 10px; background: #22c55e; color: white; border-radius: 3px; border: none; cursor: pointer;">Node 2</button>
        </div>
        <div style="background: var(--bg-page); padding: 0.4rem; border-radius: 4px; border: 1px solid var(--border-subtle);">
          <div style="font-size: 10px; font-weight: bold; color: var(--text-muted);">AZ-1b</div>
          <button id="qnode3" onclick="toggleQuorumNode(3)" style="margin: 2px; padding: 2px 6px; font-size: 10px; background: #22c55e; color: white; border-radius: 3px; border: none; cursor: pointer;">Node 3</button>
          <button id="qnode4" onclick="toggleQuorumNode(4)" style="margin: 2px; padding: 2px 6px; font-size: 10px; background: #22c55e; color: white; border-radius: 3px; border: none; cursor: pointer;">Node 4</button>
        </div>
        <div style="background: var(--bg-page); padding: 0.4rem; border-radius: 4px; border: 1px solid var(--border-subtle);">
          <div style="font-size: 10px; font-weight: bold; color: var(--text-muted);">AZ-1c</div>
          <button id="qnode5" onclick="toggleQuorumNode(5)" style="margin: 2px; padding: 2px 6px; font-size: 10px; background: #22c55e; color: white; border-radius: 3px; border: none; cursor: pointer;">Node 5</button>
          <button id="qnode6" onclick="toggleQuorumNode(6)" style="margin: 2px; padding: 2px 6px; font-size: 10px; background: #22c55e; color: white; border-radius: 3px; border: none; cursor: pointer;">Node 6</button>
        </div>
      </div>
      <div id="quorumStatus" style="font-family: var(--font-mono); font-size: 11px; padding: 0.6rem; border-radius: 4px; background: rgba(34, 197, 94, 0.1); color: #22c55e; border: 1px solid rgba(34, 197, 94, 0.3);">
        ✓ Online Nodes: 6/6 | Write Quorum (4/6): SATISFIED | Read Quorum (3/6): SATISFIED
      </div>
    </div>

    <!-- 3. S3 STORAGE COST BREAK-EVEN -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="hard-drive"></i> S3 Tier Cost Estimator (1,000 GB)
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 0.75rem;">
        Monthly storage cost comparison for 1 Terabyte of data stored in Mumbai region:
      </p>
      <div style="font-family: var(--font-mono); font-size: 11px; line-height: 1.7; color: var(--text-muted);">
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding: 3px 0;">
          <span>S3 Standard ($0.023/GB)</span>
          <strong style="color:var(--text-normal);">$23.00 / mo</strong>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding: 3px 0;">
          <span>S3 Standard-IA ($0.0125/GB)</span>
          <strong style="color:#60a5fa;">$12.50 / mo (45% savings)</strong>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding: 3px 0;">
          <span>S3 Glacier Flexible ($0.004/GB)</span>
          <strong style="color:#34d399;">$4.00 / mo (82% savings)</strong>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 3px 0;">
          <span>S3 Glacier Deep Archive ($0.00099/GB)</span>
          <strong style="color:#a78bfa;">$0.99 / mo (95.7% savings)</strong>
        </div>
      </div>
    </div>

    <!-- 4. EBS GP3 VS IO2 IOPS SIZER -->
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem;">
      <h3 style="font-size: 15px; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <i data-lucide="sliders"></i> EBS GP3 Baseline Performance
      </h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 0.75rem;">
        EBS gp3 baseline allocation included free of charge with every volume:
      </p>
      <ul style="font-size: 12px; color: var(--text-muted); line-height: 1.8; margin-left: 1.2rem;">
        <li><strong>Free Baseline IOPS:</strong> 3,000 IOPS (any volume size, 1 GiB to 16 TiB).</li>
        <li><strong>Free Baseline Throughput:</strong> 125 MB/s included without cost.</li>
        <li><strong>Scalable Limits:</strong> Provision up to 16,000 IOPS and 1,000 MB/s independently of volume capacity.</li>
      </ul>
    </div>

  </div>

  <!-- LIVE AWS CLI TERMINAL SANDBOX -->
  <h3 style="margin-top: 2.5rem; color: var(--text-normal); font-size: 18px; display: flex; align-items: center; gap: 0.5rem;">
    <i data-lucide="terminal"></i> Live Interactive AWS CloudShell &amp; CLI Sandbox
  </h3>
  <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 1rem;">
    Type commands such as <code class="code-inline">aws ec2 describe-instances</code>, <code class="code-inline">aws s3 ls</code>, <code class="code-inline">aws iam list-users</code>, <code class="code-inline">aws sts get-caller-identity</code>, or <code class="code-inline">help</code> below:
  </p>

  <div class="terminal-block" style="border: 1px solid var(--border-strong);">
    <div class="terminal-header">
      <div class="terminal-header-left">
        <span class="term-dot dot-red"></span>
        <span class="term-dot dot-yellow"></span>
        <span class="term-dot dot-green"></span>
        <span class="terminal-title"><i data-lucide="terminal" style="width:13px;height:13px;"></i> AWS CloudShell v2 • Bash • ap-south-1 (Mumbai)</span>
      </div>
      <div class="terminal-actions"><button class="btn-term-action" onclick="clearCliTerminal()"><i data-lucide="trash-2" style="width:12px;height:12px;"></i> Clear</button></div>
    </div>
    <div class="code-body" style="background: #090d16; min-height: 260px; font-family: var(--font-mono); font-size: 12px; padding: 1rem; color: #e2e8f0;">
      <div id="cliOutput" style="white-space: pre-wrap; line-height: 1.5; margin-bottom: 0.75rem;">
<span style="color: #60a5fa;">====================================================================================
ENTERPRISE CLOUD ADMINISTRATION AWS INTERACTIVE TERMINAL
AWS CLI v2.15.15 • Python/3.11.6 Linux/6.1.0-amazon-nitro • Region: ap-south-1
Type 'help' to view available mock AWS CLI commands.
====================================================================================</span>
</div>
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <span style="color: #34d399; font-weight: bold;">[cloud-admin@aws-cli ~]$</span>
        <input type="text" id="cliInput" placeholder="aws ec2 describe-instances..." style="flex: 1; background: transparent; border: none; outline: none; color: #fff; font-family: var(--font-mono); font-size: 12px;" onkeydown="handleCliKeyDown(event)">
      </div>
    </div>
  </div>

</article>

<script>
// Subnet CIDR calculation logic
function calculateCidr() {
  const val = document.getElementById('cidrInput').value.trim();
  const match = val.match(/\/(\d+)$/);
  const out = document.getElementById('cidrResult');
  if (!match) {
    out.innerHTML = '<span style="color:#ef4444;">Error: Please specify valid CIDR prefix (e.g. 10.0.0.0/24)</span>';
    return;
  }
  const prefix = parseInt(match[1]);
  if (prefix < 16 || prefix > 28) {
    out.innerHTML = '<span style="color:#ef4444;">VPC Subnet mask must be between /16 and /28</span>';
    return;
  }
  const total = Math.pow(2, 32 - prefix);
  const usable = total - 5;
  out.innerHTML = `• Subnet Prefix: /${prefix}<br>` +
                  `• Total Addresses: ${total.toLocaleString()}<br>` +
                  `• Usable EC2 Hosts: <strong style="color:var(--primary);">${usable.toLocaleString()}</strong> (Total - 5 AWS Reserved)<br>` +
                  `• Reserved Addresses: .0 (Net), .1 (VPC Router), .2 (DNS), .3 (Future), .255 (Broadcast)`;
}

// Aurora Quorum simulation logic
const quorumState = [true, true, true, true, true, true];
function toggleQuorumNode(idx) {
  quorumState[idx - 1] = !quorumState[idx - 1];
  const btn = document.getElementById('qnode' + idx);
  btn.style.background = quorumState[idx - 1] ? '#22c55e' : '#ef4444';
  const online = quorumState.filter(Boolean).length;
  const writeOk = online >= 4;
  const readOk = online >= 3;
  const stat = document.getElementById('quorumStatus');
  stat.style.background = writeOk ? 'rgba(34, 197, 94, 0.1)' : 'rgba(239, 68, 68, 0.1)';
  stat.style.borderColor = writeOk ? 'rgba(34, 197, 94, 0.3)' : 'rgba(239, 68, 68, 0.3)';
  stat.style.color = writeOk ? '#22c55e' : '#ef4444';
  stat.innerHTML = `${writeOk ? '✓' : '✗'} Online Nodes: ${online}/6 | Write Quorum (4/6): ${writeOk ? 'SATISFIED' : 'QUORUM LOSS (WRITES BLOCKED)'} | Read Quorum (3/6): ${readOk ? 'SATISFIED' : 'READ LOSS'}`;
}

// AWS CLI Terminal Emulator
function clearCliTerminal() {
  document.getElementById('cliOutput').innerHTML = '';
}

function handleCliKeyDown(e) {
  if (e.key === 'Enter') {
    const input = document.getElementById('cliInput');
    const cmd = input.value.trim();
    input.value = '';
    executeAwsCommand(cmd);
  }
}

function executeAwsCommand(cmd) {
  const out = document.getElementById('cliOutput');
  out.innerHTML += `\n<span style="color:#34d399;">[cloud-admin@aws-cli ~]$</span> <span style="color:#fff;">${cmd}</span>\n`;
  
  const c = cmd.toLowerCase().trim();
  if (c === 'clear') {
    out.innerHTML = '';
    return;
  }
  if (c === 'help') {
    out.innerHTML += `<span style="color:#94a3b8;">Available Commands:
  aws ec2 describe-instances       List active virtual server instances
  aws s3 ls                       List configured S3 storage buckets
  aws iam list-users              List enterprise IAM administrative identities
  aws sts get-caller-identity     Display current AWS identity and ARN
  aws rds describe-db-instances   List managed Aurora/RDS database nodes
  aws lambda list-functions       Display deployed serverless functions
  uname -a                        Display Linux kernel and Nitro environment
  clear                           Clear terminal screen</span>\n`;
  } else if (c.includes('describe-instances')) {
    out.innerHTML += `<span style="color:#a78bfa;">{
  "Reservations": [
    {
      "Instances": [
        {
          "InstanceId": "i-09ab7c12d5ef34567",
          "InstanceType": "c6i.2xlarge",
          "State": { "Name": "running", "Code": 16 },
          "PrivateIpAddress": "10.0.10.42",
          "PublicIpAddress": "13.235.12.98",
          "SubnetId": "subnet-01a2b3c4d5e6f7",
          "Architecture": "x86_64",
          "Hypervisor": "nitro",
          "LaunchTime": "2026-10-27T08:30:00Z"
        }
      ]
    }
  ]
}</span>\n`;
  } else if (c.includes('s3 ls')) {
    out.innerHTML += `<span style="color:#38bdf8;">2026-10-15 04:12:00 cu-cloud-static-website
2026-10-18 11:45:22 app-artifacts-prod
2026-10-22 09:18:04 cloudtrail-audit-logs</span>\n`;
  } else if (c.includes('list-users')) {
    out.innerHTML += `<span style="color:#f59e0b;">{
  "Users": [
    { "UserName": "devops-admin", "UserId": "AIDAJ456EXAMPLE", "Arn": "arn:aws:iam::123456789012:user/devops-admin" },
    { "UserName": "cloud-architect", "UserId": "AIDAJ789EXAMPLE", "Arn": "arn:aws:iam::123456789012:user/cloud-architect" }
  ]
}</span>\n`;
  } else if (c.includes('get-caller-identity')) {
    out.innerHTML += `<span style="color:#34d399;">{
  "UserId": "AIDASAMPLESESSION",
  "Account": "123456789012",
  "Arn": "arn:aws:iam::123456789012:user/devops-admin"
}</span>\n`;
  } else if (c.includes('describe-db-instances')) {
    out.innerHTML += `<span style="color:#ec4899;">{
  "DBInstances": [
    {
      "DBInstanceIdentifier": "aurora-db-cluster-instance-1",
      "DBInstanceClass": "db.r6g.xlarge",
      "Engine": "aurora-mysql",
      "DBInstanceStatus": "available",
      "Endpoint": { "Address": "aurora-db.cluster-cxyz123.ap-south-1.rds.amazonaws.com", "Port": 3306 },
      "MultiAZ": true
    }
  ]
}</span>\n`;
  } else if (c.includes('list-functions')) {
    out.innerHTML += `<span style="color:#60a5fa;">{
  "Functions": [
    {
      "FunctionName": "ProcessOrderAPI",
      "Runtime": "python3.12",
      "Role": "arn:aws:iam::123456789012:role/LambdaExecutionRole",
      "Handler": "lambda_function.lambda_handler",
      "CodeSize": 4128,
      "Timeout": 15,
      "MemorySize": 256
    }
  ]
}</span>\n`;
  } else if (c.includes('uname')) {
    out.innerHTML += `Linux aws-cloudshell 6.1.0-amazon-nitro #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux\n`;
  } else if (c === '') {
    // empty enter
  } else {
    out.innerHTML += `<span style="color:#ef4444;">aws: error: unknown command or parameter '${cmd}'. Type 'help' for available commands.</span>\n`;
  }
}
</script>
"""
