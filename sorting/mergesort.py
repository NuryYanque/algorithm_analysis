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

def mergesort(L):
    if len(L) == 1:
        return L
    C = []    
    q = len(L)//2
    # print('p,r,q: ', p, r, q)
    A = mergesort(L[:q])
    B = mergesort(L[q:])
    C = intercala(A, B)
       
    return C

# A = [2, 6, 10, 14]
# B = [5, 8, 11, 15]
# C = intercala(A, B)
# print(C)
L = [5, 2, 3, 6, 1, 9, 4]
C = mergesort(L)
print(C)

