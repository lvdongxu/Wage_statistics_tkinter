# -*- encoding: utf-8 -*-
'''
@File    :   wage_excel.py
@Time    :   2020/01/05 23:00:06
@Author  :   Dongxu Lv 
@Version :   0.1
@Contact :   lvdongxu@sjtu.edu.cn
@License :   (C)Copyright 2020- , SJTU-DMNE-He
@Desc    :   工资导出到excel的函数
'''

# here put the import lib
import pandas as pd

def rd_excel(path):
    '''
    @description: 读取样板excel并获得文科处所有助管的姓名
    @param : 有一个输入参数
        1.      path: 路径到excel文件级别，主要是pandas不支持相对路径查询
    @return: 有两个返回参数
        1. name_list: 助管姓名列表返回
        2. dataFrame: pandas读取excel的数据类型，一次读完之后都可以不用读了
    '''
    dataFrame = pd.read_excel(path) # 笔记本工资表路径
    name_list = list(dataFrame['姓名'])
    return name_list, dataFrame  

def wage_to_df(class_dict, dataFrame):
    '''
    @description: 根据Person类的返回值修改dataFrame里面对应的表单数据
    @param : 有两个输入参数
        1. class_dict: Person类返回的字典数据
        2.  dataFrame: rd_excel获得的pandas读excel返回的数据类型
    @return: 无返回值
    '''
    # 这样的[][]赋值会出现SettingWithCopyWarning，最后出现问题，所以得换一种写法        
    # dataFrame["上午值班次数"][dataFrame["姓名"] == class_dict["姓名"]] = class_dict["上午值班次数"]
    # dataFrame["下午值班次数"][dataFrame["姓名"] == class_dict["姓名"]] = class_dict["下午值班次数"]
    # dataFrame["加班小时数"][dataFrame["姓名"] == class_dict["姓名"]] = class_dict["加班小时数"]
    # dataFrame["总酬金"][dataFrame["姓名"] == class_dict["姓名"]] = class_dict["总酬金"]

    # 改变后的标准写法，得用loc[ , ]来写就没有问题
    dataFrame.loc[class_dict["姓名"], "上午值班次数"] = class_dict["上午值班次数"]
    dataFrame.loc[class_dict["姓名"], "下午值班次数"] = class_dict["下午值班次数"]
    dataFrame.loc[class_dict["姓名"], "加班小时数"] = class_dict["加班小时数"]
    dataFrame.loc[class_dict["姓名"], "总酬金"] = class_dict["总酬金"]
    new_dataFrame = dataFrame
    return new_dataFrame
     
def pd_to_excel(dataFrame, path):
    '''
    @description: 将整理好的数据导出到excel里面去
    @param : 
    @return: 
    '''
    dataFrame.to_excel(path, sheet_name='Sheet1', index=False, header=True)