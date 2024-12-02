lists = [[], []]
with open('input.txt', 'r') as f:
    for line in f.readlines():
        numbers = [int(w) for w in line.strip().split()]
        for i in range(len(numbers)):
            lists[i].append(numbers[i])
for i in range(len(lists)):
    lists[i].sort()
distance = 0
for i in range(len(lists[0])):
    distance += abs(lists[0][i] - lists[1][i])
print(distance)

from collections import Counter

c = Counter(lists[1])
similarity = 0
for n in lists[0]:
    if n in c:
        similarity += n * c[n]

print(similarity)
