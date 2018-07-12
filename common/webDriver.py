from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import common.md_logger as myLogger
import common.md_config as myConfig
#根据配置选择浏览器类型
class Driver(object):

    def __init__(self,*args):
        print("执行了哦。。。。。")
        global driver
        myLog = myLogger.myLog.logger()
        browserType = int(myConfig.getDriver())
        testUrl = myConfig.getUrl()
        if browserType == 1:
            fp = webdriver.FirefoxProfile()
            # 设置下载方式, 0是桌面 1是我的下载 2是自定义
            fp.set_preference("browser.down.folderList", 2)
            # 自定义下载地址
            fp.set_preference("browser.download.dir", "E:\\fileUp\\excel")
            # 总是询问文件的保存位置,True代表不再询问
            fp.set_preference("browser.download.useDownloadDir", True)
            # 下载的时候是否显示下载管理器；默认true显示，false不显示
            fp.set_preference("browser.download.manager.showWhenStarting", False)
            # 无需确认下载的文件格式
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                              "application/octet-stream, application/vnd.ms-excel,"
                              " text/csv, application/zip,application/xml")
            try:
                driver = webdriver.Firefox()
            except Exception as e:
                myLog.error('浏览器firefox driver有误 %s', e)

        elif browserType == 2:
            try:
                driver = webdriver.Chrome()
            except Exception as e:
                myLog.error('浏览器chrome driver有误 %s', e)
        driver.get(testUrl)
        driver.maximize_window()



    '''def __new__(cls, *args, **kwargs):
        print("单例模式运行")
        #单例模式运行浏览器
        if not hasattr(Driver, '_instance'):
                Driver._instance = object.__new__(cls)
        return Driver._instance'''
