"""
Time   : 2020/6/8 18:49
Author : huyangh
输入两个正整数计算它们的最大公约数和最小公倍数
"""
num1 = int(input('Please input the first number:'))
num2 = int(input('Please input the second number:'))
if num1 < num2:
    small = num1
else:
    small = num2

for i in range(small, num1 * num2 + 1):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break

for j in range(1, small + 1):
    if num1 % j == 0 and num2 % j == 0:
        gcd = j

print('The LCM of the two values is: %d.' % (lcm))
print('The GCD of the two values is: %d.' % (gcd))