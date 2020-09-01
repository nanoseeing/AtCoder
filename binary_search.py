""" 探索系 """


def is_ok(x):
    pass


# 2分探索（めぐる式）
def binary_search(ng, ok):

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


# 3分探索
def ternary_search(left, right, e=1e-09):

    while right - left > e:
        mid1 = (2 * left + right) / 3
        mid2 = (left + right * 2) / 3

        if is_ok(mid1) < is_ok(mid2):
            right = mid2
        else:
            left = mid1

    return (left + right) / 2
