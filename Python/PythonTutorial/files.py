# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:07:41 2020

@author: Sakshi Agarwal
"""

f = open("E:\\Technical\\Python\\test.txt", "a") 
""" f.write("\nI love SQL.") """
f.close()



fr = open("E:\\Technical\\Python\\test.txt", "r")
fw = open("E:\\Technical\\Python\\test_wc.txt", "w")

"""print(fr.read()) """

for line in fr:
    tokens = line.split(' ')
    fw.write("wordcount:" + str(len(tokens)) + " " + line)
    print(len(tokens))

fw.close()
fr.close()

 
with open("E:\\Technical\\Python\\test.txt", "r") as fw:
    print(fw.read())
    
    
print(fw.closed)    