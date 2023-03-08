
import random

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(100):
    roll_one = random.randint(1,6)
    roll_two = random.randint(1,6)
    total = roll_one + roll_two
    counts[total-1] = counts[total-1] + 1

print("Final list: ", counts)
