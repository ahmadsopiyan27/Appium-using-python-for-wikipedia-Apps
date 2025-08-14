import os
from time import sleep

os.system('adb install "C:/Users/LENOVO/DemoApp.apk"')
sleep(2)
os.system('adb shell input tap 420 1097')
sleep(1)
os.system('adb shell input swipe 540 1887 540 320')
sleep(2)
os.system('adb shell input keyevent KEYCODE_BACK')
sleep(3)
os.system('adb uninstall com.code2lead.kwad')
