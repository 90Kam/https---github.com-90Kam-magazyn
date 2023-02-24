import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import html
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime
from selenium.webdriver.common.keys import Keys

# sys.path.insert(0,"C:\\Users\\Kam and Judy\\magazyn\\https---github.com-90Kam-magazyn")
sys.path.insert(0,"C:\\Users\\VRT\\Desktop\\nowy_magazyn\\https---github.com-90Kam-magazyn")
from locators import locators
from sites import main_page
from credentials import credentials


class TestDepartmentsModule:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(main_page.main_page)
        driver.maximize_window()
        driver.find_element(By.XPATH, locators.działy_button).click()
    @classmethod
    def teardown_class(cls):
        driver.close()
        driver.quit()

    @pytest.mark.parametrize("department_name, is_added", [
        ("WEB", True),
        ("", False),
        ("asdcfdasertorportkmvbmfkrtkrfrtyops", False)
    ]) 

    def test_add_department(self, department_name, is_added):
        driver.find_element(By.XPATH, locators.add_new_department_button).click()
        driver.find_element(By.NAME, locators.new_department_input).send_keys(department_name)
        driver.find_element(By.XPATH, locators.submit_adding_new_department).click()

        if is_added == True:
            time.sleep(0.5)
            driver.find_element(By.XPATH, locators.magnifier_button).click()
            driver.find_element(By.XPATH, locators.magnifier_input).send_keys(department_name)
            time.sleep(0.5)
            finding_department_name = driver.find_element(By.XPATH, locators.found_department)
            assert department_name == finding_department_name.text
        else:
            print(department_name)

    @pytest.mark.parametrize("edited_department, is_edited", [
        ("QA",  True),
        ("", False)
]) 
    def test_edit_department(self, edited_department, is_edited):
        print('testtestu')

        time.sleep(1)
        driver.find_element(By.XPATH, locators.edit_department_button).click()
        name = driver.find_element(By.NAME, locators.new_department_input)
        for letter in name.get_attribute("class"):
            name.send_keys(Keys.BACKSPACE)
        name.send_keys(edited_department)
        driver.find_element(By.XPATH, locators.submit_edit_employee_button).click()
        if is_edited == True:
            time.sleep(0.5)
            driver.find_element(By.XPATH, locators.magnifier_button).click()
            driver.find_element(By.XPATH, locators.magnifier_input).send_keys(edited_department)
            time.sleep(0.5)    
            finding_department = driver.find_element(By.XPATH, locators.found_department)
            assert finding_department.text == edited_department
        else:
            print(driver.find_element(By.XPATH, locators.found_department).text)


# now = datetime.now()

# date = now.strftime('%Y - %m - %d')

# folder_name = f"{date}"
# os.mkdir(folder_name)

# report_name = f"report.html"
# report_path = os.path.join(folder_name, report_name)
# with open (report_path, 'w') as f:
#     f.write(report.html)

# print(f"Folder '{folder_name}' and report file '{report_name}' have been created")

