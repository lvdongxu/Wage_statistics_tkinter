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
import numpy as np
import pandas as pd
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变默认输出的标准编码


# df = pd.read_excel('D:\\onedrive\\文科处助管\\工资统计\\wage_11.16_12.15.xls') # 笔记本工资表路径
df = pd.read_excel('F:/PythonProject/Wage_statistics_tkinter/GUI/wage_11.16_12.15.xls') # 实验室主机工资表路径
height, width = df.shape
# print(df.iloc[3,1])
print(df.loc[2])

# dict_key = ['姓名', '上午值班次数', '下午值班次数', '加班小时数', '总酬金']
# dict_value = ['王晓情', 2, 3, 4, 5]
# p = dict(zip(dict_key, dict_value))
# print(p)
# 
# df['加班小时数'][df['姓名'] == '王晓情'] = p['加班小时数']
# df.to_excel('F:/PythonProject/Wage_statistics_tkinter/GUI/wage_11.16_12.15.xls', sheet_name='Sheet1', index=True, header=True)