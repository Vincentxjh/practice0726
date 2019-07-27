#第六个练习 - 横版古诗变为竖版输出

verse1 = "千山鸟飞绝"
verse2 = "万径人踪灭"
verse3 = "孤舟蓑笠翁"
verse4 = "独钓寒江雪"
list = [list(verse1), list(verse2), list(verse3), list(verse4)]
print("-- 横版 --\n")
for i in range(4):
    for j in range(5):
        print(list[i][j], end="")
        if j == 4:
            print()

list.reverse()
#reverse()方法用于将列表进行逆向排序

print("\n-- 竖版 --\n")
for i in range(5):
    for j in range(4):
        print(list[j][i], end="")
        if j == 3:
            print()