""" 二分探索 """


def binary_search(min_n, max_n):

    while max_n - min_n != 1:
        tn = (min_n + max_n) // 2
        if judge(tn):
            max_n = tn
        else:
            min_n = tn

    return max_n
