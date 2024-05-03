import random
import statistics

name = input("<------  Enter Player Name:  ------>\n")
print(f"<------  Welcome, {name} Welcome to the Number Guessing Game  ------>")
start = input("<------  Would you like to play? Y/N  ------>\n").upper()

low = 1
high = 10
high_scores = []


def start_game(low, high):
    answer = random.randint(1, 10)
    counter = 0
    game_data = []
    if len(high_scores) == 0:
        print("There is no highscore yet")
    else:
        print(f"The best guesses to beat are {min(high_scores)}")
    while True:
        try:
            guess = int(input(f"<------  Choose a number between {low} & {high}  ------>\n"))
        except ValueError:
            print("Oops, please choose a valid number.")
            continue
        counter += 1
        if guess > answer:
            print(f"Oops {guess}, that is too high!")
            if guess > high:
                print(f"Please choose a number within the range - {low} & {high}")
        elif guess < answer:
            print(f"Oops {guess}, that is too low!")
            if guess < low:
                print(f"Please choose a number within the range - {low} & {high}")
        else:
            print(f"{guess} was correct! Well done!")
            print(f"That took {counter} guesses.")
            high_scores.append(counter)
            sorted_high_scores = sorted(high_scores)
            contin = input("<------  Would you like to continue playing? Y/N  ------>\n").upper()
            if contin == "Y":
                start_game(low, high)
            else:
                print("Okay, see you next time!")
                game_stats = input("<------  Would you like to see your stats from this game? Y/N  ------>\n").upper()
                if game_stats == "Y":
                    print(f"<-  The mean of your guesses was: {statistics.mean(sorted_high_scores)}  ->")
                    print(f"<-  The median of your guesses was: {statistics.median(sorted_high_scores)}  ->")
                    print(f"<-  The mode of your guesses was: {statistics.mode(sorted_high_scores)}  ->")
                    print(sorted_high_scores)
                break
            break


if start == "Y":
    start_game(low, high)
else:
    print("Okay, see you next time!")