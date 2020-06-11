"""
Time   : 2020/6/9 12:55
Author : huyangh
找出10000以内的完美数。
说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
"""
for num in range(4, 10000):
    sum = 0
    for factor in range(1, int(num / 2) + 1):
        if num % factor == 0:
            sum += factor
    if sum == num:
        print(num)
