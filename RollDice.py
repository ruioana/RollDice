"""This is a roll the dice game. it will be you vs the computer"""

from random import randint
from time import sleep
def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print ("The maximum possible value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print ("Your guess is to high.. try again!")
  else:
    print ("Rolling...")
    sleep(2)
    print ("The 1st roll is: %d" % first_roll)
    sleep(1)
    print ("The 2nd roll is: %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    if guess > total_roll:
        print ("You won!")
    else:
        print ("You lost!")
roll_dice(15)  