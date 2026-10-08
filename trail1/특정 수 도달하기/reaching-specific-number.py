a = list(map(int,input().split()))
cnt = 0
Len = 0
for i in a:
    if i < 250:
        cnt += i
        Len += 1
    else:
        break

print("%d %.1f"%(cnt,(cnt/Len)))