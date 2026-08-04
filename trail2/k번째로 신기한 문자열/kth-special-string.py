a,b,c = input().split()
arr = []
for i in range(int(a)):
    d = input()
    list(d)
    if c == d[0:len(c)]:
        arr.append(d)
arr.sort()
print(arr[int(b)-1])
