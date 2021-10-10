# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:25:31 2020

@author: Sakshi Agarwal
"""

class Accident(Exception):
    
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User Defined Exception ", self.msg)


try:
    ##raise MemoryError('memory error')
    raise Accident('crash between two cars')
except MemoryError as e:
    print(e)
except Accident as e:
    e.print_exception()    