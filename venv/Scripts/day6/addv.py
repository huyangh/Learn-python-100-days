#定义可变参数的函数
def addv(*args):
    """
    任意个数的数字相加，0也可
    """
    sum = 0
    for item in args:
        sum += item
    return sum