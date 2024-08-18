# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:16:54 2024

@author: Xuanha 
"""

a=float(input("nhập độ dài cạnh a: "))
b=float(input("nhập độ dài cạnh b: "))
c=float(input("nhập độ dài cạnh c: "))
if a+b>c and a+c>b and b+c>a:
    print("a, b, c là ba cạnh của tam giác ")
else:
    print("a, b, c không là ba cạnh của tam giác ")