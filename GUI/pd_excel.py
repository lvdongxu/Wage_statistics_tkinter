# -*- encoding: utf-8 -*-
'''
@File    :   pd_excel.py
@Time    :   2020/01/04 23:50:04
@Author  :   Dongxu Lv 
@Version :   0.1
@Contact :   lvdongxu@sjtu.edu.cn
@License :   (C)Copyright 2020- , SJTU-DMNE-He
@Desc    :   None
'''

# here put the import lib
import pandas as pd
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码


df = pd.read_excel('D:\\onedrive\\文科处助管\\工资统计\\wage_11.16_12.15.xls')
height, width = df.shape
print(df.iloc[3,1])

dict_key = ['姓名', '上午值班次数', '下午值班次数', '加班小时数', '总酬金']
dict_value = 
# data_list = []
# for _h in range(0,height):
#     _data_row = []
#     for _w in range(1, width+1):
#         _data_row.append()