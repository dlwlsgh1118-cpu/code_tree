k = int(input())
arr = list(map(int,input().split()))
List = []
for i in arr:
    List.append(i)
    if len(List) % 2 != 0:
        List.sort()
        print(List[len(List)//2],end=' ')

