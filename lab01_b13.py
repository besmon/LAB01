# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:11:28 2024

@author: ASUS
"""

a = int(input("nhap ngày: "))
b = int(input("nhap thang: "))
c = int(input("nhap nam: "))
#cau a
if 1<=a<31 and 1<=b<12 and c>0:
    print("ngay thang nam sinh la: ", f"{a}/{b}/{c}")
#cau b
    print("ngay thang nam sinh la: ", f"{a}/{b}/{str(c) [2:]}")
#cau c
    print("ngay thang nam sinh la: ", f"{c}/{b}/{a}")
else:
    print("không hợp lệ!")
    