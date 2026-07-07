A = input()

# Please write your code here.
def f(a):
    List = []
    for i in a:
        if i in List:
            continue
        else:
            List.append(i)
    return List

if len(f(A)) >= 2:
    print("Yes")
else:
    print("No")