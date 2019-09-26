import math

W = [
  '1' , '333', '999999999', '7777777', '4444' , '1', '22', '55555'
]

# W = [
#   '333', '4444', '999999999', '7777777', '22' , '1', '22', '55555'
# ]
# Sol = [
#   1, 333
#   999999999,
#   7777777,
#   4444, 1, 22
#   55555
# ]
# W = [
#    '999999999',
# ]
M = 10

def penalty(arr, i, j):
    # print(arr[i:j+1])
    cost = sum([len(arr[x]) for x in range(i, j+1)]) + (j - i) 
    # print(cost)
    if cost > M:
        p = math.inf
    else:
        p = (M - cost) ** 3
    #print(cost, M, p)
    return p     

def memo_text_justify4(words, n):
    memo = [-1] * n
    text_justify4(words, 0, n, memo)
    print(memo)

def text_justify4(words, i, n, memo):
    # print('i, n: ', i, n)
    if i == n:
        return 0
    if memo[i] != -1:
        return memo[i] 
    
    penalty_i_n = penalty(words, i, n-1)
    # if sinde the word[i:n] begins the last line
    if penalty_i_n != math.inf:
        memo[i] = 0
        return memo[i]
    
    memo[i] = math.inf 
    for j in range(i, n):
        
        penalty_i_j = penalty(words, i, j)
        # if penalty is infinity then that j breaks the line
        if penalty_i_j == math.inf:
            break
        new_penalty = penalty_i_j + text_justify4(words, j+1, n, memo)
        if (memo[i] > new_penalty):
            memo[i] = new_penalty    
    return memo[i]

print(W)
memo_text_justify4(W, len(W))