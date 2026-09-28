n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
student = []
for i in range(n):
    student.append((name[i], height[i], weight[i]))

student.sort(key = lambda x : x[1])

for i in student:
    print(*i)