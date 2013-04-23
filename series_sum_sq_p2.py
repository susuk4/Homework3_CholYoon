def series_sum_sq(n):
    if n>0:
        totalsum = 0
        for i in range(1,n,1):
            totalsum = totalsum + i**2
        return totalsum
    elif n==0:
        totalsum = 0
        return totalsum
    elif n<0:
        raise ValueError, str(n)+" is not positive integer"
    else: 
        raise ValueError, str(n)+" is not an integer"
#Time n = 100000
#100 loops, best of 3: 5.58 ms per loop
%timeit(series_sum_sq(10000))
