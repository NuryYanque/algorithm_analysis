# top-down
def memoized_corte_hastes(n, pn):
    memo = [0] 
    memo.extend([-1 for i in range(n)])    
    return corte_hastes(n, pn, memo)

def corte_hastes(n, pn, memo):
    if memo[n] >= 0:
        return memo[n]    
    max_lucro = -1
    for i in range(1, n+1):       
        max_lucro = max(max_lucro, pn[i-1]+corte_hastes(n-i, pn, memo))            
        memo[n] = max_lucro
        print(memo)
    return max_lucro

n = 9
pn = [1, 5, 8, 9, 10, 17, 17, 20, 24]
# max_lucro = memoized_corte_hastes(4, pn)
# print(max_lucro)


# bottom - up
def corte_hastes_dp(n, pn):
    maxlucro_memo = [0]    
    for i in range(1, n+1):
        maximo_lucro = -1
        for j in range(1, i+1):
            maximo_lucro = max(maximo_lucro, pn[j-1]+maxlucro_memo[i-j])
        maxlucro_memo.append(maximo_lucro)
    print(maxlucro_memo)
    return maximo_lucro

# print(corte_hastes_dp(4, pn))

# recover the best cuts

def corte_hastes_dp(n, pn):
    maxlucro_memo = [0]
    best_cuts = [0] * (n+1)
    for i in range(1, n+1):
        maximo_lucro = -1
        for j in range(1, i+1):
            if maximo_lucro < pn[j-1]+maxlucro_memo[i-j]:
                maximo_lucro = pn[j-1]+maxlucro_memo[i-j]
                best_cuts[i] = j
        maxlucro_memo.append(maximo_lucro)
    print(maxlucro_memo)
    print(best_cuts)
    return maximo_lucro, best_cuts

maxlucro, bestcuts = corte_hastes_dp(4, pn)

print("Maximo Lucro: ", maxlucro)

def lista_cortes(bestcuts, n):
    if n == 0:
        return 0 
    if bestcuts[n] == n:
        return 0
    else:
        i = n
        cuts = []
        while(i > 0):
            cuts.append(bestcuts[i])
            i = i - bestcuts[i]        
        # append(lista_cortes(bestcuts,n-bestcuts[n]))             
        return cuts

print("Com os seguintes cortes: ", lista_cortes(bestcuts, 4))
