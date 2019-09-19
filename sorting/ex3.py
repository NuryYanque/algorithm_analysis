def intercala(a, b, cont):
    i = 0
    j = 0
    A = []
    # cont = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            A.append(a[i])
            i += 1
            # cont += (j+1)
        else:
            A.append(b[j])
            cont += (j+1)
            j += 1            
    A = A + a[i:] + b[j:]
    return A, cont

def mergeSort(C, cont):    
    if len(C) == 1:
        return C, 0        
    B = []
    q = len(C) // 2
    a, cont_a = mergeSort(C[:q], cont)
    print("a: ", a, cont_a)    
    b, cont_b = mergeSort(C[q:], cont)
    print("b: ", b, cont_b)
    B, cont = intercala(a, b, (cont_a + cont_b))    
    print("B: ", B, cont)
    return B, cont
    
#c = [4, 5, 10, 2, 1, 3,3, 6, 8]
c = [4, 2, 5, 3, 6, 1]
B, count = mergeSort(c, cont=0)
print(B)
print(count)

# a = [4, 5, 10]
# b = [1, 2, 3, 6]
c = [4, 5, 10, 2, 1, 3, 6, 8]
a = [4, 5]
b = [2, 10]
# print(intercala(a, b, cont=0))

# cont = 0
# mergeSort(c, cont=0)
#print(A)
