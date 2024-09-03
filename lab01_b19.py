# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:17:59 2024

@author: ASUS
"""

a = int(input("nhap a"))
b = int(input("nhap b"))
c = int(input("nhap c"))
d = int(input("nhap d"))

if a==b==c==d:
    print("nhap so khac") 
else:
    if a<b and a<c and a<d:
        gtnn = a
    elif b<a and b<c and b<d:
        gtnn = b
    elif c<a and c<b and c<d:
        gtnn = c
    else:
        gtnn = d
print("gia tri nho nhat la: ", gtnn)
    
    