# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:30:21 2024

@author: ASUS
"""

a = float(input("nhap a"))
b = float(input("nhap b"))
c = float(input("nhap c"))
a!=0
dt = b**2 -4*a*c
if dt<0:
    print("phuong trinh vo nghiem")
elif dt==0:
    print("phuong trinh co 1 nghiem kep x=", -b/(2*a))
else:
    x1 = ((-b) + (dt)**1/2)/2*a
    x2 = ((-b) - (dt)**1/2)/2*a
    print("phuong trinh co 2 nghiem phan biet x1, x2 lan luot la ", x1,x2)