import unittest
import HTMLTestRunner
import io
import os
import subprocess
from appium import webdriver
import logging
from time import sleep
logging.basicConfig(filename='logging.txt', level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s:%(message)s")
global driver


def setUpModule():
    os.system("C:\\Python35\\work\\appium_close.bat")
    os.system("C:\\Python35\\work\\appium_up.bat")
    sleep(10)
    print('开始')
    global driver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = '80QBCPF2262H'
    desired_caps['app']='C:\\Users\\QinYinglin\\Downloads\\xiazaibao_android.apk'
    desired_caps['noReset']=True
    desired_caps['appPackage'] = 'com.xunlei.timealbum'
    desired_caps['appActivity'] = 'com.xunlei.timealbum.ui.BootActivity'
    desired_caps[
        'waitappActivity'] = 'com.xunlei.timealbum.ui.account.LoginGuideActivity'
    desired_caps['unicodeKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    logging.info('connected the device!' + desired_caps['deviceName'])
    sleep(3)
    return driver


def tearDownModule():
    global driver
    logging.info('unconnected the device!')
    driver.quit()
    os.system("C:\\Python35\\work\\appium_close.bat")

# 定义通用操作的类


class commomModule(object):
    """docstring for commomModule"""
    global driver

    def __init__(self):
        super(commomModule, self).__init__()

    # 定义查找元素的函数
    def find_element(self, arg):
        try:
            element = driver.find_element_by_id(arg)
            logging.info('find the element:' + arg)
        except Exception as e:
            logging.info('can not find the element by id:' + arg)
            element = driver.find_element_by_name(arg)
            logging.info('find the element:' + arg)
        except Exception as f:
            element = driver.find_element_by_class_name(arg)
            logging.info('find the element:' + arg)
        except Exception as g:
            element = driver.find_element_by_xpath(arg)
            logging.info('find the element:' + arg)
        except Exception as h:
            logging.info('can not find the element')
            element = None
            raise h
        finally:
            return element

    # 定义点击元素的函数
    def click_element(self, arg):
        try:
            self.find_element(arg)
        except Exception as e:
            logging.info('can not find the element:' + arg)
            raise e
        else:
            cl = self.find_element(arg)
            logging.info('click the element:' + arg)
            return cl.click()


    # 定义登录函数
    def login(self, account, password):
        try:
            driver.wait_activity(
                'com.xunlei.timealbum.ui.account.PhoneLoginActivity', 5)
            self.click_element('com.xunlei.timealbum:id/account_login')
            driver.wait_activity(
                'com.xunlei.timealbum.ui.account.LoginActivity', 5)
            self.click_element(
                'com.xunlei.timealbum:id/textview_login_user_name')
            '''
            if self.find_element('com.xunlei.timealbum:id/clearBtn1'):
                self.click_element('com.xunlei.timealbum:id/clearBtn1')
                # 如果记住上次帐号，则先清
                sleep(1)
            '''
            logging.info('输入帐号')
            self.find_element(
                'com.xunlei.timealbum:id/textview_login_user_name').send_keys(account)
            self.click_element(
                'com.xunlei.timealbum:id/textview_login_user_pwd')
            logging.info('输入密码')
            self.find_element(
                'com.xunlei.timealbum:id/textview_login_user_pwd').send_keys(password)
            logging.info('点击登录')
            login_result = self.click_element(
                'com.xunlei.timealbum:id/login_ok_layout')
        except Exception as e:
            login_result = None
            raise e
        finally:
            return login_result

    # 定义输入信息的函数
    # 定义触控的函数
    # 定义截图的函数
    # 定义了获取当前activity的函数
    def iscurrent_activity(self, arg):
        try:
            current_activity = 'com.xunlei.timealbum' + driver.current_activity
            assert(current_activity == arg)
        except Exception as e:
            logging.info(arg + ' is not current_activity！！！')
            raise e
        else:
            logging.info(arg + ' is current_activity')
    
    def clickOK(self):
        i=0
        while i<10:
            if self.click_element("确定"):
                pass
            else:
                logging.info('第'+i+'次，找不到确定按钮')
                pass
            i=i+1
            print('finding')
            sleep(1)



class Unittest_t(unittest.TestCase):
    global driver
    """docstring for unittest_t"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 登录引导界面检查用例
    def test_login_guide(self):
        try:
            el = commomModule()
            el.find_element("登录迅雷帐号")
            el.find_element("注册帐号")
            el.find_element("暂不登录")
        except Exception as e:
            driver.save_screenshot("异常：登录引导页面" + ".png")
            logging.info("！！！登录引导界面检查异常！！！")
            raise e
        else:
            driver.save_screenshot("登录引导页面" + ".png")
            logging.info("登录引导界面检查正常")

    # 登录界面检查用例
    def test_login(self):
        try:
            element = commomModule()
            element.click_element('com.xunlei.timealbum:id/login')
            sleep(1)
            element.click_element('com.xunlei.timealbum:id/account_login')
            el.login('15874156104', '19891989')
        except Exception as e:
            driver.save_screenshot("异常：登录界面" + ".png")
            logging.info("异常：无法进入登录界面")
            self.assertIsNone(element, 'can not click login!')
            raise e
        else:
            logging.info("进入登录界面")
            driver.save_screenshot("登录界面" + ".png")

    # 注册界面检查用例
    def test_register(self):
        try:
            element = driver.find_element_by_id(
                'com.xunlei.timealbum:id/register').click()
            sleep(1)
        except Exception as e:
            driver.save_screenshot("异常：注册按钮" + ".png")
            logging.info("异常：无法进入注册界面")
            #self.assertIsNone(element,'can not click register!')
            raise e
        else:
            try:
                element = driver.find_element_by_id(
                    'com.xunlei.timealbum:id/register_table')
            except Exception as e:
                driver.save_screenshot("异常：注册界面" + ".png")
                logging.info("异常：无法进入注册界面")
                #self.assertIsNone(element,'can not go to register_table!')
                raise e
            else:
                logging.info("进入注册界面")
                driver.save_screenshot("注册界面" + ".png")
                element = driver.find_element_by_id(
                    'com.xunlei.timealbum:id/left_btn').click()
                sleep(3)

    # 暂不登录界面检查用例
    def test_login_later(self):
        try:
            el = commomModule()
            el.click_element("暂不登录")
            driver.wait_activity(
                'com.xunlei.timealbum.ui.qrcode.BindDeviceGuideActivity',5)
            el.click_element("暂不关联")
            driver.wait_activity(
                'com.xunlei.timealbum.ui.xzbmain.XZBMainActivity', 5)
            el.clickOK()
            el.click_element('com.xunlei.timealbum:id/iv_mine_avatar')
            el.login('15874156104', '19891989')
        except Exception as e:
            driver.save_screenshot("异常：暂不登录按钮" + ".png")
            logging.info("异常：无法点击暂不登录")
            self.assertIsNone(el, 'can not click login_later!')
            raise e
        else:
            logging.info('登录成功！')

        # 检查登陆成功的用例
        def test_login_suc():
            pass

        # 检查登录失败的用例
        def test_login_fail():
            pass

        # 测试用例
    def test_test(self):
        try:
            el = commomModule()
            el.iscurrent_activity(
                'com.xunlei.timealbum.ui.account.LoginGuideActivity')
        except Exception as e:
            raise e


def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Unittest_t('test_test'))
    suiteTest.addTest(Unittest_t('test_login_guide'))
    suiteTest.addTest(Unittest_t('test_login_later'))
    return suiteTest
'''
if __name__ == '__main__':
	unittest.main(defaultTest = 'suite')
'''
if __name__ == '__main__':
    HtmlFile = "c:\\python35\\work\\result.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title="appium自动化测试", description="用例执行情况")
    runner.run(suite())
    fp.close()
    os.popen("C:\\Users\\QinYinglin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe C:\\Python35\\work\\result.html")
