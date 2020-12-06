import threading
 
def printA(result):
    result.append('A')
def printB(result):
    result.append('B')
def printC(result):
    result.append('C')
def printD(result):
    result.append('D')
while True:
    try:
        result = []
        n = int(input())
        for i in range(n):
            t1 = threading.Thread(target=printA(result))
            t2 = threading.Thread(target=printB(result))
            t3 = threading.Thread(target=printC(result))
            t4 = threading.Thread(target=printD(result))
            t1.start()
            t1.join()
            t2.start()
            t2.join()
            t3.start()
            t3.join()
            t4.start()
            t4.join()
        print ("".join(result))
    except:
        break
