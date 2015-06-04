import random

#GLOBAL CONSTANT USED TO ASSIGN NUMBER OF DICE TO GAME PLAY.
DICE = [20,12,10,8,6,4] #list of different sided dice used in game.


def check_for_number(input,question):
    '''
    validates user input to make sure it's a valid number and re-asks the question if it isn't.
    '''
    try:
        int(input)
        if int(input) > 0:
            return input
        else:
            print "Value entered must be greater than 0"
            num = raw_input(question)
            return check_for_number(num,question)
    except:
        print "Value entered is not a number"
        num = raw_input(question)
        return check_for_number(num,question)


def dice_choice_check(dice_choice,dice_list):
    '''
    validates user input to make sure the correct sided dice exists in game.
    '''
    try:
    	int(dice_choice)
    	if int(dice_choice) not in dice_list:
    		print "Dice not valid, please re-enter choice"
        	return False
    	else:
        	dice_list.remove(int(dice_choice))
        	return True
    except:
    	print "Value entered is text. Please re-enter values."
    	return False

def set_players(num_players):
    '''
    generates list of players and assigns values to a player list used for game play.
    returns list of players with values.
    '''
    print "\n"
    players = []
    for player in range(0,int(num_players)):
    	player_number = player + 1
        new_player= raw_input("Player "+ str(player_number) + "- What is your name? ")
        current_score = 0
        round_score = 0
        round_wins = 0
        player_tracker = [new_player,[4,6,8,10,12,20],current_score,round_score,round_wins]
        players.append(player_tracker)
    return players


def start_game():
    '''
    Displays start message at beginning of game explaining rules to players.
    '''
    print "\n"
    print "                      WELCOME TO DICE WAR!!!!!"
    print "====================================================================="
    print "OBJECT OF GAME IS TO ROLE A DICE SCORE HIGHER THAN THE OTHER PLAYERS"
    print "SELECT FROM 6 DIFFERENT SIDED DICE AND ROLL ONE PER ROUND"
    print "GOOD LUCK!"
    print "\n"

def break_tie_round(player_list, player_index_list,die_choice):
	'''
	runs a tie-breaker game if there is a tie in the round
	'''
	round_score = []
	for player in player_index_list:
		dice_roll = random.randrange(1,die_choice)
		print player_list[player][0] + " rolls a " + str(dice_roll)
		round_score.append(dice_roll)
	return round_score

def determine_round_winner(player_list):
    '''
    checks to see which player has won the round
    '''
    top_score = 0
    round_score = []
    player_list_wins = []
    for player in player_list:
        round_score.append(player[3])
    get_max_values = [val for val, max_val in enumerate(round_score) if max_val == max(round_score)]
    get_max_values_length = len(get_max_values)
    if get_max_values_length > 1:
        print "There is a Tie!"
        tie_message = "There will be a roll off to determine the winner with the 20 sided dice between "
        for tie_winner in get_max_values:
            player_list_wins.append(player_list[tie_winner])
            tie_message += player_list[tie_winner][0]
            tie_message += ", "
        break_tie_check = False
        while break_tie_check == False:
        	round_score = break_tie_round(player_list,get_max_values,20)
        	get_max_values = [val for val, max_val in enumerate(round_score) if max_val == max(round_score)]
    		get_max_values_length = len(get_max_values)
    		if get_max_values_length == 1:
    			break_tie_check = True
    max_round_score = max(round_score)
    winner_round = round_score.index(max_round_score)
    player_list[winner_round][4] += 1
    return winner_round

def get_max_value(dice_rolls):
    '''
    checks to see if there is a tie
    '''
    all_max_roll_index = []
    counter_index = 0
    max_roll = max(dice_rolls)
    for roll in dice_rolls:
        if roll == max_roll:
            all_max_roll_index.append(counter_index)
        counter_index = counter_index + 1
    return all_max_roll_index

def get_min_sided_dice(dice):
    '''
    Gets the index of the dice choosen with the min number of sides.
    '''
    all_min_sided_index = []
    counter_index = 0
    min_sided = min(dice)
    for sides in dice:
	    if sides == min_sided:
		    all_min_sided_index.append(counter_index)
	    counter_index = counter_index + 1
    return all_min_sided_index

def tiebreaker(player_list, player_list_index,die_choice):
    '''
    determines the winner in the event of a tie
	'''
    tie = True
    print "There is a tie!"
    dice_roll_turn = []
    for player in player_list_index:
    	dice_roll = random.randrange(1,die_choice)
    	dice_roll_turn.append(dice_roll)
        print player_list[player][0] + " rolls same die again. " + "New rolls score is " + str(dice_roll)
    new_max_player = get_max_value(dice_roll_turn)
    
    new_max_length = len(new_max_player)
    if new_max_length == 1:
    	tie = False
    	new_max_player = new_max_player[0]
    	new_player = player_list_index[new_max_player]
    	tie_list = [tie,new_player]
    	return tie_list
    else:
    	return tiebreaker(player_list,new_max_player,die_choice)


def check_if_winner(player_list,num_rounds):
    '''
    checks to see at the end of a round if a player wins.
    '''
    top_score = 0
    final_round_scores = []
    for player in player_list:
        final_round_scores.append(player[4])
    top_score = max(final_round_scores)
    if top_score == int(num_rounds):
    	player_wins = final_round_scores.index(top_score)
        print player_list[player_wins][0] + " wins!" + " Great Job!"
        game_over = True
        return game_over
    else:
    	game_over = False
    	print "Begin Next Round"
    	return game_over

def play_round(player_list,num_rounds):
    '''
    main game play for a round
    '''
    DICE_SCORE = [1,2,3,4,5,6]
    players = player_list
    dice_roll_turn = []

    print "\n"
    for player in players:
        player_name = player[0]
        player_dice = player[1]
        dice_check = False
        while dice_check == False:
        	dice_choice = raw_input(str(player_name) + " - Please select a Dice Choice?  "+ str(player_dice) + " ")
        	dice_check = dice_choice_check(dice_choice,player[1])
        dice_choice = int(dice_choice)
        player[2] = dice_choice
        dice_roll = random.randrange(1,dice_choice)
        dice_roll_turn.append(dice_roll)
        print player_name + " Rolls a " + str(dice_roll)
    print "\n"
    all_max_values = get_max_value(dice_roll_turn)
    num_max_values = len(all_max_values)
    if num_max_values > 1:
    	choices = []
    	for value in all_max_values:
    		choices.append(players[value][2])
    	min_dice_rolled = get_min_sided_dice(choices)
    	min_dice_rolled_first = min_dice_rolled[0]
    	min_dice_sides = min(choices)
    	num_min_dice_rolled = len(min_dice_rolled)
    	if num_min_dice_rolled > 1:
    		tie = [True,0]
    		while tie[0] == True:
    			tie_check = tiebreaker(players,min_dice_rolled,min_dice_sides)
    			tie[0] = tie_check[0]
    		winner = tie_check[1]
    		final_score = 1
    	else:
    		winner = min_dice_rolled[0]
    		final_score = 1
    else:
    	get_max = max(dice_roll_turn)
    	get_min = min(dice_roll_turn)
    	winner = dice_roll_turn.index(get_max)
    	loser = dice_roll_turn.index(get_min)
    	score_winner = players[winner][2]
    	score_loser = players[loser][2]
    	final_score = int(DICE.index(score_winner)) - int((DICE.index(score_loser)))
    	if final_score <= 0:
        	final_score = 1
    	else:
        	final_score = final_score + 1
    players[winner][3] = players[winner][3] + final_score
    print str(players[winner][0])+" Wins Turn!"
    if len(player_list[0][1]) != 0:
    	print "{0:^45}".format("Current Round Scores")
    	print "================================================"
    	print "{0:15}{1:<15}{2:<15}".format("Player","Round Score","Total Score")
    	for player in players:
        	print "{0:15}{1:^15}{2:^15}".format(player[0],player[3],player[4])
    else:
    	winner_of_round = determine_round_winner(player_list)
    	print players[winner_of_round][0] + " Wins Round!"
    	print "{0:^45}".format("Final Round Score")
    	print "================================================"
    	print "{0:15}{1:<15}{2:<15}".format("Player","Round Score","Total Score")
    	for player in players:
        	print "{0:15}{1:^15}{2:^15}".format(player[0],player[3],player[4])
        print "\n"


def play_game(player_values_list,num_rounds):
    '''
    plays a single game with the dice
	'''
    top_score = 0
    game_over = False
    while game_over == False:
        round_score = []
        num_dice = len(DICE)
        while num_dice != 0:
            play_round(player_list,num_rounds)
            num_dice = num_dice - 1
        game_over = check_if_winner(player_list,num_rounds)
        if game_over == False:
        	for player in player_list:
        		round_score.append(player[3])
        		player[3] = 0
        		player[1] = [4,6,8,10,12,20]
        else:
        	print "GAME OVER!!!!!!"



#game play starts here. Ask user for number of players and rounds.
start_game()
num_players = raw_input("How many players? ")
checked_players = check_for_number(num_players,"How many players? ")
num_rounds = raw_input("How many rounds will it take to win? ")
checked_rounds = check_for_number(num_rounds,"How many rounds will it take to win? ")

player_list = set_players(checked_players) #player_list is generated with all scores set to 0.

play_game(player_list,checked_rounds) #plays game based on player list and number of rounds.