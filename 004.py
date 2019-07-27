#第四个练习 - 对列表进行排序

grade = [98,97,99,96,94,100,89,93,95,100,98,96]
print(grade)

newgrade = sorted(grade)
#或者用 grade.sort()也可，但如果用此方法，将改变原列表grade的顺序
print(newgrade)

newgrade1 = sorted(grade, reverse = True)
#或者用 grade.sort()也可，但如果用此方法，将改变原列表grade的顺序
#True 表示降序，False 表示升序
print(newgrade1)