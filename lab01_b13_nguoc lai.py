# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:00:26 2024

@author: ASUS
"""

a = input("nhap ngay thang nam sinh (theo dinh dang ngay/thang/nam): ")
ngay, thang, nam = a.split("/")
#cau a
print(f"ngay {ngay}, thang {thang}, nam {nam}")
#cau b
print(f"ngay {ngay}, thang {thang}, nam {str(nam) [2:]}")
#cau c
print(f"nam {nam}, thang {thang}, ngay {ngay}")
