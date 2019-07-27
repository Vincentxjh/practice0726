#第十二个练习 - 集合的交、差、并集

python = {"绮梦", "冷伊一", "香凝", "梓轩"}
c = set(["冷伊一", "和路雪", "圣博", "梓轩"])
print("选择Python的学生有：", python, "\n")
print("选择C语言的学生有：", c, "\n")
print("两门课都选的学生有：", python & c, "\n")
print("所有参加选修课的学生有：", python | c, "\n")
print("只选Python没有选C语言的学生有：", python - c, "\n")
