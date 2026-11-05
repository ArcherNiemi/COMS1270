import math
# Archer Niemi 11-5-2026

def find_number(lower_bound, upper_bound, real_number, guesses):
    for i in range(guesses):
        mid_number = ((upper_bound - lower_bound) / 2) + lower_bound
        if real_number > mid_number:
            lower_bound = mid_number
        else:
            upper_bound = mid_number

    if math.ceil(lower_bound) == math.floor(upper_bound):
        return math.floor(upper_bound)

def find_number_of_guesses(lower_bound, upper_bound):
    guesses = 0
    while(math.ceil(lower_bound) != math.floor(upper_bound)):
        mid_number = ((upper_bound - lower_bound) / 2) + lower_bound
        if lower_bound > mid_number:
            lower_bound = mid_number
        else:
            upper_bound = mid_number
        guesses += 1
    return guesses

def main():
    print(find_number_of_guesses(1,8))

if __name__ == "__main__":
    main()