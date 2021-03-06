"""
Time   : 2020/6/14 21:52
Author : huyangh
读取并输出文本文件中的内容，带异常处理。用with关键字指定上下文环境，并在离开时自动释放资源
"""
def main():
    try:
        with open('沁园春雪.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()