total_products = int(input())
product_prices = [int(x) for x in input().split(" ")]
# print(product_prices)
count = 0
for product_price in product_prices:
    cube_root = round(product_price**(1/3))
    cube = cube_root ** 3
    if cube == product_price:
        count = count +1
print(count)