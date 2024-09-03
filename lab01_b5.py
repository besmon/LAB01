# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:47:05 2024

@author: ASUS
"""

time = input("nhập vào giờ, phút, giây (theo định dạng hh:mm:ss): ")
hh, mm, ss = map(int, time.split(":"))
if 0<=hh<24 and 0<=mm<60 and 0<=ss<60:
    a= hh*3600 + mm*60 + ss
    print("tổng số giây đổi ra là: ", a)
else:
    print("không hợp lệ!")