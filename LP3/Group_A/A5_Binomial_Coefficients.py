"""A5: Binomial coefficient C(n,k) using Pascal's triangle DP."""
def choose(n,k):
    if n<0 or k<0 or k>n: raise ValueError('Require 0 <= k <= n')
    row=[0]*(k+1);row[0]=1
    for i in range(1,n+1):
        for j in range(min(i,k),0,-1): row[j]+=row[j-1]
    return row[k]
if __name__=='__main__':
    n=int(input('n [5]: ') or '5');k=int(input('k [2]: ') or '2')
    print(f'C({n},{k}) = {choose(n,k)}')
