def count(n):
    t=0
    ss=[]
    res=0
    for i in range(2,n+1):
        for j in range(1,i):
            if (i%j)==0:
                ss.append(j)
        for x in ss:
            t+=x
        if t==i:
            res=res+1
        else:
            t=0
            ss=[]
    return res

while True:
    
        n=int(input())
        if n<0 or n>500000:
            break
        res=count(n)
        print(res)

