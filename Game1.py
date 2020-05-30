from random import randint
import unittest
# This function displays the leaderboard and sorts it.


def display_leaderboard(which_leaderboard):
    with open("Game 1 Leaderboard.txt", "r") as leaderboard_file:
        print(f"{which_leaderboard} Leaderboard:\n")
        leaderboard_data = leaderboard_file.read().strip().split("\n")
        leaderboard = [player_details.split(",")
                       for player_details in leaderboard_data]
        sorted_leaderboard = sorted(
            leaderboard, key=lambda player: int(player[1]), reverse=True
        )
        for place, player in enumerate(sorted_leaderboard, 1):
            print(f"{place}){player[0]} scored: {player[1]} points.")
    print()


try:
    display_leaderboard("Current")
except FileNotFoundError:
    pass


#  This is the list of authorised players.
authorised_players = ["Ammar", "Bob", "Kevin", "James", "Lebron", "Steve"]

# This function is to check if the player is on the authorised players list.


def authorisation(which_player):

    while True:
        name = input(
            f"Player {which_player} enter your name.\n").strip().title()
        if name not in authorised_players:
            print("\nYou are not authorised to play.\n")
        else:
            print("\nYou are authorised play\n")
            return name


p1_name = authorisation("one")
p2_name = authorisation("two")

p1_score = 0
p2_score = 0


# This function picks a random number between 1 and 6 and shows them what they rolled.
def roll_a_dice(which_dice_roll):

    dice_roll = randint(1, 6)
    input(f" Your {which_dice_roll} roll was {dice_roll}.")
    return dice_roll


player_one_turn = True
allowed_rounds = 10

# This loops ten times because there are five rounds for two players.
for i in range(allowed_rounds):

    input(f"{p1_name if player_one_turn == True else p2_name}  this round:")
    dice_roll_one = roll_a_dice("first")
    dice_roll_two = roll_a_dice("second")
    points = dice_roll_one + dice_roll_two

    # If both dice rolls are equal it will roll a third dice.
    if dice_roll_one == dice_roll_two:
        input(" Both your dice rolls were equal you will now roll a third dice.")
        dice_roll_three = roll_a_dice("third")
        points += dice_roll_three

    input(f" Your score for this round is {points} points.")

    # If there score was even they get ten points added to their score. If it is odd it will subtract five.
    if (points % 2) == 0:
        input(" Your score was even you get 10 points added to your score.")
        points += 10
    else:
        input(" Your score was odd you get 5 points subtracted from your score.")
        points -= 5

    # If the players score is below zero it will reset it to zero.
    if points == 0:
        points = 0

    input(f" Your score for this round is {points} points.")

    # This checks whos players turn it is and adds the score for the round to the player total.
    if player_one_turn == True:
        p1_score += points
        player_one_turn = False
    else:
        p2_score += points
        player_one_turn = True

    input("\nPress enter to continue.\n")

# If both players scores are equal they will keep rolling until someone wins.
while p1_score == p2_score:
    tie_breaker_one = randint(1, 6)
    tie_breaker_two = randint(1, 6)
    input(f"{p1_name} you rolled {tie_breaker_one}. {p2_name} you rolled {tie_breaker_two}.")
    p1_score += tie_breaker_one
    p2_score += tie_breaker_two

# This checks for the winner.
if p1_score > p2_score:
    print(
        f"{p1_name} wins the game with {p1_score} points. {p2_name} got {p2_score} points."
    )
    winner_name = p1_name
    winner_score = p1_score
elif p1_score < p2_score:
    print(
        f"{p2_name} wins the game with {p2_score} points. {p1_name} got {p1_score} points."
    )
    winner_name = p2_name
    winner_score = p2_score

# This will write the winner's score to the leaderboard file.
with open("Game 1 Leaderboard.txt", "a") as leaderboard_file:
    leaderboard_file.write(f"{winner_name},{winner_score}\n")

# This displays the updated leaderboard.
display_leaderboard("\nUpdated")
