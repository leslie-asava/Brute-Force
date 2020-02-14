import hashlib

print("[+] Enter the hashing you want")
algorithm_choice = input("user> ")
print("[+] Now enter the string you want to hash")
text = input("user> ")
if algorithm_choice == "blake2b":
    algorithm = hashlib.blake2b
elif algorithm_choice == "blake2s":
    algorithm = hashlib.blake2s
elif algorithm_choice == "md5":
    algorithm = hashlib.md5
elif algorithm_choice == "sha1":
    algorithm = hashlib.sha1
elif algorithm_choice == "sha224":
    algorithm = hashlib.sha224
elif algorithm_choice == "sha256":
    algorithm = hashlib.sha256
elif algorithm_choice == "sha3_224":
    algorithm = hashlib.sha3_224
elif algorithm_choice == "sha3_512":
    algorithm = hashlib.sha3_224
elif algorithm_choice == "sha384":
    algorithm = hashlib.sha384
elif algorithm_choice == "sha512":
    algorithm = hashlib.sha512
elif algorithm_choice == "shake_128":
    algorithm = hashlib.shake_128
elif algorithm_choice == "shake_256":
    algorithm = hashlib.shake_256
elif algorithm_choice == "shake3_256":
    algorithm = hashlib.shake3_256

if algorithm_choice == "ntlm":
    hashed = hashlib.new('md4', text.encode('utf-16le'))
else:
    hashed = algorithm(text.encode())
    
print(hashed.hexdigest())
input("[+] Press Enter key to exit")
