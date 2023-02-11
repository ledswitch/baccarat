from random import choice
credit = 200.0
cards = [2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 1]
bet = 0
tie = False
while True:
    print("You have $" + "{:.2f}".format(credit))
    if credit <= 0:
        print("You have no credit left! Goodbye")
        break
    if not tie:
        bet = input("How much do you want to bet?")
        if not bet.isnumeric() or int(bet) <= 0 or int(bet) > credit:
            print("Invalid Bet")
            continue
    else:
        print("$" + bet + " bet carried over from tie.")
        tie = False
    outcome = input("Are you backing the (b)ank or the (p)layer or (q)uit?")
    if outcome == "q":
        print("You finished with $" + str(credit))
        break
    if outcome != "b" and outcome != "p":
        print("Invalid Backing")
    player_hand = (choice(cards) + choice(cards)) % 10
    bank_hand = (choice(cards) + choice(cards)) % 10
    print(str(player_hand) + " player")
    print(str(bank_hand) + " banker")
    if not (player_hand == 8 or player_hand == 9 or bank_hand == 8 or bank_hand == 9):
        if player_hand <= 5:
            third_card = choice(cards)
            player_hand += third_card % 10
            if bank_hand <= 2:
                bank_hand += choice(cards) % 10
            if bank_hand == 3 and third_card != 8:
                bank_hand += choice(cards) % 10
            if bank_hand == 4 and 2 <= third_card <= 7:
                bank_hand += choice(cards) % 10
            if bank_hand == 5 and 4 <= third_card <= 7:
                bank_hand += choice(cards) % 10
            if bank_hand == 6 and 6 <= third_card <= 7:
                bank_hand += choice(cards) % 10
        print("After drawing rules: ")
        print(str(player_hand) + " player")
        print(str(bank_hand) + " banker")
    if player_hand > bank_hand:
        print("Player Win")
        if outcome == "p":
            print("You win " + "$" + bet)
            credit += int(bet)
        else:
            print("You lose " + "$" + bet)
            credit -= int(bet)
    elif bank_hand > player_hand:
        print("Bank Win")
        if outcome == "b":
            print("You win " + "$" + str(round(int(bet) * 0.95, 2)))
            credit += round(int(bet) * 0.95, 2)
        else:
            print("You lose " + "$" + bet)
            credit -= int(bet)
    else:
        print("Tie")
        print("You win " + "$" + 8 * bet)
        credit += 8 * int(bet)
        tie = True
