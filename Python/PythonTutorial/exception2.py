# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:38:37 2020

@author: Sakshi Agarwal
"""

def process_file():
    
    try:
        f = open("E:\\Technical\\Python\\test.txt") 
        x = 1/0
    except FileNotFoundError as e:
        print("inside except..")
        
    finally:
        print("cleaning up file.")
        f.close()
        print(f.closed)


process_file()    
