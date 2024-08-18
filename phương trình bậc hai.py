# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:44:58 2024

@author: Xuanha 
"""
import math 
a=float(input("nhập hệ số a: "))
b=float(input("nhập hệ số b: "))
c=float(input("nhập hệ số c: "))
denta=b*b-4*a*c
if denta<0:
    print("phương trình vô nghiệm ")
elif denta==0:
    print("phương trình có nghiệm kép")
    print("x1=x2=", -b/2*a )
else:
    print("phương trình có hai nghiệm phân biệt ")
    x1 = (-b + math.sqrt(denta)) / (2 * a)
    x2 = (-b - math.sqrt(denta)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
   
          
    