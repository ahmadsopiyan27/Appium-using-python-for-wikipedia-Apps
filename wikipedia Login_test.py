from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# seting capabilities
options = UiAutomator2Options()

options.app_package = "org.wikipedia"
options.app_activity = ".main.MainActivity"
options.platform_name = "Android"
options.udid = "RRCT20019EJ"
options.no_reset = True

driver = webdriver.Remote('http://127.0.0.1:4723',options=options)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.ID, 'org.wikipedia:id/menu_icon').click()
# 

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'org.wikipedia:id/main_drawer_account_container')))
    driver.find_element(AppiumBy.ID, 'org.wikipedia:id/main_drawer_account_container').click()

except TimeoutException:
    print('pop up tidak muncul')





