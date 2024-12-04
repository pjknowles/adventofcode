import re

with open('input.txt', 'r') as f:
    text = f.read()
match = re.findall(r'do\(\)|don\'t\(\)|mul\( * *[0-9]+ *,[0-9]+ *\)', text, re.MULTILINE)


def compute(instructions, filter=False):
    global total
    total = 0
    active = True
    for instance in instructions:
        if instance == 'do()':
            active = True
        elif instance == 'don\'t()':
            active = not filter
        elif active:
            numbers = re.findall(r'[0-9]+', instance)
            total += int(numbers[0]) * int(numbers[1])
    return total


print(compute(match))
print(compute(match, True))
