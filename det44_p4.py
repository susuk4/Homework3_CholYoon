def det44(m):
    det44val = m[0][0]*(m[1][1]*((m[2][2]*m[3][3]-m[2][3]*m[3][2])-m[1][2]*(m[2][1]*m[3][3]-m[2][3]*m[3][2])+m[1][3]*(m[2][1]*m[3][2]-m[2][2]*m[3][1])))
    -m[0][1]*(m[1][0]*(m[2][2]*m[3][3]-m[3][2]*m[2][3])-m[1][2]*(m[2][0]*m[3][3]-m[2][3]*m[3][0])+m[1][3]*(m[2][0]*m[3][2]-m[2][2]*m[3][0]))
    +m[0][2]*(m[1][0]*(m[2][1]*m[3][3]-m[3][1]*m[2][3])-m[1][1]*(m[2][0]*m[3][3]-m[3][0]*m[2][3])+m[1][3]*(m[2][0]*m[3][1]-m[2][1]*m[3][0]))
    -m[0][3]*(m[1][0]*(m[2][1]*m[3][2]-m[3][1]*m[2][2])-m[1][1]*(m[2][0]*m[3][2]-m[2][2]*m[3][0])+m[1][2]*(m[2][0]*m[3][1]-m[2][1]*m[3][0]))
    return det44val

#Matrix = [[3.00,5.21,6.33,1.66],[8.99,19.22,11.33,12.1],[3.44,5.66,18.22,11.34],[1.23,5.15,6.34,3.54]]
%timeit(det([[3.00,5.21,6.33,1.66],[8.99,19.22,11.33,12.1],[3.44,5.66,18.22,11.34],[1.23,5.15,6.34,3.54]]))
#625 loops, best of 3: 87.4 µs per loop
