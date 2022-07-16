from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#set chromedriver.exe path
# driver = webdriver.Chrome(executable_path='../drivers/chromedriver') #this is not use
driver = webdriver.Chrome(ChromeDriverManager().install()) #using code here
#url launch
driver.get("http://fisica.udea.edu.co")
#identify edit box with name
# l = driver.find_element_by_link_text('Instituto') #not use this 
driver.find_element("link text", "Instituto").click()
#input text
# l.send_keys('Selenium Python')
#obtain value entered
# v = l.get_attribute('value')
# print('Value entered: ' + v)
#driver close
driver.close()