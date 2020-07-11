# 尺取法

count = 0
r = 0
for l in range(N):
    while r < N:
        if judge():
            r += 1
        else:
            break
    count += r - l
    if r == l:
        r += 1
