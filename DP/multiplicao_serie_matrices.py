import math

def memoized_matrix_chain_order(p, n):
    w, h = n, n
    memo = [[math.inf for i in range(w)] for j in range(h)]
    best_parentization = [[-1 for i in range(w)] for j in range(h)]
    return lookup_chain(p, 0, n-1, memo, best_parentization)

def lookup_chain(p, i, j, memo, best_parentization):
    if memo[i][j] < math.inf:
        return memo[i][j]
    if i == j:
        memo[i][j] = 0
    else:
        for k in range(i,j):
            m1, best_parentization = lookup_chain(p, i, k, memo, best_parentization)
            m2, best_parentization = lookup_chain(p, k+1, j, memo, best_parentization)
            mult =  m1 + m2 + p[i-1]*p[k]*p[j]
            if mult < memo[i][j]:
                memo[i][j] = mult
                best_parentization[i][j] = k    
    print(best_parentization)
    return memo[i][j], best_parentization

p = [10, 10, 20, 30, 10, 15, 30]
n = 6

multiplications_quantity, best_parentization = memoized_matrix_chain_order(p, n)
print("Minimum quantity of multiplications: ", multiplications_quantity)

def list_chain_order(best_parentization, n):
    i, j = n-1, n-1
    chain_order = []
    while(i>=0 and j>=0):
        k = list_chain_order[i][j]
        print('('+i+','+k+')  e  ('+(k+1)+','+j+')')

print(list_chain_orden(best_parentization, n))        
