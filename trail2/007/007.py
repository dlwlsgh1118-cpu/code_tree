class Spy:
    def __init__(self,secretcode,meetingpoint,time):
        self.secretcode = secretcode
        self.meetingpoint = meetingpoint
        self.time = time

s_code, m_point, time = tuple(input().split())

# 객체 생성
s = Spy(s_code, m_point, int(time))

print("secret code :",end=' ')
print(s.secretcode)
print("meeting point :",end=' ')
print(s.meetingpoint)
print("time :",end=' ')
print(s.time)
