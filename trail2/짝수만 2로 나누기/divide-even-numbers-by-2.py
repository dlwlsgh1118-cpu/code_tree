n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def change(arr):
    for i,j in enumerate(arr):
        if j % 2 == 0:
            arr[i] = j//2
            
    return arr

for i in change(arr):
    print(i, end=' ')