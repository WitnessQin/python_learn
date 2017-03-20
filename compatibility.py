import re
import time
import os
import operator

global appPackage
global apkpath
global appActivity
apkpath="C:\\Users\\QinYinglin\\Downloads\\xiazaibao_android.apk"
appActivity='com.xunlei.timealbum.ui.BootActivity'

#安装apk
def installapp(path):
	global appPackage
	print('installing apk:'+appPackage)
	installresult=list(os.popen('adb install '+path).readlines())
	if "success" in str(installresult).lower():
		print('apk installed success: '+appPackage)
		return True
	else:
		print('fail to install apk: '+appPackage)
		return False

#判断app是否已经安装
def isappinstall():
	global appPackage
	isinstall=list(os.popen('adb shell pm list package |findstr '+appPackage.strip('\'')).readlines())
	if isinstall:
		print('apk has installed: '+appPackage)
		return True
	else:
		print('apk has not installed: '+appPackage)
		return False

#根据apk文件分析包名，得到appPackage
def getpackagename(path):
	if os.path.exists(path):
		global appPackage
		appPackageAdb=list(os.popen('aapt dump badging '+path+'|findstr "package"').readlines())
		appPackagename=re.findall(r'\'com\w*.*?\'',appPackageAdb[0])
		appPackage=str(appPackagename[0])
		print('apk\'s package name is: '+appPackage)
		return appPackage
	else:
		print('apk do not exists!')
		return None

#卸载app
def uninstallapp():
	global appPackage
	uninstall=list(os.popen('adb uninstall '+appPackage.strip('\'')).readlines())
	print('uninstalling apk:'+appPackage)
	if "success" in str(uninstall).lower():
		print('success uninstall '+appPackage)
		return True
	else:
		print('faile to uninstall '+appPackage)
		return False

def runapp():
	global appPackage
	global appActivity
	dorun=list(os.popen('adb shell am start -n '+appPackage+'/'+appActivity))
	if 'error' in str(dorun).lower():
		print('can not run the app: '+appPackage)
		return False
	else:
		print('app is running: '+appPackage)
		return True

def cleanconfig():
	global appPackage
	clean=list(os.popen('adb shell pm clear '+appPackage.strip('\'')).readlines())
	if "success" in str(clean).lower():
		print('success to clean the config of: '+appPackage)
		return True
	else:
		print('faile to clean the config of: '+appPackage)
		return False

def screenshot():
	timenow=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
	pathnow=os.path.abspath('.')+'\\screenshot\\'
	if os.path.exists(pathnow):
		pass
	else:
		os.mkdir(pathnow)
	os.popen('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
	os.popen('adb pull /sdcard/screenshot.png '+pathnow+timenow+'.png')
	print('screenshot has sent to :'+pathnow)

'''
getpackagename(apkpath)
if isappinstall():
	uninstallapp()
else:
	pass
installapp(apkpath)
runapp()
screenshot()
cleanconfig()
#uninstallapp()
'''

screenshot()