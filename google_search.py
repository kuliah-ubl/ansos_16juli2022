# Created by Muhamad Syafii
# Kelp : SI Magister
# Saturday, 16/07/2022
# Copyright (c) 2022 by Univ Budi Luhur
# All Rights Reserved


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#set chromedriver.exe path
# driver = webdriver.Chrome(executable_path='../drivers/chromedriver') #this is not use
driver = webdriver.Chrome(ChromeDriverManager().install()) #using code here
#url launch
driver.get("http://google.com")
#identify edit box with name
driver.implicitly_wait(30)
driver.find_element(By.NAME, "q").send_keys('hello world')
driver.find_element(By.NAME, "btnK").click()
driver.close()