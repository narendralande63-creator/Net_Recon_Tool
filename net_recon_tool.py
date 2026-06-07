#!/usr/bin/env python3
# Project :- Network Recon Tool:-

import subprocess
import argparse

print("===============================================")
print("\t\t Net Recon Tool V.2")
print("===============================================\n")


def get_argument():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-t", dest="target", help="Kindly Specify The Target", required=True)
    parser.add_argument("--dns", action="store_true", help="Perform DNS lookup",)
    parser.add_argument("--ping", action="store_true", help="Perform Ping Operation",)
    parser.add_argument("--trace", action="store_true", help="Perform the traceroute",)
    parser.add_argument("--all", action="store_true", help="perfrom all Operations",)
    
    args = parser.parse_args()
    return args


def dns_lookup(target):
    
    print("[+] DNS Lookup\n")
    
    try:
        result = subprocess.run(
            ["nslookup",target],
            capture_output=True,
            text = True,
            check = True
        )
        print(result.stdout)
    
    except subprocess.CalledProcessError:
        print("[-] Unable to fetch ",target)
    
    print("--------------------------------------\n")
    
def ping_target(target):
    
    
    print("[+] Ping Test\n")
    
    
    try:
        ping_result = subprocess.run(
            ["ping","-c","4",target],
            capture_output= True,
            text = True,
            check = True
    )
        print(ping_result.stdout)
    
    except subprocess.CalledProcessError:
        
        print("[-] Cannot Ping",target,)
    
    print("--------------------------------------\n")

    
def traceroute(target):
    
    print("[+] Traceroute\n")
    
    try:
        
        result_traceroute = subprocess.run(
            ["traceroute",target],
            capture_output= True,
            text = True,
            check = True
    )
        print(result_traceroute.stdout)
        
    except subprocess.CalledProcessError:
        print("[-] Unable to trace the route")
    
    
    print("Recon Completed\n")
    print("--------------------------------------\n")  

args = get_argument()
print("[+] Starting Recon\n")

if not (args.dns or args.ping or args.trace or args.all):
    print("[-] Please specify an option")
    print("[-] To know more :- [-h]")

if args.all:
    dns_lookup(args.target)
    ping_target(args.target)
    traceroute(args.target)

else:
    
    if args.dns:
        dns_lookup(args.target)
    
    if args.ping:
        ping_target(args.target)

    if args.trace:
        traceroute(args.target)
