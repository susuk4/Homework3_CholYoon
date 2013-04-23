def series_sum_sq(n):
    totalsum = 0
    for i in range(1,n,1):
        totalsum = totalsum + i**2
    return totalsum

#Time n = 100000
#100 loops, best of 3: 5.9 ms per loop
%timeit(series_sum_sq(10000))
