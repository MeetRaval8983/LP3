"""A4: 0/1 knapsack using bottom-up dynamic programming."""
def knapsack(items,capacity):
    if capacity<0 or any(w<0 for _,w in items): raise ValueError('Weights and capacity must be nonnegative')
    n=len(items);dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i,(value,weight) in enumerate(items,1):
        for c in range(capacity+1):
            dp[i][c]=dp[i-1][c]
            if weight<=c: dp[i][c]=max(dp[i][c],value+dp[i-1][c-weight])
    c=capacity;selected=[]
    for i in range(n,0,-1):
        if dp[i][c]!=dp[i-1][c]:
            selected.append(i);c-=items[i-1][1]
    return dp[n][capacity],selected[::-1]
if __name__=='__main__':
    n=int(input('Items count [sample=3]: ') or '0')
    items=[(int(input('Value: ')),int(input('Integer weight: '))) for _ in range(n)] if n else [(60,10),(100,20),(120,30)]
    capacity=int(input('Integer capacity [50]: ') or '50')
    print('Maximum value, selected 1-based item indices:',knapsack(items,capacity))
