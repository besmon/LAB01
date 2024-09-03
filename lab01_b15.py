# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:13:01 2024

@author: ASUS
"""

a = float(input("nhap a: "))
b = float(input("nhap b: "))
c = (a+b)/(((a)**(1/3))+((b)**(1/3)))
d = (a*b)**(1/3)
e = (a)**(1/3)
f = ((b)**(1/3))
A = (c - b) / ((e-f)**2)
print("ket qua la: ", round(A,3))
