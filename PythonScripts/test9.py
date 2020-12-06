def clk(n):
    if n==0:
        return 1
    else:
        return (clk(n-1)+clk(n-3))

while True:
    
    n=int(input())
    print(n)
    res=clk(n)
    print(res)


while True:
    try:
        m=int(input())
        n=int(input())
        c=0
        ss=[]
        for i in range(n):
            line=input()
            ss.append(line)
        ss.sort()
        for i in range(n-1):
            bj=ss[i].split()
            gw=ss[i+1].split()
            if int(gw[0])<int(bj[1]):
                c+=1
        if c==0:
            if n%m==0:
                res=int(n/m)
            else:
                res=int(n/m)+1        
        else:
            if n%m==0:
                qq=int(n/m)
                if (c+1) <= qq:
                    res=qq
                else:
                    res=c+1
            else:
                qq=int(n/m)+1
                if (c+1) <= qq:
                    res=qq
                else:
                    res=c+1
        print(res)
    except:
        break
