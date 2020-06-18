"""
Time   : 2020/6/18 18:44
Author : huyangh
调用天行API的“十万个为什么”查询接口，读取用户输入，返回查找结果
"""
import requests


def main():
    # 通过requests模块的get函数获取网络资源
    print('“十万个为什么”查找程序，欢迎使用')
    word = input('请输入你想查找的关键字：')
    url = 'http://api.tianapi.com/txapi/tenwhy/index?key=b1e74cefa0029cca67eb9959777738d0&word=*'

    resp = requests.get(url.replace('*', word, 1))
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()

    gettitle   = data_model['newslist'][0]['title']
    getcontent = data_model['newslist'][0]['content']
    print('标题：' + gettitle)
    print('内容：' + getcontent)



if __name__ == '__main__':
    main()