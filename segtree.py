""" セグメント木 """


# 0-index
class SegTree:

    def __init__(self, init_val, segfunc, ide_ele):

        n = len(init_val)
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        self.num = 2**(n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num

        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]

        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res


if __name__ == '__main__':

    a = [14, 5, 9, 13, 4, 12, 11, 1, 7, 8]
    seg = SegTree(a, segfunc=min, ide_ele=float('inf'))
    print(seg.query(0, 5))
    seg.update(3, 2)
    print(seg.query(0, 5))
    seg.update(3, 100)
    print(seg.query(0, 5))
