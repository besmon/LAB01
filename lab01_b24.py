# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:39:15 2024

@author: ASUS
"""

h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
if 0<=h<24 and 0<=m<60 and 0<=s<60:
    print(" gio, phut, giay hop le: ", f"{h}:{m}:{s}")
else:
    print("khong hop le!")