order_first = []
order_second = []
with open("input.txt", 'r') as file:
    for column in file:
        first = int(column.split()[0])
        second = int(column.split()[1])
        order_first.append(first)
        order_second.append(second)

order_first.sort()
order_second.sort()

total = 0
for i in range(len(order_first)):
    distance = abs(order_first[i] - order_second[i])
    total += distance

print(total)
