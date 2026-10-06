import hashlib
import socket

print("=== Lucknow Ethical Hack Toolkit v1.0 ===")
print("1. Password Strength Check")
print("2. Simple Port Scanner (only for localhost)")
print("3. Exit")

choice = input("Option chuno (1/2/3): ")

if choice == "1":
    p = input("Test password: ")
    h = hashlib.sha256(p.encode()).hexdigest()
    print(f"Hash: {h}")
    common = ["123456","password","qwerty","letmein","admin","lucknow123"]
    for c in common:
        if hashlib.sha256(c.encode()).hexdigest() == h:
            print("[WEAK] Ye common password hai!")
            break
    else:
        print("[STRONG] Mast! Strong password hai.")

elif choice == "2":
    print("\n[Scanner] Sirf apne phone / localhost ke liye")
    target = "127.0.0.1"
    print(f"Scanning {target}...")
    for port in [22, 80, 443, 8080]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        s.close()
else:
    print("Bye!")
