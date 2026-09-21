n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

list = [0 for _ in range(200)]
cnt = 0
for i in range(n):
    for j in range(segments[i][0],segments[i][1] + 1):
        list[j] += 1

print(max(list))