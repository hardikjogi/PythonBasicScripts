# This is a guess the number game.
import random
print('Hello. What is your name?')
name = input()

print('Well, ' + name + ' , I am thinking of a number between 0 and 50')
secretNumber = random.randint(1,50)

#Ask the player to guess 7 times
for guessesTaken in range(1,8):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
      print('Your guess  is too low')
    elif guess > secretNumber:
      print('Your guess is too high')
    else:
      break

if guess == secretNumber:
      print('Good job, '+ name + '! you guessed my number correctly')
else:
      print('Nope. The number I was thinking of was str(secretNumber)')
      
