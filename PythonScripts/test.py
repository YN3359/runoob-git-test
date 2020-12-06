import sys

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

while True:
    n=sys.stdin.readline().strip()
    if n:
        n=n.split(' ')
        if len(n)>1 :
            a=int(n[0])
            b=int(n[1])
            print(a*b//gcd(a, b))
    else:
        break
    
    
    
