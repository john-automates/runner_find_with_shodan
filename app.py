print("[+] START: Shodan IP Lookup")
print("[~] Importing required modules...")

import os
import sys
import json
import shodan
from datetime import datetime

def format_timestamp(timestamp):
    try:
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return str(timestamp)

try:
    print("[~] Checking command line arguments...")
    if len(sys.argv) != 3:
        print("[ERROR] Usage: python app.py <ip_address> <api_key>")
        sys.exit(1)

    ip_address = sys.argv[1]
    api_key = sys.argv[2]
    
    print(f"[~] Looking up information for IP: {ip_address}")
    
    # Initialize the Shodan API
    api = shodan.Shodan(api_key)
    
    # Get host information
    host = api.host(ip_address)
    
    # Prepare output directory
    os.makedirs("outputs", exist_ok=True)
    output_file = os.path.join("outputs", f"{ip_address}_shodan_results.md")
    
    # Format the results in Markdown
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Shodan Results for {ip_address}\n\n")
        
        # Basic Information
        f.write("## Basic Information\n\n")
        f.write(f"- **IP:** {ip_address}\n")
        f.write(f"- **Organization:** {host.get('org', 'N/A')}\n")
        f.write(f"- **ISP:** {host.get('isp', 'N/A')}\n")
        f.write(f"- **Country:** {host.get('country_name', 'N/A')}\n")
        f.write(f"- **City:** {host.get('city', 'N/A')}\n")
        f.write(f"- **Last Update:** {format_timestamp(host.get('last_update', 'N/A'))}\n\n")
        
        # Open Ports
        f.write("## Open Ports\n\n")
        ports = host.get('ports', [])
        if ports:
            for port in ports:
                f.write(f"- {port}\n")
        else:
            f.write("No open ports found\n")
        f.write("\n")
        
        # Services/Banners
        f.write("## Services\n\n")
        for item in host.get('data', []):
            f.write(f"### Port {item.get('port', 'N/A')}\n\n")
            f.write(f"- **Protocol:** {item.get('transport', 'N/A')}\n")
            f.write(f"- **Service:** {item.get('product', 'N/A')}\n")
            f.write(f"- **Version:** {item.get('version', 'N/A')}\n")
            
            # Add banner if available
            if 'data' in item:
                f.write("\n**Banner:**\n```\n")
                f.write(str(item['data']).strip())
                f.write("\n```\n")
            f.write("\n")
        
        # Vulnerabilities
        vulns = host.get('vulns', [])
        if vulns:
            f.write("## Vulnerabilities\n\n")
            for vuln in vulns:
                f.write(f"- {vuln}\n")
        
    print(f"[+] Results saved to: {output_file}")
    print("[+] END: Shodan IP Lookup")

except shodan.APIError as e:
    print(f"[ERROR] Shodan API Error: {str(e)}")
    sys.exit(1)
except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {str(e)}")
    sys.exit(1)