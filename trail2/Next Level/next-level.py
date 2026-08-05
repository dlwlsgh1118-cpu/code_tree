class information:
    def __init__(self,user = 'codetree', Lv = 10):
        self.user = user
        self.Lv = Lv


a,b = input().split()
A1 = information()
A2 = information(a,b)

print(f"user {A1.user} lv {A1.Lv}")
print(f"user {A2.user} lv {A2.Lv}")