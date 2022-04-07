def caesarHackBF(cipher_text, LETTERS):

    length = len(LETTERS)

    for i in range(length):
        plain_text = ""

        for char in cipher_text:
            if char in LETTERS:

                position = LETTERS.find(char)
                position = position - i

                if position < 0:
                    position = position + length

                plain_text = plain_text + LETTERS[position]

            else:
                plain_text = plain_text + char

        print('Hacking key #%s: %s' % (i, plain_text))

cipher_text = 'GIEWIVrGMTLIVrHIQS'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
caesarHackBF(cipher_text, LETTERS)
