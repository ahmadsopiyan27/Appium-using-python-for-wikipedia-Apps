from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from time import sleep


options = UiAutomator2Options()

options.app_package = "com.linkedin.android"
options.app_activity = "com.linkedin.android.authenticator.LaunchActivityDefault"
options.platform_name = "Android"
options.udid = "RRCT20019EJ"
options.no_reset = True

driver = webdriver.Remote('http://127.0.0.1:4723',options=options)
# driver.implicitly_wait(10)
# os.system('adb shell input tap 437 1057')
sleep(5)
driver.find_element(AppiumBy.ID, 'com.linkedin.android:id/tab_jobs').click()
sleep(3)
os.system('adb shell input swipe 540 1287 540 320')
sleep(3)
driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="sdui:lazyColumn"]/android.view.View[2]/android.view.View[2]').click()
sleep(3)
# os.system('adb shell input swipe 540 987 540 320')
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Manual Tester, Verified, Sharp Decisions, Charlotte, NC (Hybrid), Company review time is typically 1 week, Viewed · . Easy Apply, Button').click()
sleep(3)
driver.find_element(AppiumBy.ID, 'com.linkedin.android:id/careers_top_card_job_primary_button_container').click()
sleep(3)
driver.find_element(AppiumBy.ID, 'com.linkedin.android:id/job_apply_flow_bottom_toolbar_cta_2').click()
sleep(3)
driver.find_element(AppiumBy.ID, 'com.linkedin.android:id/job_apply_flow_bottom_toolbar_cta_2').click()
sleep(3)
driver.find_element(AppiumBy.ID, 'com.linkedin.android:id/job_apply_review_bottom_toolbar_cta').click()
# sleep(3)
driver.quit()
