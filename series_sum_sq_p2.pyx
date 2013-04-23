%cython
def series_sum_sq(int n):
    cdef int number = n
    cdef long int totalsum
    if number>0:
        totalsum = 0
        for i in range(1,n,1):
            totalsum = totalsum + i**2
        return totalsum
    elif number==0:
        totalsum = 0
        return totalsum
    elif number<0:
        raise ValueError, str(n)+" is not positive integer"
    else: 
        raise ValueError, str(n)+" is not an integer"
       
#625 loops, best of 3: 912 µs per loop
