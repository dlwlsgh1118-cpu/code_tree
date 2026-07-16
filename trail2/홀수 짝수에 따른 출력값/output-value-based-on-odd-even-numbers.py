N = int(input())

# Please write your code here.

def f(n):
    if n <= 1:
        return n
    elif n % 2 ==0:
        return n + f(n-2)
    else:
        return n + f(n-2)

print(f(N))