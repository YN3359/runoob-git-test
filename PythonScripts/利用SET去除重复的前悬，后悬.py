import pandas as pd
import xlwt

workbook=xlwt.Workbook()
sheet=workbook.add_sheet('test')

tb=pd.read_table('D:\\PythonTest\\dic.txt',sep='|')
df=pd.DataFrame(tb)
listQ=[]
listH=[]
qianX=set()
houX=set()

for index,row in df.iterrows():
    i = 0
    #print('..........')
    for x in row:
        if pd.isna(x):
            break
        else:
            if i%2==0:
                qianX.add(str(int(x)))
                #print(qianX)
                i += 1
            else:
                houX.add(str(int(x)))
                #print(houX)
                i+=1
    listQ.append(','.join(qianX))
    listH.append(','.join(houX))
    qianX.clear()
    houX.clear()

s=len(listQ)
i = 0
j = 0
#将数据写入EXCEL
while(i<s):
    sheet.write(j, 0, listQ[i])
    sheet.write(j, 1, listH[i])
    i+=1
    j+=1
workbook.save('C:\\Users\\20142266\\Desktop\\test.xls')