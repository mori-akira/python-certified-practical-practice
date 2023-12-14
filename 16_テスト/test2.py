import doctest

'''
テスト①

>>> div(5, 2)
2.5
'''

def div(a, b):
    '''
    テスト②

    >>> [div(n, 2) for n in range(5)]
    [0.0, 0.5, 1.0, 1.5, 2.1]
    '''
    return a / b

if __name__ == '__main__':
    doctest.testmod()
