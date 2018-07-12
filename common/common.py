"""
该类主要是存放一些公共方法，比如：元素查找、截屏
、操作Excel等等
"""
from common.md_logger import myLog
myLog = myLog.logger()
class common:
    #查找某个元素是否存在
    @staticmethod
    def isElementExist(flag,driver,xpath):
        isExist = True
        if flag == 0:
            # noinspection PyBroadException
            try:
                print("driver的值是",driver)
                driver.find_element_by_xpath(xpath).is_displayed()
            except Exception as e:
                myLog.error("元素查找出错%s",e)
                isExist = False
            return isExist
        elif flag == 1:
            # noinspection PyBroadException
            try:
                driver.find_element_by_id(xpath).is_displayed()
            except Exception as e:
                myLog.error("元素查找出错%s", e)
                isExist = False
            return isExist
        elif flag == 2:
            try:
                driver.find_elements_by_name(xpath).is_displayed()
            except Exception as e:
                myLog.error("元素查找出错%s", e)
                isExist = False
            return isExist

