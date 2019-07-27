#第十三个练习 - 输出“王者荣耀”的游戏角色


tank_role = ('苏烈', '刘邦', '钟馗', '张飞', '牛魔', '程咬金', '白起',
             '刘禅', '庄周', '项羽', '廉颇', '巨灵神', '安禄山', '猪八戒')
soldier_role = ('狂铁', '裴擒虎', '孙悟空', '铠', '哪吒', '杨戬', '橘右京',
             '老夫子', '韩信', '吕布', '关羽', '夏侯淳', '雅典娜', '亚瑟')
assassin_role = ('百里玄策', '庞统', '阿珂', '不知火舞', '李白', '娜可露露',
                 '兰陵王', '宫本武藏', '韩信', '露娜')
master_role = ('杨玉环', '异星', '貂蝉', '女娲', '周瑜', '鬼谷子', '小乔',
             '武则天', '王昭君', '安其拉')
shooter_role = ('公孙离', '后裔', '刘备', '狄仁杰', '马可波罗', '李元芳',
                '鲁班七号','孙尚香')
assist_role = ('明世隐', '孙膑', '太乙真人', '蔡文姬')
hero_classify = ('坦克', '战士', '刺客', '法师', '射手', '辅助')

all_role = (tank_role, soldier_role, assassin_role, master_role, shooter_role, assist_role)
role_dict = dict(zip(hero_classify, all_role))
#以上创建角色字典还可以用下面这种方式代替
#role_dict = dict(坦克=tank_role, 战士=soldier_role, 刺客=assassin_role, 法师=master_role, 射手=shooter_role, 辅助=assist_role)

print("“王者荣耀”游戏角色：")
for key,value in role_dict.items():
    print("===", key, "===")
    for i in value:
        print(i, end=" ")
        #此for循环的作用是把作为字典值的各个元组中的各个元素打印出来。
        #如果不用这个for循环，则打印出来的是整个元组。
        #格式为：('xxx', 'xxx', 'xxx', 'xxx') ，既不美观也不满足题目要求。
    print()
