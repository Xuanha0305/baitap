# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:24:10 2024

@author: Xuanha 
"""

a=float(input("nhập hệ số a: "))
b=float(input("nhập hệ số b: "))
if a==0 and b!=0:
    print("phương trình vô nghiệm ")
elif a==0 and b==0:
    print("phương trình có vô số nghiệm  ")
elif a!=0 and b!=0:
    print("phương trình có nghiệm duy nhất x=", -b/a )
else:
    print("không xác định ")
    
    
