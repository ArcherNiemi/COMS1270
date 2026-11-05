# Archer Niemi 11-3-2026

"""COM S 1270 - Chapter 10: Exceptions

Lecture date:
Author:
Purpose: Monster Battle Simulator - Student Starter

How the game works:
Both characters start with 100 HP. Each turn, choose Attack to deal
9 damage or Heal to recover 10 HP (up to 100). If the monster survives,
it attacks for 5-15 damage. The battle ends when either character's
HP reaches 0. In Part 2, invalid input also ends the battle.

PART 1: Complete the normal game.
PART 2: Add exception handling after the game works.

Replace each ___ with your code.
"""

import random

ATTACK_DAMAGE = 9
HEAL_AMOUNT = 10

def player_turn(action, player_hp, monster_hp):
    if action == "Attack":
        if monster_hp < ATTACK_DAMAGE:
            print(f"Player attack! Monster loses {monster_hp} HP.")
            monster_hp = 0
        else:
            monster_hp -= ATTACK_DAMAGE
            print(f"Player attack! Monster loses {ATTACK_DAMAGE} HP.")

    if action == "Heal":
        player_hp += HEAL_AMOUNT
        if player_hp > 100:
            player_hp = 100
        print("You heal!")

    return player_hp, monster_hp

def monster_turn(player_hp, monster_hp):
    if monster_hp <= 0:
        return player_hp

    random_damage = random.randint(5,15)

    if player_hp < random_damage:
        damage_delt = player_hp
        player_hp = 0
    else:
        damage_delt = random_damage
        player_hp -= random_damage

    print(f"Monster attacks! You lose {damage_delt} HP")

    return player_hp


# Print the final result
def print_final_result(player_hp, monster_hp):
    print()
    print("===== Final Result =====")

    print(f"Player HP: {player_hp}")
    print(f"Monster HP: {monster_hp}")

    if player_hp <= 0:
        print("Game Over! The monster wins!")
    elif monster_hp <= 0:
        print("You defeated the monster!")
    else:
        print("The battle ended without a winner")  

def monster_battle(player_hp, monster_hp):
    if player_hp <= 0 or monster_hp <= 0:
        raise ValueError("Starting HP must be positive for both characters")

    actions = ["Attack", "Heal"]

    print("===== Monster Battle =====")
    print("===== Game Rules =====")
    print("Both characters start with 100 HP.")
    print("0 = Attack: deal 9 damage to the monster.")
    print("1 = Heal: recover 10 HP, up to 100 HP.")
    print("Healing uses your turn, even at full health.")
    print("If the monster survives, it deals 5-15 damage.")
    print("HP cannot go below 0.")
    print("Defeat the monster to win. Reach 0 HP and you lose.")
    print("Invalid input ends the battle without a winner.")
    print("======================\n")

    print("Starting Player HP:", player_hp)
    print("Starting Monster HP:", monster_hp)

    round_number = 1
    while player_hp > 0 and monster_hp > 0:

        print("\n----------------------------------------")
        print(f"Round {round_number}")

        try:
            choice = int(input("0 = Attack or 1 = Heal: "))
            action = actions[choice]
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        except IndexError:
            print("Invalid action! Choose 0 or 1.")
            continue

        player_hp, monster_hp = player_turn(action, player_hp, monster_hp)

        player_hp = monster_turn(player_hp, monster_hp)

        print("--- Current Status ---")
        print("Player HP:", player_hp)
        print("Monster HP:", monster_hp)

        round_number += 1

    print_final_result(player_hp, monster_hp)


def main():
    player_hp = 100
    monster_hp = 100

    monster_battle(player_hp, monster_hp)


# ============================================================
# PART 2: ADD EXCEPTION HANDLING
# Begin this part only after Part 1 works with valid input.
# ============================================================

# TODO 1: Call monster_battle(-10, 100) in main().
# Observe what happens. Does the game reject the starting HP?

# TODO 2: At the beginning of monster_battle(), check both starting HP
# values. If either is 0 or negative, raise ValueError with the message:
# Starting HP must be positive for both characters.
# Test again, then restore the original function call with 100 hp for both.

# TODO 3: Run the game and enter hello.
# Observe the exception type and where the error occurs.

# TODO 4: Add try/except inside the loop to catch ValueError and print:
# Invalid input! Please enter a number.
# Use break in the handler to end the loop.

# TODO 5: Run the game again and enter 5.
# Observe the exception type and where the error occurs.

# TODO 6: Add an except block to catch IndexError and print:
# Invalid action! Choose 0 or 1.
# Use break in the handler to end the loop.

# TODO 7: Put the current-status heading and HP prints in a finally
# block. Test that they still print before break exits the loop.

# TODO 8: Update print_final_result() to handle an unfinished battle.
# Determine which of these three messages to print:
# You defeated the monster!
# Game Over! The monster wins!
# The battle ended without a winner.


if __name__ == "__main__":
    main()
