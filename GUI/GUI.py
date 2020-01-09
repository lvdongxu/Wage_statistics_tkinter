# -*- encoding: utf-8 -*-
'''
@File    :   GUI.py
@Time    :   2020/01/01 18:42:20
@Author  :   Dongxu Lv 
@Version :   0.1
@Contact :   lvdongxu@sjtu.edu.cn
@License :   (C)Copyright 2020- , SJTU-DMNE-He
@Desc    :   None
'''

# here put the import lib
import tkinter as tk
import pandas as pd
import wage_excel as we

class Person:
    def __init__(self, _frame, name):
        '''
        @description: 
        @param : 
        @return: 
        '''
        self.get_name = name
        self.get_list = []
        self._dict = {}
        # 这里是上午班，下午班和加班次数的整数变量定义
        self.morning_time = tk.IntVar() 
        self.morning_time.set(0)
        self.afternoon_time = tk.IntVar()
        self.afternoon_time.set(0)
        self.extra_time = tk.IntVar()
        self.extra_time.set(0)
        self.wage = tk.IntVar()
        self.wage.set(0)
        self.wage_cal() # 在初始化必须要运行这句话，不然类字典在该助管没有值班的，button永远不被按的情况下永远都是一开始定义的空字典，

        # 一些基本参数类似于列扩展，x方向的pad
        set_columnspan = 8
        set_padx = 4

        # 单行UI设计，为了满足人数要求
        # 上午班次数统计和UI组件定义
        morning_label = tk.Label(_frame, text="上午值班次数", height=1, width=10, bg='red', fg='white')
        morning_label.grid(row=0, column=0, columnspan=2*set_columnspan, padx=set_padx) # column: 0 -> 2col-1
        morning_counter_label = tk.Label(_frame, textvariable=self.morning_time, height=1, width=10)
        morning_counter_label.grid(row=0, column=2*set_columnspan, columnspan=set_columnspan, padx=set_padx) # column: 2col -> 3col-1
        morning_plus_button = tk.Button(_frame, text='+1', command=self.morning_plus, height=1, width=4)
        morning_plus_button.grid(row=0, column=3*set_columnspan, columnspan=set_columnspan) # column: 3col -> 4col-1
        morning_minus_button = tk.Button(_frame, text='-1', command=self.morning_minus, height=1, width=4)
        morning_minus_button.grid(row=0, column=4*set_columnspan, columnspan=set_columnspan) # column: 4col -> 5col-1
        # 下午班次数统计和UI组件定义
        afternoon_label = tk.Label(_frame, text="下午值班次数", height=1, width=10, bg='blue', fg='white')
        afternoon_label.grid(row=0, column=5*set_columnspan, columnspan=2*set_columnspan, padx=set_padx) # column: 5col -> 7col-1
        afternoon_counter_label = tk.Label(_frame, textvariable=self.afternoon_time, height=1, width=10)
        afternoon_counter_label.grid(row=0, column=7*set_columnspan, columnspan=set_columnspan, padx=set_padx) # column: 7col -> 8col-1
        afternoon_plus_button = tk.Button(_frame, text='+1', command=self.afternoon_plus, height=1, width=4)
        afternoon_plus_button.grid(row=0, column=8*set_columnspan, columnspan=set_columnspan) # column: 8col -> 9col-1
        afternoon_minus_button = tk.Button(_frame, text='-1', command=self.afternoon_minus, height=1, width=4)
        afternoon_minus_button.grid(row=0, column=9*set_columnspan, columnspan=set_columnspan) # column: 9col-> 10col-1
        # 加班次数统计和UI组件定义
        extra_label = tk.Label(_frame, text="加班次数", height=1, width=10, bg='green', fg='white')
        extra_label.grid(row=0, column=10*set_columnspan, columnspan=2*set_columnspan, padx=set_padx) # column: 10col -> 12col-1
        extra_counter_label = tk.Label(_frame, textvariable=self.extra_time, height=1, width=10)
        extra_counter_label.grid(row=0, column=12*set_columnspan, columnspan=set_columnspan, padx=set_padx) # column: 12col -> 13col-1
        extra_plus_button = tk.Button(_frame, text='+1', command=self.extra_plus, height=1, width=4)
        extra_plus_button.grid(row=0, column=13*set_columnspan, columnspan=set_columnspan) # column: 13col -> 14col-1
        extra_minus_button = tk.Button(_frame, text='-1', command=self.extra_minus, height=1, width=4)
        extra_minus_button.grid(row=0, column=14*set_columnspan, columnspan=set_columnspan) # column: 14col -> 15col-1
        # 总的工资
        wage_label = tk.Label(_frame, text='总的工资', height=1, width=10, bg='black', fg='white')
        wage_label.grid(row=0, column=15*set_columnspan, columnspan=4*set_columnspan, padx=set_padx) # column: 15col -> 19col-1
        wage_counter_label = tk.Label(_frame, textvariable=self.wage , height=1, width=10, bg='black', fg='white')
        wage_counter_label.grid(row=0, column=19*set_columnspan, columnspan=4*set_columnspan, padx=set_padx) # column: 19col -> 23col-1

    def morning_plus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_morning_time = self.morning_time.get()
        cur_morning_time += 1
        self.morning_time.set(cur_morning_time)
        self.wage_cal()

    def morning_minus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_morning_time = self.morning_time.get()
        cur_morning_time -= 1
        self.morning_time.set(cur_morning_time)
        self.wage_cal()

    def afternoon_plus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_afternoon_time = self.afternoon_time.get()
        cur_afternoon_time += 1
        self.afternoon_time.set(cur_afternoon_time)
        self.wage_cal()

    def afternoon_minus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_afternoon_time = self.afternoon_time.get()
        cur_afternoon_time -= 1
        self.afternoon_time.set(cur_afternoon_time)
        self.wage_cal()

    def extra_plus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_extra_time = self.extra_time.get()
        cur_extra_time += 1
        self.extra_time.set(cur_extra_time)
        self.wage_cal()

    def extra_minus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_extra_time = self.extra_time.get()
        cur_extra_time -= 1
        self.extra_time.set(cur_extra_time)
        self.wage_cal()

    def wage_cal(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_morning_time = self.morning_time.get()
        cur_afternoon_time = self.afternoon_time.get()
        cur_extra_time = self.extra_time.get()
        cur_wage = cur_morning_time * 75 + cur_afternoon_time * 100 + cur_extra_time * 50
        self.wage.set(cur_wage)
        name = self.get_name
        self._dict = {"姓名": name, "上午值班次数": cur_morning_time, "下午值班次数": cur_afternoon_time, "加班小时数": cur_extra_time, "总酬金": cur_wage}

if __name__ == '__main__':
    root = tk.Tk()
    root.title("文科处助管工资统计")
    
    # excel路径判断
    lab_or_laptop  = 1
    git_path       = '/Wage_statistics_tkinter/GUI/'
    lab_path       = 'F:/PythonProject'
    laptop_path    = 'F:/Wenkechu_Wage_GUI'
    pattern_path   = 'wage_pattern.xls'
    new_excel_path = 'wage_new.xls'
    rd_path        = lab_path+git_path+pattern_path if lab_or_laptop == 1 else laptop_path+git_path+pattern_path
    wr_path        = lab_path+git_path+new_excel_path if lab_or_laptop == 1 else laptop_path+git_path+new_excel_path
    
    # LabelFrame定义与类创建
    name, dataFrame = we.rd_excel(rd_path)  
    print(dataFrame)  
    frame_list = []
    for _name in name[:4]:
        _frame = tk.LabelFrame(text=_name)
        _frame_class = Person(_frame, _name)
        frame_list.append(_frame_class)
        _frame.pack(side=tk.TOP)

    # 统计Button函数
    def final_statistic():
        '''
        @description: 最终统计Button的指令函数
        @param : 无输入参数
        @return: 没有返回值
        '''
        new_dataFrame = dataFrame
        for _frame_class in frame_list:
            new_dataFrame = we.wage_to_df(_frame_class._dict, new_dataFrame)
        we.pd_to_excel(new_dataFrame, wr_path)
        print(dataFrame)

    final_button = tk.Button(root, text="最终统计", command=final_statistic, bg='Red', fg='white')
    final_button.pack(side=tk.TOP, fill=tk.X)
    
    root.mainloop()