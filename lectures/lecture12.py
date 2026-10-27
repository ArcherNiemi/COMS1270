# Archer Niemi 10-27-2026
# Classes demo for class!

# We've already seem 'built in' objects
# Strings
# Lists
# Dictionaries

# Now, we want to be able to make our own data types
# A Class is like a 'blueprint' - like a blueprint for a car
# An object is like the physical thing made from that blueprint
# For example, a 'Car' class would be the blueprint
# My green Subaru would be the object
# Many pbjects can be made from the same class
# Ex: red car, green car, blue car, etc.

# Typically, we find class definitions in 'global space'
# this is the same as where we usually find function definitions

# Please note that things that look like function, but which 
# are inside a class, are called 'methods.'

# Functions exist outside a class
# Methods exist inside a class

class Student:
    # Class attributes are shared between all instances
    course = "COMS 1270"

    # __init__ gives each new object its starting values.

    def __init__(self, name, score=0):
        # Instance variables hold values for each object
        self.name = name
        self.score = score

    # An instance method is a function inside a class
    # self refers to the instance calling the method
    def print_into(self):
        print(self.name,self.score)

    # The class interface is the set of methods callers use.
    def update_score(self,score):
        if not self._valid_score(score):
            return False
        self.score = score
        return True

    # A leading underscore marks an internal helper by convention
    def _valid_score(self, score):
        return 0 <= score <= 100

    # __str__ controls what prints(student1) displays
    def __str__(self):
        return f"{self.name}: {self.score}"

    # __lt__ defines how two students compare with <
    def __lt__(self, other):
        return self.score < other.score

def main():
    student1 = Student("Jeff", 40)
    print(student1)

    student2 = Student("Bob", 80)
    print(student1 < student2)

if __name__ == "__main__":
    main()