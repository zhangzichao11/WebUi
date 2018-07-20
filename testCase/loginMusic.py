"""
登陆界面的case,登录数据来自于excel
根据用例名来区分进行不同情况的验证，并获取实际验证结果和excel里面的
预期结果进行对比
继承Driver类,获取浏览器的driver
作者:zhangzichao
"""
import time
#导入浏览器driver类
from common.webDriver import webDriver
#导入界面元素类
import pageElement.loginPage as login_Page
#导入日志模块类
from common.md_logger import myLog
#导入公共方法类
import common.common as common
import unittest
import paramunittest
loginCase = common.get_excel_value('login')
@paramunittest.parametrized(*loginCase)
class loginMusic(webDriver, unittest.TestCase):
    def setParameters(self, case_Name, user_Name, user_Pwd, excepted, reMarks):
        self.case_Name = case_Name
        self.user_Name = user_Name
        self.user_Pwd = user_Pwd
        self.excepted = excepted
        self.reMark = reMarks
    #正常登陆的case
    def test_Login(self):
        #设置用例名称
        self._testMethodDoc = self.case_Name
        myLog.logger().info('测试用例名称:' + self._testMethodDoc)
        myLog.logger().info('测试用例说明:' + self.reMark)
        login_Page.setUserName(self.driver, self.user_Name)
        login_Page.setUserPwd(self.driver, self.user_Pwd)
        login_Page.click_login(self.driver)
        #根据用例名称识别,对正常登录的case进行判断是否登录成功
        if self._testMethodDoc == 'test_login1':
            time.sleep(5)
            isLogin = login_Page.isLogin(self.driver)
            try:
                myLog.logger().info("实际结果的值是:%s", isLogin)
                myLog.logger().info("预期结果的值是:%s", self.excepted)
                self.assertEqual(isLogin, self.excepted)
                #登陆成功之后进行截屏
                common.Screenshot1()
                myLog.logger().info("info登录成功....%s", isLogin)
                login_Page.click_exit(self.driver)
            except Exception as e:
                #登陆失败之后进行截屏
                common.Screenshot1()
                myLog.logger().info("登录失败....%s", e)
        #根据用例名称识别，对用户名错误,密码正确的case进行验证
        elif self._testMethodDoc == 'test_login2':
            time.sleep(2)
            common.Screenshot1()
            #获取实际的结果值
            act_text = login_Page.userName_Error(self.driver)
            myLog.logger().info("实际结果的值是:%s", act_text)
            myLog.logger().info("预期结果的值是:%s", self.excepted)
            #和预期的结果值进行对比
            self.assertEqual(act_text, self.excepted)
        #根据用例名称识别，对用户名正确,密码错误的case进行验
        elif self._testMethodDoc == 'test_login3':
            time.sleep(2)
            common.Screenshot1()
            #获取实际结果值
            act_text = login_Page.userName_Error(self.driver)
            myLog.logger().info("实际结果的值是:%s", act_text)
            myLog.logger().info("预期结果的值是:%s", self.excepted)
            # 和预期的结果值进行对比
            self.assertEqual(act_text, self.excepted)
