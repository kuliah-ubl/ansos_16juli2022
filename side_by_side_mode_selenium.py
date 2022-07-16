# Created by Muhamad Syafii
# Kelp : SI Magister
# Saturday, 16/07/2022
# Copyright (c) 2022 by Univ Budi Luhur
# All Rights Reserved

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#set chromedriver.exe path
# driver = webdriver.Chrome(executable_path='../drivers/chromedriver') #this is not use
driver = webdriver.Chrome(ChromeDriverManager().install()) #using code here

