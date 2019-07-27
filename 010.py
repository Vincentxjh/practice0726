#第十个练习 - 应用字典推导式创建字典

name = ["绮梦", "冷伊一", "香凝", "黛兰"]
sign = ["水瓶座", "射手座", "双鱼座", "双子座"]
dictionary = {i:j for i,j in zip(name, sign)}
print(dictionary)