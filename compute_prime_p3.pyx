%cython
def compute_prime(int n):
    cdef int max = n
    cdef int i,j
    cdef list possible_val = range(0,max,1)
    denominator = [2,3,5,7,11]
    m = range(0,max,1)
    for i in denominator:
        for j in possible_val:
            if j%i == 0:
                if i!=j:
                    possible_val.remove(j)
    return possible_val

#5 loops, best of 3: 419 ms per loop
