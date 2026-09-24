n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

# Please write your code here.
lst = []
for i in range(n):
    lst.append([name[i],address[i],region[i]])
lst_sorted = sorted(lst)
class Test:
    def __init__(self,name,addr,city):
        self.name = name
        self.addr = addr
        self.city = city
data = tuple(lst_sorted[-1])
A = Test(*data)
print("name %s"% A.name)
print("addr %s"% A.addr)
print("city %s"% A.city)