
def comment_prints(fname):
    '''
    Purpose: Takes a python file and comments out any print statements.
    Input Parameter(s):
        fname: the original python file given.
    Return Value: Returns the number of print statements in the original file. If the file given cannot be found, returns -1.
    '''
    try:
        file = open(fname,"r")
        file_string = file.read()
        split = file_string.split("print(")
        x = 0
        name = "no_print_" + fname
        new_file = open(name,"w")
        for i in range(len(split)):
            if(i!=0):
                s = split[i]
                s = "#print(" + s
                split[i] = s
                x+=1
            new_file.write(split[i])
        return x
    except FileNotFoundError:
        return -1

def rotate_model(fname_in,fname_out):
    '''
    Purpose: To rotate a figure 90 degrees.
    Input Parameter(s):
        fname_in: the original file with the coordinates of the vertices and faces of the figure.
        fname_out: the new file with the coordinates of the vertices and faces of the rotated figure.
    Return Value: Returns the number of vertices in the given figure. If the file given cannot be found, returns -1.
    '''
    try:
        file = open(fname_in,"r")
        file_string = file.read()
        split = file_string.split("\n")
        x = 0
        new_file = open(fname_out,"w")
        for i in range(len(split)-1):
            s = split[i]
            n = s[0]
            if(n=="v"):
                y = s.split(" ")
                xcor = float(y[2])
                ycor = -1*float(y[1])
                y[1] = str(xcor)
                y[2] = str(ycor)
                s = " ".join(y)
                split[i] = s
                x+=1
            new_file.write(split[i]+"\n")
        return x
    except FileNotFoundError:
        return -1

def upload_scores(answer_file,assignment_name,correct_answer):
    '''
    Purpose: To score a given assignment by taking a list of students and their submitted answers and determine which students got the correct answer.
    Input Parameter(s):
        answer_file: a file that lists the email and answer given for every student that submitted the assignment.
        assignment_name: the name of the assignment being scored.
        correct_answer: the correct answer of the assignment being scored.
    Return Value: A list of the emails of students that submitted the correct answer on the assignment.
    '''
    file = open(answer_file,"r")
    file_string = file.read()
    split = file_string.split()
    split.pop(0)
    list = []
    for i in range(len(split)):
        s = split[i]
        y = s.split(",")
        if(y[1]==correct_answer):
            list.append(y[0])
    list.sort()
    return list
