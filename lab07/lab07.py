
#warmup

def warm1():
    s = "mississippi"
    x = s.count('s')
    return x

def warm2():
    s = "mississippi"
    s = s.replace("iss","ox")
    return s

def warm3():
    s = "mississippi"
    x = s.find('p')
    return x

def warm4(istring):
    p = '0123456789'
    os = ''
    for iterator in istring:
        if iterator not in p:
            os += iterator
    return os

#stretch

def list_construction():
    list = []
    x = 0
    while(x!=-1):
        s = input("Enter a word: ")
        if(len(s)<2):
            if(s==""):
                x = -1
            continue
        else:
            y = s[0]
            z = " "+s[1:]
            if(z.find(y)!=-1):
                list.append(s)
    return list

#stretch2

def palindrome_test(x):
    if(len(x)%2==0):
        z = int(len(x)/2)
    else:
        z = int((len(x)+1)/2)
    for i in range(z):
        if(x[i]==x[len(x)-(1+i)]):
            z-=1
    return z==0

def is_palindrome(x):
    s = x.lower()
    for i in range(len(s)):
        t = s[i]
        if(t.isalpha()==False):
            s = s.replace(t," ")
    s = s.replace(" ","")
    y = palindrome_test(s)
    return y

#workout

def igpay(word):
    list = ['a','e','i','o','u','A','E','I','O','U']
    if word[0] in list:
        s = word + "way"
    else:
        x = len(word)
        for i in range(len(word)):
            if word[i] in list:
                x = i
                break
        s = word[x:] + word[:x] + "ay"
        t = word[0]
        if(t.isupper()==True):
            s = s.lower()
            s = s.capitalize()
    return s
