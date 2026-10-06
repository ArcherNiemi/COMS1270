# Archer Niemi 10-6-2026
# Strings demo for class!

def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


def main():
    # String recap / redux
    # A string is a collection data type consisting of individual characters
    # Strings are immutable, meaning they cannot be changed oce they are created
    name = "Bob"
    print(name)

    print(name[0])

    # name[0] = "C" # Cob

    print("------------------------------")

    # String slicing
    # Slicing a string is similar to indexing into a string
    # Example:
    animal = "Leopard"
    # indexing:
    letter_L = animal[0]
    print(letter_L)

    # Slicing uses:
    # string_name[start:stop:step]
    # start is inclusive stop is non-inclusive.
    word = "Python"
    print("Word:", word)
    print("Length:", len(word))
    print("All but first character:", word[1:])

    new_word = "M" + word[1:] # Mython
    print(new_word)

    extra_new_word = new_word[:3] # Myt
    print(extra_new_word)

    super_extra_new_word = new_word[2:5] # tho
    print(super_extra_new_word)

    print("----------------------------")

    # It should be noted, that we can index into a string backwards!
    # This is done with negative numbers!
    fruit = "banana"
    last_letter = fruit[:-2] # bana
    print(last_letter)

    print("----------------------------")

    # Group Exercise

    course_code = "COMS1270"

    # Use slices to print COMS and 1270 on separate lines.

    print(course_code[:4])
    print(course_code[4:])

    print("----------------------------")

    # Step Example
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    evens = alphabet[0::2]
    odds = alphabet[1::2]
    print(evens)
    print(odds)

    # Reverse string
    hello = "Hello World!"
    revere_hello = hello[::-1]
    print(revere_hello)

    print("----------------------------")

    input_string = "Leopard" # drapoeL
    anwser = reverse_string(input_string)
    print(f"The reverse of {input_string} is {anwser}")

if __name__ == "__main__":
    main()