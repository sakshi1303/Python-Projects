# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:59:30 2020

@author: Sakshi Agarwal
"""

class Vehicle:
    
    def general_usage(self):
        print("general use: transportation")
        
        
class Car(Vehicle):
    
    def __init__(self):
        print("I am Car.")
        self.wheels = 4
        self.has_roof = True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family.")
        
        
class MotorCycle(Vehicle):
    
    def __init__(self):
        print("I am MotorCycle.")
        self.wheels = 2
        self.has_roof = False
        
    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing.")
        
        
c = Car()
##c.general_usage()
c.specific_usage()

m = MotorCycle()
##m.general_usage()
m.specific_usage()

print(isinstance(c, Car))
print(isinstance(m, Car))


print(issubclass(Car, Vehicle))
print(issubclass(Car, MotorCycle))




        