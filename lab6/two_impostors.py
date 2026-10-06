def is_less_than(a, b):
    return a < b

def has_correct_sum(a, b, expected_sum):
    return a + b == expected_sum

def has_divisible_product(a, b, divisor):
    return (a * b) % divisor == 0

def has_minimum_difference(a, b, minimum_difference):
    return b - a > minimum_difference

def has_maximum_difference(a, b, maximum_difference):
    return b - a < maximum_difference

def does_not_divide_evenly(a, b):
    return a % b != 0 and b % a != 0

def is_impostor_pair(a, b, expected_sum, product_divisor,
minimum_difference, maximum_difference):
    return is_less_than(a, b) and has_correct_sum(a, b, expected_sum) and has_divisible_product(a, b, product_divisor) and has_minimum_difference(a, b, minimum_difference) and has_maximum_difference(a, b, maximum_difference) and does_not_divide_evenly(a, b)

def find_impostors(num_employees, expected_sum, product_divisor,
minimum_difference, maximum_difference):
    for a in range(1,num_employees+1):
        for b in range(1,num_employees+1):
            if(is_impostor_pair(a, b, expected_sum, product_divisor,minimum_difference, maximum_difference)):
                return (a,b)
    return None

def main():
    employees = 20
    sum = 23
    divisor = 12
    min_difference = 5
    max_difference = 9999
    impostors = find_impostors(employees, sum, divisor, min_difference, max_difference)
    print(impostors)

if __name__ == "__main__":
    main()