"""A2: Greedy unit-time job sequencing to maximize profit."""
def schedule(jobs):
    jobs=sorted(jobs,key=lambda j:j[2],reverse=True)
    slots=[None]*min(len(jobs),max((j[1] for j in jobs),default=0))
    for job in jobs:
        name,deadline,profit=job
        if deadline<=0 or profit<=0: continue
        for i in range(min(deadline,len(slots))-1,-1,-1):
            if slots[i] is None:
                slots[i]=job
                break
    return [j[0] if j else '-' for j in slots],sum(j[2] for j in slots if j)
if __name__=='__main__':
    sample=[('J1',2,100),('J2',1,19),('J3',2,27),('J4',1,25),('J5',3,15)]
    count=int(input('Jobs count [sample=5]: ') or '0')
    jobs=[(input('Job ID: '),int(input('Deadline: ')),float(input('Profit: '))) for _ in range(count)] if count else sample
    print('Scheduled slots and total profit:',schedule(jobs))
