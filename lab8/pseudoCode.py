# board = [
#     ["P", ".", "G"],
#     [".", "#", "K"],
#     ["T", "M", "V"]
# ]
# Move right
# Move right
# Move down

# To determine if valid move check the location you are trying to move to and make sure it is not a wall and is within the bounds
# To make move player you check find the move tile based on where you are right now and then you check if it is valid then change the players position to be there and resolve related effects
# To collect items just check the character of the space and determine what to change
# To check trap do the same thing as collect item (I don't know why this exists)
# To check win count all keys floppsie has and make sure it is greater than or equal to 8 and that floppsie is on a v space