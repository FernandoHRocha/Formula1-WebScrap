from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import xlrd
import time
import os

path="chromedriver.exe"
site="https://www.formula1.com/en/results.html/2021/drivers.html"

def buttonClick(path):
    button = WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.XPATH,path)))
    button.click()

def findElement(path):
    element = WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.XPATH,path)))
    return element

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get(site)

#accept cookies
buttonClick('/html/body/div[5]/div/div/div[2]/div[3]/div[2]/button[2]')

#find table
tableScore = findElement('/html/body/div[2]/main/article/div/div[2]/div[2]/div[2]/div/table')