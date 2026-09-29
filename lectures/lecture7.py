# Archer Niemi 9-24-2026
# Loops demo for class

def count_divisors(number):
    # div = 1
    # count = 0
    # while div != (number + 1):
    #     if number % div == 0:
    #         count += 1
    #     div += 1

    count = 0
    for div in range(1, int(number**0.5) + 1):
        if div ** 2 == number:
            count += 1
        elif number % div == 0:
            count += 2
    return count

def main():
    text_value = 36
    answer = count_divisors(text_value)

    print(f"There are {answer} divisors of {text_value}!")

if __name__ == "__main__":
    main()