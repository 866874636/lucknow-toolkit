# Part 2: Fast Port Scanner - Threading wala
import socket
from datetime import datetime

target = input("Target IP daalo (ex: scanme.nmap.org): ")
print(f"\n[ scanning {target} ]")
print(f"Time: {datetime.now()}\n")

# Common ports jo hamesha test karte hain - safe and legal target
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5900, 8080]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} : OPEN")
    s.close()

print("\n[ Scan Khatam ]")

