n = int(input())

# Please write your code here.

def f(n):
    if n == 0:
        return

    f(n-1)
    print('*'*n)

f(n)