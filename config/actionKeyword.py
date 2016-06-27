# -*- coding:utf-8 -*-
__author__ = 'tsbc'

from selenium import webdriver
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from public import BasePage

class Actionkeywords(BasePage.Action):
	"""定义关键字方法"""

	def openBrowser(self):
		"""打开浏览器方法"""
		self.driver = webdriver.Chrome()

		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

	def navigate(self, url):
		"""
		跳转Url地址
		"""
		self.driver.get(url)
		time.sleep(3)
		current_url = self.driver.current_url  #当前页面的地址链接
		print "实际跳转的链接url:"+current_url
		if current_url.split(':')[0] =="https": #如果跳转的网页是https 直接不运行
			raise ValueError(u'the reques of HTTPS is not what we want')
		
	def closeBrowser(self):
		"""关闭浏览器"""
		self.closealert()
		self.saveScreenshot(self.driver, "submit02")  #截图
		self.driver.quit()

	#调用send_keys
	def input_Text(self, loc, text):
		"""文本框输入内容"""
		#print loc,text
		self.send_keys(loc, text)  #send_keys 方法中就包含对输入文本框的click()和clear()  太机智了
	#
	def Submit(self, submit_loc):
		"""提交表单"""
		self.saveScreenshot(self.driver, "submit01")  #截图
		self.find_element(*submit_loc).click()

	def clickButton(self, button_loc):
		"""点击按钮"""
		#print self.find_element(*button_loc).text
		self.find_element(*button_loc).click()

	def clickElement_i(self, index, *element_loc):
		"""点击元素"""
		# print self.find_elements_i(i, *element_loc)
		self.find_elements_i(*element_loc, index=index).click()

	def verifyLogin(self, span_loc, userid_loc):
		"""登录校验"""
		spanTF = True
		try:
			#通过捕获异常，判断是否显示的出了Tip文本，显示为 True 否则为False
			self.find_element(*span_loc).text
			spanTF = True
		except:
			spanTF = False

		if spanTF:
			print self.find_element(*span_loc).text
		else:
			print self.driver.title
			self.checkTrue(self.driver.find_element(*userid_loc).text, u"登录失败")
	def switchframe(self, loc):
		#jc环境和真实环境可能 在这个iframe是有区别的，所以是否存在不影响下程序运行
		#switch_to_frame  支持id和name 如果还是不行，后面再完善
		#可能还需要考虑下进入和出来这两个动作
		#print loc  #[u'id', u'x-URS-iframe']
		try:
			#self.find_element(*loc)
			self.driver.switch_to_frame(self.find_element(*loc))   #loc是个列表  driver.switch_to_frame("login_frame")
			#self.driver.switch_to_frame(loc[1])  如果是id或者name 查找的iframe，这样也可以，上面那种方法比较支持多种方式
			#print "switch sucess"
		except:
			print "switch faile"

	def clearinput(self, *input_loc):
		"""清空input的内容 只是备用，不一定用得上,后面发觉 send_input()的时候就有这个判断了，这个方法确实多余了"""
		#
		self.find_element(*input_loc).clear()

	#调用send_keys
	def verifycode(self, loc):
		"""验证码输入内容"""
		#print loc,text
		try :
			self.send_keys(loc, "1234")
			#print u"由于出现验证码，验证码内容暂时输入1234，所以登录无法成功"
		except:
			print u"不需要输入验证码或输入失败"
	
	
