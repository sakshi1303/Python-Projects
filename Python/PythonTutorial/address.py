# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:43:11 2020

@author: Sakshi Agarwal
"""

book = {}

book['tom'] = {
        'name' : 'tom',
        'address' : '1 red street, NY',
        'phone' : 98989898
     }

book['bob'] = {
        'name' : 'bob',
        'address' : '1 green street, NY',
        'phone' : 23424234
        }

import json
s= json.dumps(book)
with open("E://Technical//Python//book.txt", "w") as f:
    f.write(s)
    
print('done!!')    
