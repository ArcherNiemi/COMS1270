# Archer Niemi 9-1-2026
# Lecture 2 demo

# import modules
# please note, all the modules you use should be imported at the top
import math
import random

# A variable, is a name for a value
x = 10
print(x)

# A variable can receive a new value
y = 20
print(y)

x = y
print(x)

# Expressions in python are evaluated on the right hand side
x = x * 2
z = x + y
print(z)

# the type() function shows an object's type
# the id() function shows its identity
temperature = 72
print(temperature)
print(type(temperature))
print(id(temperature))

print(type("Hello"))

# A number with a decimal point is a float
miles = float(input("Please enter a distance in miles: "))
hours_to_fly = miles / 500.0
print(miles, "miles would take:")
print(hours_to_fly, "hours to fly")

# e means times 10 to a power
speed_of_light = 3.0e8
print(speed_of_light)

# f"{.Xf}" shows X digits after the decimal point
pi = 3.1415926
print(f"{pi:.2f}")

# Arithmetic operators
# common:
print(7 + 3)
print(7 - 2)
print(7 * 3)
print(7 / 2)
print(7 // 2)
print(7 % 2)

print("---------")

# order of operations: PEMDAS

result = 2 + 3 * 4 - 4 / 2 # 2 + 12 - 2
print(result)

# parens change order of operations
result = (2 + 3) * 4
print(result)

# convert minutes to hours and leftover minutes
total_minutes = 135
hours = total_minutes // 60 # floor divide gets the whole number part of a division
minutes = total_minutes % 60 # mod gets the left over (remainder) part
print(hours, minutes)

# modules
print(math.pi)

print(random.random())