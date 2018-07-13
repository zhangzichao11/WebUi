import os
import HTMLTestRunner
import unittest
from common.md_logger import myLog
if __name__ == '__main__':
      print(os.path.join(os.path.dirname(__file__) + '/'))
      suite = unittest.defaultTestLoader.discover(
            start_dir=os.path.join(os.path.dirname(__file__) + '/'),
            pattern='loginMusic.py',
            top_level_dir=None)
      #获取report的存放路径
      filePath = myLog().getReportPath()
      fb = open(filePath, 'wb')
      runner = HTMLTestRunner.HTMLTestRunner(stream=fb, verbosity=2, title='WEB UI TEST', description='Test Description')
      runner.run(suite)