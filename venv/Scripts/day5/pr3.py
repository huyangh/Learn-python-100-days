"""
Time   : 2020/6/9 12:48
Author : huyangh
生成斐波那契数列的前20个数
"""
a = 0
b = 1
count = 0
while count < 20:
    a, b = b, a + b
    count += 1
    print(a, end= '\t')