import pytest
from appium import webdriver
import time
import os
from selenium.webdriver.common.by import By


@pytest.fixture(scope='session')
def desired_caps():
    return {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "redmi",
        "udid": "3efa057c",
        "appPackage": "com.planet.forme",
        "appActivity": "com.planet.forme.ui.activities.main.MainActivity"
    }


@pytest.fixture(scope='session')
def appium_driver(desired_caps):
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def test_wrong_login(desired_caps, appium_driver):
    """
    Негативный тест с некорректными данными для входа.
    """
    driver = appium_driver
    log_in_button = driver.find_element(By.ID, 'com.planet.forme:id/logInTabButton')
    log_in_button.click()

    search_login_box = driver.find_element(By.ID, 'com.planet.forme:id/loginInput')
    search_login_box.send_keys('a')

    search_password_box = driver.find_element(By.ID, 'com.planet.forme:id/passwordInput')
    search_password_box.send_keys('123456tgyfdI')

    sign_in_button = driver.find_element(By.ID, 'com.planet.forme:id/signInButton')
    sign_in_button.click()

    assert sign_in_button.is_displayed()


def test_login(desired_caps, appium_driver):
    """
    Позитивный тест с корректынми данными для входа.
    Логин: gigas59600
    Пароль: gigas59600
    """
    driver = appium_driver

    log_in_button = driver.find_element(By.ID, 'com.planet.forme:id/logInTabButton')
    log_in_button.click()

    search_login_box = driver.find_element(By.ID, 'com.planet.forme:id/loginInput')
    search_login_box.send_keys('gigas59600')

    search_password_box = driver.find_element(By.ID, 'com.planet.forme:id/passwordInput')
    search_password_box.send_keys('gigas59600')

    sign_in_button = driver.find_element(By.ID, 'com.planet.forme:id/signInButton')
    sign_in_button.click()

    time.sleep(2)

    search_button = driver.find_element(By.ID, 'com.planet.forme:id/navigationGlobalSearch')
    search_button.click()
    search_text_box = driver.find_element(By.ID, 'com.planet.forme:id/searchEditText')
    search_text_box.send_keys('yuiopfvghjk')
    time.sleep(2)
    no_results = driver.find_element(By.ID, 'com.planet.forme:id/noResultsPlaceholder')
    assert no_results.is_displayed()

    clear_search_button = driver.find_element(By.ID, 'com.planet.forme:id/clearSearchButton')
    clear_search_button.click()

    search_text_box.send_keys('ресторан')
    filter = driver.find_element(By.ID, 'com.planet.forme:id/btnFilter')
    filter.click()
    different_filter = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.CompoundButton[2]')
    different_filter.click()
    apply_button = driver.find_element(By.ID, 'com.planet.forme:id/btnApplyFilter')
    apply_button.click()
    results = driver.find_element(By.ID, 'com.planet.forme:id/recyclerGlobalSearch')
    assert results.is_displayed()
