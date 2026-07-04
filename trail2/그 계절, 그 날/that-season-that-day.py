Y, M, D = map(int, input().split())
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Please write your code here.
def year_(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    return False

if year_(Y):
    days_in_month[M] = 29

if days_in_month[M] < D:
    print(-1)
else:
    if 3 <= M <= 5:
        print("Spring")
    elif 6<= M <= 8:
        print("Summer")
    elif 9<= M <= 11:
        print("Fall")
    elif M == 12 or M <= 2:
        print("Winter")