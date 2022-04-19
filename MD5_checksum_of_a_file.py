import hashlib

file_name = input("Enter the path to the input file: ")
block_size = input("Enter the block size: ")

md5_hash = hashlib.md5()
with open(file_name,"rb") as fileRead:
    while True:
        bytes = fileRead.read(int(block_size))
        if not bytes:
            break
        else:
            md5_hash.update(bytes)
    print(md5_hash.hexdigest())

    #ref : https://www.quickprogrammingtips.com/python/how-to-calculate-md5-hash-of-a-file-in-python.html




