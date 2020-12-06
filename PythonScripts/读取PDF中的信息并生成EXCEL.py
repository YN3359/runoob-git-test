import pdfplumber
import xlwt
import re

def extractPDF():
    #文本文档路径
    txtPath='C:\\Users\\20142266\\Desktop\\test.txt'
    file_handle1=open(txtPath,'w')
    # PDF路径
    pdfPath='C:\\Users\\20142266\\Desktop\\第九批.pdf'
    content=''
    #先提取PDF数据导文本文档
    with pdfplumber.open(pdfPath) as pdf:
        pages=pdf.pages
        for page in pages:
            text = page.extract_text()
            content+=text

        file_handle1.write(content)
        file_handle1.close()
    #去掉文档中的空行和空格,并在指定位置生成完成版TXT
    dirPath='C:\\Users\\20142266\\Desktop\\test2.txt'
    with open(txtPath, 'r') as fr, open(dirPath, 'w') as fd:
        for text in fr.readlines():
            if text.split():
                fd.write(text)
        fr.close()
        fd.close()

def txtToExcel():
    dirPath = 'C:\\Users\\20142266\\Desktop\\test2.txt'
    txt1 = open(dirPath, 'r')
    text = ''
    #生成EXCEL
    workbook=xlwt.Workbook()
    sheet=workbook.add_sheet('test')
    j=1
    #将数据去掉换行符等
    for line in txt1.readlines():
        line = line.strip()
        line = line.strip('  ')
        line = line.replace('  ', '')
        line = line.strip('\n')
        line = line.strip('\r\n')
        line = line.strip('\r')
        text += line

    text1 = re.split('车辆基本信息|、', text)
    s = len(text1)
    print(s)
    i = 0
    #将数据写入EXCEL
    while(i<s):
        sheet.write(j, 0, text1[i])
        j+=1
        #print(text1[i])
        #根据批次替换strLike
        strLike='变更扩展车型注：*表示当批发生变更或扩展的配置(一) 符合' \
                     '《关于完善新能源汽车推广应用财政补贴政策的通知》（财建〔2020〕86号）' \
                     '产品技术要求的新能源车型1'
        if text1[i]==strLike:
            i=i+1
        else:
            i+=2
    #保存
    workbook.save('C:\\Users\\20142266\\Desktop\\test.xls')
    txt1.close()

if __name__ == '__main__':
    extractPDF()
    txtToExcel()

