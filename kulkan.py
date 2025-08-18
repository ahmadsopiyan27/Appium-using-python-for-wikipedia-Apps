from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# seting capabilities
options = UiAutomator2Options()

options.app_package = "com.barangkulakan.mobile"
options.app_activity = "com.barangkulakan.mobile.MainActivity29"
options.platform_name = "Android"
options.udid = "RRCT20019EJ"
options.no_reset = True
import os

driver = webdriver.Remote('http://127.0.0.1:4723',options=options)
driver.implicitly_wait(10)


# os.system('adb shell input swipe 540 1887 540 320')
os.system('adb shell input tap 932 1784')

# menu klik search buka wikipedia

driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="btnProductItem"])[7]').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Garuda').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'HET1000, Garuda Pilus Fried Chicken Edisi Jakarta -14g/PGFC8J, Rp 755, PT. Sinar Niaga Sejahtera').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Masukkan Tas Belanja').click()
driver.find_element(AppiumBy.XPATH, '(//android.widget.TextView[@text=""])[1]').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Tambah Barang ').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="1"]').click()
# os.system('adb shell input tap 885 2336')
# driver.quit()

# sleep(2)
# os.system('adb shell input keyevent 3')
#  update


# berkala

