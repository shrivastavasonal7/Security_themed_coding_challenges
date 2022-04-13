import hashlib
import bcrypt
Hash_algo_available = hashlib.algorithms_available

#print(Hash_algo_available)

module = hashlib.sha256() #Selecting the hashing module
module.update(b"I am Sonal")  # .update is an inbuilt function in hashlib that takes data as input and generates the hashes. The letter b indicates the string is a byte string, and .digest gives you the hash string generated from the data:
print(module.hexdigest())

input_pwd = b"IamSonal"
hashed_pwd = bcrypt.hashpw(input_pwd, bcrypt.gensalt())

print(hashed_pwd)