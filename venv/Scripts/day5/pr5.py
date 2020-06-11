"""
Time   : 2020/6/9 13:08
Author : huyangh
输出100以内所有的素数
"""
import math
for num in range(2, 100):
    count = 0
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            count += 1
    if count == 0:
        print(num)
