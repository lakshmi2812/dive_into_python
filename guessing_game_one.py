#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too #low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

def guessing_game_one():
    random_num = random.randint(1,9)
    print(random_num)
    count = 0
    usr_input = 0
    while usr_input != random_num and usr_input!= 'exit':
        usr_input = input('Please enter a number: ')
        if usr_input == 'exit':
            print('Game over!')
            break
        elif int(usr_input) > random_num:
            count+=1
            print('Your number is greater')
        elif int(usr_input) < random_num:
            count+=1
            print('Your number is smaller')
        else:
            print('You guessed the number! Congrats! You won!!')
            print('You have taken ' + str(count) + ' guesses!')
    

if __name__ == '__main__':
    #usr_input = input('Please enter a number: ')
    guessing_game_one()
    

    