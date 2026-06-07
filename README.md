# Net_Recon_Tool_v2

Net Recon Tool:- (1st Project)
A simple python-based network reconnaissance tool build for cybersecurity learning and practice

Features:-
1. DNS Lookup
2. Ping Test
3. Traceroute
4. Command Line Arguments using argparse
5. Error handling using try/except

Requirements:-
1. Python 3
2. Linux (tested on Kali Linux)

Usage:-
1. Run DNS Lookup = python3 ./net_recon_tool.py -t 1.1.1.1 --dns
2. Run Ping Test = python3 ./net_recon_tool.py -t 1.1.1.1 --ping
3. Run Traceroute = python3 ./net_recon_tool.py -t 1.1.1.1 --trace
4. Run All Recon Modules = python3 ./net_recon_tool.py -t 1.1.1.1 --all

Learning Objectives:-
1. Python Functions
2. subprocess
3. argparser / optparser
4. Error Handling
5. Basic Cybersecurity REconnaissance

Future Improvements:-
1. Save results to a file
2. Better output formatting
3. Add Port Scanning
4. Add ARP Scanning with Scapy

Author:-
Narendra Lande
