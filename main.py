import itertools
import hashlib
import datetime
import os

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOLS = r",<.>/?;:'[{}]\|!@#$%^&*()_-+=`~" + '"'
DIGITS = "1234567890"
banner = r"""                      __________                __                     _____                           
                      \______   \_______ __ ___/  |_  ____           _/ ____\___________   ____  ____  
                       |    |  _/\_  __ \  |  \   __\/ __ \   ______ \   __\/  _ \_  __ \_/ ___\/ __ \ 
                       |    |   \ |  | \/  |  /|  | \  ___/  /_____/  |  | (  <_> )  | \/\  \__\  ___/ 
                       |______  / |__|  |____/ |__|  \___  >          |__|  \____/|__|    \___  >___  >
                              \/                         \/                                   \/    \/ 
                        
                                              -- Algorithms Available --

                                         [*] blake2b              [*] sha3_512
                                         [*] blake2s              [*] sha384
                                         [*] md5                  [*] sha512
                                         [*] sha1                 [*] shake_128
                                         [*] sha224               [*] shake_256
                                         [*] sha256               [*] shake3_256
                                         [*] sha3_224             [*] ntlm
                        """
character_set = []

for character in LOWERCASE:
	character_set.append(character)
for character in UPPERCASE:
	character_set.append(character)
for character in SYMBOLS:
	character_set.append(character)
for character in DIGITS:
	character_set.append(character)
def ntlm(text):
	hashed = hashlib.new('md4', text.encode('utf-16le'))
	return hashed
def main():
	running = True
	length = 0

	print(banner)

	print("\n[+] Please enter the hashing algorithm to use")
	algorithm_choice = input(">>> ")

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
	elif algorithm_choice == "ntlm":
		pass
	else:
		print("[+] Invalid Choice. Do you want to start again? (Y or N)")
		response = input(">>> ")
		if response.upper() == "Y":
			try:
				os.system("cls")
			except:
				os.sytem("clear")
			main()
		else:
			return
	print("[+] Enter the hash you wish to brute-force")
	hash_input = input(">>> ")
	start_time = datetime.datetime.now()

	while running:
		if running:
			combinations = itertools.product(character_set,repeat=length+1)
			print("            [*] Current combination length : "+str(length+1)+" "+str(datetime.datetime.now()-start_time))
			for each in combinations:
				combination = ""
				combination = combination.join(each)
				if algorithm_choice != "ntlm":
					hashed = algorithm(combination.encode())
				else:
					hashed = hashlib.new('md4', combination.encode('utf-16le'))

				if hash_input == hashed.hexdigest():
					print("\n[!] Password found : '"+combination+"'  "+str(datetime.datetime.now()-start_time))
					running = False
					print("[+] Do you want to run again? (Y or N)")
					response = input(">>> ")
					if response.upper() == "Y":
						try:
							os.system("cls")
						except:
							os.sytem("clear")
						main()
					break
			length+=1
		else:
			break

main()
