
def tribble_growth(init_pop,days):
    '''
    Purpose: To simulate the growth of a population of tribbles over a certain amount of days.
    Input Parameter(s):
        init_pop: the initial population of tribbles.
        days: the amount of days that the simulation will last.
    Return Value: A list that includes the current population of tribbles on each day of the simulation.
    '''
    curr_pop = init_pop
    list = []
    list.append(init_pop)
    for i in range(days):
        curr_pop = int(curr_pop*1.1)
        list.append(curr_pop)
    return list

def vampire_growth(initial_vampires,nightly_kill):
    '''
    Purpose: To simulate change in the population of vampires until the vampires have either been eradicated or have overrun the town.
    Input Parameter(s):
        initial_vampires: the initial population of vampires.
        nightly_kill: the amount of vampires that will be killed by the slayer each night of the simulation.
    Return Value: A list that includes the current population of vampires on each day of the simulation.
    '''
    curr_pop = initial_vampires
    list = []
    list.append(initial_vampires)
    while(curr_pop>0 and curr_pop<=100):
        curr_pop = int(curr_pop*1.5)-nightly_kill
        if(curr_pop<0):
            list.append(0)
        else:
            list.append(curr_pop)
    return list

move = 'R'
dict = {'W':0, 'L':0, 'T':0}

def rps_round(comp_move):
    '''
    Purpose: To simulate one round of rock, paper, scissors.
    Input Parameter(s):
        comp_move: the move that the computer will use against the player
    Return Value: A list that includes the user's move and the result of the game: 'W' for player win, 'L' for player loss, and 'T' for tie.
    '''
    list = []
    user_move = input("Enter R, P, or S: ")
    while(user_move!='R' and user_move!='P' and user_move!='S'):
        print("Invalid Input")
        user_move = input("Enter R, P, or S: ")
    list.append(user_move)
    print("Computer selects " + comp_move)
    global dict
    global move
    if(comp_move == user_move):
        list.append('T')
        print("Tie!")
        dict['T']+=1
    elif(comp_move == 'R' and user_move == 'S'):
        list.append('L')
        print("Computer wins!")
        dict['L']+=1
    elif(comp_move == 'S' and user_move == 'P'):
        list.append('L')
        print("Computer wins!")
        dict['L']+=1
    elif(comp_move == 'P' and user_move == 'R'):
        list.append('L')
        print("Computer wins!")
        dict['L']+=1
    else:
        list.append('W')
        print("Player wins!")
        dict['W']+=1
    move = user_move
    return list

def rps_game(num_rounds):
    '''
    Purpose: To simulate a series of rock, paper, scissors games.
    Input Parameter(s):
        num_rounds: the amount of games that will be simulated between the user and the computer.
    Return Value: A dictionary that represents the player's record against the computer during the simulation.
    '''
    global dict
    dict = {'W':0, 'L':0, 'T':0}
    global move
    move = 'R'
    for i in range(num_rounds):
        rps_round(move)
    local_dict = dict
    return local_dict
