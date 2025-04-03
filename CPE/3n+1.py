cache = {1: 1}

def collatz_length(n):
    N=n
    c_l=1
    if n in cache:
        return cache[n]
    
    while True:
        if n==1:
            cache[N]=c_l
            break

        if(n%2==1):
            n=3*n+1
            c_l+=1

        else:
            n=n//2
            c_l+=1
    return cache[N]

while True:
    try:
        a,b=map(int,input().split())
        maxC_L=0
        c=a
        d=b
        if b<a:
            c=b
            d=a
        
        for i in range(c,d+1):
            l=collatz_length(i)
            if(maxC_L<l):           
                maxC_L=l
                    
        print(a,b,maxC_L)
        
    except EOFError:
        break
    