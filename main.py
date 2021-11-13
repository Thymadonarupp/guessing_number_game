from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's guest against acutual answer
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high 😫")
    #track number of remain attemps
    return turns - 1
  elif guess < answer:
    print("Too low 😬")
    #track number of remain attemps
    return turns - 1
  else:
    print(f"You got the answer🥳 . The answer is {answer}")

#function set diffculty
def set_difficulty():
  level = input("Choose the difficulty 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #choose a random number 1-100
  print('Welcome to the guessing game! 😍 ')
  print("I'm thinking of a number between 1 and 100 🧐")
  answer = randint(1,100)
  print(f"Pssst, the correct answer is {answer}")

  #let the users guess numbers
  turns = set_difficulty()
  
  #repeat until they get it right
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print("You run out of guess, you lose  🤒 ")
      return

game()