a = int(input())
arr = list(map(int,input().split()))
arr.sort()
for i in arr:
    print(i,end=' ')

print()
for i in arr[::-1]:
    print(i,end=' ')