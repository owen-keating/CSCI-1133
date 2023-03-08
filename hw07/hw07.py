
def complement(strand):
    '''
    Purpose: To produce the complement strand to a given strand of DNA.
    Input Parameter(s):
        strand: a string of characters that represents the given DNA sequence.
    Return Value: A string of characters that represents the complement DNA sequence.
    '''
    strand = strand.lower()
    for i in range(len(strand)):
        if(strand[i]=="a"):
            x = "t"
        elif(strand[i]=="t"):
            x = "a"
        elif(strand[i]=="c"):
            x = "g"
        elif(strand[i]=="g"):
            x = "c"
        else:
            x = " "
        strand = strand[:i] + x + strand[i+1:]
    strand = "".join(strand.split())
    return strand

def mark(strand):
    '''
    Purpose: To search through a DNA strand and locate start and stop codons.
    Input Parameter(s):
        strand: the original DNA sequence given.
    Return Value: A new DNA sequence in which start codons have been replaced by ">>>" and stop codons have been replaced by "<<<".
    '''
    x = int(len(strand)/3)
    for i in range(x):
        if(strand[i*3:i*3+3]=="atg"):
            strand = strand[:i*3] + ">>>" + strand[i*3+3:]
        if(strand[i*3:i*3+3]=="taa" or strand[i*3:i*3+3]=="tag" or strand[i*3:i*3+3]=="tga"):
            strand = strand[:i*3] + "<<<" + strand[i*3+3:]
    return strand

def spam_table(spam,not_spam):
    '''
    Purpose: To determine if certain words are more likely to be found in spam emails or non-spam emails.
    Input Parameter(s):
        spam: a list containing strings of spam emails.
        not_spam: a list containing strings of emails that are not spam.
    Return Value: A dictionary containing words and a number corresponding to each word - a positive number means the word is found more often in spam messages, while a negative number means the word is found more often in non-spam messages.
    '''
    dict = {}
    s = " " + " ".join(spam) + " "
    s = s.lower()
    spam = s.split(" ")
    t = " " + " ".join(not_spam) + " "
    t = t.lower()
    not_spam = t.split(" ")
    for word in spam:
        dict.update({word:s.count(" " + word + " ") - t.count(" " +word + " ")})
    for word in not_spam:
        dict.update({word:s.count(" " + word + " ") - t.count(" " + word + " ")})
    dict.pop("")
    return dict

def spam_check(email,table):
    '''
    Purpose: To check an email and predict if it is spam or not.
    Input Parameter(s):
        email: the email that is being checked for whether or not it is spam.
        table: a dictionary of different words and their spam tendencies, some of which may be found within the email.
    Return Value: The spam prediction given to the email as well as its spam score - a positive number if the email contained more spam prone language, and a negative number if the email contained less spam prone language.
    '''
    x = 0
    email = email.lower()
    list = email.split(" ")
    for word in list:
        if word in table:
            x+=table[word]
    if(x>0):
        print("Spam")
    else:
        print("Not Spam")
    return x
