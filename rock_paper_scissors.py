import random, sys

# while true, keep the game running, have wins/losses ties initialized to 0 and
# print those out if the game quits

# at the end of the rock/paper/scissors round, 
def generate():
    number = random.randint(1,3)
    if number == 1:
        return "ROCK"
    elif number == 2:
        return "PAPER"
    else:
        return "SCISSORS"
    
wins = 0
ties = 0
losses = 0

while True:
    option = input("Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit ")
    if option == "q":
        break
    elif option == "r":
        print("ROCK vs...")
        other = generate()
        print(other)
        if other == "PAPER":
            print("You lose!")
            losses += losses + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
        elif other == "SCISSORS":
            print("You win!")
            wins += wins + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
        else:
            print("It's a tie!")
            ties += ties + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
    elif option == "p":
        print("PAPER vs...")
        other = generate()
        print(other)
        if other == "SCISSORS":
            print("You lose!")
            losses += losses + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
        elif other == "ROCK":
            print("You win!")
            wins += wins + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
        else:
            print("It's a tie!")
            ties += ties + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
    else:
        print("SCISSORS vs...")
        other = generate()
        print(other)
        if other == "ROCK":
            print("You lose!")
            losses += losses + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
        elif other == "PAPER":
            print("You win!")
            wins += wins + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue
        else:
            print("It's a tie!")
            ties += ties + 1
            print("Wins: " + str(wins) + " Ties: " + str(ties) + " Losses: " + str(losses))
            continue

print("GG, your final total was:")
print("Wins: " + str(wins) + " " + "Ties: " + str(ties) + " Losses: " + str(losses))