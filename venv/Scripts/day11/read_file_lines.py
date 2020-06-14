"""
Time   : 2020/6/14 21:57
Author : huyangh
按行读取文件
"""
import time


def main():
    # 通过for-in循环逐行读取
    with open('沁园春雪.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            # time.sleep(0.2)
    print()
    print()

    # 读取文件按行读取到列表中
    with open('沁园春雪.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # print(lines)
        for _ in lines:
            print(_, end='')


if __name__ == '__main__':
    main()