# Archer Niemi 9-3-2026
# Expressions problems demo

def calculate_prices(total_value, difference):
    item1 = (total_value - difference) / 2
    item2 = item1 + difference

    return item1, item2

def main():
    total_value = 27
    difference = 15

    item1, item2 = calculate_prices(total_value, difference)
    print("The price of item1 is:", item1, "The price of item2 is:", item2)

if __name__ == "__main__":
    main()