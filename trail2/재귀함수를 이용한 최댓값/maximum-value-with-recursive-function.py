n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
def f(arr,n,end):
    global cnt

    if n == end:
        return
    elif cnt < arr[n]:
        cnt = arr[n]
    f(arr,n+1,end)
    return cnt

print(f(arr,0,n))