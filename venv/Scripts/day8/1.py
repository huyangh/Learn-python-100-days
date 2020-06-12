"""
Time   : 2020/6/12 19:43
Author : huyangh
Generate a list containing 330 random numbers ranging from 1.95 to 2.40
"""
from random import random
def main():
    a = [0] * 330
    for i in range(len(a)):
        a[i] = 1.95 + 0.45 * random()
        print('%.2f' % a[i])






if __name__ == '__main__':
    main()