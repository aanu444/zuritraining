from operator import truediv
import random


def play():
    user=input("What's your choice? 'R' for Rock, 'P' for Paper or 'S' for Scissors\n")
    user=user.lower()

    computer=random.choice(["R", "P", "S"])

    if user == computer:
        return "You and the computer have chosen {}. It is a tie".format(computer)

    if a_win(user,computer):
        return "You have chosen {} and the computer has chosen {}. You are the winner!!!".format(user,computer)
    
    return "You have chosen {} and the comuter has chosen {}. You have lost :((".format(user,computer)

def a_win(player, enemy):
    if(player =="R" and enemy =="S") or (player == "S" and enemy == "P") or (player == "P" and enemy == "R"):
        return True
    return False

def play_best_of(n):
    player_wins=0
    computer_wins=0
    wins_necessary= math.ceil(n/2)
    print(wins_necessary)

    



    

