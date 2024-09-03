# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:41:56 2024

@author: ASUS
"""

N = int(input("nhập số nguyên N có 2 chữ số: "))
a = N//10 + N%10
if 10<=N<=99:
    print("tổng các chữ số của N: ", a)
else:
    print("không hợp lệ!")