#!/usr/bin/python
# Date : 17-April-2018
# Purpose : Basic Calculator

A = int(input ("ENter the value for A : "))
B = int(input ("ENter the value for B : "))
C = int(input("Enter your option \n 1) SUM \n 2) Subtraction \n 3) Multiplicaton \n 4) Division : "))

if (C == 1):
    print ("A + B = ", A + B)
elif (C == 2):
    print ("A - B = ", A - B)
elif (C == 3):
    print ("A * B = ", A * B)
elif (C == 4):
    print ("A / B = ", A / B)
else:
    print ("Enter a valid option and try again")

#End