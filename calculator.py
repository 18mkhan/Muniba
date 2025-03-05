class Calculator:
	def __init__(self):
		self.acc = 0

	def Add(self,value):
		self.acc += value

	def Subtract(self,value):
		self.acc -= value

	def multiply(self,value):
		self.acc *= value

	def Divide(self,value):
		self.acc /= value

MyCalc = Calculator()
MyCalc.Add(4)
MyCalc.Add(3)

import math
class Scientific(Calculator):

	def sin(self):
		self.acc = math.sin(self.acc)
		
	def cos(self):
		self.acc = math.cos(self.acc)

	def tan(self):
		self.acc = math.cos(self.acc)

MyCalc = Scientific(Calculator)
MyCalc.sin(30)

class Programmingcalc(calculator):
	base = 10
	def setBinary(self):
		self.base = 2
	def setHex(self):
		self.hex = 16

	def equal(self):
		if self.base == 10:
			super.equal()
		else:
			temp = self.convertBase(self.acc, self.base)
			print(temp)
	def convertBase(self,value,base):
		if value < base: return str(self.transalateHex
