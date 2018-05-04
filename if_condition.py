#!/usr/bin/python
# Date : 17-Apr-2018
# Purpose : If condition example

a=int(input('Enter the value for A : '))

b=int(input('Enter the value for B : '))

print ("Welcome the value of A = ", a, " & value of B =",b)
'''
sum = a + b
sub = a - b
mul = a * b
div = a / b
asqu = a ** 2
bsqu = b ** 2
mod = a % b

print ("A + B = ", sum, '\n',"A - B = ", sub, "A * B = ", mul, "\n","A / B", div,"\n", "A ^2 = ", asqu,"\n","B ^2 = ",bsqu,"\n")
print ("---------------------------\n")
print ( a, "+", b, "=", sum, '\n', a, "-",b, "=", sub,"\n", a, "*",b, "=", mul, "\n",a, "/",b,"=", div,"\n",a, "^2 = ", asqu,"\n",b,"^2 = ",bsqu,"\n")

'''

if (a > b):
    print (a, "is Greater than", b)
elif (a < b):
    print (a, "is smaller than", b)
else:
    print (a, "is equal to", b)