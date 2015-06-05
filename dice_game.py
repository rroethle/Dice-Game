import random
import getpass #used to mask user input for die choice
#GLOBAL CONSTANT USED TO ASSIGN NUMBER OF DICE TO GAME PLAY.
DICE = [20,12,10,8,6,4] #list of different sided dice used in game.


def check_for_number(input,question,allow_zero):
    '''
    validates user input to make sure it's a valid number and re-asks the question if it isn't.
    if allow_zero is equal to 0 then the zero value is not allowed. If allow_zero is equal to 0 then it is.
    '''
    zero_value = allow_zero
    try:
        int(input)
        if zero_value == 0:
            if int(input) > 0:
                return input
            else:
                print "Value entered must be greater than 0"
                num = raw_input(question)
                return check_for_number(num,question,zero_value)
        else:
            if int(input) >= 0:
                return input
            else:
                print "Value entered must not be negative"
                num = raw_input(question)
                return check_for_number(num,question,zero_value)
    except:
        print "Value entered is not a number"
        num = raw_input(question)
        return check_for_number(num,question,zero_value)


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

def set_players(num_players,num_computers):
    '''
    generates list of players and assigns values to a player list used for game play.
    returns list of players with values.
    list values are player name, DICE, current score of the roll, current round score, number of round wins, and if player
    is a computer or player. 6 values in all for each list item.
    '''
    print "\n"
    players = []
    for player in range(0,int(num_players)):#human players
    	player_number = player + 1
        new_player= raw_input("Player "+ str(player_number) + "- What is your name? ")
        current_score = 0
        round_score = 0
        round_wins = 0
        player_or_computer = 0 #0 refers to player
        player_tracker = [new_player,[4,6,8,10,12,20],current_score,round_score,round_wins,player_or_computer]
        players.append(player_tracker)
    for computer in range(0,int(num_computers)):#computer players
        computer_number = computer + 1
        computer_player = "Computer " + str(computer_number)
        current_score = 0
        round_score = 0
        round_wins = 0
        player_or_computer = 1 #1 refers to computer player
        computer_tracker = [computer_player,[4,6,8,10,12,20],current_score,round_score,round_wins,player_or_computer]
        players.append(computer_tracker)
    return players


def start_game():
    '''
    Displays start message at beginning of game explaining rules to players.
    '''
    print "\n"
    print "                      WELCOME TO DICE WAR!!!!!"
    print "====================================================================="
    print "OBJECT OF GAME IS TO ROLE A DICE SCORE HIGHER THAN THE OTHER PLAYERS"
    print "SELECT FROM 6 DIFFERENT SIDED DICE AND ROLL ONE PER TURN. PLAYER WITH"
    print "THE HIGHEST ROLE WINS ROUND. SELECT LOWER SIDED DIE AND BEAT PLAYERS"
    print "WITH HIGHER SIDED DICE AND EARN BONUS POINTS (1 EXTRA PER LEVEL HIGHER)"
    print "IF TIE SCORE, PLAYER WITH LOWER SIDED DICE WINS. OTHERWISE YOU HAVE A "
    print "WAR! A TIEBREAKER ROLE WILL DETERMINE THE WINNER. SCORE MORE POINTS THAN"
    print "YOUR OPPONENTS IN THE 6 TURNS AND WIN THE ROUND. TIE SCORES WILL RESULT"
    print "IN AN ULTIMATE WAR ROLE OFF WITH THE 20 SIDED DICE TO WIN THE ROUND."
    print "THE GAME IS WON WHEN A PLAYER WINS THE NUMBER OF ROUNDS DETERMINED BEFORE"
    print "THE GAME. PLAY WITH AS MANY PLAYERS OR COMPUTERS AS YOU'D LIKE."
    print "GOOD LUCK AND HAVE FUN!"
    print "GOOD LUCK!"
    print "\n"

def break_tie_round(player_list, player_index_list,die_choice):
	'''
	runs a tie-breaker game if there is a tie in the round
    returns a new round score based on a new random roll of the dice .
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
    if there is a tie, rolls a 20 sided die to determine the winner until someone wins.
    returns the winner of the round.
    '''
    top_score = 0
    round_score = []
    player_list_wins = []
    for player in player_list:
        round_score.append(player[3])
    #uses list comprehensions and enumerate to check to see if there are multipl max values.
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
        	round_score = break_tie_round(player_list,get_max_values,20)#20 refers to the numer of sides the dice has
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
    returns all max values given a list containing dice rolls.
    will return multiple winners if there are multiple max values
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
    Gets the index of the dice choosen with the minimum number of sides from a dice list.
    Used to calculate the minimum dice rolled with multiple players to determine score.
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
    determines the winner in the event of a tie of a turn roll
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
    checks to see at the end of a round if a player wins. If there is one, a winner statement is printed.
    returns either true or false that the game is over.
    '''
    top_score = 0
    final_round_scores = []
    for player in player_list:
        final_round_scores.append(player[4])
    top_score = max(final_round_scores)
    if top_score == int(num_rounds):
    	player_wins = final_round_scores.index(top_score)
    	winner_statement = player_list[player_wins][0] + " wins!" + " Great Job!"
        #print player_list[player_wins][0] + " wins!" + " Great Job!"
        #print "====================================================="
        print "{0:^60}".format(winner_statement)
        print "========================================================================="
        print "\n"
        game_over = True
        return game_over
    else:
    	game_over = False
    	print "Begin Next Round"
    	return game_over

def play_round(player_list,num_rounds):
    '''
    main game play for a round. Prints winner of a round at the end.
    '''
    DICE_SCORE = [1,2,3,4,5,6]
    players = player_list
    dice_roll_turn = []
    output_results = []
    print "\n"
    for player in players:
        player_name = player[0]
        player_dice = player[1]
        dice_check = False
        while dice_check == False:
            if player[5] == 0:#used for human players as 0 indicates a human player.
                dice_choice = getpass.getpass(str(player_name) + " - Please select a Dice Choice?  "+ str(player_dice) + " ")
                #dice_choice = raw_input(str(player_name) + " - Please select a Dice Choice?  "+ str(player_dice) + " ")
                #print "\n"*100 #prints 100 blank lines to hide choice from other players
                dice_check = dice_choice_check(dice_choice,player[1])#checks to make sure dice choosen is in the list.
            else:
                dice_check = True
        if player[5] == 1:#used for computer players as 0 indicates a computer player and randomly chooses a dice to roll from dice list.
            dice_choice = random.choice(player[1])
            player[1].remove(dice_choice)
        dice_choice = int(dice_choice)
        player[2] = dice_choice
        dice_roll = random.randrange(1,dice_choice)
        dice_roll_turn.append(dice_roll)
        result = player_name + " Selects a " + str(dice_choice) + " Sided Dice and Rolls a " + str(dice_roll)
        output_results.append(result)
    print "\n"
    all_max_values = get_max_value(dice_roll_turn)
    num_max_values = len(all_max_values)
    if num_max_values > 1: #checks to see if there is multiple max values and if there is a tie and generates tie-breaker information
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
    			tie_check = tiebreaker(players,min_dice_rolled,min_dice_sides) #runs tiebreaker round
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
    for result in output_results: #prints output of turn for each player roll.
        print result
    print "\n"
    print str(players[winner][0])+" Wins Turn!"
    print "\n"
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
    plays a single game with the dice. runs play_round to run through a complete set of dice.
    asks user at the end if they would like to play again.
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
            play_again = raw_input("Play again? Type 'y' to play again or any other key to end")
        if play_again == 'y':
            return True
        else:
            return False


#game play starts here. Ask user for number of players and rounds.
game_play = True

#the user can contine to play game as long as they select y at the end.
#when checking the user input, the last value (either a 0 or 1) determine if the try/except statement should include 0 when checking
#if the value is 1, then it will allow 0 and if it is 0 then the input will not allow the value.
while game_play == True:
    start_game()
    num_players = raw_input("How many human players? ")
    checked_players = check_for_number(num_players,"How many human players? ",0)
    num_computers = raw_input("How many computer players? ")
    checked_computers = check_for_number(num_computers,"How many computer players? ",1)
    num_rounds = raw_input("How many rounds will it take to win? ")
    checked_rounds = check_for_number(num_rounds,"How many rounds will it take to win? ",0)
    player_list = set_players(checked_players,checked_computers)#generates a seperate player list storing the values associated with each player
    game_play = play_game(player_list,checked_rounds) #plays game based on player list generated from set_players