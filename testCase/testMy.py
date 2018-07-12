from common.webDriver import Driver
import unittest
import time
import os
import HTMLTestRunner
import testCase.loginMusic as loginMusic
import unittest
from common.md_logger import myLog
if __name__ == '__main__':
      print(os.path.join(os.path.dirname(__file__) + '/'))
      suite = unittest.defaultTestLoader.discover(
            start_dir=os.path.join(os.path.dirname(__file__) + '/'),
            pattern='login*.py',
            top_level_dir=None)
      print(os.path.join(os.path.dirname(__file__) + '/'))
      #suite = unittest.makeSuite(unittest.TestCase)
      #获取report的存放路径
      filePath = myLog().getReportPath()
      print("路径是:",filePath)
      fb = open(filePath, 'wb')
      print("fb是:",fb)
      runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='WEB UI TEST', description='Test Description')
      print("suite",suite)
      runner.run(suite)