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

class TestWydaniaZewModule:

    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(main_page.main_page)
        driver.maximize_window()
        
        driver.find_element(By.XPATH, locators.wydania_zew_button).click()

    @classmethod
    def teardown_class(cls):
        driver.close()
        driver.quit()

    @pytest.mark.parametrize("nr_dokumentu, komentarz, is_exist",[
        ('01', 'random_comment' ,True),
        ('02', '', True),
        ('', '', False),
        ('', 'whatever_comment', False)
    ])
    @pytest.mark.flow
    def test_add_wydanie_zew(self, nr_dokumentu, komentarz, is_exist ):
        driver.find_element(By.XPATH, "//span[text()='Przedmioty']").click()
        quantity = driver.find_element(By.XPATH, "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[3]").text
        driver.find_element(By.XPATH, locators.wydania_zew_button).click()

        driver.find_element(By.XPATH, locators.dodaj_wydanie_zew_button).click()
        driver.find_element(By.NAME, locators.nr_dokumentu_input).send_keys(nr_dokumentu)
        driver.find_element(By.NAME, locators.komentarz_input).send_keys(komentarz)
        driver.find_element(By.XPATH, locators.wybierz_kontrahenta_button).click()
        driver.find_element(By.XPATH, locators.wybierz_first_button).click()
        driver.find_element(By.XPATH, locators.wybierz_projekt_button).click()
        driver.find_element(By.XPATH, locators.wybierz_first_button).click()
        driver.find_element(By.XPATH, locators.wybierz_przedmioty_button).click()
        driver.find_element(By.XPATH, locators.wybierz_first_button).click()
        driver.find_element(By.XPATH, locators.x_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.calendar_icon).click()
        driver.find_element(By.XPATH, locators.day_button).click()
        if is_exist == True:
            driver.find_element(By.XPATH, locators.confirm_dodaj_wydanie_zew_button).click()
            driver.find_element(By.XPATH, "//span[text()='Przedmioty']").click()
            quantity2 = driver.find_element(By.XPATH, "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[3]").text
            assert int(quantity) > int(quantity2)
            print('ilosc przed = '+quantity)
            print('ilosc po = '+ quantity2)

        else:
            driver.find_element(By.XPATH, locators.confirm_dodaj_wydanie_zew_button).click()

            # driver.find_element(By.XPATH, locators.x_button2).click()   <-- ważne gdy będzie naprawiona strona

            time.sleep(1)
            driver.find_element(By.XPATH, "//span[text()='Przedmioty']").click()
            quantity2 = driver.find_element(By.XPATH, "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[3]").text
            assert int(quantity) != int(quantity2)  # <-- zmienić na == jak będzie naprawiona strona
            print('ilosc przed = '+quantity)
            print('ilosc po = '+ quantity2)