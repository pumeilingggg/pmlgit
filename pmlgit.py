# from selenium import  webdriver
# dir = webdriver.Chrome()
# dir.get('http://www.baidu.com')
#
# from selenium import webdriver
# browser = webdriver.Chrome
# browser.quit()
#
# #引入web

# from  selenium import webdriver #引入驱动
# import time #引入时间
#
# driver = webdriver.Chrome()  #引入谷歌驱动
# driver.get('http://www.baidu.com')  #打开百度页面
# time.sleep(2)  #停留两秒
# driver.refresh()  #刷新
# driver.maximize_window()  #最大化页面
#
# driver.get('http://www.taobao.com')  #打开淘宝
# driver.back()  #回退到上一个页面
# driver.forward()  #前进一个页面
#
# time.sleep(3)  #停留3秒
#
# driver.quit()  #退出浏览器

from  selenium import webdriver #引入驱动
import time #引入时间

driver = webdriver.Chrome()  #引入谷歌驱动
driver.get('http://www.baidu.com')  #打开百度页面
driver.find_element_by_id('kw').send_keys('新闻') #输入内容
driver.find_element_by_class_name('s_btn').click() #点击按钮
time.sleep(2)  #停留两秒
driver.find_element_by_partial_link_text('中心首页_新浪网').click() #点击新浪网
time.sleep(2)  #停留两秒

