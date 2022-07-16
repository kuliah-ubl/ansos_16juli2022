from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#set chromedriver.exe path
# driver = webdriver.Chrome(executable_path='../drivers/chromedriver') #this is not use
driver = webdriver.Chrome(ChromeDriverManager().install()) #using code here

