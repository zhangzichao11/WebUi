import os
from common.HTMLTestRunner import HTMLTestRunner
import unittest
import common.md_config as myConfig
from common.common import common
from common.md_logger import myLog
if __name__ == '__main__':
      '''运行之前获取config.ini配置里面的result,0表示result文件夹下面的内容每次运行都保存下来，
      1表示只保存最后一次运行的结果'''
      result = myConfig.getResult()
      if result == 1:
            imPath = os.path.split(os.path.dirname(__file__))[0] + '/result/image'
            logPath = os.path.split(os.path.dirname(__file__))[0] + '/result/logs'
            reportPath = os.path.split(os.path.dirname(__file__))[0] + '/result/report'
            common.delFile(imPath)
            common.delFile(logPath)
            common.delFile(reportPath)
      suite = unittest.defaultTestLoader.discover(
            start_dir = os.path.join(os.path.dirname(__file__) + '/'),
            pattern = '*Music.py',
            top_level_dir = None)
      #获取report的存放路径
      filePath = myLog().getReportPath()
      fb = open(filePath, 'wb')
      runner = HTMLTestRunner(stream=fb, verbosity=2, title='WEB UI TEST', description='Test Description')
      runner.run(suite)