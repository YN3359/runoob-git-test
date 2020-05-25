from selenium import webdriver
from time import sleep
import pandas as pd
tb=pd.read_table('D:\\PythonTest\\123.txt',sep='|')
df=pd.DataFrame(tb)
driver=webdriver.Chrome()
sleep(5)
driver.get('http://code.vidc.info/subPage/login.aspx')
driver.find_element_by_id("UserName").send_keys("hx271014u006")
driver.find_element_by_id("Password").send_keys("Jzw123654.Ab1!")
driver.find_element_by_id("loginButton").click()
str=driver.get_cookies()
cookie1=str[0]['value']
cookie2=str[1]['value']
driver.add_cookie({'name':'td_cookie','value':cookie1})
driver.add_cookie({'name':'ASP.NET_SessionId','value':cookie2})
driver.get('http://code.vidc.info/subPage/content.aspx')
for index,row in df.iterrows():
        text=row[0]
        if text[3]=='5': #专用类车型
                print(index)
                driver.find_element_by_id("Basis_sccmc").send_keys("3401027")
                driver.find_element_by_id("Basis_Country").send_keys("中国")
                driver.find_element_by_id("Item_U00009").send_keys("国产")
                sleep(1)
                driver.find_element_by_id("type1").send_keys("汽车")
                sleep(2)
                driver.find_element_by_id("type2").send_keys("专用车")
                sleep(2)
                driver.find_element_by_id("type3").send_keys("运输类专用汽车")
                driver.find_element_by_id("Item_A00003").send_keys("江淮牌")
                driver.find_element_by_id("Item_U00010").send_keys("是")
                driver.find_element_by_id("Item_CA0006").send_keys(row[0])	#车辆型号
                driver.find_element_by_id("Item_CA0015").send_keys(row[1])	#车辆名称
                driver.find_element_by_id("Item_CA0012").send_keys(row[2])      #外廓长
                driver.find_element_by_id("Item_CA0013").send_keys(row[3])      #宽
                driver.find_element_by_id("Item_CA0014").send_keys(row[4])	#高
                driver.find_element_by_id("Item_CA0008").send_keys(row[7])	#发动机型号
                driver.find_element_by_id("Item_CA0009").send_keys(row[9])	#发动机功率
                driver.find_element_by_id("Item_CA0019a").send_keys(row[8])	#燃料种类
                driver.find_element_by_id("Item_CA0018").send_keys(row[6])	#轴数
        elif text[3]=='4': #牵引类车型
                print(index)
                driver.find_element_by_id("Basis_sccmc").send_keys("3401027")
                driver.find_element_by_id("Basis_Country").send_keys("中国")
                driver.find_element_by_id("Item_U00009").send_keys("国产")
                sleep(1)
                driver.find_element_by_id("type1").send_keys("汽车")
                sleep(2)
                driver.find_element_by_id("type2").send_keys("货车")
                sleep(2)
                driver.find_element_by_id("type3").send_keys("半挂牵引车")
                driver.find_element_by_id("Item_A00003").send_keys("江淮牌")
                driver.find_element_by_id("Item_U00010").send_keys("是")
                driver.find_element_by_id("Item_CA0006").send_keys(row[0]) 	#车辆型号
                driver.find_element_by_id("Item_CA0015").send_keys(row[1]) 	#车辆名称	
                driver.find_element_by_id("Item_CA0012").send_keys(row[2])		#外廓长
                driver.find_element_by_id("Item_CA0013").send_keys(row[3])		#宽
                driver.find_element_by_id("Item_CA0014").send_keys(row[4])		#高
                driver.find_element_by_id("Item_CA0008").send_keys(row[7])		#发动机型号
                driver.find_element_by_id("Item_CA0009").send_keys(row[9])	#发动机功率
                driver.find_element_by_id("Item_CA0019a").send_keys(row[8])	#燃料种类
                driver.find_element_by_id("Item_CA0018").send_keys(row[6])
                s=int(row[5])
                driver.find_element_by_id("Item_CA0017").send_keys(s)
        else:               #载货自卸类车型
                print(index)
                driver.find_element_by_id("Basis_sccmc").send_keys("3401027")
                driver.find_element_by_id("Basis_Country").send_keys("中国")
                driver.find_element_by_id("Item_U00009").send_keys("国产")
                sleep(1)
                driver.find_element_by_id("type1").send_keys("汽车")
                sleep(1)
                driver.find_element_by_id("type2").send_keys("货车")
                sleep(1)
                driver.find_element_by_id("type3").send_keys("普通货车")
                driver.find_element_by_id("Item_A00003").send_keys("江淮牌")
                driver.find_element_by_id("Item_U00010").send_keys("是")
                driver.find_element_by_id("Item_CA0006").send_keys(row[0]) 	#车辆型号
                driver.find_element_by_id("Item_CA0015").send_keys(row[1]) 	#车辆名称	
                driver.find_element_by_id("Item_CA0012").send_keys(row[2])		#外廓长
                driver.find_element_by_id("Item_CA0013").send_keys(row[3])		#宽
                driver.find_element_by_id("Item_CA0014").send_keys(row[4])		#高
                driver.find_element_by_id("Item_CA0008").send_keys(row[7])		#发动机型号
                driver.find_element_by_id("Item_CA0009").send_keys(row[9])	#发动机功率
                driver.find_element_by_id("Item_CA0019a").send_keys(row[8])	#燃料种类
                driver.find_element_by_id("Item_CA0018").send_keys(row[6])
                s=int(row[5])
                driver.find_element_by_id("Item_CA0016").send_keys(s)
                
        driver.find_element_by_id("Button_save").click()
        sleep(3)
        alert=driver.switch_to.alert #处理完成备案后的弹出框，自动确认
        alert.accept()
        sleep(2)
        driver.get('http://code.vidc.info/subPage/content.aspx') #重新定位到备案填写界面
        sleep(2)

print("完成备案")
                
