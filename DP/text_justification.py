import math

# W = [
#   '1' , '333', '999999999', '7777777', '4444' , '1', '22', '55555'
# ]

W = [
  '333', '4444', '999999999', '7777777', '22' , '1', '22', '55555'
]


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
    print(arr[i:j+1])
    cost = sum([len(arr[x]) for x in range(i, j+1)]) + (j - i) 
    # print(cost)
    if cost > M:
        p = math.inf
    else:
        p = (M - cost) ** 3
    print(cost, M, p)
    return p 
    # print(penalty(4, 7))

def memo_text_justify4(words, n):
    memo = [-1] * n
    text_justify4(words, 0, n, memo)
    print(memo)

def text_justify4(words, i, n, memo):
    print('i, n: ', i, n)
    if (memo[i] != -1):
        return memo[i]
    if i == (n-1):
        return 0
    min_penalty = math.inf
    for j in range(i+1, n):
        # print(n, i, j)
        new_penalty = penalty(words, i, j) + text_justify4(words,j,n,memo)
        if  new_penalty < min_penalty:
            min_penalty = new_penalty
        # memo[i] = min(memo[j], )
    memo[i] = min_penalty
    print('memo:', i, memo[i])
    return min_penalty
print(W)
memo_text_justify4(W, len(W))

#   if p >= 0:
#     if i == len(words) - 1: 
#       numLine += 1
#       p = 0
#     memo[i] = p
#     pos[i] = numLine 
#     return p
#   elif p < 0:
#     memo[i] = math.inf
#     numLine += 1
#     for k in range(i, len(words)):
#       p2 = penalty(words, i, k)
#       if p2 < 0:
#         break
#       memo[i] = min(memo[i], p2 + text_justify3(words, k + 1, memo, pos, numLine))
#       pos[k] = numLine
    
#   return memo[i]

# def memo_text_justify(words, n):
#   memo = [[math.inf for i in range(n)] for j in range(n)]
#   return text_justify(words, 0, n-1, memo)


def memo_text_justify2(words, n):
  memo = [[math.inf for i in range(n)] for j in range(n)]
  print(text_justify2(words, 0, n - 1, n - 1, memo))
  for x in memo:
    print(x)

def memo_text_justify3(words, n):
  memo = [math.inf for i in range(n)]
  pos = [math.inf for i in range(n)]

  print(text_justify3(words, 0, memo, pos, 0))
  print(memo)
  print(pos)

  index = 0
  sol = [[words[index]]]
  for i in range(1, len(pos)):
    if (pos[i] > pos[index]):
      sol.append([words[i]])
      index = i
    else:
      sol[len(sol) - 1].append(words[i])
  
  for x in sol:
    print(' '.join(x))


# def text_justify(words, i, j, memo):
#   if memo[i][j] != math.inf: return memo[i][j]
#   d = sum([len(words[x]) for x in range(i, j + 1)]) + j - i
#   if M >= d:
#     memo[i][j] = 0
#   else:
#     for k in range(i,j+1):
#       memo[i][k] = min(memo[i,k], penalty(i, k) + text_justify(words[k+1:j+1], k+1, j, memo))
#   print(memo)

# def text_justify2(words, i, j, lenW, memo):
#   if memo[i][j] != math.inf: return memo[i][j]
#   p = penalty(words, i, j)
#   if p >= 0:
#     if j == lenW: 
#       p = 0
#     memo[i][j] = p
#     return p
#   elif p < 0:
#     memo[i][j] = math.inf
#     for k in range(i,j + 1):
#       p2 = penalty(words, i, k)
#       if p2 < 0: break
#       memo[i][j] = min(memo[i][j], p2 + text_justify2(words, k + 1, j, lenW, memo))
#   return memo[i][j]

def text_justify3(words, i, memo, pos, numLine):
  if (memo[i] != math.inf):
    return memo[i]

  p = penalty(words, i, len(words) - 1)
  if p >= 0:
    if i == len(words) - 1: 
      numLine += 1
      p = 0
    memo[i] = p
    pos[i] = numLine 
    return p
  elif p < 0:
    memo[i] = math.inf
    numLine += 1
    for k in range(i, len(words)):
      p2 = penalty(words, i, k)
      if p2 < 0:
        break
      memo[i] = min(memo[i], p2 + text_justify3(words, k + 1, memo, pos, numLine))
      pos[k] = numLine
    
  return memo[i]

# memo_text_justify2(W, len(W))

# memo_text_justify3(W, len(W))