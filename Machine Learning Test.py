
import numpy
import sklearn
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver_path = 'C:/Users/bbbak/Documents/DynastyFFScouting/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://hoopshype.com/salaries/players/')