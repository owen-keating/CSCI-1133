
def create_username(first,last):
    str = last + first[0]
    return str

def readable(input_list):
    s = "On " + input_list[6] + " " + str(input_list[7]) + ", " + str(input_list[5]) + ", " + input_list[0] + ", " + input_list[1] + " received " + str(input_list[8]) + " inches of precipitation."
    return s

def switch(teams,driver):
    s = teams[driver]
    teams[s] = teams[driver]
    del teams[driver]
    teams[s] = driver
    return teams

def winners(finish_order,teams):
    s = finish_order[0]
    s2 = teams[s]
    x = s + " and " + s2 + " won the race!"
    return x
