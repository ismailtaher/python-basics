import sys  # to exit game
import random  # to randomly choose for computer
from enum import Enum  # to map user inputs to values

# Enum (short for Enumeration) is a way to create a group of named constant values.
# using an Enum to make the values for Rock, Paper, and Scissors more readable.


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input(
    'Enter... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n')

# casting to int bcz val input by user is always sting data
player = int(playerchoice)

if player > 3 or player < 1:
    sys.exit("You must enter a value between 1 & 3")

# computer will randomly choose between these vals in the string i.e. 1, 2 or 3
computerchoice = random.choice("123")

# casting to number for computer choice
computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("🥳 You win!")
elif player == 2 and computer == 1:
    print("🥳 You win!")
elif player == 3 and computer == 2:
    print("🥳 You win!")
elif player == computer:
    print("😮 Tie game!")
else:
    print("🐍 Python wins!")
