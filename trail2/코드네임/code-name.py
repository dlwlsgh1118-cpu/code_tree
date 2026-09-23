# 요원 한 명의 코드네임과 점수를 함께 담는 클래스를 선언합니다.
class User:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score


# 요원 5명의 코드네임과 점수를 입력받습니다.
users = []

for _ in range(5):
    code_name, score = tuple(input().split())
    users.append(User(code_name, int(score)))


# 점수가 가장 낮은 요원의 위치를 찾습니다.
min_idx = 0
for i in range(1, 5):
    if users[min_idx].score > users[i].score:
        min_idx = i

# 점수가 가장 낮은 요원의 코드네임과 점수를 출력합니다.
print(users[min_idx].code_name, users[min_idx].score)
