"""
Time   : 2020/6/12 20:36
Author : huyangh
练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
"""
from math import sqrt


class Point(object):
    """
    描述平面上的点并提供移动点和计算到另一个点距离的方法
    """
    def __init__(self, list):
        """
        初始化方法
        :param a: a为含有两个元素的列表，分别为x坐标和y坐标
        """
        self.x = list[0]
        self.y = list[1]


    def moveBy(self, dx, dy):
        """
        按增量移动位置
        :param x: dx
        :param y: dy
        """
        self.x += dx
        self.y += dy


    def moveTo(self, x, y):
        """
        移动到指定位置
        :param x: x
        :param y: y
        :return:
        """
        self.x = x
        self.y = y


    def distanceTo(self, other):
        """
        返回两点之间的距离
        :param other:   另一个点的对象
        """
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def main():
    p1 = [1, 0]
    p2 = [1, 1]
    a = Point(p1)
    b = Point(p2)

    a.moveBy(2, 4)
    print(a.x, a.y)

    b.moveTo(0, 0)
    print(b.x, b.y)

    d = a.distanceTo(b)
    print(d)


if __name__ == '__main__':
    main()