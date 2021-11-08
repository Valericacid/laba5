def medians(n, m):
    c = n + m
    c.sort()
    length = len(c)
    cen = int(length / 2)
    if length % 2 == 0:
        return (c[cen - 1] + c[cen]) / 2
    else:
        return c[cen]

