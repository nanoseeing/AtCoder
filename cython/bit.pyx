""" Binary Index Tree """


# 1-index

cdef class Bit:

    cdef int n
    cdef int[500001] tree

    def __init__(self, int n):
        self.n = n

    cdef add(self, int i, int x): # a[i] += val
        while i <= self.n:
            self.tree[i] += x
            i += i & -i

    cdef sum(self, int i): # (0, i] の累積和
        cdef int s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s

    cdef bisect_left(self, int v): # 累積和 が v 以上になる最小の i

        if v > self.tree[self.n]:
            return -1

        cdef int i = 0
        cdef int step = self.n >> 1

        while step:
            if self.tree[i + step] < v:
                i += step
                v -= self.tree[i]
            step >>= 1

        return i + 1
