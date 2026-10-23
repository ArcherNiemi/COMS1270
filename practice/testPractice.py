def findWord(message,word):
    currentIndex = 0
    for char in message:
        if word[currentIndex] == char:
            currentIndex += 1
            if currentIndex >= len(word):
                return True
    return False

def longestStreak(message):
    currentStreak = 1
    maxStreak = 1
    currentChar = ""
    for char in message:
        if char == currentChar:
            currentStreak += 1
            if currentStreak > maxStreak:
                maxStreak = currentStreak
        else:
            currentStreak = 1
            currentChar = char
    return maxStreak

def isPerfectNumber(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i
    if number == total:
        return True
    else:
        return False

def main():
    print("thing " + str(1))

if __name__ == "__main__":
    main()