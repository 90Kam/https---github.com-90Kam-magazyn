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

sys.path.insert(0,"C:\\Users\\Kam and Judy\\magazyn\\https---github.com-90Kam-magazyn")

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
    


def edit_department(edited_department):
    driver.find_element(By.XPATH, locators.edit_department_button).click()
    name = driver.find_element(By.NAME, locators.new_department_input)
    for letter in name.get_attribute("class"):
        name.send_keys(Keys.BACKSPACE)
    name.send_keys(edited_department)
    driver.find_element(By.XPATH, locators.submit_edit_employee_button).click()

@pytest.mark.parametrize("department_name, is_added", [
    ("Graficy", True),
    ("", False),
    ("asdcfdasertorportkmvbmfkrtkrfrtyops", False)
]) 

def test_add_department(department_name, is_added):
    add_new_department(department_name)
    if is_added == True:
        search_department(department_name)
        finding_department_name = driver.find_element(By.XPATH, locators.found_department)
        assert department_name == finding_department_name.text
    else:
        print(department_name)

@pytest.mark.parametrize("edited_department, is_edited", [
    ("QA",  True),
    ("", False),
    ("this_string_has_more_than_32_characters", False)
]) 
def test_edit_department(edited_department, is_edited):
    edit_department(edited_department)
