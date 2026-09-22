# Archer Niemi 9-22-2026
# Loops demo for class!

def main():
    # Without loops, work would need to be repeated manually:
    print(1)
    print(2)
    print(3)

    print("-------------------------")

    # There are two kinds of loops: while loops and for loops
    # We use a for loop when we know exacty how many times we want to repeat
    # We use a while loop when we don't know excactly how mny times we want to repeat
    # Technically, the two loops are (mostly) interchangeable

    # Example: while loop

    # loop variavle:
    x = 1
    while x <= 3:
        print(x)
        x += 1

    print("-------------------------")

    # couting down:

    seconds = 3
    while seconds > 0:
        print(seconds)
        seconds -= 1

    print("-------------------------")

    # calculate the sum from 1 to 100
    number = 1
    total = 0
    while number <= 100:
        total += number
        number += 1
    print("Sum from 1 to 100:", total)

    print("-------------------------")

    # Student exercise:
    # Save $10 each month until the balance reaches $50

    money = 0
    while money < 50:
        money += 10
    print(f"I finally saved ${money}")

    print("-------------------------")

    # Counter

    counter = 1
    while counter <= 20:
        print(counter, end=", ")
        counter += 1

    # Exercise:
    # The aboce code currently outputs this:
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    # Notice the unwanted final comma
    # We want to output this instead: 
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    # Notice, there is no final comma

    print()
    counter = 1
    while counter < 20:
        print(counter, end=", ")
        counter += 1
    print(counter)

    print("-------------------------")

    # For loops:
    # A for loop (in python) visits each item in a collection
    # Example:
    names = ["Kai", "Sam", "Alex"]

    for name in names:
        print(f"Hi, {name}!")

    # We can loop through a list of numbers
    numbers = [2,5,8,11]
    for number in numbers:
        if number == 8:
            print(f"Found {number}!")

    print("-------------------------")

    # We can print the characters in a string, because a string is an immutable collection of characters
    word = "Python"
    for character in word:
        print(character)

    print("-------------------------")

    # The range() function is how for loops are primarily (usually) constructed when using numbers
    for i in range(1, 10):
        print(i)

    print("-------------------------")

    # range() has 3 positional parameters
    # start: where we start the range (inclusive)
    # stop: where we stop the range (non - inclusive)
    # step: how many to 'count by'

    for i in range(1, 15, 3):
        print(i)

    print("-------------------------")

    # counting down:

    for i in range(10, 1, -1):
        print(i)

    print("-------------------------")

    # Student exercise:
    # Using a 'for' loop, print the following values:
    # 2,4,6,8,10
    for i in range(2,11,2):
        print(i)


if __name__ == "__main__":
    main()