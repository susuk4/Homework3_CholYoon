def compute_prime(n):
    denominator = [2,3,5,7,11]
    possible_val = range(0,n,1)
    for i in denominator:
        for j in possible_val:
            if j%i == 0:
                if i!=j:
                    possible_val.remove(j)
    return possible_val

%timeit(compute_prime(10000))
#1 loops, best of 3: 391 ms per loop
