from PIL import Image
from selenium import webdriver
import time

global driver

url='http://10.10.63.253:9080/secure/Dashboard.jspa?selectPageId=10172'
image_path='d:\\test\\web.png'
element_id='gadget-10730-chrome'
element_image_path='d:\\test\\web-1.png'

#拉起浏览器打开对应页面
def openurl(url):
	global driver
	driver=webdriver.Edge()
	driver.maximize_window()
	driver.get(url)
	time.sleep(3)
	
#根据id查找元素的大小，并对大图进行截取保存
def catchscreeen(image_path,element_id,element_image_path):
	mainimage=Image.open(image_path)
	try:
		location=driver.find_element_by_id(element_id).location
		size=driver.find_element_by_id(element_id).size
		print('find the element: '+element_id)
	except Exception as e:
		print('can not find the element: '+element_id)
		raise e
	rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
	lastimage=mainimage.crop(rangle)
	lastimage.save(element_image_path)

openurl(url)
driver.save_screenshot(image_path)
catchscreeen(image_path,element_id,element_image_path)
driver.close()