# O(n^2)

import math

W = [ '1' , '333', '999999999', '7777777', '4444' , '1', '22', '55555']
M = 10

sum_length_text = [0] * (len(W) + 1)

for i in range(0,len(W)):
  sum_length_text[i+1] = sum_length_text[i] + len(W[i])

def penalty(arr, i, j):    
    length_text = sum_length_text[j+1] - sum_length_text[i] + j - i    
    if length_text > M:
        p = math.inf
    else:
        p = (M - length_text) ** 3    
    return p     

def memo_text_justify4(words, n):
    memo = [-1] * n
    words_break_line = [-1] * n
    text_justify4(words, 0, n, memo, words_break_line)
    print(memo)
    print(words_break_line)
    break_ = 0
    while break_ < n:
        start, break_ = break_, words_break_line[break_]
        print(words[start:break_])

def text_justify4(words, i, n, memo, words_breaks):
    # print('i, n: ', i, n)
    if i == n:
        return 0
    if memo[i] != -1:        
        return memo[i] 
    
    penalty_i_n = penalty(words, i, n-1)
    # if sinde the word[i:n] begins the last line
    if penalty_i_n != math.inf:
        memo[i] = 0
        words_breaks[i] = n
        return memo[i]
    
    memo[i] = math.inf 
    for j in range(i, n):
        
        penalty_i_j = penalty(words, i, j)
        # if penalty is infinity then that j breaks the line
        if penalty_i_j == math.inf:
            break
        new_penalty = penalty_i_j + text_justify4(words, j+1, n, memo, words_breaks)
        if (memo[i] > new_penalty):
            memo[i] = new_penalty
            words_breaks[i] = j + 1
    return memo[i]

print(W)
memo_text_justify4(W, len(W))