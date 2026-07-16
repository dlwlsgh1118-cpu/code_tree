N = int(input())

# Please write your code here.
def f(n):
    if n == 1 or n == 0:
        return n
    
    return f(n-1) + f(n-2)

print(f(N))