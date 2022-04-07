def caesar_encrypt(plain_text,k):
    cipher = ""
    length = len(plain_text)

    for i in range(length):
        char = plain_text[i]

        if (char.isupper()):

            '''Here is how your cypher works - 
            1. Take the ASCII value of a letter, subtract the value of "A" from it giving you a 0 based number.
            2. Add the key value to this number shifting it by k places.
            3. Now divide the number you got above by 26, discard the quotient and use the remainder. 
            This is the modulo operator %. This always keeps you numbers in the 0-25 range, 
            since dividing by 26 will never a have a remainder great than 25.
            4. Add 65 to it to convert it into an "encrypted" uppercase letter.
            This allows the key to be ANY number and still keeps the "encrypted" output within the ASCII range of A-Z.'''

            cipher += chr((ord(char) + k-65) % 26 + 65)

        else:

            cipher += chr((ord(char) + k - 97) % 26 + 97)


    return cipher

plain_text = "this is caesar cipher"
k = 4

print("Plain Text : " + plain_text)
print("Shift pattern : " + str(k))
print("Cipher: " + caesar_encrypt(plain_text,k))