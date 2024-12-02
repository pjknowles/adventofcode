n_safe = 0
n_safe_modified = 0


def safety(numbers):
    safe = True
    for i in range(1, len(numbers)):
        safe = safe and (numbers[i] - numbers[i - 1]) * (numbers[1] - numbers[0]) > 0 and abs(
            numbers[i] - numbers[i - 1]) > 0 and abs(numbers[i] - numbers[i - 1]) < 4
    return safe


with open('input.txt', 'r') as f:
    for line in f.readlines():
        numbers = [int(w) for w in line.strip().split()]
        if safety(numbers):
            n_safe += 1
        for discard in range(len(numbers)):
            modified_numbers = numbers[:discard] + numbers[discard + 1:]
            if safety(modified_numbers):
                n_safe_modified += 1
                break
print(n_safe, n_safe_modified)
