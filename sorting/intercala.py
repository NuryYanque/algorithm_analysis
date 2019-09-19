def intercala(A,B):
    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C = C + A[i:] + B[j:]
    return C

A = [[2, 6, 10, 14], 
     [5, 8, 11, 15], 
     [4, 7, 13, 17],
     [3, 9, 12, 16]]
def intercala_klistas(n, k, A):
    # print(len(A), A)
    if len(A) == 1:
        return A[0]
    q = len(A)//2
    L = intercala_klistas(n, k , A[:q])
    print('L: ', L)
    R = intercala_klistas(n, k, A[q:])
    print('R: ', R)
    C = intercala(L, R)
    print(C)
    return C

print(intercala_klistas(16, 4, A))

