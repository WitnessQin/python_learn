#from appium import webdriver
import re
import time
import os

#测试包的路径及文件名
appLocation="C:\\Users\\QinYinglin\\Downloads\\xiazaibao_android.apk"
#获取设备di
readDeviceID=list(os.popen('adb devices').readlines())
deviceID=re.findall(r'^\w*\b',readDeviceID[1])
#获取设备系统版本号
deviceAndriodVersion=list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion=re.findall(r'^\w*\b',deviceAndriodVersion[0])
#读取apk的包名
#appPackageAdb=list(os.popen('aapt dump badging '+appLocation).readlines())
#appPackage=re.findall(r'\'com\w*.*?\'',appPackageAdb[0])
print(deviceID[0],deviceVersion[0])
