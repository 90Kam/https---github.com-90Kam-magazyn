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
sys.path.insert(0,"C:\\Users\\Kam and Judy\\magazyn\\https---github.com-90Kam-magazyn")
from locators import locators
from sites import main_page
from credentials import credentials

class TestSources:

    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(main_page.main_page)
        driver.maximize_window()
        driver.find_element(By.XPATH, locators.zrodla_finansowania_button).click()


    def add_new_source_of_founding(source_of_founding_name):
        driver.find_element(By.XPATH, locators.add_source_of_founding_button).click()
        driver.find_element(By.NAME, locators.source_of_founding_input).send_keys(source_of_founding_name)
        driver.find_element(By.XPATH, locators.submit_new_source_of_founding_button).click()

    def searching_source_of_founding(searched_source_of_founding):
        driver.find_element(By.XPATH, locators.magnifier_button).click()
        driver.find_element(By.XPATH, locators.magnifier_input).send_keys(searched_source_of_founding)
        time.sleep(1)

    def edit_source_of_founding(edited_source_of_founding):
        driver.find_element(By.XPATH, locators.edit_source_of_founding_button).click()
        name = driver.find_element(By.XPATH, locators.source_of_founding_input)
        name2 = driver.find_element(By.XPATH, locators.found_source_of_founding_name).text
        letter = 0
        while letter < len(name2):
            name.send_keys(Keys.BACKSPACE)
            letter = letter + 1
        name.send_keys(edited_source_of_founding)

    @pytest.mark.parametrize("source_of_founding_name, is_added", [
        ("testowe zrodlo", True),
        ("", False)
    ]) 
    def test_add_source_of_founding(source_of_founding_name, is_added):
        TestSources.add_new_source_of_founding(source_of_founding_name)
        if is_added == True:
            TestSources.searching_source_of_founding(source_of_founding_name)
            finding_source_of_founding = driver.find_element(By.XPATH, locators.found_source_of_founding_name)
            assert source_of_founding_name == finding_source_of_founding.text

        else:
            print(driver.find_element(By.XPATH, locators.found_source_of_founding_name).text)

