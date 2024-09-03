# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:15:50 2024

@author: ASUS
"""

a = float(input("nhap a"))
b = float(input("nhap b"))
c = float(input("nhap c"))

if a==b==c:
    print("nhap so khac") 
else:
    if a>b and a>c:
        gtln = a
    elif b>a and b>c:
        gtln = b
    else:
        gtln = c
print("gia tri lơn nhat la: ", gtln)