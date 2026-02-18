import random


# Intialise rounds points
user_points = 0
comp_points = 0
double_points = "no"

# Roll the dice for the user and note if they got a double
user_one = random.randint(1,6)
user_two = random.randint(1,6)

if user_one == user_two:
    double_points = "yes"

# roll the dice for the computer
comp_one = random.randint(1,6)
comp_two = random.randint(1,6)

# Update the user / computer points
user_points += user_one + user_two
comp_points += comp_one + comp_two

# Output the results
print("\nInitial Points")
print(f"User     -Roll 1: {user_one} \t| Roll 2: {user_two} \t| Total: {user_points} ")
print(f"Computer -Roll 1: {comp_one} \t| Roll 2: {comp_two} \t| Total: {comp_points} ")

# Let the user know if they qualify for double point
if double_points == "yes":
    print("Great news - if you win, you will earn double points!")




# if user has fewer points, they start the game
if user_points < comp_points:
    print("You start because your initial roll was less than the computer\n")

# if user and computer roll equal points...
elif user_points == comp_points:
    print("The initial rolls were the same, the user start!")

# if computer has fewer points, switch the computer to 'player 1'
else:
    player_1, player_2 = player_2, player_1
    first, second = second, first
