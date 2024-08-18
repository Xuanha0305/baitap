# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:45:35 2024

@author: xuanha 
"""

quangduong=float(input("nhập quãng đường đi được(km) "))
if quangduong<1:
    print("số tiền phải trả là 20000 ")
elif quangduong<=3:
    print("số tiền phải trả là ", 20000+(quangduong-1)*13000 )
elif quangduong<=8:
    print("số tiền phải trả là ", 3*13000+(quangduong-3)*12000 )
else:
    st=(3*13000+5*12000+(quangduong-8)*10000 )*0.92 
    print("số tiền phải trả là ", st)
   