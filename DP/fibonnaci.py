# top-down 
# recursion version
def memoized_fibonacci(n):
    memo = [-1] * (n+1)    
    return dp_fibonacci(n, memo)


def dp_fibonacci(n, memo):
    if memo[n] != -1:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = dp_fibonacci(n-1, memo) + dp_fibonacci(n-2, memo)
    return memo[n]
    
# f = memoized_fibonacci(9)
# print(f)


# bottom-up
# without recursion
def fibonacci(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibonacci(9))
