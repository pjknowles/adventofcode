lists = [[], []]
with open('input.txt', 'r') as f:
    for line in f.readlines():
        numbers =[int(w) for w in line.strip().split()]
        for i in range(len(numbers)):
            lists[i].append(numbers[i])
for i in range(len(lists)):
    lists[i].sort()
distance = 0
for i in range(len(lists[0])):
    distance += abs(lists[0][i] - lists[1][i])
print(distance)