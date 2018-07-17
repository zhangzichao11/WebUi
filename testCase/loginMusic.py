"""
登陆界面的case
继承Driver类,获取浏览器的driver
"""
import time
#导入浏览器driver类
from common.webDriver import webDriver
#导入界面元素类
import pageElement.loginPage as loginPage
#导入日志模块类
from common.md_logger import myLog
#导入公共方法类
from common.common import common
import unittest

class loginMusic(webDriver,unittest.TestCase):

    #正常登陆的case
    def test_login1(self):
        myLog.logger().info("正常登录case")
        loginPage.setUserName(self.driver, 'zhangzichao@newborntown.com')
        loginPage.setUserPwd(self.driver, 'zhangzichao')
        loginPage.click_login(self.driver)
        time.sleep(5)
        isLogin = loginPage.isLogin(self.driver)
        try:
            self.assertEqual(isLogin, True)
            #登陆成功之后进行截屏
            common.Screenshot1()
            myLog.logger().info("info登录成功....%s", isLogin)
            loginPage.click_exit(self.driver)
        except Exception as e:
            #登陆失败之后进行截屏
            common.Screenshot1()
            myLog.logger().info("登录失败....%s", e)
    #用户名错误的case
    def test_login2(self):
        myLog.logger().info("用户名错误case")
        loginPage.setUserName(self.driver, 'zhangzichao1@newborntown.com')
        loginPage.setUserPwd(self.driver, 'zhangzichao')
        loginPage.click_login(self.driver)
        time.sleep(2)
        #用户名错误验证之后进行截屏
        common.Screenshot1()
    # 密码错误的的case
    def test_login3(self):
        myLog.logger().info("密码错误case")
        loginPage.setUserName(self.driver, 'zhangzichaoaa@newborntown.com')
        loginPage.setUserPwd(self.driver, 'zhangzichao1')
        loginPage.click_login(self.driver)
        time.sleep(2)
        #验证密码错误之后进行截屏
        common.Screenshot1()