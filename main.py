#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(0,100)
print(f"Pssst, the correct answer is {random_number}")
lvl = input("Choose a difficulty. Type 'easy' or 'hard':")
easy_count = 10
hard_count = 5
global_count = 0
if lvl == "easy":
  global_count = easy_count
else:
  global_count = hard_count
while global_count > 0:
  print(f"You have {global_count} attempts remaining to guess the number")
  guess = int(input("Make a guess:"))
  if guess< random_number:
    print("Too low.")
    print("Guess again.")
  elif guess > random_number :
    print("Too high.")
    print("Guess again.")
  elif guess == random_number :
    print(f"You got it! The answer was {guess}.")
    break
  global_count -= 1