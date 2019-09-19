def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and (A[j] > key):
            A[j+1] = A[j]            
            j -= 1        
        A[j+1] = key
        # print(A)
    return A

A = [5,3,8,2,9,1,7]
A_sorted = insertion_sort(A)
print(A_sorted)

