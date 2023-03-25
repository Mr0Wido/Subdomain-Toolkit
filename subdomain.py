#!/usr/bin/env python3

import subprocess
from tqdm import tqdm
import requests
import subprocess
import argparse

# Subdomain Tools
subdomain_tools = ['sublist3r', 'amass', 'subfinder', 'assetfinder', 'findomain']

# Input
parser = argparse.ArgumentParser(description='Subdomain enumeration tool')

parser.add_argument('-u', '--url', help='Domain name to scan', required=True)

args = parser.parse_args()

domain_name = args.url


# Saving file
output_file = 'subdomains.txt'

with open(output_file, 'w') as f:
    pass


all_subdomains = set()
for tool in tqdm(subdomain_tools, desc="Finding subdomains  ", total=len(subdomain_tools)):
    subdomain_tools = {
        'sublist3r': ['-d'],
        'amass': [],
        'subfinder': [],
        'assetfinder': ['-subs-only'],
        'findomain': ['-t']
    }

    try:
        if tool == 'amass':
            output = subprocess.check_output([tool, 'intel', '-whois', '-d', domain_name]).decode()
            
        elif tool == "subfinder":
            output = subprocess.Popen([tool, '-d', domain_name,], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
   
        else:
            output = subprocess.check_output([tool] + subdomain_tools[tool] + [domain_name]).decode()
            subdomains = set(output.splitlines())
            all_subdomains.update(subdomains)
        
        with open(f'{tool}.txt', 'w') as f:
            f.write('\n'.join(subdomains))

    except subprocess.CalledProcessError as e:
        print(f"{tool} returned non-zero exit status {e.returncode}. Error message: {e.output.decode()}")
    continue

def filter_subdomains(filename):
    with open(filename, 'r') as f:
        subdomains = set(f.read().splitlines())
    with open(filename, 'w') as f:
        f.write('\n'.join(subdomains))

filter_subdomains(output_file)

all_subdomains = set()
for tool in subdomain_tools:
    try:
        with open(f'{tool}.txt', 'r') as f:
            subdomains = set(f.read().splitlines())
        all_subdomains.update(subdomains)
        subprocess.run(['rm', f'{tool}.txt'], check=True)
    except FileNotFoundError:
        continue

print(f"Totol {len(all_subdomains)} subdomains found.")

filtered_subdomains = set()
for subdomain in tqdm(all_subdomains, desc="Filtering subdomains"):
    url = f"http://{subdomain}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            filtered_subdomains.add(subdomain)
    except:
        pass

    with open(output_file, 'w') as f:
        f.write('\n'.join(filtered_subdomains))

print(f"A totol of {len(filtered_subdomains)} subdomain with only 200 OK response were found and saved in '{output_file}' file.")
