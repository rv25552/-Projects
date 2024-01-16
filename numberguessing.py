import random
import time
print('Welcome to the game')
n = random.randint(1, 100)
print('You have 2 chances to guess the number')
count = 2
while count!=0:
    a= int(input('Guess the number: '))
    if  a== n:
        print("Yay! That's right. You won!")
        break
    elif a > n:
        print('The number is less than ',a)
    else:
        print('The number is greater than ',a)
