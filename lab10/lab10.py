
def make_dictionary(list1,list2):
  dict = {}
  for i in range(len(list1)):
    dict[list1[i]] = list2[i]
  return dict

def score_dict(list1,list2):
  dict = make_dictionary(list1,list2)
  barb = dict['barb']
  print(barb)
  dict['john'] = 19
  list1.append('john')
  print(dict)
  sum = 0
  for i in range(len(dict)):
    num = dict[list1[i]]
    sum = sum + num
  print("average: " + str(sum/len(dict)))

def get_score(name,dict):
  try:
    num = dict[name]
  except KeyError:
    print("name does not exist in dictionary")
    num = -1
  return num

def morse_code():
  morse_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--','N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.','S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}
  sent = input("Enter a message:")
  sent = sent.upper()
  list = []
  for i in sent:
    list.append(morse_dictionary[i])
  message = " ".join(list)
  return message

def rank_suit_count(cards):
  rank = {}
  suit = {}
  for i in range(len(cards)):
    s = cards[i]
    x = s[0]
    try:
      rank[x]+=1
    except KeyError:
      rank[x]=1
    y = s[1]
    try:
      suit[y]+=1
    except KeyError:
      suit[y]=1
  return (rank,suit)
