def rock_paper_scissors(player1, player2):
    congrats_msg = 'Congrats! You have won' 
    while True:
        if player1 == 'rock' and player2 == 'scissors':
            print(congrats_msg +  " " + 'Player1!')
            ui1 = input('Player1, Are you up for another game? y/n?')
            ui2 = input('Player2, Are you up for another game? y/n?')
            if ui1 == 'n' or ui2 == 'n':
                print('Sorry, the other player is not interested! :(')
                break
            break
        elif player1 == 'scissors' and player2 == 'rock':
            print(congrats_msg + " " + 'Player2!')
            break
        elif player1 == 'scissors' and player2 == 'paper':
            print(congrats_msg + " " + 'Player1!')
            break
        elif player1 == 'paper' and player2 == 'scissors':
            print(congrats_msg + " " + 'Player2!')
            break
        elif player1 == 'paper' and player2 == 'rock':
            print(congrats_msg + " " + 'Player1!')
            break
        elif player1 == 'rock' and player2 == 'paper':
            print(congrats_msg + " " + 'Player2!')
            break
        elif player1 == player2:
            print('It\'s a tie!')
            break
        else:
            print('Something\'s wrong. Try again!')
            break
        ui1 = input('Player1, Are you up for another game? y/n?')
        ui2 = input('Player2, Are you up for another game? y/n?')
        if ui1 == 'n' or ui2 == 'n':
            print('Sorry, the other player is not interested! :(')
            break
        else:
            rock_paper_scissors(player1, player2)
            break
    
if __name__ == '__main__':
    player1 = input('Player1 - Please enter your choice: ')
    player2 = input('Player2 - Please enter your choice: ')
    rock_paper_scissors(player1, player2)
        