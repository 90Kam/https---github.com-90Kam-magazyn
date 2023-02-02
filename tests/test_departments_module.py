import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.common.keys import Keys

sys.path.insert(0,"C:\\Users\\VRT\\Desktop\\magazyn")

from locators import locators
from sites import main_page
from credentials import credentials

def setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(main_page.main_page)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, locators.działy_button).click()
    time.sleep(3)

def add_new_department(department_name):
    driver.find_element(By.XPATH, locators.add_new_department_button).click()
    driver.find_element(By.NAME, locators.new_department_input).send_keys(department_name)
    driver.find_element(By.XPATH, locators.submit_adding_new_department).click()

    
def search_department(searched_department):
    driver.find_element(By.XPATH, locators.magnifier_button).click()
    driver.find_element(By.XPATH, locators.magnifier_input).send_keys(searched_department)
    time.sleep(1)
    driver.find_element(By.XPATH, locators.found_department).text

def test_add():
    add_new_department('siemka')
    search_department('siemka')
