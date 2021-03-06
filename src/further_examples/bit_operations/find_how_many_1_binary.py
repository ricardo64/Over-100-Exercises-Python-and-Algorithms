#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

''' Find how many 1s in the binary:
    1) Start with a mask of 1
    2) Mask with AND
    3) if result (if true): count += 1
    (obs: to find the int of a bin do int('1001', 2)) and to show in bin do bin(int))
    
    >>> find_how_many_1_in_a_binary(9)
    2

'''



def find_how_many_1_in_a_binary(n):
    counter = 0
    while n:
        if n & 1:
            counter += 1
        n >>= 1
    return counter


    
    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

