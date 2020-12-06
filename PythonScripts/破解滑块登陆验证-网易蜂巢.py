from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd

if __name__ == '__main__':

    driver=webdriver.Chrome()
    sleep(1)
    driver.get('https://id.163yun.com/login?h=fc&referrer=https%3A%2F%2Fc.163.com%2Flogin%2Fcallback%3Fredirect%3D')
    driver.find_element_by_xpath('//*[@id="bg"]/div[2]/div/div/div/div/div[2]/form/div[1]/div/input').send_keys('13739232860')
    driver.find_element_by_xpath('//*[@id="bg"]/div[2]/div/div/div/div/div[2]/form/div[2]/div/input').send_keys('yjy0819NN-')
    driver.find_element_by_xpath('//*[@id="bg"]/div[2]/div/div/div/div/div[2]/form/div[3]/div/div/div[1]/div[1]/span').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="bg"]/div[2]/div/div/div/div/div[2]/form/div[6]/button').click()
    sleep(1)
