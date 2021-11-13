from selenium import webdriver
import time
from selenium.webdriver.common.by import By


LINK = 'https://planetfor.me'


def test_ui_selenium():
    browser = webdriver.Chrome()
    with browser:
        browser.get(LINK)
        button = browser.find_element(By.XPATH, "//span[contains(text(), 'Панорамные виды Москвы')]")
        button.click()

        time.sleep(1)

        browser.switch_to.window(browser.window_handles[1])
        title = browser.find_element(By.CSS_SELECTOR, '.font-semi-22.mg-top-15')
        title_text = title.text
        assert "Панорамные виды Москвы" == title_text

        places = browser.find_elements(By.CSS_SELECTOR, 'div.pfm-content-group div.pfm-grid-view-4 > a')
        assert len(places) == 12
