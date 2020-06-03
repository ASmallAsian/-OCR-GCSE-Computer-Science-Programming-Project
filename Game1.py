import json
from operator import itemgetter
from random import randint

# This check to see if the leaderboard file exists
try:
    # This reads the leaderboard file if it exists
    is_leaderboard_empty = False
    with open("leaderboardFile.json") as scores_file:
        leaderboard = json.load(scores_file)
except FileNotFoundError:
    # This creates a new leaderboard if doesn't already exist
    is_leaderboard_empty = True
    leaderboard = {"players": []}


# This function displays the leaderboard and prints the top five highest scores
def display_leaderboard(leaderboard_version, which_leaderboard):

    print(f"{leaderboard_version} Leaderbord:\n")

    for position, player_info in enumerate(which_leaderboard["players"], 1):
        if position <= 5:
            print(
                f"{position}) {player_info['name']} scored: {player_info['score']}")

    print()


#  This is the list of authorised players.
authorised_players = ["Alan", "Bob", "Kevin", "James", "Lebron",  "Steve"]


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


# This will display the leaderboard if it exists
if is_leaderboard_empty == False:
    display_leaderboard("Current", leaderboard)
else:
    pass

p1_info = {"name": authorisation("one"), "score": 0}
p2_info = {"name": authorisation("two"), "score": 0}


# This function picks a random number between 1 and 6 and shows them what they rolled.
def roll_a_dice(which_dice_roll):

    dice_roll = randint(1, 6)
    input(f" Your {which_dice_roll} roll was {dice_roll}.")
    return dice_roll


player_one_turn = True
allowed_rounds = 10

# This loops ten times because there are five rounds for two players.
for i in range(allowed_rounds):

    input(
        f"{p1_info['name'] if player_one_turn == True else p2_info['name']}  this round:")
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
        p1_info['score'] += points
        player_one_turn = False
    else:
        p2_info['score'] += points
        player_one_turn = True

    input("\nPress enter to continue.\n")

# If both players scores are equal they will keep rolling until someone wins.
while p1_info['score'] == p2_info['score']:
    tie_breaker_one = randint(1, 6)
    tie_breaker_two = randint(1, 6)
    input(
        f"{p1_info['name']} you rolled {tie_breaker_one}. {p2_info['name']} you rolled {tie_breaker_two}.")
    p1_info['score'] += tie_breaker_one
    p2_info['score'] += tie_breaker_two

# This checks for the winner.
if p1_info['score'] > p2_info['score']:
    print(
        f"{p1_info['name']} wins the game with {p1_info['score']} points. {p2_info['name']} got {p2_info['score']} points."
    )
    winner_name = p1_info['name']
    winner_score = p1_info['score']

elif p1_info['score'] < p2_info['score']:
    print(
        f"{p2_info['name']} wins the game with {p2_info['score']} points. {p1_info['name']} got {p1_info['score']} points."
    )
    winner_name = p2_info['name']
    winner_score = p2_info['score']


# This adds the winners score to the leaderboard list
leaderboard["players"].append({"name": winner_name, "score": winner_score})

# This sorts the leaderboard in descending order
sorted_leaderboard = {"players": sorted(
    leaderboard["players"], key=itemgetter("score"), reverse=True)}

# This writes the updated leaderboard to the leaderboard file
with open("leaderboardFile.json", "w") as scores_file:
    leaderboard_data = json.dump(sorted_leaderboard, scores_file, indent=4)

# This displays the updated leaderboard
display_leaderboard("\nUpdated", sorted_leaderboard)
