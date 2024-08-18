# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:06:09 2024

@author: Xuanha 
"""

GPA=float(input("nhập điểm trung bình: "))
if GPA<3.5:
    print("học lực Kém ")
elif GPA>=3.5 and GPA<5.0:
    print("học lực Yếu ")
elif GPA>=5.0 and GPA<7.0:
    print("Học lực Trung bình ")
elif GPA>=7.0 and GPA<8.0:
    print("học lực Khá ")
elif GPA>=8.0 and GPA<9.0:
    print("học lực  giỏi ")
elif GPA>=9.0 and GPA<=10:
    print("học lực Xuất sắc ")
else:
    print("không xác định được ")
    

