# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:29:13 2024

@author: Xuanha 
"""

a=float(input("nhập độ dài cạnh a: "))
b=float(input("nhập độ dài cạnh b: "))
c=float(input("nhập độ dài cạnh c: "))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("là tam giác đều ")
    elif a==b or a==c or b==c:
        print("là tam giác cân ")
    elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
        print("là tam giác vuông ")
    else:
        print("là tam giác thường ")

    
    
        