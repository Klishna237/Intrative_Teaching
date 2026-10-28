# -*- coding: utf-8 -*-
"""
SOHO Security and Perimeter Architecture (Part of Unit 5):
- Article it5-soho-gateway: Converged SOHO Gateway Architecture & DHCP DORA Handshake
- Article it5-nat-pat: NAT vs PAT (NAT Overload) Socket Translation State Tables
- Article it5-wifi-security: Wireless Security Evolution: WEP, WPA2-PSK 4-Way Handshake vs WPA3 SAE
- Article it5-firewall-dmz: Stateful Packet Inspection (SPI) Firewalls, Port Forwarding & DMZ Isolation
"""

IT_SOHO_HTML = """
<!-- Page: SOHO Gateway & DHCP -->
<article class="doc-page" id="it5-soho-gateway">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 05 • Page 14</span>
    <span class="meta-tag">Bloom's: Understand / Apply</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">41.</span> The 4-in-1 Converged SOHO Gateway Architecture &amp; DHCP DORA Lifecycle
  </h2>

  <p class="lead-para">
    A Small Office / Home Office (SOHO) router is not a single discrete networking device; it is a converged consumer embedded appliance physically integrating four distinct networking components onto a single cost-effective PCB: a WAN transceiver/modem, a Layer 3 routing engine running embedded Linux, a multi-port Layer 2 Ethernet switch, and a dual-band wireless access point.
  </p>

  <div class="diagram-container">
    <div class="diagram-title">Inside the 4-in-1 Converged SOHO Router</div>
    <div class="arch-stack-visual">
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-kernel">WAN INTERFACE (Cable DOCSIS / Fiber ONT / DSL)</span>
        <div class="tier-desc">Public Dynamic IP assigned by ISP via DHCP • Stateful Packet Inspection (SPI) Firewall • NAT/PAT Engine</div>
      </div>
      <div style="text-align: center; color: var(--primary); font-weight: 800; font-family: var(--font-mono); font-size: 11px;">
        &Updownarrow; Embedded Linux MIPS/ARM Kernel & Routing Subsystem &Updownarrow;
      </div>
      <div class="arch-tier-box">
        <span class="tier-badge tier-badge-user">INTERNAL LAN FABRIC (Private Subnet 192.168.1.0/24)</span>
        <div class="tier-desc">Embedded DHCP Server • Local DNS Forwarding Proxy • 4-Port Layer 2 Gigabit Ethernet Switch • 802.11ax Wi-Fi 6 AP</div>
      </div>
    </div>
  </div>

  <div class="callout callout-mnemonic">
    <div class="callout-header"><i data-lucide="zap"></i> The DHCP 4-Step Negotiation Handshake: DORA</div>
    <p>
      When an unconfigured client connects to an Ethernet or Wi-Fi network, it obtains IP configuration via the <strong>DORA</strong> process:
    </p>
    <ul>
      <li><strong>Discover (Client &rarr; Broadcast):</strong> Client sends DHCPDISCOVER on UDP Port 67 (Source: 0.0.0.0:68 &rarr; Destination: 255.255.255.255:67) with client MAC address.</li>
      <li><strong>Offer (Server &rarr; Broadcast/Unicast):</strong> SOHO router replies with DHCPOFFER containing an unallocated IP (e.g. 192.168.1.105), subnet mask (255.255.255.0), lease duration (86400s), and router IP.</li>
      <li><strong>Request (Client &rarr; Broadcast):</strong> Client broadcasts DHCPREQUEST formally accepting the offered IP and notifying any other DHCP servers that their offers are declined.</li>
      <li><strong>Acknowledge (Server &rarr; Unicast):</strong> SOHO router replies with DHCPACK, finalizing the lease and updating its internal ARP binding table.</li>
    </ul>
  </div>

  <div class="page-footer-meta">
    <span>Next: NAT & PAT Socket Translation</span>
    <span>Unit 05 • Page 14</span>
  </div>
</article>

<!-- Page: NAT & PAT -->
<article class="doc-page" id="it5-nat-pat">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 05 • Page 15</span>
    <span class="meta-tag">Bloom's: Analyze / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">42.</span> Network Address Translation (NAT) &amp; Port Address Translation (PAT / NAT Overload)
  </h2>

  <p class="lead-para">
    Because RFC 1918 private IPv4 addresses (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) are blocked by Internet core routers, SOHO gateways rely on Network Address Translation to dynamically map hundreds of internal private client sockets to a single globally routable public IPv4 address assigned by the ISP.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Internal Client Socket</th>
          <th>NAT Gateway Translation (State Table)</th>
          <th>Public WAN Destination Socket</th>
          <th>Protocol</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>`192.168.1.50:52140` (Workstation A)</td>
          <td><strong>`203.0.113.88:41001`</strong> &rarr; Translated Public Socket</td>
          <td>`142.250.190.46:443` (Google Web Server)</td>
          <td>TCP</td>
        </tr>
        <tr>
          <td>`192.168.1.75:52140` (Laptop B)</td>
          <td><strong>`203.0.113.88:41002`</strong> &rarr; Distinct Ephemeral Port</td>
          <td>`142.250.190.46:443` (Google Web Server)</td>
          <td>TCP</td>
        </tr>
        <tr>
          <td>`192.168.1.99:61200` (Smartphone C)</td>
          <td><strong>`203.0.113.88:41003`</strong> &rarr; Distinct Ephemeral Port</td>
          <td>`151.101.1.140:443` (Cloudflare CDN)</td>
          <td>TCP</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="cpu"></i> Silicon Mechanics: Why Static NAT Differed from PAT (NAT Overload)</div>
    <p>
      In <em>Static NAT</em>, one private IP maps permanently to one public IP (1:1 ratio), providing zero address conservation. In <em>Port Address Translation (PAT / NAT Overload)</em>, the router tracks both the IP address and the Layer 4 source TCP/UDP port number. Even if two different internal laptops transmit from identical source ports (`52140`), the router's Netfilter/iptables connection tracking module (`conntrack`) assigns each a unique public source port (`41001` vs `41002`). Up to <strong>64,512 concurrent outward connections</strong> can theoretically be multiplexed through a single public IP address!
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Wireless Security Evolution</span>
    <span>Unit 05 • Page 15</span>
  </div>
</article>

<!-- Page: Wi-Fi Security -->
<article class="doc-page" id="it5-wifi-security">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 05 • Page 16</span>
    <span class="meta-tag">Bloom's: Understand / Evaluate</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">43.</span> Wireless Security Evolution: WEP, WPA2-PSK (4-Way Handshake) vs WPA3 SAE
  </h2>

  <p class="lead-para">
    Radio frequency (RF) broadcasts propagate through physical walls, making Wi-Fi networks vulnerable to eavesdropping and packet injection unless protected by robust cryptographic authentication and encryption suites.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Standard</th>
          <th>Encryption Cipher</th>
          <th>Integrity Mechanism</th>
          <th>Authentication Protocol</th>
          <th>Primary Vulnerability</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>WEP (1997)</strong></td>
          <td>RC4 Stream Cipher (40/104-bit key)</td>
          <td>CRC-32 (Linear, unkeyed)</td>
          <td>Shared Key / Open</td>
          <td><strong>24-bit Initialization Vector (IV)</strong> repeats after ~5,000 packets; crackable in &lt;60 seconds via FMS/KoreK attacks!</td>
        </tr>
        <tr>
          <td><strong>WPA2-PSK (2004)</strong></td>
          <td>AES-CCMP (128-bit block cipher)</td>
          <td>CBC-MAC</td>
          <td>Pre-Shared Key (4-Way EAPOL Handshake)</td>
          <td>Vulnerable to <em>offline dictionary attacks</em> if an attacker captures the 4-way handshake, and KRACK key reinstallation attacks.</td>
        </tr>
        <tr>
          <td><strong>WPA3-SAE (2018)</strong></td>
          <td>AES-GCMP (128/256-bit Galois/Counter)</td>
          <td>BIP-GMAC</td>
          <td>Simultaneous Authentication of Equals (SAE Dragonfly Handshake)</td>
          <td>Zero offline dictionary vulnerability; provides <strong>Forward Secrecy</strong> (capturing traffic today does not allow decrypting it if the password is discovered tomorrow!).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-deep">
    <div class="callout-header"><i data-lucide="shield-check"></i> Cryptographic Mechanics: WPA3 Simultaneous Authentication of Equals (SAE)</div>
    <p>
      In WPA2-PSK, the Pairwise Master Key (PMK) is derived solely from `PBKDF2(Passphrase, SSID)`. Because the formula contains no fresh session exchange, an eavesdropper recording the 4-Way Handshake can run millions of passphrase guesses through Hashcat offline at gigahashes/second without touching the target network.
      <br><br>
      In WPA3-Personal, SAE executes a zero-knowledge proof based on the <strong>Dragonfly Key Exchange</strong> (Diffie-Hellman over elliptic curves). Both parties prove knowledge of the password without ever transmitting it or any hash derived from it. The attacker cannot verify whether a password guess is correct without actively engaging in an interactive online exchange with the access point, which enforces rate-limiting to completely eliminate brute-force guessing!
    </p>
  </div>

  <div class="page-footer-meta">
    <span>Next: Firewalls, Port Forwarding & DMZ</span>
    <span>Unit 05 • Page 16</span>
  </div>
</article>

<!-- Page: Firewalls, Port Forwarding & DMZ -->
<article class="doc-page" id="it5-firewall-dmz">
  <div class="page-header-meta">
    <span class="meta-tag">IT Fundamentals • CSC104</span>
    <span class="meta-tag">Unit 05 • Page 17</span>
    <span class="meta-tag">Bloom's: Apply / Analyze</span>
  </div>

  <h2 class="section-title">
    <span class="sec-num">44.</span> Stateful Packet Inspection (SPI) Firewalls, Port Forwarding &amp; DMZ Isolation
  </h2>

  <p class="lead-para">
    The SOHO gateway acts as the initial perimeter defense boundary separating trusted internal LAN clients from untrusted public Internet traffic through hardware state tracking and access filtering rules.
  </p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Perimeter Mechanism</th>
          <th>Operational Logic</th>
          <th>Typical Use Case</th>
          <th>Security Risk Exposure</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>SPI Firewall</strong></td>
          <td>Monitors TCP 3-way handshakes and connection states (SYN, ESTABLISHED, RELATED); automatically drops unsolicited inbound packets with zero matching outbound state entry</td>
          <td>Default residential &amp; corporate protection</td>
          <td>Minimal; blocks 99.9% of automated port scanning probes</td>
        </tr>
        <tr>
          <td><strong>Port Forwarding (DNAT)</strong></td>
          <td>Statically rewrites the destination IP of inbound WAN packets on a specific port (e.g. WAN:8080 &rarr; LAN 192.168.1.100:80)</td>
          <td>Hosting an on-premises web server, IP security camera NVR, or Minecraft server</td>
          <td>Moderate; exposes only that single specific service port to public Internet attacks</td>
        </tr>
        <tr>
          <td><strong>DMZ Host</strong></td>
          <td>Directs <em>all unmapped incoming ports</em> across all 65,535 TCP/UDP ports directly to a single internal LAN IP address</td>
          <td>Testing gaming consoles with strict NAT issues</td>
          <td><strong>Severe</strong>; strips all router firewall filtering from the host, exposing it directly to zero-day exploits and worm propagation</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer-meta">
    <span>Unit 05 SOHO Security Complete</span>
    <span>Unit 05 • Page 17</span>
  </div>
</article>
"""
