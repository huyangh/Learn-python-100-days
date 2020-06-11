"""
Time   : 2020/6/11 17:04
Author : huyangh
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random


def veri_code_generator():
    """
    产生用户指定长度的验证码
    """
    length = int(input('Please input the length you want:'))
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    last_index = len(chars) - 1
    veri_code = ''

    for _ in range(length):
        veri_code += chars[random.randint(0, last_index)]
    print(veri_code)


def main():
    veri_code_generator()


if __name__ == '__main__':
    main()

