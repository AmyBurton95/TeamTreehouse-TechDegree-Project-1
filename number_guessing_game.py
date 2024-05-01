import random
import statistics

name = input("<------  Enter Player Name: ") + "!"
print(f"<------  Welcome, {name} Welcome to the Number Guessing Game  ------>")
start = input("<------  Would you like to play? Y/N  ").upper()

attempts_list = []
low = 1
high = 10
high_scores = []


def start_game(low, high):
    answer = random.randint(1, 10)
    counter = 0
    if len(high_scores) == 0:
        print("There is no highscore yet")
    else:
        print(f"The best guesses to beat are {min(high_scores)}")
    while True:
        try:
            guess = int(input(f"<------  Choose a number between {low} & {high}: "))
        except ValueError:
            print("Oops, please choose a valid number.")
            continue
        counter += 1
        if guess > answer:
            print(f"Oops {guess}, that is too high!")
            attempts_list.append(guess)
        elif guess < answer:
            print(f"Oops {guess}, that is too low!")
            attempts_list.append(guess)
        else:
            print(f"{guess} was correct! Well done!")
            print(f"That took {counter} guesses.")
            attempts_list.append(guess)
            sorted_attempts = sorted(attempts_list)
            high_scores.append(counter)
            contin = input("<------  Would you like to continue playing? Y/N ").upper()
            if contin == "Y":
                start_game(low, high)
            else:
                print("Okay, see you next time!")
                game_stats = input("<------  Would you like to see your stats from this game? Y/N  ").upper()
                if game_stats == "Y":
                    print(f"<-  The mean of your guesses was {statistics.mean(sorted_attempts)}")
                    print(f"<-  The median of your guesses was {statistics.median(sorted_attempts)}")
                    print(f"<-  The mode of your guesses was {statistics.mode(sorted_attempts)}")
                    print(sorted_attempts)
                break
            attempts_list.append(guess)
            break


if start == "Y":
    start_game(low, high)
else:
    print("Okay, see you next time!")

