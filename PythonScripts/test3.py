import sys

def contZ(n):
    s=0
    while(n>0):
        com=str(n*n)
        if com.endswith(str(n)):
            s+=1
        n=n-1
    return s

while True:
    try:
        n=int(input())
        if n<0:
            break
        res=contZ(n)
        print(res)
    except:
        break


import sys

def judge(i,j,num):
    if 

while True:
    num1=[]
    num2=[]
    num3=[]
    try:
        n=int(input())
        if n<=0:
            break
        else:
            line=map(int, input().split())
        for i in line:
            if i%5==0:
                num1.append(i)
            elif i%3==0:
                num2.append(i)
            else:
                num3.append(i)
        l5=sum(num1)
        l3=sum(num2)
        
    except:
        break
