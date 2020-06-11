"""
Time   : 2020/6/11 18:40
Author : huyangh
练习3：设计一个函数返回给定文件名的后缀名。
"""


# 我的写法
def suffixof(name):
    for index, char in enumerate(name):
        if char != '.':
            pass
        else:
            print(name[index + 1 : len(name)])

# 别人的写法
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def main():
    filename = input('Please input a filename, suffix included:')
    suffixof(filename)
    print(get_suffix(filename, True))


if __name__ == '__main__':
    main()