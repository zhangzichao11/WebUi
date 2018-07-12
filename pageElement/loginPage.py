"""
登陆界面的元素
"""
from common.common import common
#登录名
def setUserName(driver,userName):
    print("\nmyDriver",driver)
    driver.find_element_by_name('email').send_keys(userName)
#登录密码
def setUserPwd(driver, userPwd):
    driver.find_element_by_name('password').send_keys(userPwd)
#登录按钮
def click_login(driver):
    driver.find_element_by_id('login').click()
#判断是否登录成功
#0:xpath 1:id 2:name
def isLogin(driver):
    isExist = common.isElementExist(0,driver,'//*[@id="wrapper"]/nav/ul/li[1]/a')
    return isExist
#退出登录
def click_exit(driver):
    driver.find_element_by_xpath('//*[@id="wrapper"]/nav/ul/li[2]/a').click()
