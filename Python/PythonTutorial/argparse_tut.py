# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:14:43 2020

@author: Sakshi Agarwal
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation", choices = ["add","sub","mul"])
    
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    
    if args.operation == 'add':
        res = n1+n2
    elif args.operation == 'sub':
        res = n1-n2
    elif args.operation == 'mul':
        res = n1*n2
    else:
        print('unsupported arguments')
    
    print("Result=", res)

