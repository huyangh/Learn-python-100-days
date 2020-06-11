"""
Time   : 2020/6/11 17:02
Author : huyangh
练习1：在屏幕上显示跑马灯文字。
"""
import os
import time


def main():
    content = '这是一个跑马灯程序…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()