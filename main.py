import random

lst = ["rock", "paper", "scissor"]
d1 = {
    "rock": "\U0001FAA8",
    "paper": "\U0001F4C4",
    "scissor": "\U00002702"
}

player_win_count  = 0
comp_win_count = 0

while True:

    player_choice = input("If you want to exit so Enter |exit| , If you don't want exit so Enter |not|: ")
    if player_choice == "not":

        comp = random.randrange(0, 3)
        player = int(input("Enter:0 for Rock , Enter:1 for Paper and Enter:2 for Scissor: "))
        if player==0 and comp==2:
            print(f"player wins because player chose {d1[lst[player]]} ")
            player_win_count+=1

        elif player == 1 and comp==0:
            print(f"player wins because player chose {d1[lst[player]]} ")
            player_win_count += 1

        elif player==2 and comp==1:
            print(f"player wins because player chose {d1[lst[player]]} ")
            player_win_count += 1

        elif comp == 0 and player==2:
            print(f"comp wins because player chose {d1[lst[comp]]} ")
            comp_win_count+=1

        elif comp==1 and player==0:
            print(f"comp wins because player chose {d1[lst[comp]]} ")
            comp_win_count += 1

        elif comp==2 and player==1:
            print(f"comp wins because player chose {d1[lst[comp]]} ")
            comp_win_count += 1

        elif (player ==0 and comp==0) or (player == 1 and comp==1) or (player == 2 and comp==2):
            print(f"match is tie because player has {d1[lst[player]]} and comp has also {d1[lst[comp]]}")
            player_win_count+=1
            comp_win_count+=1
        else:
            print("your enter wrong entries please enter right number")
    elif player_choice == "exit":
        break
    else:
        print("Please choose correct entry, So If you don't want to play Enter exit or You want to play enter not")

if comp_win_count<player_win_count:
    print(f"---Congratulations! your score is {player_win_count}!---")
elif comp_win_count>player_win_count:
    print(f"---You lost! your score is {player_win_count}!---")
else:
    print(f"---Game is Tie your score {player_win_count} and comp score is {comp_win_count}---")

print("--We hope you enjoyed your game--")
