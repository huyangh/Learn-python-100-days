"""
Time   : 2020/6/16 11:24
Author : huyangh
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re


def main():
    name = input('Please input your user name:')
    qq   = input('Please input your qq number:')
    name_re = re.compile(r'^\w{6,20}$')
    qq_re = re.compile(r'^[1-9]\d{4,11}$')

    if(name_re.match(name)):
        print('username valid!')
    else:
        print('username invalid!')

    if(qq_re.match(qq)):
        print('QQ number valid!')
    else:
        print('QQ number invalid!')


if __name__ == '__main__':
    main()