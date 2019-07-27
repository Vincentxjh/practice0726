#第十五个练习 - 电视剧收视率排行榜

print("电视剧收视率排行榜:")
tv_play_tuple = ("《GIve up,hold on to me》",
                 "《The private deshes of the husbands》",
                 "《My father-in-law will do martiaiarts》",
                 "《North Canton still believe in love》",
                 "《Impossibel task》",
                 "《Sparrow》",
                 "《East of dream Avenue》",
                 "《The prodigal son of the frontier town》",
                 "《Distant distance》",
                 "《Music legend》")
audience_ratings_list = [1.4, 1.343, 0.92, 0.862, 0.553, 0.411, 0.164, 0.259, 0.394, 0.562]
tv_dictionary = dict(zip(tv_play_tuple, audience_ratings_list))
for i,j in tv_dictionary.items():
    print(i, "收视率：", j, "%")

print("\n电视剧收视率排行榜（按收视率高低排序）:")
sort_tv_dictionary = sorted(tv_dictionary.items(), key=lambda item:item[1], reverse=True)
#以上语句用于把字典按照item[1]，也就是字典值的顺序来排序，若要按字典键的顺序来排，则改为item[0]
for i,j in sort_tv_dictionary:
    print(i, "收视率：", j, "%")