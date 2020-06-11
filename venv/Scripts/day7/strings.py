"""
Time   : 2020/6/11 14:53
Author : huyangh
演示字符串操作和运算符
"""


def string_basic():
    """
    字符串基本操作
    """
    s1 = 'hello, world!'
    s2 = "hello, world!"
    # 以三个双引号或单引号开头的字符串可以折行
    s3 = """
        hello, 
        world!
        """
    print(s1, s2, s3, end='')
    print()

    # 用\进行转义
    s1 = '\'hello, world!\''
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')
    print()

    # 用r取消\的转义作用
    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2, end='')
    print()

    # \后接8进制，16进制，unicode编码
    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u80e1\u6d0b'
    print(s1, s2)
    print()

    # 字符串运算符 + *
    s1 = 'hello ' * 3
    print(s1)  # hello hello hello
    s2 = 'world'
    s1 += s2
    print(s1)  # hello hello hello world

    # 用in / not in 进行成员运算
    print('ll' in s1)  # True
    print('good' in s1)  # False

    # 切片运算 从字符串中取出指定位置的字符(下标运算)
    str2 = 'abc123456'
    print(str2[2])  # c
    # 切片运算 从指定的开始索引到指定的结束索引
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    # 反向切片获得倒序字符串
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    print()


def string_methods():
    """
    演示字符串方法
    """
    str1 = 'hello, world!'
    # 通过内置函数len计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!
    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title())  # Hello, World!
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!
    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1
    # 与find类似但找不到子串时会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  huyangh@sina.com '
    print(str3)
    # 获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())


def string_output():
    """
    演示字符串输出方法
    """
    a, b = 5, 10
    print('%d * %d = %d.' % (a, b, a * b))
    # 使用字符串方法
    a, b = 5, 10
    print('{0} * {1} = {2}.'.format(a, b, a * b))
    # 使用新风格
    a, b = 5, 10
    print(f'{a} * {b} = {a * b}.')


def main():
    string_basic()
    string_methods()
    string_output()


if __name__ == '__main__':
    main()
