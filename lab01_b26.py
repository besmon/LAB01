# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:48:19 2024

@author: ASUS
"""

#cau a
a = float(input("nhap a"))
b = float(input("nhap b"))
c = float(input("nhap c"))
print(" thu tu tang dan la: ", sorted([a,b,c]))

#cau b
x = int(input("nhap x"))
y = list(str(x))
y.sort()
print("thu tu tang dan: ", int("".join(y)))
