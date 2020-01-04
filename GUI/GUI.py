# -*- encoding: utf-8 -*-
'''
@File    :   GUI.py
@morning_time    :   2020/01/01 18:42:20
@Author  :   Dongxu Lv 
@Version :   0.1
@Contact :   lvdongxu@sjtu.edu.cn
@License :   (C)Copyright 2020- , SJTU-DMNE-He
@Desc    :   None
'''

# here put the import lib
import tkinter as tk

class Person:
    def __init__(self, _frame):
        '''
        @description: 
        @param : 
        @return: 
        '''
        # 这里是上午班，下午班和加班次数的整数变量定义
        self.morning_time = tk.IntVar() 
        self.morning_time.set(0)
        self.afternoon_time = tk.IntVar();
        self.afternoon_time.set(0)
        self.extra_time = tk.IntVar();
        self.extra_time.set(0)
        self.wage = tk.IntVar();
        self.wage.set(0)
        # 一些基本参数类似于列扩展，x方向的pad
        set_columnspan = 8
        set_padx = 4
        # 上午班次数统计和UI组件定义
        tk.Label(_frame, text="上午值班次数", height=2, width=10, bg='red', fg='white').grid(row=0, column=0, columnspan=2*set_columnspan, padx=set_padx)
        tk.Label(_frame, textvariable=self.morning_time, height=2, width=10).grid(row=1, column=0, columnspan=2*set_columnspan, padx=set_padx)
        tk.Button(_frame, text='+1', command=self.morning_plus, height=2, width=4).grid(row=2, column=0, columnspan=set_columnspan)
        tk.Button(_frame, text='-1', command=self.morning_minus, height=2, width=4).grid(row=2, column=set_columnspan, columnspan=set_columnspan)
        # 下午班次数统计和UI组件定义
        tk.Label(_frame, text="下午值班次数", height=2, width=10, bg='blue', fg='white').grid(row=0, column=2*set_columnspan, columnspan=2*set_columnspan, padx=set_padx)
        tk.Label(_frame, textvariable=self.afternoon_time, height=2, width=10).grid(row=1, column=2*set_columnspan, columnspan=2*set_columnspan, padx=set_padx)
        tk.Button(_frame, text='+1', command=self.afternoon_plus, height=2, width=4).grid(row=2, column=2*set_columnspan, columnspan=set_columnspan)
        tk.Button(_frame, text='-1', command=self.afternoon_minus, height=2, width=4).grid(row=2, column=3*set_columnspan, columnspan=set_columnspan)
        # 加班次数统计和UI组件定义
        tk.Label(_frame, text="加班次数", height=2, width=10, bg='green', fg='white').grid(row=0, column=4*set_columnspan, columnspan=2*set_columnspan, padx=set_padx)
        tk.Label(_frame, textvariable=self.extra_time, height=2, width=10).grid(row=1, column=4*set_columnspan, columnspan=2*set_columnspan, padx=set_padx)
        tk.Button(_frame, text='+1', command=self.extra_plus, height=2, width=4).grid(row=2, column=4*set_columnspan, columnspan=set_columnspan)
        tk.Button(_frame, text='-1', command=self.extra_minus, height=2, width=4).grid(row=2, column=5*set_columnspan, columnspan=set_columnspan)
        # 总的工资
        tk.Label(_frame, text='总的工资', height=2, width=10, bg='black', fg='white').grid(row=0, column=6*set_columnspan, columnspan=4*set_columnspan, padx=set_padx)
        tk.Label(_frame, textvariable=self.wage , height=2, width=10, bg='black', fg='white').grid(row=2, column=6*set_columnspan, columnspan=4*set_columnspan, padx=set_padx)

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


root = tk.Tk()
root.title('文科处助管工资统计')
# root.geometry('400x500')

name = ['吕东旭','王晓情','李启开']
frame_list = []
for name_i in name:
    _frame = tk.LabelFrame(text=name_i)
    Person(_frame)
    _frame.pack(side=tk.TOP)


root.mainloop()



