#第七个练习 - 列出咖啡馆里的咖啡名称

coffeename = ("蓝山", "卡布奇诺", "曼特宁", "摩卡", "麝香猫", "哥伦比亚")
print("您好，欢迎光临，本店有：\n")
for name in coffeename:
    print(name + "咖啡", end="  ")
print()

#添加一款咖啡
newcoffee = ("拿铁",)
coffeename += newcoffee
print(coffeename)
