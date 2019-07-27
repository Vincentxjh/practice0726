#第三个练习 - 在旧列表后追加新列表

oldlist = ["迈克尔·乔丹", "卡里姆·阿布杜尔·贾巴尔", "哈基姆·奥拉朱旺", "查尔斯·巴克利", "姚明"]
newlist = ["贾森·基德", "史蒂夫·纳什", "格兰特·希尔"]
oldlist.extend(newlist)
print(oldlist)