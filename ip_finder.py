# IP & Domain Info Finder - Lucknow Toolkit
import socket
import requests

def get_ip_info(target):
    try:
        # Domain se IP nikalna
        ip = socket.gethostbyname(target)
        print(f"\n[+] Target: {target}")
        print(f"[+] IP Address: {ip}")

        # Public API se location info
        print("[+] Info nikal rahe hai...")
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url).json()

        if res['status'] == 'success':
            print(f"""
--- Result ---
Country: {res['country']}
City: {res['city']}
ISP: {res['isp']}
Region: {res['regionName']}
Timezone: {res['timezone']}
Map: https://www.google.com/maps?q={res['lat']},{res['lon']}
            """)
        else:
            print("[-] Info nahi mila")
            
    except Exception as e:
        print(f"Error: {e}")

print("=== Lucknow Toolkit - IP Finder ===")
target = input("Domain ya IP daalo (jaise google.com): ")
get_ip_info(target)