# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:25:21 2020

@author: Sakshi Agarwal
"""

x =  input("Enter number1:")
y =  input("Enter number2:")
try:
    z = x / int(y)
except ZeroDivisionError:
    print('Division by zero Exception..')
    z = None
except TypeError:
    print('TypeError Exception occured..')
    z = None    
except Exception as e:
    print('Exception occured: ', e, " ", type(e).__name__)
    z = None
print('Division is: ', z)