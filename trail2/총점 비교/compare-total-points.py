n = int(input())

name = []
score1 = []
score2 = []
score3 = []

lst = []
for _ in range(n):
    student_info = input().split()
    lst.append((student_info[0],int(student_info[1]),int(student_info[2]),int(student_info[3])))
lst.sort(key = lambda x : (x[1] +x[2] + x[3]))

# Please write your code here.
for i in lst:
    print(*i)