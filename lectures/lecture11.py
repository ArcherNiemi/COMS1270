# Archer Niemi 10-20-2026

def isPalindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True

def wordDecrypter(word):
    return "".join([char for char in word[::2]])

def main():
    print(isPalindrome("thht"))
    print(wordDecrypter("wxoxrxdxDxexcxrxyxpxtxexr"))

if __name__ == "__main__":
    main()