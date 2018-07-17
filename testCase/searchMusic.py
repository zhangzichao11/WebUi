from common.webDriver import webDriver
#导入登录界面元素类
import pageElement.loginPage as loginPage
#导入后台主界面元素类
import pageElement.consolePage as consolePage
#导入日志模块类
from common.md_logger import myLog
#导入公共方法类
from common.common import common
import unittest
import time
class searchMusic(webDriver,unittest.TestCase):
    def test_search(self):
        #进行正常的登录
        loginPage.setUserName(self.driver, 'zhangzichao@newborntown.com')
        loginPage.setUserPwd(self.driver, 'zhangzichao')
        loginPage.click_login(self.driver)
        time.sleep(5)
        isLogin = loginPage.isLogin(self.driver)
        try:
            self.assertEqual(isLogin, True)
            # 登陆成功之后进行截屏
            common.Screenshot1()
            myLog.logger().info("info登录成功....%s", isLogin)

        except Exception as e:
            # 登陆失败之后进行截屏
            common.Screenshot1()
            myLog.logger().info("登录失败....%s", e)
        #点击左侧的音乐歌单选项
        #consolePage.click_SoloSecurity(self.driver)
        #consolePage.click_AdsSdk(self.driver)
        consolePage.click_musicNote(self.driver)