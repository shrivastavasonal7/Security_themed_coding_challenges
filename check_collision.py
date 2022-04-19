import random
import string
import hashlib
import time

tot_time = 0
i = 1

while i <= 10:
    start_time = time.time()

    seed = random.choice(string.printable)
    print("The preimage seed is: ", seed)

    md5_hash = hashlib.sha256(seed.encode("utf-8"))
    test_hash = md5_hash.hexdigest()
    print("The md5 hash is:", test_hash)

    for char in (string.printable):
        new_hash = hashlib.sha256(char.encode("utf-8")).hexdigest()

        if new_hash == test_hash:
            print("\nCOLLISION FOUND!!!\n ")
            print("The colliding char is:",char)
            print("New hash is:", new_hash)
            break

    time_taken = time.time() - start_time
    print("Time Taken", time_taken )


    tot_time = ((tot_time + time_taken ))

    i += 1
    print("\n*************\n")

print("Average Time Taken",tot_time/10)



