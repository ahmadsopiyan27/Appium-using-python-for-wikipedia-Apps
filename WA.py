from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

# seting capabilities
options = UiAutomator2Options()

options.app_package = "com.whatsapp"
options.app_activity = ".home.ui.HomeActivity"
options.platform_name = "Android"
options.udid = "RRCT20019EJ"
options.no_reset = True
import os

driver = webdriver.Remote('http://127.0.0.1:4723',options=options)


# os.system('adb shell input swipe 540 1887 540 320')
os.system('adb shell input tap 462 1668')

# menu klik search buka wikipedia

driver.find_element(AppiumBy.ID, 'com.whatsapp:id/search_bar_inner_layout').click()

# search automation
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/search_input').send_keys('mami sayank')
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/contact_row_container').click()
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/entry').send_keys('love you 1 juta kali')
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/send').click()
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/entry').send_keys('love you 10 juta kali')
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/send').click()
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/entry').send_keys('love you 1 miliar juta kali')
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/send').click()
driver.find_element(AppiumBy.ID, 'com.whatsapp:id/whatsapp_toolbar_home').click()

# os.system('adb shell input tap 885 2336')
driver.quit()
# sleep(2)
# os.system('adb shell input keyevent 3')
#  update


# berkala

