"""
Time   : 2020/6/16 15:41
Author : huyangh
演示字符串替换
"""
import re


def main():
    sentence = 'This is a sentence for substitution.'
    sentence_sub = re.sub('sentence', 'line', sentence, flags=re.IGNORECASE)
    print(sentence_sub)


if __name__ == '__main__':
    main()