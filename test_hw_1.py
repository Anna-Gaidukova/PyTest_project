from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

def test_1():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://mirohost.net/")

    try:
        link_element = driver.find_element(By.XPATH, '//a[@href="/en/payments" and text()="Payment"]')
        link_element.click()

    except Exception as e:
        print("There is a mistake:", e)
    time.sleep(5)


    driver.quit()
    print("Test OK")