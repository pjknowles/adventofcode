import re

with open('input.txt', 'r') as f:
    lines = f.readlines()
if False:
    lines = [
        'MMMSXXMASM',
        'MSAMXMSMSA',
        'AMXSXMAAMM',
        'MSAMASMSMX',
        'XMASAMXAMM',
        'XXAMMXXAMA',
        'SMSMSASXSS',
        'SAXAMASAAA',
        'MAMMMXMMMM',
        'MXMXAXMASX',
    ]

matches = 0
t = 'XMAS'


def search(table, pattern, x, y, dx, dy):
    for i in range(len(pattern)):
        x_ = x + dx * i
        y_ = y + dy * i
        if x_ < 0 or y_ < 0 or y_ >= len(table) or x_ >= len(table[y_]) or pattern[i] != table[y_][x_]: return False
    return True


for y in range(len(lines)):
    for x in range(len(lines[y])):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if search(lines, t, x, y, dx, dy):
                    matches += 1
print(matches)

matches = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[y]) - 1):
        for d1 in range(-1, 2, 2):
            for d2 in range(-1, 2, 2):
                if search(lines, 'MAS', x - d1, y - d1, d1, d1) and search(lines, 'MAS', x + d2, y - d2, -d2, d2):
                    matches += 1
print(matches)
