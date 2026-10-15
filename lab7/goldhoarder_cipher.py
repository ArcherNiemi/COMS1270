def contains_character(text, character):
    for char in text:
        if char == character:
            return True
    return False

def remove_duplicates(text):
    endText = ""
    for character in text:
        if not contains_character(endText,character):
            endText += character
    return endText

def build_cipher_alphabet(keyword):
    noDuplicates = remove_duplicates(keyword)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in noDuplicates:
        if contains_character(alphabet,character):
            alphabet = removeChar(alphabet,character)
    endWord = noDuplicates + alphabet
    return endWord

def removeChar(text,character):
    i = 0
    while(i < len(text)):
        char = text[i]
        if char == character:
            text = text[:i] + text[i+1:]
        else:
            i += 1
    return text


def find_character(text, character):
    for i in range(len(text)):
        char = text[i]
        if char == character:
            return i

def opposite_character(character, cipher_alphabet):
    if character == " ":
        return " "

    cipherMidpoint = round(len(cipher_alphabet)/2)

    reverse_cipher = cipher_alphabet[cipherMidpoint:] + cipher_alphabet[:cipherMidpoint]

    opposite_character = reverse_cipher[find_character(cipher_alphabet,character)]

    return opposite_character

def transform(message, keyword):
    alphabet_cipher = build_cipher_alphabet(keyword)
    newMessage = ""
    for char in message:
        newMessage += opposite_character(char, alphabet_cipher)
    return newMessage

def main():
    print(transform("BANANA","CORNFLAKES"))

if __name__ == "__main__":
    main()