"""
Time   : 2020/6/8 19:22
Author : huyangh
输入一个正整数判断它是不是素数
"""
from math import sqrt
num = int(input('Please input an integer: '))
count = 0
for i in range(2, int(sqrt(num) + 1)):
    if num % i == 0:
        count += 1
if count == 0 and num != 1:
    print("This is a prime!")
else:
    print("This is not a prime!")