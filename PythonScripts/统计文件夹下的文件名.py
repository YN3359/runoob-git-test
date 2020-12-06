import os
import xlwt
import sys
import xlrd

def duqv(path,te):
    for i,j,k in os.walk(path):
        for file in k:
            te.append(os.path.splitext(file)[0])

if __name__=='__main__':
    f=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=f.add_sheet('统计文件')
    i=0
    filepath='D:\\接收\\yjy2\\召回\\国五召回\\新建文件夹'
    le=[]
    duqv(filepath,le)
    for s in le:
        sheet.write(i,0,s)
        i+=1
    f.save('C:\\Users\\20142266\\Desktop\\123.xls')
