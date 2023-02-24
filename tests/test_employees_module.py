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

# sys.path.insert(0,"C:\\Users\\VRT\\Desktop\\magazyn")
# sys.path.insert(0,"C:\\Users\\Kam and Judy\\magazyn\\https---github.com-90Kam-magazyn")
sys.path.insert(0,"C:\\Users\\VRT\\Desktop\\nowy_magazyn\\https---github.com-90Kam-magazyn")

from locators import locators
from sites import main_page
from credentials import credentials

def setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(main_page.main_page)
    driver.maximize_window()
    driver.find_element(By.XPATH, locators.pracownicy_button).click()

def add_new_employee(name2, lastname2):
    driver.find_element(By.XPATH, locators.add_employee_button).click()
    driver.find_element(By.NAME, locators.new_employee_name_input).send_keys(name2)
    driver.find_element(By.NAME, locators.new_employee_lastname_input).send_keys(lastname2)
    driver.find_element(By.XPATH, locators.submit_adding_new_employee_button).click()

def searching_employee(searched_name, searched_lastname):
    driver.find_element(By.XPATH, locators.filter_employee_button).click()
    driver.find_element(By.XPATH, locators.filter_name_input).send_keys(searched_name)
    driver.find_element(By.XPATH, locators.filter_lastname_input).send_keys(searched_lastname)

def edit_employee(edited_employee_name, edited_employee_lastname):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH,locators.add_employee_button)))

    name2 = driver.find_element(By.XPATH, locators.found_employee_name).text
    lastname2 = driver.find_element(By.XPATH, locators.found_employee_lastname).text
    driver.find_element(By.XPATH, locators.edit_employee_button).click()
    name = driver.find_element(By.NAME, locators.new_employee_name_input)
    lastname = driver.find_element(By.NAME, locators.new_employee_lastname_input)
    print(len(name2))
    letter = 0
    while letter < len(name2):
        name.send_keys(Keys.BACKSPACE)
        letter = letter + 1
    name.send_keys(edited_employee_name)    


        

    # for letter in name.get_attribute("class"):
    #     name.send_keys(Keys.BACKSPACE)
    # time.sleep(1)
    
    letter2 = 0
    while letter2 < len(lastname2):
        lastname.send_keys(Keys.BACKSPACE)
        letter2 = letter2 + 1
    lastname.send_keys(edited_employee_lastname)

    # lastname = driver.find_element(By.NAME, locators.new_employee_lastname_input)
    # for letter in lastname.get_attribute("class"):
    #     lastname.send_keys(Keys.BACKSPACE)
    # time.sleep(1)
    # lastname.send_keys(edited_employee_lastname)
    driver.find_element(By.XPATH, locators.submit_edit_employee_button).click()
    



@pytest.mark.parametrize("name, lastname, is_added", [
    ("olek", "kanar", True),
    ("", "pararara", False),
    ("Wojtek", "", False),
    ("", "", False)
]) 
def test_add_employee(name, lastname, is_added):
    add_new_employee(name, lastname)
    print('siemka')
    if is_added == True:
        searching_employee(name, lastname)
        time.sleep(1)
        finding_name = driver.find_element(By.XPATH, locators.found_employee_name)
        finding_lastname = driver.find_element(By.XPATH, locators.found_employee_lastname)
        assert name == finding_name.text and lastname == finding_lastname.text
    else:
        print(name + lastname)
###################################################################################### tutaj trzeba dodać assercje jak zostanie naprawione dodawanie pustych stringów
@pytest.mark.parametrize("edited_name, edited_lastname, is_edited", [
    ("Adam", "makaron", True),
    ("", "Nazwisko", False),
    ("Anna", "", False),
    ("", "", False)
]) 
def test_edit_employee(edited_name, edited_lastname, is_edited):
    driver.refresh()
    edit_employee(edited_name, edited_lastname)
    if is_edited == True:
        searching_employee(edited_name, edited_lastname)
        finding_name = driver.find_element(By.XPATH, locators.found_employee_name)
        finding_lastname = driver.find_element(By.XPATH, locators.found_employee_lastname)
        assert edited_name == finding_name.text and edited_lastname == finding_lastname.text
    else:
        print(edited_name + edited_lastname)

    




    