text = input()
pattern = input()

# Please write your code here.
def f(t,p):
    r = len(p)

    for i in range(0,len(t)):

        if t[i:i+r] == p:

            return i
    return -1


print(f(text,pattern))