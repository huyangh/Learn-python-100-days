"""
Time   : 2020/6/13 13:24
Author : huyangh
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """员工"""
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # @abstractmethod
    # def calcSalary(self):
    #     pass


class Manager(Employee):
    """
    部门经理
    """
    def calcSalary(self):
        return 15000


class Programmer(Employee):
    """
    程序员
    """
    def __init__(self, name, time):
        super().__init__(name)
        self._time = time

    @property
    def time(self):
        return self._time

    def calcSalary(self):
        return self._time * 150


class Salesman(Employee):
    """
    销售员
    """
    def __init__(self, name, amount):
        super().__init__(name)
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def calcSalary(self):
        return 1200 + 0.5 * self._amount


def main():
    a = Manager('Lisa')
    b = Programmer('Guo', 160)
    c = Salesman('Peter', 15000)
    print('%s earn ￥%.2f a month.' % (a.name, a.calcSalary()))
    print('%s work %.2f hours a month and earn ￥%.2f.' % (b.name, b.time, b.calcSalary()))
    print('%s sales ￥%.2f a month and earn ￥%.2f.' % (c.name, c.amount, c.calcSalary()))


if __name__ == '__main__':
    main()