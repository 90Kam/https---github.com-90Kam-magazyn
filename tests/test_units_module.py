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
# sys.path.insert(0,"C:\\Users\\Kam and Judy\\magazyn\\https---github.com-90Kam-magazyn")
from locators import locators
from sites import main_page
from credentials import credentials

class TestUnitsModule:
    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(main_page.main_page)
        driver.maximize_window()
        driver.find_element(By.XPATH, locators.jednostki_button).click()

    @classmethod
    def teardown_class(cls):
        driver.close()
        driver.quit()

    @pytest.mark.parametrize("nazwa, status",[
        ('KG', True),
        ('', False)
    ])
    def test_add_unit(self, nazwa, status):
        driver.find_element(By.XPATH, locators.add_unit_button).click()
        driver.find_element(By.NAME, locators.add_unit_input).send_keys(nazwa)
        driver.find_element(By.XPATH, locators.submit_new_unit).click()
        if status == True:
            driver.find_element(By.XPATH, locators.magnifier_button).click()
            driver.find_element(By.XPATH, locators.magnifier_input).send_keys(nazwa)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'Toastify__toast-icon Toastify--animate-icon')]/following-sibling::div[1]")))
            time.sleep(1)
            finding_new_unit = driver.find_element(By.XPATH, locators.founded_unit)
            assert nazwa == finding_new_unit.text

        else:
            print(driver.find_element(By.XPATH, locators.founded_unit).text)
print('test dodawania jednostki')
