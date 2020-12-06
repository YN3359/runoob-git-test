from selenium import webdriver
from time import sleep
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pandas as pd

if __name__ == '__main__':
    # option=webdriver.ChromeOptions()
    # option.add_argument("--user-data-dir="+r"C:\\Users\\20142266\\AppData\\Local\\Google\\Chrome\\User Data")
    # driver = webdriver.Chrome(chrome_options=option)
    # sleep(2)
    driver = webdriver.Ie()
    #driver.get('chrome-extension://hehijbfgiekmjfkfjpbkbammjbdenadd/nhc.htm#url=http://tec.cqccms.com.cn/')
    driver.get('http://tec.cqccms.com.cn/')
    sleep(1)
    js = 'document.getElementById("submitButton").click()'
    driver.execute_script(js)
    sleep(1)
    #driver.find_element_by_id("submitButton").send_keys(Keys.ENTER)
    #testck.input_windows("核对数字证书口令","")
    ratio = driver.find_elements_by_tag_name("input")
    for a in ratio:
        if a.get_attribute('value') == '4005919':
            a.click()
        if a.get_attribute("type") == "submit":
            a.click()
    sleep(2)
    #str = driver.get_cookies()
    #print(str)
    #cookie1 = str[0]['value']
    #driver.add_cookie({'name': 'JSESSIONID', 'value': cookie1})
    URL = "http://tec.cqccms.com.cn/cocComplete!cocCompleteCreate.action?" \
          "id=201709291432251U8205&carType=HFC5181XXYP3K1A57S2QV&carCellCode" \
          "=2017011101011956&carTypeSeqCode=N36N&carCellId=5636338&collection" \
          "=A013551N36NZM95ZZEZ420000901@null@20201105173042786997%3B1@@1@0@5254506@1"
    driver.get(URL)
    myselect=driver.find_elements_by_tag_name("select")
    for i in myselect:
        if i.get_property("name")=="f3":
            try:
                Select(i).select_by_visible_text("5700")
            except selenium.common.exceptions.NoSuchElementException:
                Select(i).select_by_index(1)
        if i.get_property("name")=="f7":
            try:
                Select(i).select_by_visible_text("5700")
            except selenium.common.exceptions.NoSuchElementException:
                Select(i).select_by_index(1)



