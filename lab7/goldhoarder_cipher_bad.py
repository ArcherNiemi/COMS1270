def contains_character(text, character):
    return character in text

def remove_duplicates(text):
    usedCharacters = []
    endText = ""
    for character in text:
        if not contains_character(usedCharacters,character):
            endText += character
            usedCharacters.append(character)
    return endText

def build_cipher_alphabet(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetList = list(alphabet)
    for character in keyword:
        if contains_character(alphabetList,character):
            alphabetList.remove(character)
    restOfAlphabet = "".join(alphabetList)
    endWord = keyword + restOfAlphabet
    return endWord

def find_character(text, character):
    return text.index(character)

def opposite_character(character, cipher_alphabet):
    if character == " ":
        return " "

    cipherMidpoint = round(len(cipher_alphabet)/2)

    reverse_cipher = cipher_alphabet[cipherMidpoint:] + cipher_alphabet[:cipherMidpoint]

    cipherDictionary = dict(zip(cipher_alphabet, reverse_cipher))
    opposite_character = cipherDictionary[character]

    return opposite_character

def myZip(text1,text2):
    endList = []
    for i,char1 in enumerate(text1):
        char2 = text2[i]
        endList.append((char1,char2))
    return endList

def myEnumerate(text):
    endList = []
    for i in range(len(text)):
        char = text[i]
        endList.append((i,char))
    return endList


def transform(message, keyword):
    alphabet_cipher = build_cipher_alphabet(keyword)
    newMessage = ""
    for char in message:
        newMessage += opposite_character(char, alphabet_cipher)
    return newMessage

def main():
    print(transform("I AM SO COOL","ANOTHER"))

if __name__ == "__main__":
    main()