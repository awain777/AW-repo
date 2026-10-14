import argparse
import requests
import json

parser = argparse.ArgumentParser()
# Argument 1: The subnet IP address
parser.add_argument("subnet")
# Argument 2: The mask/CIDR 
parser.add_argument("mask")

args = parser.parse_args()
api = "https://networkcalc.com/api/ip"
class_A = "10.0.0.0"
class_B = "172.16.0.0"
class_C = "192.168.1.0"
mask = args.mask
subnet = args.subnet

def api_call():
    global hosts, first_ip, subnet_mask, subnet_bits
    url = f"{api}/{args.subnet}/{args.mask}"
    response = requests.get(url)
    data = response.json()
   
   # Extract data from the networkcalc JSON structure
    addr = data.get("address")
    hosts = addr.get("assignable_hosts")
    first_ip = addr.get("first_assignable_host")
    subnet_mask = addr.get("subnet_mask")
    subnet_bits = addr.get("subnet_bits")

def assignable_hosts(hosts, subnet):
    print("There are",hosts,"assignable hosts for the",subnet,"subnet")

def first_host(first_ip):
    print("The first address is",first_ip)

def mask_decimal(subnet_mask):
    print("The subnet mask in decimal form is", subnet_mask)

def mask_cidr(subnet_bits):
    subnet_bits = str(subnet_bits)
    mask_cidr = "/"+subnet_bits
    print("The subnet mask in cidr notation is", mask_cidr)

if __name__ == '__main__':
    api_call()
    assignable_hosts(hosts, subnet)
    first_host(first_ip)
    mask_decimal(subnet_mask)
    mask_cidr(subnet_bits)
