n = int(input())

commands = [tuple(input().split()) for _ in range(n)]

tile = {}
pos = 0

for num, direction in commands:
    num = int(num)

    for i in range(num):
        if direction == 'L':
            tile[pos - i] = 'L'
        else:
            tile[pos + i] = 'R'

    # 마지막으로 뒤집은 타일로 이동
    if direction == 'L':
        pos -= num - 1
    else:
        pos += num - 1

white = 0
black = 0

for direction in tile.values():
    if direction == 'L':
        white += 1
    else:
        black += 1

print(white, black)