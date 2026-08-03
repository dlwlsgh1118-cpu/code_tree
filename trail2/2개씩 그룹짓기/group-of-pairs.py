n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
arr = []
for i in range(len(nums)-n):
    arr.append(nums[i] + nums[-(i+1)])

print(max(arr))