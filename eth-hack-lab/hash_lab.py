import hashlib
print("=== Hash Lab Level 1 ===")
target = "letmein"
target_hash = hashlib.sha256(target.encode()).hexdigest()
print(f"Target: {target_hash}\n")
with open("wordlist.txt") as f:
    for w in f:
        w=w.strip()
        print(f"Checking {w}...")
        if hashlib.sha256(w.encode()).hexdigest() == target_hash:
            print(f"\nSUCCESS! Password is {w}")
            break

