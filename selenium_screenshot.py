from PIL import Image
from selenium import webdriver
import time

url='http://10.10.63.253:9080/secure/Dashboard.jspa?selectPageId=10172'
driver=webdriver.Edge()
driver.maximize_window()
driver.get(url)
time.sleep(3)
#拉起浏览器打开对应页面
driver.save_screenshot('d:\\test\\web.png')
#截图大图
location=driver.find_element_by_id('gadget-10730-chrome').location
size=driver.find_element_by_id('gadget-10730-chrome').size
rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
#获取特定ID的元素的大小
maxscreen=Image.open('d:\\test\\web.png')
lastimage=maxscreen.crop(rangle)
lastimage.save('d:\\test\\web-1.png')
#从大图截取小图
driver.execute_script("window.scrollBy(0,3000)")
#滚动页面
driver.close()
#关闭浏览器