n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(arr):
    for j,i in enumerate(arr):
        if i < 0:
            i = i*-1
        arr[j] = i

    return arr

for i in f(arr):
    print(i, end=' ')

        