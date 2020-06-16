"""
Time   : 2020/6/16 11:19
Author : huyangh
正则表达式测试
"""
import re


def main():
    num = input('Please input a phone number:')
    regular = re.compile('\d{11}', flags=0)
    if (regular.match(num)):
        print('Valid number!')
    else:
        print('Invalid number!')


if __name__ == '__main__':
    main()
