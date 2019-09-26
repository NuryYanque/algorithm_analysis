import math
def memoized_longest_increase_subseq(v, n):
    memo = [-1] * n
    longest_increase_subseq(v, n-1, memo)
    print(max(memo))
    # print(print_longest_increase_subseq(memo, v, n))
    # print(size_lis)
    # print_

# n^2
def longest_increase_subseq(v, k, memo):    
    if memo[k] != -1:
        return memo[k]
    # array with one element
    if k == 0:
        # memo[0] = 1
        return 1
    # maximo = -math.inf
    memo[k] = 1
    for i in range(k-1, 0, -1):
        # print(i, k, memo[k])
        lis_i = longest_increase_subseq(v, i, memo)
        # maximo = max(maximo, lis_i)
        if v[k] > v[i]:
            memo[k] = max(memo[k], 1 + lis_i)
    return memo[k]

v = [8,1,9,8,3,4,6,1,5,2]
print(v)
memoized_longest_increase_subseq(v,len(v))

# n^3
def longest_increase_subseq2(v, k, memo):    
    if memo[k] != 0:
        return memo[k]
    # array with one element
    if k == 0:
        memo[0] = 1
        return 1
    for i in range(k+1):
        memo[i] = 1
        for j in range(i):
            if v[i] > v[j]:
                memo[i] = max(memo[i], 1 + longest_increase_subseq(v, j, memo))                
    return max(memo)
                
def print_longest_increase_subseq(memo, v, n):
    index_lis = memo.index(max(memo))    
    lis = [v[index_lis]]
    for i in range(index_lis-1, 0, -1):
        if(memo[index_lis] - memo[i] == 1):
            lis.append(v[i])
            index_lis = i    
    return lis[::-1]


# Function to get index of ceiling of x in arr[low..high]*/ 
def ceilSearch(arr, low, high, x): 
      
    if x <= arr[low]: 
        return low  
     
    if x > arr[high]: 
        return -1  
      
    mid = (low + high)//2;  # low + (high - low)/2 */ 
      
    if arr[mid] == x: 
        return mid 
      
    elif arr[mid] < x: 
        if mid + 1 <= high and x <= arr[mid+1]: 
            return mid + 1
        else: 
            return ceilSearch(arr, mid+1, high, x)     
    else: 
        if mid - 1 >= low and x > arr[mid-1]: 
            return mid 
        else: 
            return ceilSearch(arr, low, mid - 1, x)

def longest_increase_subseq_nlogn(sequence, n):
    # 10000 is a large value close to infinity
    I = [10000] * (n + 1)
    # init in -infinity
    I[0] = -10000
    L = [0] * n
    lenI = 1
    for i in range(n):
        if sequence[i] > I[lenI - 1]:
            I[lenI] = sequence[i]
            L[i] = lenI
            lenI += 1
        elif sequence[i] < I[1]:
            I[1] = sequence[i]
            L[i] = 1
        # between the minor and greater
        else:
            pos = ceilSearch(I, 0, lenI - 1, sequence[i])
            I[pos] = sequence[i]
            L[i] = pos
    return L

# v = [3,1,4,2,-1,1,5,8]
# v = [1, 2, 4, 5, 3]
# v = [8,1,9,8,3,4,6,1,5,2]
# print(v)
# # memoized_longest_increase_subseq(v,len(v))

# lis_sizes = longest_increase_subseq_nlogn(v,len(v))
# lis_array = print_longest_increase_subseq(lis_sizes, v, len(v))
# print(lis_array)
