""" 探索系 """


# 2分探索
def binary_search(min_n, max_n):

    while max_n - min_n != 1:
        mid = (min_n + max_n) // 2
        if f(mid):
            max_n = mid
        else:
            min_n = mid

    return max_n


# 3分探索
def ternary_search(left, right, e=1e-09):

    while right - left > e:
        mid1 = (2 * left + right) / 3
        mid2 = (left + right * 2) / 3

        if f(mid1) < f(mid2):
            right = mid2
        else:
            left = mid1

    return (left + right) / 2
