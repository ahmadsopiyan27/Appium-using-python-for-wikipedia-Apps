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
import os

driver = webdriver.Remote('http://127.0.0.1:4723',options=options)


# os.system('adb shell input swipe 540 1887 540 320')
# os.system('adb shell input tap 645 1084')

# menu klik search buka wikipedia

driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_container').click()

# search automation
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Automation')
driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.wikipedia:id/search_results_list"]/android.view.ViewGroup[1]').click()
# sleep(2)
# os.system('adb shell input keyevent 3')
#  update


# berkala

