# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:47:05 2020

@author: Sakshi Agarwal
"""

class Human:
    
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
        
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis.")
        elif self.occupation == "actor":
            print(self.name, "shoots films.")
    
    def speaks(self):
        print(self.name, "says how are you?")
        

tom = Human("Tom Cruise", "actor")
tom.do_work()
tom.speaks()    

maria = Human("Maria Sharapova", "tennis player")
maria.do_work()
maria.speaks()    