a, b, c = map(int, input().split())

# Please write your code here.
index = -1
def f(n):
    global index
    if index == len(n)-1:
        return 0
    else:
        index += 1
    return int(n[index]) + f(n)

print(f(str(a*b*c)))