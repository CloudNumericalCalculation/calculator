#coding: utf-8
from __future__ import division
import sys
import math
try:
	expression = input()['expression']
	expression = expression.replace("^", "**");
	expression = expression.replace("and", "&");
	expression = expression.replace("xor", "^");
	expression = expression.replace("or", "|");
	expression = expression.replace("pi", "math.pi");
	expression = expression.replace("e", "math.e");
	expression = expression.replace("sqrt", "math.sqrt");
	expression = expression.replace("asin", "arcS");
	expression = expression.replace("acos", "arcC");
	expression = expression.replace("atan", "arcT");
	expression = expression.replace("sin", "math.sin");
	expression = expression.replace("cos", "math.cos");
	expression = expression.replace("tan", "math.tan");
	expression = expression.replace("arcS", "math.asin");
	expression = expression.replace("arcC", "math.acos");
	expression = expression.replace("arcT", "math.atan");
	expression = expression.replace("log", "math.log10");
	expression = expression.replace("ln", "math.log");
	expression = eval(expression)
except:
	print '请输入正确的表达式'
	sys.exit(1)
print expression
sys.exit(0)
