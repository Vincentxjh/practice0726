#第十七个练习 - 追加练习
#有时候需要单独取出字典的键或值，需要用到dictionary.title()方法，具体如下：
favorite_languages = {'Jen':'Python', 'sarah':'C', 'edward':'ruby', 'phil':'Python'}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " + language.title() + ".")

#有时候一个字典的键对应多个值的时候，也可以用这种方法：
favorite_languages = {'Jen':['Python', 'ruby'],
                      'sarah':['C'],
                      'edward':['ruby', 'go'],
                      'phil':['Python', 'heskell']}
for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are :")
    for languages in language:
        print(languages.title())