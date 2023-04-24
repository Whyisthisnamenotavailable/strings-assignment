# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_one = "Ruud Gullit"
player_two = "Marco Van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_one + " " + str(goal_0) +", " + player_two + " " + str(goal_1)
print(scorers)

report = f"The goals were scored by: {player_one} in minute {goal_0} \n and by {player_two} in minute {goal_1}"

print(report)

player = "Ruud Gullit"
first_name = player[0:(player.find(" "))]
print(first_name)

last_name = player[(player.find(" ")+1):]
last_name_len = len(last_name)
print(last_name_len)

name_short = str(first_name[0]) + ". " + str(last_name)
print(name_short)

chant = ((first_name + "! ") * len(first_name))[:-1]
print(chant)

if chant[-1] != " ":
    good_chant = chant
    print("chant is good")
else:
    print("chant is bad")


