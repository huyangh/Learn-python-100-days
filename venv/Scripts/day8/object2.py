"""
Time   : 2020/6/12 20:02
Author : huyangh
演示访问可见性
"""
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')

    # test.__bar()        # AttributeError: 'Test' object has no attribute '__bar'
    test._Test__bar()        # 访问私有方法

    # print(test.__foo)        # AttributeError: 'Test' object has no attribute '__foo'
    print(test._Test__foo)        # 访问私有属性


if __name__ == "__main__":
    main()