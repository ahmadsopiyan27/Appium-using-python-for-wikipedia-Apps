from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

# seting capabilities
options = UiAutomator2Options()

options.app_package = "org.wikipedia"
options.app_activity = ".main.MainActivity"
options.platform_name = "Android"
options.udid = "RRCT20019EJ"
options.no_reset = True

driver = webdriver.Remote('http://127.0.0.1:4723',options=options)

# menu klik search buka wikipedia

driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_container').click()

# search automation
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Automation')

# lanjut buat testcase nya


#  assertionnnya



#  reporting

#  test