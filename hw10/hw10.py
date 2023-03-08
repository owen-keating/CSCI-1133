
import random

def weighted_select(dict):
    '''
    Purpose: To simulate choosing a word out of a group of words that all have a different probability of being selected.
    Input Parameter(s):
        dict: a dictionary of words and their frequency of occurring - words paired with larger numbers have a higher chance of being chosen.
    Return Value: The word chosen randomly considering the different probabilities of each word being selected.
    '''
    list = []
    for word in dict:
        x = dict[word]
        for i in range(x):
            list.append(word)
    y = random.randint(0,len(list)-1)
    return list[y]

def bigram_count(string):
    '''
    Purpose: To analyze a string of words and determine which words most frequently follow other words.
    Input Parameter(s):
        string: a given string of words.
    Return Value: A dictionary of words, each paired with its own dictionary representing how frequently other words follow it.
    '''
    dict = {}
    list = string.split()
    for i in range(len(list)-1):
        try:
            x = dict[list[i]]
            try:
                x[list[i+1]]+=1
            except KeyError:
                x[list[i+1]]=1
            dict[list[i]] = x
        except KeyError:
            dict[list[i]] = {list[i+1]:1}
    return dict

def random_sentence(dict,starting_word,length):
    '''
    Purpose: To produce a random sentence using a starting word and a dictionary that contains other words that may be used in the sentence.
    Input Parameter(s):
        dict: a dictionary with words that can be used in the random sentence, each paired with its own dictionary representing how frequently other words follow it.
        starting_word: the first word of the random sentence.
        length: the number of words that will be in the generated sentence.
    Return Value: A random sentence that has been generated using a list of words.
    '''
    sentence = starting_word
    current = starting_word
    for i in range(length-1):
        try:
            s = weighted_select(dict[current])
            sentence = sentence + " " + s
            current = s
        except KeyError:
            s = starting_word
            sentence = sentence + " " + s
            current = s
    return sentence

def rand_sent_file(fname,length):
    '''
    Purpose: To produce a random sentence using words avaliable in a given text file.
    Input Parameter(s):
        fname: the given text file that contains the words used to create a random sentence.
        length: the number of words that will be in the generated sentence.
    Return Value: A random sentence that has been generated using words found in the given text file.
    '''
    file = open(fname,"r")
    file_string = file.read()
    split = file_string.split("\n")
    split.pop(-1)
    list = []
    for i in range(len(split)):
        s = split[i]
        s_split = s.split(" ")
        for j in range(len(s_split)):
            list.append(s_split[j])
    x = random.randint(0,len(list)-2)
    word = list[x]
    dict = bigram_count(file_string)
    sentence = random_sentence(dict,word,length)
    return sentence
