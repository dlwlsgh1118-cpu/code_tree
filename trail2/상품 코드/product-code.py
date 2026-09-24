product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class information:
    def __init__(self,name,price):
        self.name = name
        self.price = price

A = information(product_name,product_code)

print("product 50 is codetree")
print(f"product {A.price} is {A.name}")