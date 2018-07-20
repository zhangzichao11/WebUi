"""
该类主要是存放一些公共方法，比如：元素查找、截屏
、操作Excel等等
"""
#导入日志模块
from common.md_logger import myLog
#导入截图模
from PIL import ImageGrab
#读excel模块
import xlrd
import time,os
import shutil
'''
filePath:current path
qr：file name format
'''
filePath = os.path.split(os.path.dirname(__file__))[0]
'''
find element
flag:True or Flase
xpath:element xpath
'''
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
'''
Screenshot function
imPath:picture save path
imType: picture type
'''
def Screenshot(imPath,imType):
    im = ImageGrab.grab()
    im.save(imPath, imType)

def Screenshot1():
    rq = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    # log文件的存放路径
    imPath = filePath + '/result/image/' + rq + '.png'
    im = ImageGrab.grab()
    im.save(imPath)
def Screenshot2(imPath):
    im = ImageGrab.grab()
    im.save(imPath)
'''
Delete folder content
path: folder path
'''
def delFile(path):
    shutil.rmtree(path)
    os.makedirs(path)
'''
excel_name:excel file name
sheet_name:sheet name
return:sheet value
'''
def get_excel_value(sheet_name):
    cls = []
    excel_path = filePath + '/data/testCase.xls'
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'case_Name':
            cls.append(sheet.row_values(i))
    return cls

