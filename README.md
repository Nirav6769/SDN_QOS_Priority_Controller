# SDN_QOS_Priority_Controller
Simple SDN mini project implementing QoS traffic prioritization using Ryu, Mininet, and OpenFlow.

Problem Statement
This project demonstrates a simple Software Defined Networking (SDN) solution using Mininet and the Ryu controller to implement traffic prioritization.
The goal is to show how different types of traffic can be handled with different priorities using OpenFlow rules. ICMP traffic (ping) is given higher priority than UDP traffic to simulate Quality of Service (QoS) behavior.

Approach
A single-switch topology (s1) with two hosts (h1, h2) is created in Mininet
A custom Ryu controller handles packet_in events
Flow rules are installed dynamically based on packet type
Flow Rules:
ICMP traffic → Priority 200 (High priority)
UDP traffic → Priority 10 (Low priority)
Default rule → Flood
This demonstrates match–action behavior in SDN.

Setup & Execution
Requirements:
Mininet
Ryu Controller
Open vSwitch
Python3

Steps:
Start Ryu Controller:
ryu-manager qos_controller.py
Run Mininet:
sudo mn --topo single,2 --controller remote --switch ovsk,protocols=OpenFlow13
Test connectivity:
pingall

Results & Analysis
ICMP packets experience low latency even during UDP traffic
UDP traffic does not affect ping significantly
Flow table shows higher priority rules for ICMP
Packet counters increase according to matched traffic

This confirms correct priority-based traffic handling.
