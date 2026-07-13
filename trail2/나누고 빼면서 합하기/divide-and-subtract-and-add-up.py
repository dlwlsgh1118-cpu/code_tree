n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def f(a,n,m):
    sum = 0
    while m > 0:
        sum += a[m-1]
        if m % 2 == 0:
            m = m//2
        else:
            m -= 1
        
    return sum
    
print(f(A,n,m))
    
        