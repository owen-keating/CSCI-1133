
#WARMUP 1:
# 1. base case is [], no values
# 2. 
# sum([1, 2, 3, 4, 5, 6, 7, 8, 9]) = sum([1, 2, 3, 4, 5, 6, 7, 8] + 9
# sum([1, 2, 3, 4, 5, 6, 7, 8)] = sum([1, 2, 3, 4, 5, 6, 7]) + 8
# ...so on so forth
# 3. factorials can be expressed in terms of recurrence relation, so it will always work
# Your recursive case must always move towards the base case
# 4. see replit

def sum_list(vals):
  #if length of list is 0, return 0
  if len(vals)==0:
    return 0
  else: 
    #return the value of the sum of first index of vals and the sum of all the values from [1] to the end of list
    return vals[0] + sum_list(vals[1:])
  
print(sum_list([8,6,7,5,3,0,9]))
print(sum_list([]))

#WARMUP 2: Reversing a String
def reverse_string(st):
  if len(st)==0:
    return st
  #if /= 0, reverse function is recursively called to slive the part of the string except character at [0], and concatenate the first character to the end of the sliced string
  else:
    return reverse_string(st[1:]) + st[0]

print(reverse_string('hello'))

#STRETCH:Fibonacci Numbers
def fibonacci(n):
  #any number less than zero is not valid, first number in sequence is 0
  if n<0:
    print('invalid')
  #first number in sequence is 0
  elif n==0:
    return 0
  #second fib number is 1
  elif n==1:
    return 1
  #Fn formula
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
print(fibonacci(20))

#STRETCH 2: Reversing a list
def double_reverse(lst):
  if len(lst)==0:
    return lst
  else:
    return [reverse_string(lst[-1])] + double_reverse(lst[:-1])

print(double_reverse(['hello','double','reverse']))


#WORKOUT: Deep Square
def deep_square(n_list):
  #make new list for the squared values later
  new_list = []
  for n in n_list:
    new_list.append(n)
  for i in range(len(new_list)):
    #determining if integer 
    if type(new_list[i]) != list:
      #squaring each value
      new_list[i] = new_list[i]**2
    else:
      #assigning the result to new_list[i]
      new_list[i] = deep_square(new_list[i]) 
    return new_list

print(deep_square([[-1, [2], [3], [[[-4,5]]], [], []]]))
print(deep_square([-7, [2, 5, [-3], [], [[5, 7], 1]], -7]))
