# coding = utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os

option = webdriver.EdgeOptions()

option.binary_location = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
edge_driver_binary = "D:\BaiduNetdiskDownload\msedgedriver\msedgedriver\msedgedriver.exe"
driver = webdriver.edge(options=option)
driver.get("http://www.baidu.com")
sleep(2)
driver.find_element(by=By.ID,value="kw").send_keys("Test")
driver.find_element(by=By.ID,value="su").click()
sleep(2)
driver.quit()