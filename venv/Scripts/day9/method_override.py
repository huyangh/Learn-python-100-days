"""
Time   : 2020/6/13 13:05
Author : huyangh
演示方法重写和多态
"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    # 在类中定义抽象方法，则该方法不能实例化
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    pet2 = Pet('df')
    for pet in pets:
        pet.make_voice()
    # pet2.make_voice()       # TypeError: Can't instantiate abstract class Pet with abstract methods make_voice


if __name__ == '__main__':
    main()