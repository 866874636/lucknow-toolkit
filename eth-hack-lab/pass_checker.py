import hashlib
import time

print("=== Password Strength Lab - Level 2 ===")
my_pass = input("Apna test password likho: ")

my_hash = hashlib.sha256(my_pass.encode()).hexdigest()
print(f"\nTumhara Hash: {my_hash}\n")

common = ["123456","password","qwerty","letmein","admin","lucknow123"]

start = time.time()
found = False
for guess in common:
    if hashlib.sha256(guess.encode()).hexdigest() == my_hash:
        print(f"[WEAK] Password '{guess}' common hai! 0 sec me crack ho gaya.")
        found = True
        break

if not found:
    print("[STRONG] Good! Ye common list me nahi hai, strong hai.")

print(f"Time: {time.time()-start:.2f}s")
