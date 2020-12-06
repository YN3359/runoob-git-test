import sys

def calculate(num):
    x=1
    while(abs(num-x*x*x)>0.01):
        x=(2*x+float(num)/x/x)/3
    
    return round(x,1)

if __name__=="__main__":
    try:
        while True:
            print("请输入一个整数")
            ss=int(sys.stdin.readline().strip())
            if ss==0:
                 break
            res=calculate(ss)
            
            print(res)
    except:
        pass
