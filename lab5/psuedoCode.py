# General Solution
# 
# Inputs: Number of People
# for each person find the percent taken by dividing the index of the loop by the number of people
# find the amount taken by multiplying the pie remaining wit hthe percent taken
# subtract the amount take from the pie remaining
# if the amount taken is greater than the most ever taken set the most ever taken to the amount and the index of the loop to the most taken perosn
#
#
# function calculatePiePerPerson(number_of_people)
#   pie_remaining is 100
#   most_taken = -1
#   most_taken_person = -1
#   loop for each person
#       percent_taken is (index_of_loop + 1) / number_of_people
#       amount_taken is pie_remaining * percent_taken
#       pie_remaining is pie_remaining - amount_taken
#       if amount_taken is greater than most_taken
#           most_taken is amount_taken
#           most_taken_person is index_of_loop + 1
#   return most_taken_person
#
# Testing
# number_of_people is 4
# 
# percent taken is 1/4
# amount taken is 25
# pie_remaining is 75
# most_taken is 25
# most_taken_person is 1
# 
# percent taken is 2/4
# amount taken is 37.5
# pie_remaining is 37.5
# most_taken is 37.5
# most_taken_person is 2
#
# percent taken is 3/4
# amount taken is 28.125
# pie_remaining is 9.375
# 
# percent taken is 4/4
# amount taken is 9.375
# pie_remaining is 0
# 
# return 2