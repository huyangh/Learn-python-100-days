"""
Time   : 2020/6/11 18:56
Author : huyangh
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
"""
# 我的做法
def max_2(x):
    y = sorted(x, reverse=True)
    return y[0 : 2]


# 别人的做法
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def main():
    x = [1, 3, 34, 78, 45, 324, 89, 1212]
    print(max_2(x)[0], max_2(x)[1])
    print(max2(x)[0], max2(x)[1])


if __name__ == '__main__':
    main()