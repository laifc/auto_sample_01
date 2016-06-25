# -*- coding:utf-8 -*-
__author__ = 'tsbc'

from selenium import webdriver
import unittest
import HTMLTestRunner
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from public import BasePage
from config import actionKeyword
maillist=[]
otherlist=[]
class Mail_Case(unittest.TestCase):
	"""邮箱类的入口引擎"""
	#脚本初始化
	@classmethod
	def setUpClass(cls):
		print "setUpClass"
		# cls.driver = webdriver.Firefox()
		# cls.driver.implicitly_wait(30)
		cls.filepath = "dataEngine\\Book1.xls"

	#测试用例
	def action(self, *txt):
		"""
		测试Demo
		"""
		print "action"
		exeKeyword = actionKeyword.Actionkeywords()
		base = BasePage.Action()
		case_id = txt[1]
		geturl = txt[4]
		username = txt[5]
		password = txt[6]
		# casedata = base.getTabledata(self.filepath, "Test Cases")
		k =5
		stepdata = base.getTabledata(self.filepath, "Test Steps")
		print type(stepdata),"stepdata"
		for j in stepdata:
			if txt[0] == j[0]:
				#print j[2]
				#print j[0]
				# print j[3]
				if j[3] == "openBrowser":
					print j[2]  #步骤说明
					exeKeyword.openBrowser()
				elif j[3] == "input":
					#print
					print j[2]  #输入
					#j[4]  代表元素编号
					loc = base.locate(j[4])	#返回值内容为：("id","inputid")、("xpath","/html/body/header/div[1]/nav")格式
					print  loc  #[u'id', u'password1']
					exeKeyword.input_Text(loc, txt[k])   #k=4  第一次是账号，第二次是密码  username = txt[4]
					k += 1
				elif j[3] == "submit":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.Submit(loc)  #"""提交表单"""  会先截图
				elif j[3] == "verifyLogin": #登录校验
					print j[2]
					loc_1 = base.locate(j[4])
					loc_2 = base.locate(j[5])
					exeKeyword.verifyLogin(loc_1, loc_2)
					#def verifyLogin(self, span_loc, userid_loc):
				elif j[3] == "closeBrowser":
					print j[2]
					time.sleep(5)
					exeKeyword.closeBrowser()
				elif j[3] == "geturl":
					print j[2]
					url = txt[4]
					exeKeyword.navigate(url)
				elif j[3] == "clickelement":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.clickElement_i(0, loc)  #为什么index要设2？被我修改成0
				elif j[3] == "switchframe":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.switchframe(loc)
					#print

				elif j[3] == "verifycode":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.verifycode(loc)

					#可能还有其他功能，但是没有用到就没有拿出来判断  这个可能会存在问题，但是考虑性能的话这个是对的

	@staticmethod   #？什么功能
	def getTestFunc(*txt):
		def func(self):
			self.action(*txt)
		return func    #返回一个test函数对象出去

	#脚本退出
	@classmethod
	def tearDownClass(cls):
		print "End"
		# cls.driver.quit()

class Other_Case(unittest.TestCase):
	"""其他网站的入口引擎"""
	#脚本初始化
	@classmethod
	def setUpClass(cls):
		print "setUpClass"
		# cls.driver = webdriver.Firefox()
		# cls.driver.implicitly_wait(30)
		cls.filepath = "dataEngine\\Book1.xls"

	#测试用例
	def action(self, *txt):
		"""
		测试Demo
		"""
		print "action"
		exeKeyword = actionKeyword.Actionkeywords()
		base = BasePage.Action()
		case_id = txt[1]
		username = txt[5]
		password = txt[6]
		# casedata = base.getTabledata(self.filepath, "Test Cases")
		k =5
		stepdata = base.getTabledata(self.filepath, "Test Steps")
		print type(stepdata),"stepdata"
		for j in stepdata:
			if txt[0] == j[0]:
				if j[3] == "openBrowser":
					print j[2]  #步骤说明
					exeKeyword.openBrowser()
				elif j[3] == "input":
					print j[2]  #输入
					#j[4]  代表元素编号
					loc = base.locate(j[4])	#返回值内容为：("id","inputid")、("xpath","/html/body/header/div[1]/nav")格式
					print  loc  #[u'id', u'password1']
					exeKeyword.input_Text(loc, txt[k])   #k=4  第一次是账号，第二次是密码  username = txt[4]
					k += 1
				elif j[3] == "submit":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.Submit(loc)  #"""提交表单"""  会先截图
				elif j[3] == "verifyLogin": #登录校验
					print j[2]
					loc_1 = base.locate(j[4])
					loc_2 = base.locate(j[5])
					exeKeyword.verifyLogin(loc_1, loc_2)
					#def verifyLogin(self, span_loc, userid_loc):
				elif j[3] == "closeBrowser":
					print j[2]
					time.sleep(5)
					exeKeyword.closeBrowser()
				elif j[3] == "geturl":
					print j[2]
					url = txt[4]
					exeKeyword.navigate(url)
				elif j[3] == "clickelement":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.clickElement_i(0, loc)  #为什么index要设2？被我修改成0 暂时写死只能选定元素的第一个
				elif j[3] == "switchframe":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.switchframe(loc)

				elif j[3]	==	"veritycode":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.veritycode(loc)
				'''
				elif j[3] == "clear":
					print j[2]
					loc = base.locate(j[4])
					exeKeyword.clearinput(loc)
				'''


					#print

					#可能还有其他功能，但是没有用到就没有拿出来判断  这个可能会存在问题，但是考虑性能的话这个是对的

	@staticmethod   #？什么功能
	def getTestFunc(*txt):
		def func(self):
			self.action(*txt)
		return func    #返回一个test函数对象出去

	#脚本退出
	@classmethod
	def tearDownClass(cls):
		print "End"
		# cls.driver.quit()


def __generateTestCases():
	print "__generateTestCases"
	login_page = BasePage.Action()
	mailcasedata = login_page.getTabledata("dataEngine\\Book1.xls", "Mail Cases")
	print mailcasedata
	for i in mailcasedata:
		TCid = i[0]
		if i[3] == "Y":
			print "【Run】"+i[1]+"："
			print " + -"*8
			table = login_page.getTabledata("dataEngine\\Book1.xls", "case data")
			print "case data",table
			for txt in table:
				if (txt[2] == "Y") & (txt[0] == TCid):
					#print txt,"txt"
					maillist.append("test_"+str(txt[0])+"_"+str(txt[1]))
					#[u'test_other_tianya', u'case_0005', u'Y', u'\u6b63\u786e\u7684\u7528\u6237\u540d\u3001\u5bc6\u7801\u9a8c\u8bc1', u'auto_tianya', u'123qwe', u'', u'', u'', u'', u'SKIP'] txt
					setattr(Mail_Case, 'test_%s_%s' % (txt[0], txt[1]), Mail_Case.getTestFunc(*txt))  ##通过setattr自动为TestCase类添加成员方法，方法以“test_”开头
					#setattr(x,“foobar”,123)相当于x.foobar = 123。  上面这行功能具体是什么，单元测试用例都是要以test开头的
	print maillist
	
	othercasedata = login_page.getTabledata("dataEngine\\Book1.xls", "Other Cases")
	print othercasedata
	for i in othercasedata:
		TCid = i[0]
		if i[3] == "Y":
			print "【Run】"+i[1]+"："
			print " + -"*8
			table = login_page.getTabledata("dataEngine\\Book1.xls", "case data")
			print "case data",table
			for txt in table:
				if (txt[2] == "Y") & (txt[0] == TCid):
					#print txt,"txt"
					otherlist.append("test_"+str(txt[0])+"_"+str(txt[1]))
					#[u'test_other_tianya', u'case_0005', u'Y', u'\u6b63\u786e\u7684\u7528\u6237\u540d\u3001\u5bc6\u7801\u9a8c\u8bc1', u'auto_tianya', u'123qwe', u'', u'', u'', u'', u'SKIP'] txt
					setattr(Other_Case, 'test_%s_%s' % (txt[0], txt[1]), Other_Case.getTestFunc(*txt))  ##通过setattr自动为TestCase类添加成员方法，方法以“test_”开头
					#setattr(x,“foobar”,123)相当于x.foobar = 123。  上面这行功能具体是什么，单元测试用例都是要以test开头的
	print otherlist	
	
	
__generateTestCases()



if __name__ == '__main__':


	#suite=unittest.makeSuite(ExecutionEngin)  #这个方法  会导致邮箱类型  微博类型等都在同一个class中  测试报告不好看   
	testunit=unittest.TestSuite()   #定义一个单元测试容器  
	for i in maillist:
		testunit.addTest(Mail_Case(i))
	for i in otherlist:
		testunit.addTest(Other_Case(i))	
	
	tt = time.strftime("%Y%m%d %H.%M.%S",time.localtime(time.time()))
	#定义自动化报告目录
	filename='C:\\JC_AutoReport '+tt+'.html'
	fp=file(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(
	stream=fp,
    title=u'33',
    description=u'2212'
    )
	runner.run(testunit)


