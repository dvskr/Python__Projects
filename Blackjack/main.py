from random import choice
from art import logo

print(logo)
def deal():
    cards=['A',2,3,4,5,6,7,8,9,10,'J','K','Q']
    pick=choice(cards)
    print(f"card drawn {pick}")
    if pick=="A":
        card_value=11
        return card_value
    if pick=="J" or pick=="K" or pick=="Q":
        card_value=10
        return card_value
    else:
        card_value=pick
        return card_value

game_start=input("Do you want to start the game choose: yes or no\n")

game=False
if game_start=="yes":
    game=True

player_round=True
dealer_round=True

while game:

    dealer_list=[]
    player_list=[]
    player_round = True
    dealer_round = True

    dealer_list.append(deal())
    print(f"dealer Current count is {sum(dealer_list)}")


    while player_round:
        player_list.append(deal())
        if sum(player_list)>21 and 11 in player_list:
            player_list.remove(11)
            player_list.append(1)
        print(f"player Current count is {sum(player_list)}")
        if sum(player_list)>21:
            print("You Bust Dealer wins the game")
            player_round=False
            dealer_round=False
            one_more_round = input("Do you want to play one more round Yes or No?\n").lower()
            if one_more_round == "yes":
                game = True
            else:
                game = False
        else:
            player_decision=input("Do you want to pick one more card?: Yes or No\n").lower()

            if player_decision=="no":
                player_round=False

    while dealer_round:
        dealer_list.append(deal())
        if 17 <= sum(dealer_list) <= 21:
            dealer_round=False
        if sum(dealer_list) > 21 and 11 in dealer_list:
            dealer_list.remove(11)
            dealer_list.append(1)
        print(f"dealer Current count is {sum(dealer_list)}")

        if sum(dealer_list)>21:
            print("Dealer Bust Player wins the round")
            one_more_round = input("Do you want to play one more round Yes or No?\n").lower()
            if one_more_round == "yes":
                game = True
            else:
                game = False
        if sum(dealer_list)>sum(player_list) and sum(dealer_list)>=17:
            print("Dealer wins the round")
            one_more_round = input("Do you want to play one more round Yes or No?\n").lower()
            if one_more_round == "yes":
                game = True
            else:
                game = False
        if sum(dealer_list)==sum(player_list) and sum(dealer_list)>=17:
            print("Game Draw")
            one_more_round = input("Do you want to play one more round Yes or No?\n").lower()
            if one_more_round == "yes":
                game = True
            else:
                game = False

        if sum(player_list) > sum(dealer_list) >= 17:
            print("Player Wins")
            one_more_round = input("Do you want to play one more round Yes or No?\n").lower()
            if one_more_round == "yes":
                game = True
            else:
                game = False


