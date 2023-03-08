
def calc_angle(sides):
    '''
    Purpose: To determine how many degrees to rotate before drawing the next side of a regular polygon with a given number of sides.
    Input Parameter(s):
        sides: the number of sides of the polygon given.
    Return Value: The exterior angle measure of a regular polygon with a given number of sides.
    '''
    angle = 360/sides
    return angle

def draw_polygon(tr,n_sides,side_length):
    '''
    Purpose: To draw a regular polygon using a given number of sides and given side length.
    Input Parameter(s):
        tr: the turtle object used in the function.
        n_sides: the number of sides the polygon will have.
        side_length: the length of the polygon's sides.
    Return Value: A polygon will be drawn with the number of sides and side lengths given.
    '''
    x = calc_angle(n_sides)
    for i in range(n_sides):
        tr.forward(side_length)
        tr.right(x)

def wizards(grades,life,sleep):
    '''
    Purpose: To find the students that met the criteria of getting good grades, maintaining a social life, and getting enough sleep.
    Input Parameter(s):
        grades: a list of students that have good grades.
        life: a list of students that have a social life.
        sleep: a list of the students that got enough sleep.
    Return Value: A list that contains the students that got good grades, had a social life, and got enough sleep.
    '''
    wizards = []
    for i in range(len(grades)):
        if(grades[i] in life and grades[i] in sleep):
            wizards.append(grades[i])
            i+=1
    return wizards

def func2():
    '''
    Purpose: Print the statement "Who needs loops?" four times.
    Input Parameter(s): none.
    Return Value: Returns four lines, each containing "Who needs loops?".
    '''
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")

def func1():
    '''
    Purpose: Calls a function six times that prints a statement four times each.
    Input Parameter(s): none.
    Return Value: Returns the statement in the function called a total of 24 times.
    '''
    func2()
    func2()
    func2()
    func2()
    func2()
    func2()

def print_97():
    '''
    Purpose: To print a statement a large amount of times without using loops by calling a function four times that prints a statement 24 times each.
    Input Parameter(s): none.
    Return Value: Returns the statement "Who needs loops?" a total of 97 times.
    '''
    func1()
    func1()
    func1()
    func1()
    print("Who needs loops?")
