# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:59:39 2024

@author: ASUS
"""

hinh = input(" chon hinh (v - h.vuong, cn - h.chu nhat, t - h.tron): ")
if hinh == "v":
    a = float(input("nhap do dai canh hinh vuong "))
    S = a*a
    C = 4*a
    print(f"chu vi la {C}, dien tich la {S}")
elif hinh == "cn":
     r = float(input("nhap do dai chieu rong"))
     d = float(input("nhap do dai chieu dai"))
     S = r*d
     C = (r+d)*2
     print(f"chu vi la {C}, dien tich la {S}")
elif hinh == "t":
    R = float(input("nhap ban kinh hinh tron"))
    S = 3.14*R*R
    C = 2*3.14*R
    print(f"chu vi la {C}, dien tich la {S}")
else:
    print("khong hop le!")
    
