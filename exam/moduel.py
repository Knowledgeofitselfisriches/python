# def test():
# 	from random import *
# 	print(randint(1,9))
# 	print('---')
# print(globals())	
# import sys
# print(sys.path)
# print(sys.argv)# test()
# from datetime import datetime
# class User:
# 	status = False
# 	info   = {}
# 	logintime={}

# 	def __init__(self,name,psd,blist,):
# 		self.info['name'] = name
# 		self.info['psd']  = psd
# 		self.blist= blist
# 		self.logintime[name] = []
# 	def login(self,name,psd):
# 		if self.info['name'] == name and self.info['psd'] == psd:
# 			self.status = True

# 			self.logintime[name].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# 			print(self.logintime[name])
# 		else:
# 			print('密码或账号出错')	
# u = User('lwt','lwt',[])
# u.login('lwt','lwt')
# print(u.status)

# print(u.logintime)
# u.login('lwt','lwt')
# print(u.logintime)
import random

def security_code(n):

	char = []
	number =[str(i) for i in range(0,10)]
	low = [chr(i) for i in range(65,91)]
	upp = [chr(i) for i in range(97,123)]

	char.extend(upp)
	char.extend(low)
	char.extend(number)

	random.shuffle(char)

	print(" ".join(char[:n]))	

security_code(4)
# for i in dir(random):
# 	print(i)
print(random.randrange())
def code(n):
	code = ''
	for i in range(0,n):
		ran1 = random.randint(0,9)
		ran2 = chr(random.randint(65,90))
		ran = random.choice((ran1,ran2))
		"".join([code,str(ran)])
	return code	




