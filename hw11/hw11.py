
import os

def collatz(num):
    '''
    Purpose: To simulate the Collatz conjencture, where starting at a positive integer, you will eventually reach 1 by dividing by 2 or multiplying by 3 and adding 1.
    Input Parameter(s):
        num: the given starting number for the collatz sequence.
    Return Value: Returns the collatz sequence that results from the given starting number.
    '''
    if(num==1):
        return [1]
    elif(num%2==1):
        return [num] + collatz(num*3+1)
    else:
        return [num] + collatz(num//2)

def is_decoy(list):
    '''
    Purpose: Searches through a list of lines in a text file and determines if the file is a decoy or not.
    Input Parameter(s):
        list: a list of strings, each item representing a line from a text file.
    Return Value: Returns true if the file is a decoy, and false if the file is not a decoy.
    '''
    if(list==[]):
        return False
    elif(list[-1][0] in ['A','C','M','E']):
        return True
    else:
        list.pop(-1)
        return is_decoy(list)

def get_targets(path):
    '''
    Purpose: Searches through a folder of files and determines which files are not decoys.
    Input Parameter(s):
        path: the folder that is being searched through for decoy files.
    Return Value: Returns a list of files in the given folder that are not decoys.
    '''
    list = []
    for file in os.listdir(path):
        if os.path.isfile(path+'/'+file):
            f = open(path+'/'+file,"r")
            if(is_decoy(f.readlines())==False):
                print(path+'/'+file)
                list.append(path+'/'+file)
        else:
            get_targets(path+'/'+file)
    return list
