n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def f(arr,que):
    sum = 0
    for i in que:
        n,m = i
        for j in range(n-1,m):
            sum += arr[j]
        print(sum)
        sum = 0

f(arr,queries)