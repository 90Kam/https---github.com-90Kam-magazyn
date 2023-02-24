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

sys.path.insert(0,"C:\\Users\\VRT\\Desktop\\nowy_magazyn\\https---github.com-90Kam-magazyn")
# sys.path.insert(0,"C:\\Users\\VRT\\Desktop\\magazyn")
# sys.path.insert(0,"C:\\Users\\Kam and Judy\\magazyn\\https---github.com-90Kam-magazyn")
from locators import locators
from sites import main_page
from credentials import credentials

class TestAddSource:

    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(main_page.main_page)
        driver.maximize_window()
        driver.find_element(By.XPATH, locators.zrodla_finansowania_button).click()

    @classmethod
    def teardown_class(cls):
        driver.close()
        driver.quit()

    @pytest.mark.parametrize("nazwa, status",[
        ('Adam', True),
        ('', False)
    ])
    def test_add_source_of_founding(self, nazwa, status):
        driver.find_element(By.XPATH, locators.add_source_of_founding_button).click()
        driver.find_element(By.NAME, locators.source_of_founding_input).send_keys(nazwa)
        driver.find_element(By.XPATH, locators.submit_new_source_of_founding_button).click()
        if status == True:
            driver.find_element(By.XPATH, locators.magnifier_button).click()
            driver.find_element(By.XPATH, locators.magnifier_input).send_keys(nazwa)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'Toastify__toast-icon Toastify--animate-icon')]/following-sibling::div[1]")))
            time.sleep(1)
            finding_source_of_founding = driver.find_element(By.XPATH, locators.found_source_of_founding_name)
            assert nazwa == finding_source_of_founding.text

        else:
            print(driver.find_element(By.XPATH, locators.found_source_of_founding_name).text)

    @pytest.mark.parametrize("edited_source_of_founding, status",[
        ('wlasne', True),
        ('', False)
    ])

    def test_edit_source_of_founding(self, edited_source_of_founding, status):
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.edit_source_of_founding_button).click()
        time.sleep(1)
        name = driver.find_element(By.NAME, locators.source_of_founding_input)
        name2 = driver.find_element(By.XPATH, locators.found_source_of_founding_name).text
        letter = 0
        while letter < len(name2):
            name.send_keys(Keys.BACKSPACE)
            letter = letter + 1
        name.send_keys(edited_source_of_founding)
        driver.find_element(By.XPATH, locators.submit_edited_source_of_founding).click()
        if status == True:
            driver.refresh()
            time.sleep(1)
            assert driver.find_element(By.XPATH, locators.found_source_of_founding_name).text == edited_source_of_founding
        else:
            print(edited_source_of_founding)