# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:32:59 2024

@author: ASUS
"""

gio = int(input("nhap gio: "))
phut = int(input("nhap phut: "))
giay = int(input("nhap giay: "))
if 0<=gio<24 and 0<=phut<60 and 0<=giay<60:
    A = gio*3600 + phut*60 + giay
    print("tong so giay la: ", A)
else:
    print("khong hop le!")