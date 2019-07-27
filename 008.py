#第八个练习 - 用元组生成生成器对象

#无论是遍历，还是转换成列表或元组，
#生成器对象都只能被使用一次，使用一次以后想再使用，得重新创建
number = (i for i in range(4))
print(number)
#print(tuple(number))   #将生成器对象转换成元组
#print(list(number))    #将生成器对象转换成列表
for j in number:
    print(j, end=" ")