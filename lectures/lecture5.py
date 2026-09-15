# Archer Niemi 9-15-2026
# Branching Demo for class

def main():
    print(f"My name is: {__name__}")

    # Branching syntax rules:
    # 1. Put : at the end of if, elif, and else.
    # 2. Indent the code inside each branch

    score = 21

    # if
    if score > 50:
        print(f"Score is: {score}")

    # if-else
    if score > 90:
        print(f"Score is: {score}")
    else:
        print("Score is less than 90!")

    # if-elif-else
    if score > 90:
        print(f"Score is: {score}")
    elif score > 80:
        print("Awesome! Greater than 80!")
    else:
        print("Very low score!")

    print("-----------------------------------")

    # Detecting equal values with branches

    # Use == to compare values
    # Use = to assign a value
    # Use != to check whether values are not equal

    number = 10
    weather = "sunny"

    if number != weather:
        print("That was strange...")
    else:
        print("Moving on with life")

    print("-----------------------------------")

    # Student Exercise
    # red -> "Stop"
    # yellow -> "Slow Down"
    # green -> "Go"

    light = "yellow"

    if light == "red":
        print("Stop")
    elif light == "yellow":
        print("Slow Down")
    else:
        print("Go")

    print("-----------------------------------")

    # Detecting ranges with branches

    # Branch order matters

    grade = 95

    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")

    print("-----------------------------------")

    # Using boolean operators

    # Remeber, boolean values are either True or False
    # The logical operators we use are: and, or, not

    # The 'rules' are that:
    # False and 'anything' is False
    # True or 'anything' is True
    # not flips True to False and False to True

    # Check:
    age = 20
    has_id = True
    day = "Saturday"
    is_raining = False

    if age >= 18 and has_id:
        print("You may enter.")

    if day == "Saturday" or day == "Sunday":
        print("Weekend")

    if not is_raining:
        print("Outdoor event can continue")


# We start with an 'if' statement
# we ask Python if the __name__ variable has been set to the string "__main__"
# __name__ is a variable that is 'baked into the cake' of Python
# Typically, anything starting with two underscores (called a 'dunder') the user does not 'mess with.'
# The name "__main__" is assigned to the file/ module that we run from the terminal
# Every file/ module has its own name. That name is typically the same as the file name.
# In this case, it is different - only one thing (ever) can be called __main__ 
if __name__ == "__main__":
    main()