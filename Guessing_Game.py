#guessing Game
#Importing Random Module from Python Library
import random

def Guess(lowValue, highValue, randNum, count = 0):
    if (highValue >= lowValue):
        guess = lowValue + (highValue - lowValue)//2

        # if guess is in the middle, it is found!

        if (guess == randNum):
            return count
        elif (guess > randNum):
            count = count + 1
            return Guess(lowValue, guess - 1, randNum, count)
        else:
            count = count + 1
            return Guess(guess + 1, highValue, randNum, count)
    else:
        
        return -1



#Generate a random number between 1 and 100
randNum = random.randint(1, 101)

count = 0
guess = -99

#While Loop to run the program if guess is not randNum
while (guess != randNum):
    guess = int(input ("Enter your guess between 1 and 100:"))
    if (guess < randNum):
        print('Your number is lower than guessing number')
    elif (guess > randNum):
        print('Your number is higher than guessing number')
    else:
        print('You guess the right number.')
        break
    count = count + 1
print ("Altogether, I took " + str(count) + " steps to guess the number")
print ('Computer took '+ str(Guess(0,100,randNum))+ ' steps!')
