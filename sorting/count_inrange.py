def count_inrange(A,k,a,b):
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
    query = C[b] - C[a-1]
    return query

A = [3,4,2,1,4,5,7,3,9,10,5,3,6,2]
k = 10

query = count_inrange(A,10,5,5)
print(query)
