import socket
import threading
from datetime import datetime

target = input("Target daalo (scanme.nmap.org): ")
print(f"\n--- {target} ka Final Scan ---\n")

f = open("report.txt", "w")
f.write(f"Scan Report for {target}\nDate: {datetime.now()}\n")
f.write("-"*40 + "\n")

def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "Service ON"
        result = f"Port {port}: OPEN [+] -> {banner}"
        print(result)
        f.write(result + "\n")
        s.close()
    except:
        pass

threads = []
for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

f.close()
print("\nScan khatam! Report 'report.txt' me save ho gayi.")
