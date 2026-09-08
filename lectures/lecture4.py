# Archer Niemi 9-8-2026
# zyBooks Chapter 3 Demos

# Section 3-1 Strings

# input() returns a string
name = input("Please Enter Your Name: ")
place = input("Please Enter a Place: ")
verb = input("Please Enter a Verb: ")
noun = input("Please Enter a Noun: ")

print(name + " went out to " + place + ". He " + verb + " all over the " + noun + "!")

# To 'mass comment'/'mass uncomment' test: CRTL+/

# input() always returns a string value. If we want something else, we need to convert it:
# int()
# float()
# str()
# bool()

number = float(input("Please input an float: "))
number = int(number)
print(type(number))
number = str(number)
print("My favorite number is: " + number)
print(type(number))

# String indices start at 0
name = "Floopsie Hugglebun"
print(name[0])

# Two primary classification of types in Python
# Mutable types:
# Lists, Dictionaries, Sets
# Immutable types
# Integers, Floats, Booleans, Tuples, and Strings

name = "Peter"
print(id(name))
name += " Petwolf"
print(id(name))
print(name)

# Lists
prices = ["$20", 14.99, 5]
print(prices)
print(prices[0])

prices[0] = "$20.99"
print(prices)

print(prices[0][0])

# .append() method
prices.append("7")
print(prices)

# .pop() method
prices.pop()
print(prices)

prices.pop(0)
print(prices)

# .remove() method
prices.append(14.99)
print(prices)
prices.remove(14.99)
print(prices)

# Tuples
coordinates = (10,20)
print(type(coordinates))
print(coordinates)

#Dictionaries
fruits = {"Apples": 3, "Oranges": 5, "Dragon Fruit": 10, "Grapes": 9}

print(fruits["Grapes"])