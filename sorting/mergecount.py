def intercala(A,B, count):
    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            count = count + len(A) - i
            C.append(B[j])
            j += 1
    C = C + A[i:] + B[j:]
    return C, count

def mergecount(L, cont):
    if len(L) == 1:
        return L, 0
    C = []    
    q = len(L)//2
    # print('p,r,q: ', p, r, q)
    A, a_cont = mergecount(L[:q], cont)
    print(A, a_cont)
    B, b_cont = mergecount(L[q:], cont)
    print(B, b_cont)
    C, c_cont = intercala(A, B, (a_cont+b_cont))
    print(C, c_cont)
    return C, c_cont

# A = [2, 6, 10, 14]
# B = [5, 8, 11, 15]
# C = intercala(A, B)
# print(C)
L = [5, 2, 3, 6, 1, 9, 4]
C, invertions = mergecount(L, 0)
print(C, invertions)

