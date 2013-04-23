%cython
cdef float det44m(list a, list b):
    row1 = [0,0,0,0]
    row2 = [0,0,0,0]
    row3 = [0,0,0,0]
    row4 = [0,0,0,0]
    cdef list fm = [row1,row2,row3,row4]
    cdef int row
    cdef int col
    for row in range(0,4,1):
        rowtemp = [a[row][0],a[row][1],a[row][2],a[row][3]]
        for col in range(0,4,1):
            coltemp = [b[0][col],b[1][col],b[2][col],b[3][col]]
            fm[row][col] = rowtemp[0]*coltemp[0]+rowtemp[1]*coltemp[1]+rowtemp[2]*coltemp[2]+rowtemp[3]*coltemp[3]
    return fm

#625 loops, best of 3: 161 µs per loop
