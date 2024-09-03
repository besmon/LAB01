# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:50:44 2024

@author: ASUS
"""

print("Nhập thời gian đầu tiên:")
h1= int(input("Nhập giờ: "))
m1 = int(input("Nhập phút: "))
s1 = int(input("Nhập giây: "))
print("Nhập thời gian thứ hai:")
h2 = int(input("Nhập giờ: "))
m2 = int(input("Nhập phút: "))
s2 = int(input("Nhập giây: "))
if 0<=h1<24 and 0<=m1<60 and 0<=s1<60 and 0<=h2<24 and 0<=m2<60 and 0<=s2<60:
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 +m2*60 +s2
    T = t1+t2
    H = t1-t2
    
    gio_T = T//3600
    phut_T = (T//3600)//60
    giay_T = (T//3600)%60
    
    gio_H = H//3600
    phut_H = (H//3600)//60
    giay_H = (H//3600)%60
    
    print(f"tong 2 gio la: {gio_T} gio, {phut_T} phut, {giay_T} giay")
    print(f"hieu 2 gio la: {gio_H} gio, {phut_H} phut, {giay_H} giay")
else:
    print("khong hop le!")