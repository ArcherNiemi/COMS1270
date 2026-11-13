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

def list_shifter(seats,shift):
    new_seats = []
    for i in range(len(seats)):
        seat_index = (i + shift) % len(seats)
        new_seats.append(seats[seat_index])
    return new_seats

def number_finder(numbers):
    double_numbers = find_double_numbers(numbers)
    for number in numbers:
        if not number in double_numbers:
            return number

def find_double_numbers(numbers):
    double_numbers = []
    for i in range(len(numbers)-1):
        if numbers[i] in numbers[i+1:]:
            double_numbers.append(numbers[i])
    return double_numbers

def find_pair(numbers, target):
    for i,number1 in enumerate(numbers):
        for j,number2 in enumerate(numbers):
            if number1 + number2 == target and i != j:
                return (number1,number2)

def find_primes(upper_bound):
    primes = []
    for i in range(2,upper_bound):
        if is_prime(i):
            primes.append(i)
    return primes

def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def main():
    print(find_primes(100))

if __name__ == "__main__":
    main()