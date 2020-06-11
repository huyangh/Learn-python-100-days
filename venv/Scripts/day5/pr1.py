"""
Time   : 2020/6/8 20:08
Author : huyangh
找出所有水仙花数。水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
"""
def cube(n):
    return n * n * n

#暴力方法
# for i in range(1, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             if cube(i) + cube(j) + cube(k) == 100 * i + 10 * j + k:
#                 print('%d%d%d' % (i, j, k))

#利用求模运算
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)