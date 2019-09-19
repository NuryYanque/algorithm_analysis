A = [4, 2, 8, 6, 3, 5]
def particione(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < pivot:            
            i += 1
            A[i], A[j] = A[j], A[i]
            # print('A[i], A[j]: ', A[i], A[j])
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

# print(particione(A, 0, len(A)-1))

def quicksort(A, low, high):
    if low < high:
        pivot = particione(A, low, high)
        print(A, pivot)
        quicksort(A, low, pivot-1)
        quicksort(A, pivot+1, high)
    # return L + R
    
quicksort(A, 0, len(A)-1)
print(A)