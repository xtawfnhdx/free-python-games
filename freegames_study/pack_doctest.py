import doctest


class t1():
    """
    这是一个类
    """
    def f1(self):
        """
        这是一个函数
        """
        pass
#help(t1)

def f2(x,y):
    '''
    >>> f2(2,3)
    6
    >>> f2('a',3)
    aaa

    '''
    print(x*y)


if __name__=="__main__":
    doctest.testmod(verbox=True)