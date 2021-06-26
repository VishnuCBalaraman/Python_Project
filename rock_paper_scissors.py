import random


def Game(player_choice):
    list1=["rock","paper","scissors"]
    player_mark=0
    comp_mark=0
    comp_choice=random.choice(list1)
    print("-----------------------------")
    print("Your Choice:",player_choice,"\nComputer Choice:",comp_choice)
    if player_choice == comp_choice:
        print("Both players selected",player_choice,". It's a tie!\n")
    elif player_choice == "rock":
        if comp_choice == "scissors":
            print("Rock smashes Scissors! You win\n")
            player_mark += 1
        else:
            print("Paper covers Rock! You lose\n")
            comp_mark += 1
    elif player_choice == "paper":
        if comp_choice == "rock":
            print("Paper covers Rock! You win\n")
            player_mark += 1
        else:
            print("Scissors cuts Paper! You lose\n")
            comp_mark += 1
    elif player_choice == "scissors":
        if comp_choice == "paper":
            print("Scissors cuts Paper! You win\n")
            player_mark += 1
        else:
            print("Rock smashes Scissors! You lose\n")
            comp_mark += 1

    return comp_mark,player_mark

def play(count):
    c_mark=0
    p_mark=0
    while(count>0):
        player_choice = input("\nEnter a choice (rock, paper, scissors): ")
        if player_choice=="rock" or player_choice=="paper" or player_choice=="scissors":
            comp_mark,player_mark=Game(player_choice)
            c_mark=c_mark+comp_mark
            p_mark=p_mark+player_mark
        else:
            print("----------------------------")
            print("Invalid Input\n")
        count=count - 1
    return c_mark,p_mark

class rock_paper_scissors:

    print("\\\** WELCOME TO ROCK-PAPER-SCISSORS GAME **//\n")
    count=int(input("How many times do you want to play : "))
    comp_mark,player_mark=play(count)

    if(comp_mark > player_mark):
	    print("YOU LOST!\nComputer Score:",comp_mark,"\nYour Score:",player_mark)
    elif(comp_mark == player_mark):
        print("IT'S A TIE!\nComputer Score:",comp_mark,"\nYour Score:",player_mark)
    else:
	    print("YOU WON!\nComputer Score:",comp_mark,"\nYour Score:",player_mark)
