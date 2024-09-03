# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:10:00 2024

@author: ASUS
"""

a =int(input("nhap so xe cua ban (gom 4 so): "))
b = a//100 + a%100 
c = b//10 + b%10 
d = c//10 + c%10
if 999< a <=9999:
    print("so nut cua xe ban la: ", d)
else:
    print("khong hop le!")
    