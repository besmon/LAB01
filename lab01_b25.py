# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:44:03 2024

@author: ASUS
"""

a = input("nhap 1 chu cai: ")
if len(a)==1 and a.islower():
    print("chu cai in hoa la: ", a.upper())
elif len(a)==1 and a.upper():
    print("chu cai viet thuong la: ", a.lower())
else:
    print("khong hop le!")