from comm.webDriver import webDriver
#导入登录界面元素类
import pageElement.loginPage as loginPage
#导入后台主界面元素类
import pageElement.consolePage as consolePage
#导入日志模块类
from comm.md_logger import myLog
#导入公共方法类
import comm.common as common
import paramunittest
import unittest
import time
searchCase = common.get_excel_value('search')
@paramunittest.parametrized(*searchCase)
class searchMusic(webDriver,unittest.TestCase):
    def setParameters(self, case_Name, user_Name, user_Pwd,search_Id, file_Path, excepted, reMarks):
        self.case_Name = case_Name
        self.user_Name = user_Name
        self.user_Pwd = user_Pwd
        self.search_Id = search_Id
        self.file_Path = file_Path
        self.excepted = excepted
        self.reMark = reMarks
    def test_search(self):
        # 设置用例名称
        self._testMethodDoc = self.case_Name
        myLog.logger().info('测试用例名称:' + self._testMethodDoc)
        myLog.logger().info('测试用例说明:' + self.reMark)
        if self._testMethodDoc == 'test_search':
            time.sleep(5)
            #先进行正常的登录
            loginPage.setUserName(self.driver, self.user_Name)
            loginPage.setUserPwd(self.driver, self.user_Pwd)
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
            consolePage.click_MusicNote(self.driver)
            time.sleep(2)
            #输入要查询的playid
            consolePage.input_Id(self.driver,self.search_Id)
            #点击查询按钮
            consolePage.click_Query(self.driver)
            #点击导出歌单选项
            consolePage.export_list(self.driver)
            #点击对话框的的导出按钮
            time.sleep(2)
            consolePage.export_btn(self.driver)
            time.sleep(6)
            #导入歌单文件
            consolePage.import_list(self.driver,self.file_Path)
            time.sleep(5)
            common.Screenshot1()
            self.assertEqual(True,self.excepted)
            myLog.logger().info("歌单导入成功....")