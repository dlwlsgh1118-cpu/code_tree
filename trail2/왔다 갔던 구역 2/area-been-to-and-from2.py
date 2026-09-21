n = int(input())

x = []
direction = []

for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    direction.append(di)

lst = [0]
state = 0

for i in range(n):
    if direction[i] == 'L':

        # 왼쪽으로 이동해야 하는데 리스트 범위를 벗어나는 경우
        if state - x[i] < 0:
            extend = x[i] - state
            lst[0:0] = [0] * extend
            state += extend

        # 왼쪽으로 이동
        for _ in range(x[i]):
            state -= 1
            lst[state] += 1

    else:  # R

        # 오른쪽으로 이동해야 하는데 리스트 범위를 벗어나는 경우
        if state + x[i] > len(lst):
            lst.extend([0] * (state + x[i] - len(lst)))

        # 오른쪽으로 이동
        for _ in range(x[i]):
            lst[state] += 1
            state += 1


cnt = 0

for value in lst:
    if value >= 2:
        cnt += 1

print(cnt)