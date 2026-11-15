"""A1: Fibonacci sequence; count loop iterations as computational steps."""
def fibonacci(n):
    a,b=0,1
    result=[]
    steps=0
    for _ in range(n):
        result.append(a)
        a,b=b,a+b
        steps+=1
    return result,steps
if __name__=='__main__':
    n=int(input('Number of terms [10]: ') or '10')
    if n<0: raise ValueError('Number of terms must be nonnegative')
    sequence,steps=fibonacci(n)
    print('Fibonacci:',sequence)
    print('Loop steps:',steps,'Time complexity: O(n)')