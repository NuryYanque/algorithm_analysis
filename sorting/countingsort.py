def countingsort(A,n,k):
    # fill array with zeros 10 times
    # complexity tetha(k)
    C = [0] * (k+1)
    # complexity tetha(n)
    for i in range(len(A)):        
        C[A[i]] += 1
    print('count: ', C)
    # accumulated of elementos for taking into account same numbers
    for i in range(2,k+1):
        C[i] = C[i] + C[i-1]    
    print('accum: ', C)
    B = [0] * len(A)
    # print(len(B), len(A))    
    for i in range(len(A)-1, 0, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1        
    return B

A = [3,4,2,1,4,5,7,3,9,10,5,3,6,2]
k = 10

# O(n+k)
B = countingsort(A,len(A),k)
print('sorted: ', B)
