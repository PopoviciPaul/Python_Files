#import operator
#ops = { "+": operator.add, "-": operator.sub } # etc.

#print(ops["-"](1,1)) # prints 2


# Hello World program in Python
from numbers import Number    
import operator
import re

#xx = '134*34'
#r1 = re.findall(r"[0-9]+[-+*/][0-9]+", xx)


#expression = str(r1[0])
#print(expression)                         # you have the expression: term1 <sign> term2

#terms = re.findall(r"[0-9]+", expression) # you have the terms in terms[0], terms[1]

#sign = re.findall(r"[-+*/]" ,expression)

#print("Term 1 is: %d" % float(terms[0]))
#print("Term 2 is: %d" % float(terms[1]))
#print("Sign is: %s" % sign[0])


#x = "result = float(terms[0]) {} float(terms[1])".format(sign[0])

#print(x)
#exec(x)

#string_to_execute = 'result=x' 

#exec(string_to_execute)


strg = "-10.55+3"


terms = re.findall("[-+]?\d*\.\d+|\d+", strg)

#terms = re.findall(r"[0-9]+\.?[0-9]+", strg)
print(terms)
