"""A3: Greedy fractional knapsack using value/weight ratio."""
def fractional_knapsack(items,capacity):
    if capacity<0 or any(w<=0 for _,w in items): raise ValueError('Capacity >=0 and weights >0 required')
    value=0.0; chosen=[]
    for i,(v,w) in sorted(enumerate(items,1),key=lambda x:x[1][0]/x[1][1],reverse=True):
        if capacity<=0: break
        fraction=min(1.0,capacity/w)
        value+=v*fraction;capacity-=w*fraction
        chosen.append((i,round(fraction,4)))
    return value,chosen
if __name__=='__main__':
    n=int(input('Number of items [sample=3]: ') or '0')
    items=[(float(input('Value: ')),float(input('Weight: '))) for _ in range(n)] if n else [(60,10),(100,20),(120,30)]
    capacity=float(input('Capacity [50]: ') or '50')
    print('Maximum value and (item, fraction):',fractional_knapsack(items,capacity))
