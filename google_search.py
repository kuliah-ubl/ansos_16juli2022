from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#set chromedriver.exe path
# driver = webdriver.Chrome(executable_path='../drivers/chromedriver') #this is not use
driver = webdriver.Chrome(ChromeDriverManager().install()) #using code here
#url launch
driver.get("http://google.com")
#identify edit box with name
# l = driver.find_element_by_link_text('Instituto') #not use this 
driver.find_element(By.ID, "lst-ib").clear()
driver.find_element(By.ID, "lst-ib").send_keys('hello world')
#input text
# l.send_keys('Selenium Python')
#obtain value entered
# v = l.get_attribute('value')
# print('Value entered: ' + v)
#driver close
driver.close()