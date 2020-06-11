"""
Time   : 2020/6/11 20:30
Author : huyangh
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    list = [1] * 30
    count, index, number = 0, 0, 0
    while count < 15:
        if list[index]:
            number += 1
            if number == 9:
                list[index] = 0
                count += 1
                number = 0
        index += 1
        index %= 30       # 避免下标越界的方法
    print(list)        # 1是基督徒，0是非基督徒


if __name__ == '__main__':
    main()
