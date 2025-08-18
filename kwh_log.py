from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import pytest


def clear_data():
    os.system('adb clearapp com.code2lead.kwad')
# seting capabilities
@pytest.fixture
def setup():
    options = UiAutomator2Options()
    options.app_package = "com.code2lead.kwad"
    options.app_activity = "com.code2lead.kwad.MainActivity"
    options.platform_name = "Android"
    options.udid = "RRCT20019EJ"
    driver = webdriver.Remote('http://127.0.0.1:4723',options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
    clear_data()





def test_login_positif(setup):
    setup.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Login').click()
    setup.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Et4').send_keys('admin@gmail.com')
    setup.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Et5').send_keys('admin123')
    setup.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Btn3').click()

    titletext =setup.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Enter Admin"]').text
    assert titletext == 'Enter Admin'



