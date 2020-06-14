"""
Time   : 2020/6/14 22:24
Author : huyangh
利用json模块将字典或列表以JSON格式保存到文件中
"""
import json


def main():
    mydict = {
        'name': '郭平雷',
        'age': 26,
        'qq': 121226654,
        'friends': ['胡洋', '俞圣韬', '刘斌'],
        'CPUs': [
            {'brand': 'Intel', 'max_frequency': 3600},
            {'brand': 'AMD', 'max_frequency': 3400},
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()