#第五个练习 - 列表推导式

import random
#在1000～10000之间随机生成6个数作为原价
price = [random.randint(1000,10000) for i in range(6)]
print("原价格：", price)
sale = [int(i * 0.5) for i in price]
print("售价(原价打五折)：", sale)
price1 = [j for j in price if j > 3000]
print("原价大于3000的有：", price1)