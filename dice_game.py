import random


def check_for_number(input,question):
	try:
		int(input)
		if int(input) > 0:
			pass
		else:
			print "Value entered must be greater than 0"
			num_players = raw_input(question)
			return num_players
	except:
		print "Value entered is not a number"
		num_players = raw_input(question)
		return num_players

def dice_choice_check(dice_choice,dice_list):
	if int(dice_choice) not in dice_list:
		print "Dice not valid, please re-enter choice"
		return dice_list
	else:
		dice_list.remove(int(dice_choice))
		return dice_list

def play_game(num_players,num_rounds):
	DICE = [20,12,10,8,6,4]
	DICE_SCORE = [1,2,3,4,5,6]
	players = []
	dice_roll_turn = []
	for player in range(0,num_players):
		new_player= raw_input("What is your name? ")
		current_score = 0
		round_score = 0
		round_wins = 0
		player_tracker = [new_player,[4,6,8,10,12,20],current_score,round_score,round_wins]
		players.append(player_tracker)
	for player in players:
		player_name = player[0]
		player_dice = player[1]
		dice_choice = raw_input(str(player_name) + " Please select a Dice Choice?  "+ str(player_dice) + " ")
		dice_choice_check(dice_choice,player[1])
		dice_choice = int(dice_choice)
		player[2] = dice_choice
		dice_roll = random.randrange(1,dice_choice)
		dice_roll_turn.append(dice_roll)
	get_max = max(dice_roll_turn)
	get_min = min(dice_roll_turn)
	winner = dice_roll_turn.index(get_max)
	loser = dice_roll_turn.index(get_min)
	score_winner = players[winner][2]
	score_loser = players[loser][2]
	
	final_score = (DICE.index(score_winner)+1) - (DICE.index(score_loser)+1) + 1
	if final_score < 0:
		final_score = 1
	else:
		final_score = final_score
	players[winner][3] = players[winner][3] + final_score

	#for roll in dice_roll_turn:
	#	print roll

num_players = raw_input("How many players? ")
check_for_number(num_players,"How many players? ")
num_rounds = raw_input("How many rounds will it take to win? ")
check_for_number(num_rounds,"How many rounds will it take to win? ")

while num_rounds != 0:
	print num_rounds
	for i in range(0,6):
		play_game(int(num_players),int(num_rounds))
	num_rounds = int(num_rounds) - 1




