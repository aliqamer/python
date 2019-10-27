
def lesser_of_two_evens(n1, n2):

    max = n1
    if n1 % 2 == 0 and n2 % 2 == 0:
        if n1 > n2:
            max = n1
        else:
            max = n2
    else:
        if n1 > n2:
            max = n2
        else:
            max = n1
    return max


if __name__ == '__main__':
    import sys
    res = lesser_of_two_evens(12, 8)
    print('max: ', res)
