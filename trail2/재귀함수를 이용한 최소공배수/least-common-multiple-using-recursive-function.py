n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.




def lcm(a,b):
    return a*b // gcd(a,b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(i):
    if i == len(arr)-1:
        return arr[i]

    return lcm(arr[i], solve(i+1))

print(solve(0))