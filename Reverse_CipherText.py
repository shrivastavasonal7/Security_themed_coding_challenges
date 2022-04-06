def reverseWords(Plain_text):

    words = Plain_text.split(" ")

    new_words = [word[::-1] for word in words] # This will reverse the word at their original position

    cipher_text = " ".join(new_words)

    return cipher_text

def reverseWordsAndPosition(Plain_text):

    length = len(Plain_text) -1

    new_word = ""

    while length >= 0:

        new_word = new_word + Plain_text[length]
        length = length -1

    return new_word

Plain_text = "This is not a cipher text"

print(reverseWords(Plain_text))
print(reverseWordsAndPosition(Plain_text))




