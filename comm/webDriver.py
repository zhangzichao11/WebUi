from selenium import webdriver
from comm.md_logger import myLog
import comm.md_config as myConfig
#根据配置选择浏览器类型
class webDriver:

    """ @classmethod
     def setUp(cls):
         print("do something before test.Prepare environment.")

     @classmethod
     def tearDown(cls):
         print("do something after test.Clean up.")"""
    @classmethod
    def tearDownClass(cls):
        #所有的test运行完后运行一次
        print("tearDownClass\n")
        #关闭浏览器驱动
        cls.driver.quit()
        #cls.driver.close()

    # noinspection PyGlobalUndefined
    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        global driver
        #所有的test运行前运行一次
        # noinspection PyUnreachableCode
        #获取浏览器配置信息
        browserType = int(myConfig.getDriver())
        #获取测试url
        testUrl = myConfig.getUrl()
        if browserType == 1:
            fp = webdriver.FirefoxProfile()
            # 设置下载方式, 0是桌面 1是我的下载 2是自定义
            fp.set_preference("browser.down.folderList", 2)
            # 自定义下载地址
            fp.set_preference("browser.download.dir", 'f:\\project')
            # 总是询问文件的保存位置,True代表不再询问
            fp.set_preference("browser.download.useDownloadDir", True)
            # 下载的时候是否显示下载管理器；默认true显示，false不显示
            fp.set_preference("browser.download.manager.showWhenStarting", False)
            # 无需确认下载的文件格式
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                              "application/octet-stream, application/vnd.ms-excel,"
                              " text/csv, application/zip,application/xml")
            try:
                cls.driver = webdriver.Firefox()
            except Exception as e:
                myLog.logger().error('浏览器firefox driver有误 %s', e)
        elif browserType == 2:
            try:
                #download.default_directory：设置下载路径
                #profile.default_content_settings.popups：设置为0,禁止弹出窗口
                options = webdriver.ChromeOptions()
                prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'f:\\project'}
                options.add_experimental_option('prefs', prefs)
                cls.driver = webdriver.Chrome(chrome_options=options)
            except Exception as e:
                myLog.logger().error('浏览器chrome driver有误 %s', e)
        cls.driver.get(testUrl)
        cls.driver.maximize_window()
