# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:11:45 2020

@author: Sakshi Agarwal
"""

class Father():
    
    def gardening(self):
        print("I enjoy Gardening.")
        
    def skills(self):
        print("programming, teaching")

class Mother():
    
    def cooking(self):
        print("I enjoy Cooking.")
        
        
    def skills(self):
        print("art, teaching")
        
        
class Child(Father, Mother):
    
    def sports(self):
        print("I enjoy Sports.")


    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("running")

c = Child()
c.gardening()
c.cooking()
c.sports()
c.skills()        