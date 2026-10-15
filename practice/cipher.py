NUMBERS_AND_VOWELS = {"1":"a","3":"e","5":"i","7":"o","9":"u","a":"1","e":"3","i":"5","o":"7","u":"9"}
ODD_NUMS = ("1","3","5","7","9")
VOWELS = ("a","e","i","o","u")

REVERSE_ALPHABET = {"a": "z","b": "y","c": "x","d": "w","e": "v","f": "u","g": "t","h": "s","i": "r","j": "q","k": "p","l": "o","m": "n","n": "m","o": "l","p": "k","q": "j","r": "i","s": "h","t": "g","u": "f","v": "e","w": "d","x": "c","y": "b","z": "a"}

def main():
    inputString = input().lower()

    while(inputString != "quit"):
        decryptedString = decryptMessage(inputString)
        encryptedString = encryptMessage(inputString)

        print(f"Decrypted: {decryptedString}")
        print(f"Encrypted: {encryptedString}")

        inputString = input().lower()

    print("done")

def decryptMessage(message):
    message = message.lower()
    decryptedMessage = ""
    # nextChar = ""
    for i,char in enumerate(message):
        # if i+1 < len(message):
        #     nextChar = message[i+1]
        # else:
        #     nextChar = ""

        # if nextChar == char or not char.isalnum():
        #     decryptedMessage += char
        if not char.isalnum():
            decryptedMessage += char
        elif char in ODD_NUMS:
            decryptedMessage += NUMBERS_AND_VOWELS[char]
        elif char.isalpha():
            decryptedMessage += REVERSE_ALPHABET[char]
        else:
            decryptedMessage += "_"
    
    return decryptedMessage

def encryptMessage(message):
    message = message.lower()
    encryptedMessage = ""
    # nextCharOpp = ""
    for i,char in enumerate(message):
        # if i+1 < len(message) and message[i+1].isalpha() and message[i+1] != " ":
        #     nextCharOpp = REVERSE_ALPHABET[message[i+1]]
        #     print(nextCharOpp,char)
        # else:
        #     nextCharOpp = ""

        # if nextCharOpp == char or not char.isalnum():
        #     encryptedMessage += char
        if not char.isalnum():
            encryptedMessage += char
        elif char in VOWELS:
            encryptedMessage += NUMBERS_AND_VOWELS[char]
        elif char.isalpha():
            encryptedMessage += REVERSE_ALPHABET[char]
        else:
            encryptedMessage += "_"
    
    return encryptedMessage

if __name__ == "__main__":
    main()