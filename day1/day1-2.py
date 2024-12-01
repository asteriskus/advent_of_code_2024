from collections import Counter
with open("input.txt", "r") as file:
    lines = [line.split() for line in file]

first = [int(line[0]) for line in lines]
second = [int(line[1]) for line in lines]
counter = Counter(second)
total = 0
for id in first:
    times = id * counter[id]
    total += times

print(total)
