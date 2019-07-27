#第十四个练习 - 模拟火车订票系统

train_num_list = [["车次", "出发站-到达站", "出发时间", "到达时间", "历时"],
                  ["T40", "长春-北京", "00：12", "12：20", "12：08"],
                  ["T298", "长春-北京", "00：06", "10：50", "10：44"],
                  ["Z158", "长春-北京", "12：48", "12：06", "08：18"],
                  ["Z62", "长春-北京", "21：58", "06：08", "08：20"]]

for i in range(5):
    for j in range(5):
        if i == 0:
            print("%2s" % train_num_list[i][j], end="    ")
        else:
            print("%4s"%train_num_list[i][j], end="    ")
            if j == 1:
                print(end="    ")
            elif j == 2:
                print(end="  ")
    print()
#以上语句为了使打印对齐，初学只能用这种方法

judge = True
while judge:
    train_num = input("请输入要购买的车次：")
    for i in range(5):
        if train_num == train_num_list[i][0]:
            person_name = input("请输入乘车人（用逗号分隔）：")
            print("您已购买", train_num_list[i][0], "次列车" , train_num_list[i][1],
            train_num_list[i][2],"开，请", person_name, "尽快换取纸质车票。【铁路客服】")
            judge = False
    if judge == True:
        print("输入有误，请重新输入！")


