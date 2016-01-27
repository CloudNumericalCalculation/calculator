import os
import math
try:
	expression = raw_input()
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
	print expression
	os._exit(0)
except:
	os._exit(1)
