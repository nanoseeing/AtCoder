""" Binary Index Tree """


# 1-index
class Bit:

    def __init__(self, a):  # 配列か要素数で初期化
        if hasattr(a, "__iter__"):
            le = len(a)
            self.n = 1 << le.bit_length()
            self.values = values = [0] * (self.n + 1)
            values[1:le + 1] = a[:]
            for i in range(1, self.n):
                values[i + (i & -i)] += values[i]
        elif isinstance(a, int):
            self.n = 1 << a.bit_length()
            self.values = [0] * (self.n + 1)
        else:
            raise TypeError

    def add(self, i, val):  # a[i] += val
        n, values = self.n, self.values
        while i <= n:
            values[i] += val
            i += i & -i

    def sum(self, i):  # (0, i] の累積和
        values = self.values
        res = 0
        while i > 0:
            res += values[i]
            i -= i & -i
        return res

    def bisect_left(self, v):  # 累積和 が v 以上になる最小の i
        n, values = self.n, self.values
        if v > values[n]:
            return None
        i, step = 0, n >> 1
        while step:
            if values[i + step] < v:
                i += step
                v -= values[i]
            step >>= 1
        return i + 1
