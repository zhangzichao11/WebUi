"""
该类主要是存放一些公共方法，比如：元素查找、截屏
、操作Excel等等
"""
#导入日志模块
from common.md_logger import myLog
#导入截图模
from PIL import ImageGrab
import time,os
import shutil
class common:
    #查找某个元素是否存在
    @staticmethod
    def isElementExist(flag,driver,xpath):
        isExist = True
        if flag == 0:
            # noinspection PyBroadException
            try:
                driver.find_element_by_xpath(xpath).is_displayed()
            except Exception as e:
                myLog.logger().error("元素查找出错%s",e)
                isExist = False
            return isExist
        elif flag == 1:
            # noinspection PyBroadException
            try:
                driver.find_element_by_id(xpath).is_displayed()
            except Exception as e:
                myLog.logger().error("元素查找出错%s", e)
                isExist = False
            return isExist
        elif flag == 2:
            try:
                driver.find_elements_by_name(xpath).is_displayed()
            except Exception as e:
                myLog.logger().error("元素查找出错%s", e)
                isExist = False
            return isExist
    #截屏功能
    @staticmethod
    def Screenshot(imPath,imType):
        im = ImageGrab.grab()
        im.save(imPath, imType)

    @staticmethod
    def Screenshot1():
        # 文件的日期格式
        rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        # log文件的存放路径
        imPath = os.path.split(os.path.dirname(__file__))[0] + '/result/image/' + rq + '.png'
        im = ImageGrab.grab()
        im.save(imPath)
    #删除文件夹内容
    @staticmethod
    def delFile(path):
        shutil.rmtree(path)
        os.makedirs(path)

