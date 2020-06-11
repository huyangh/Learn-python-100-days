"""
Time   : 2020/6/9 12:35
Author : huyangh
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
    鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
    百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
#穷举法
for male in range(0, int(100 / 5)):
    for female in range(0, int(100 / 3)):
        chick = 100 - male - female
        if male * 5 + female * 3 + chick / 3 == 100:
            print(male, female, chick)
