import hashlib

print("[+] Enter the hashing you want")
response = input("user> ")

if response == "blake2b":
    algorithm = hashlib.blake2b
elif response == "blake2s":
	algorithm = hashlib.blake2s
elif response == "md5":
	algorithm = hashlib.md5
elif response == "sha1":
	algorithm = hashlib.sha1
elif response == "sha224":
	algorithm = hashlib.sha224
elif response == "sha256":
	algorithm = hashlib.sha256
elif response == "sha3_224":
	algorithm = hashlib.sha3_224
elif response == "sha3_512":
	algorithm = hashlib.sha3_224
elif response == "sha384":
	algorithm = hashlib.sha384
elif response == "sha512":
	algorithm = hashlib.sha512
elif response == "shake_128":
	algorithm = hashlib.shake_128
elif response == "shake_256":
	algorithm = hashlib.shake_256
elif response == "shake3_256":
	algorithm = hashlib.shake3_256

print("[+] Now enter the string you want to hash")
response = input("user> ")
hashed = algorithm(response.encode())
print(hashed.hexdigest())
input("[+] Press Enter key to exit")