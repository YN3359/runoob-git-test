from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd

if __name__ == '__main__':
    #从文本文档读入数据
    tb = pd.read_table('D:\\PythonTest\\123.txt', sep='|')
    df = pd.DataFrame(tb)

    #开启自动化填报
    driver=webdriver.Chrome()
    sleep(3)
    driver.get('https://ucenter.miit.gov.cn/login.jsp?toUrl=http%3A%2F%2Fhgz.miit.gov.cn%2Fenterprise%2Flogin')
    driver.find_element_by_id("name").send_keys("YJY20142266")
    driver.find_element_by_id("password").send_keys("qaz123wsx+-")
    driver.find_element_by_id("btn").click()
    sleep(1)
    #这步很关键，必须点掉弹窗才能输入验证码
    driver.switch_to.default_content()
    driver.find_element_by_class_name("layui-layer-btn0").click()
    s=input("请输入验证码：")
    driver.find_element_by_id("yznum").send_keys(s)
    driver.find_element_by_id("subbtn").click()
    sleep(2)
    #先get再add
    str = driver.get_cookies()
    print(str)
    cookie1 = str[0]['value']
    driver.add_cookie({'name': 'cssSessionId', 'value': cookie1})
    #点掉提示窗
    driver.find_element_by_class_name("publicNotice_close").click()
    #进入备案界面，才用xpath定位方式
    driver.find_element_by_xpath("//div[text()=\"配置信息\"]").click()

    driver.get("http://hgz.miit.gov.cn/#/admin/Configuration-information-list")
    sleep(1)
    driver.get("http://hgz.miit.gov.cn/#/admin/apply-config-list")
    sleep(1)
    print("开始备案配置序列号：")
    
    for index, row in df.iterrows():
        text = row[0]
        #实时打印备案到哪一行，方便查看
        print((index+1))
        #载货类
        if text[3]=="1" or text[3]=="3":
            # 大类
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[1]").send_keys("汽车")
            sleep(1)
            #中类
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[2]").send_keys("货车")
            sleep(1)
            #小类
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[3]").send_keys("普通货车")
            sleep(2)
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[5]/div[2]/input").send_keys(row[0])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[5]/div[4]/input").send_keys(row[1])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[6]/div[4]/select").send_keys("国产")
            inputx =driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[6]/div[2]/div/div/input")
            #tkey="安徽江淮汽车集团股份有限公司重型车分公司"
            #driver.execute_script("arguments[0].value=arguments[1]",inputx, tkey)
            sleep(1)
            inputx.click()
            sleep(2)
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()
            sleep(1)
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[7]/div[2]/select").send_keys("江淮牌")
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[1]/div[4]/input").send_keys(row[7])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[2]/div[2]/input").send_keys(row[9])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[4]/div[4]/input").send_keys(row[10])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[2]/div[4]/input").send_keys(row[2])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[3]/div[2]/input").send_keys(row[3])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[3]/div[4]/input").send_keys(row[4])
            s = int(row[5])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[4]/div[2]/input").send_keys(s)
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[11]/div[2]/select").send_keys(row[6])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[12]/div[2]/select[1]").send_keys(row[8])
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[27]/div[2]/select").send_keys("非新能源")
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[2]/span[4]").click()
            sleep(2)
        #牵引
        elif text[3] == '4':
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[1]").send_keys(
                "汽车")
            sleep(1)
            # 中类
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[2]").send_keys(
                "货车")
            sleep(1)
            # 小类
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[3]").send_keys(
                "半挂牵引车")
            sleep(2)
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[5]/div[2]/input").send_keys(row[0])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[5]/div[4]/input").send_keys(row[1])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[6]/div[4]/select").send_keys("国产")
            inputx = driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[6]/div[2]/div/div/input")
            #tkey = "安徽江淮汽车集团股份有限公司重型车分公司"
            #driver.execute_script("arguments[0].value=arguments[1]", inputx, tkey)
            inputx.click()
            sleep(2)
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()
            sleep(2)
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[7]/div[2]/select").send_keys("江淮牌")
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[1]/div[4]/input").send_keys(row[7])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[2]/div[2]/input").send_keys(row[9])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[4]/div[4]/input").send_keys(row[10])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[2]/div[4]/input").send_keys(row[2])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[3]/div[2]/input").send_keys(row[3])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[3]/div[4]/input").send_keys(row[4])
            s = int(row[5])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[4]/div[2]/input").send_keys(s)
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[11]/div[2]/select").send_keys(
                row[6])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[12]/div[2]/select[1]").send_keys(
                row[8])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[27]/div[2]/select").send_keys(
                "非新能源")
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[2]/span[4]").click()
            sleep(2)
        #专用类
        else:
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[1]").send_keys(
                "汽车")
            sleep(1)
            # 中类
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[2]").send_keys(
                "专用车")
            sleep(1)
            # 小类
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[2]/div[2]/select[3]").send_keys(
                "运输类专用车")
            sleep(2)
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[5]/div[2]/input").send_keys(row[0])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[5]/div[4]/input").send_keys(row[1])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[6]/div[4]/select").send_keys("国产")
            inputx = driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[6]/div[2]/div/div/input")
            tkey = "安徽江淮汽车集团股份有限公司重型车分公司"
            #driver.execute_script("arguments[0].value=arguments[1]", inputx, tkey)
            sleep(1)
            inputx.click()
            sleep(2)
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()
            sleep(2)
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[3]/div[7]/div[2]/select").send_keys("江淮牌")
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[1]/div[4]/input").send_keys(row[7])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[2]/div[2]/input").send_keys(row[9])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[5]/div[2]/input").send_keys(row[10])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[2]/div[4]/input").send_keys(row[2])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[3]/div[2]/input").send_keys(row[3])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[3]/div[4]/input").send_keys(row[4])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[11]/div[2]/select").send_keys(
                row[6])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[12]/div[2]/select[1]").send_keys(
                row[8])
            driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div/section/section/div/div/div/div[1]/div[5]/div[27]/div[2]/select").send_keys(
                "非新能源")
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/div/div/div/div[2]/span[4]").click()
            sleep(2)
            
        driver.get("http://hgz.miit.gov.cn/#/admin/Configuration-information-list")
        sleep(1)
        driver.get("http://hgz.miit.gov.cn/#/admin/apply-config-list")
        sleep(1)
    #完成备案后打印
    print("完成备案")
