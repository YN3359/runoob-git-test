import sys

while True:
    line=sys.stdin.readline().strip()
    if len(line)==0:
            break
    st=[int(n) for n in line.split(' ')]
    s1=0
    ave=0.0
    t=0
    k=0
    for s in st:
        if s < 0:
                t=t+1
        else:
                s1=s1+s
                k=k+1
                
    if k>0:
        ave=round(s1/k,1)
        
    print(t)
    print(ave)


while True:
    try:
        n=int(input())
        if n:
            num=[int(v) for v in input().split()]
            conl=int(input())
            if conl==0:
                num.sort()
            else:
                num.sort(reverse=True)
            for i in num:
                print(i)
            
        else:
            break 
    except:
        pass
