
def mms(counts):
    '''
    Purpose: To determine if a set of M&M's sorted by color will be eaten by Muriel.
    Input Parameter(s):
        counts: a dictionary of each color of M&M's given along with the amount of M&M's for each color.
    Return Value: The answer to whether or not Muriel is satisfied and will eat the M&M's.
    '''
    if(counts['yellow']>counts['blue']):
        if(counts['green']%3==0):
            return "Yes"
        elif(counts['green']%5==0):
            return "Yes"
        else:
            return "No"
    else:
        return "No"

def choice(text,optionA,optionB,optionC):
    '''
    Purpose: To list a situation with three possible solutions.
    Input Parameter(s):
        text: a description of the situation given.
        optionA: the first possible answer to the situation.
        optionB: the second possible answer to the situation.
        optionC: the third possible answer to the situation.
    Return Value: The answer that was selected by the user.
    '''
    print(text+'\n'+'\n'+"A. "+optionA+'\n'+"B. "+optionB+'\n'+"C. "+optionC)
    str = input("Choose A, B, or C: ")
    if(str=='A'):
        return str
    if(str=='B'):
        return str
    if(str=='C'):
        return str
    else:
        print("Invalid option, defaulting to A")
        return "A"

def adventure():
    '''
    Purpose: A simulation that takes the user on an adventure with different situations.
    Input Parameter(s): none
    Return Value: Returns 'true' when the user picks correct solutions and completes the adventure and 'false' when the user incorrectly picks solutions and does not complete the adventure.
    '''
    count=0
    if(count==0):
        str = choice("What's the best play in Madden","Quick Slants","RPO Peek Zone Bubble","Read Option")
        if str=='A':
            count+=1
        elif str=='B':
            count+=3
        else:
            return False
    if(count==1):
        str = choice("What's the best zombies map","Town","Origins","Der Eisendrache")
        if str=='A':
            count+=1
        elif str=='B':
            return True
        else:
            count+=1
    if(count==2):
        str = choice("Who's the best UFC fighter","Khabib Nurmagomedov","Jon Jones","Conor McGregor")
        if str=='A':
            return False
        elif str=='B':
            count+=1
        else:
            return True
    if(count==3):
        str = choice("What's Conor McGregor's Specialty","Left Hook","Wrestling","Spinning Back Kick")
        if str=='A':
            return True
        elif str=='B':
            return False
        else:
            return True
