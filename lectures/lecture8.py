# Archer Niemi 9-29-2026
# Functions demo for class

# Global variables
global_number = 5

# Function definition:

# Starts with the def keyword
# Floowed by a function name
# Then, a set of parens
# The parens contain optional function parameters
# Example:
def add_plus_two(a,b):
    answer = a + b + 2
    return answer

# As an important note - function parameters appear in the function signature (see above)
# However, function arguments appear when someone calls the function in code.
# Example:
def add_plus_three(a,b):
    # Here, a and b are function parameters
    answer = a + b + 3
    return answer

# In python, parameters and arguments can be any type which is supported by the function's operations
# Example:
def add(a,b):
    answer = a + b
    return answer

# As an advanced thing to know, be aware that functions are technically objects
# Meaning - we can pass them (name only) into other functions

def circle_area(radius):
    return 3.14 * radius ** 2

def wacky_area(radius):
    return radius ** 3

def circle_volumne(radius, height):
    base_area = circle_area(radius)
    volume = base_area * height
    return volume

# Please note - we have default values of function parameters, so long as those default values come
# at the end of the parameter list
def cylinder_measurements(radius, area_function, height=1):
    base_area = area_function(radius)
    volume = base_area * height
    return base_area, volume

# Student Exercise:
# 1. Write the price of a quantity of items as a function (price * quantity)
# 2. Write the total of an order including (price, quantity, and delivery fee) as a function
# 3. Print out the results

def cost(price, quantity):
    return price * quantity

def order_total(order, delivery_fee): # Takes in a list of dicts with price, quantity and delivery fee
    total = 0
    for item in order:
        item_cost = cost(item["price"], item["quantity"])
        total += item_cost
    total += delivery_fee
    return total

# Function stubs
# A stub is an unfinished function - where we either print a placeholder value or use pass
# Remember - 'pass' does nothing

def print_report():
    print("FIXME: Finish the report steps.")
    # Or use pass

# Function scope defines where a specific variable or name is available.
# Local scope: inside a function
# Global scope: at module level

# Typically, global level variables are kept at the very top of a module
def print_variables(parameter_number=-1):
    global global_number
    print(global_number)

    local_number = 7
    print(local_number)

    print(parameter_number)

    # Updating global values in a function
    global_number = 1
    global_number += 1
    print(global_number)

# Order of visibility:
# Global
#   ↓
# Local / Parameter values

def main():
    # We can call a function anywhere we like so long as it is defined
    # Here, we are calling it from the main() function
    value = add_plus_two(1,2)
    print(f"The value is: {value}")

    # Here, 2 and 3 are not parameters, but are called arguments:
    value = add_plus_three(2,3)
    print(f"The value is: {value}")

    value = add("Hello ","World!")
    print(f"The value is: {value}")

    value = add(3,4)
    print(f"The value is: {value}")

    print("---------------------")

    area, volume = cylinder_measurements(2, wacky_area, 5)
    print(f"Area, Vol: {area}, {volume}")

    print("------------------------")

    total = order_total([{"price": 10, "quantity": 5},{"price": 50, "quantity": 2},{"price": 2, "quantity": 20}],20)
    print(f"Total: ${total}")

    print("------------------------")

    print_report() # remeber, we always have to use parens

    print("------------------------")

    print_variables()
    # print(local_number) Ths does not work - local_number exists only inside the function
    print(global_number)

if __name__ == "__main__":
    main()