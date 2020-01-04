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
        # root.title('文科处助管工资统计')
        # root.geometry('600x400')
        self.morning_time = tk.IntVar() 
        self.morning_time.set(0)
        # tk.Label(_frame, text='shit').pack(side=tk.LEFT)
        tk.Label(_frame, textvariable=self.morning_time, height=2, width=10).pack(side=tk.LEFT)
        tk.Button(_frame, text='+1', command=self.morning_plus, height=2, width=4).pack(side=tk.LEFT)
        tk.Button(_frame, text='-1', command=self.morning_minus, height=2, width=4).pack(side=tk.LEFT)


    def morning_plus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_morning_time = self.morning_time.get()
        cur_morning_time += 1
        self.morning_time.set(cur_morning_time)

    def morning_minus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_morning_time = self.morning_time.get()
        cur_morning_time -= 1
        self.morning_time.set(cur_morning_time)

root = tk.Tk()
root.title('文科处助管工资统计')
root.geometry('600x400')

name = ['吕东旭','王晓情','李启开']
frame_list = []
for name_i in name:
    _frame = tk.LabelFrame(height=1000, width=6000, text=name_i)
    Person(_frame)
    _frame.pack(side=tk.TOP)


root.mainloop()



