while True:
    
        dic={}
        n=int(input())
        for i in range(n):
            k,v=map(int,input().split())
            if k in dic.keys():
                dic[k]=dic[k]+v
                print(dic[k])
            else:
                dic[k]=v
                print(dic[k])
        for k,v in dic.items():
            print('{} {}'.format(k, v))


while True:
    try:
        n=int(input())
        ss=[]
        for i in range(n):
            st1=input()
            ss.append(st1)
        for line in ss:
            length=len(line)
            if length<8:
                line=line+(8-length)*'0'
                print(line)
            elif length==8:
                print(line)
            else:
                m=length%8
                s=int(length/8)
                last=line[(8*s):8*s+m]+(8-m)*'0'
                for j in range(s):
                    print(line[(8*j):(8*j+8)])
                print(last)
    except:
        break
