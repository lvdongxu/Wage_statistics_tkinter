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

class Person:
    def __init__(self, root):
        '''
        @description: 
        @param : 
        @return: 
        '''
        root.title('文科处助管工资统计')
        root.geometry('600x400')
        self.Time = tk.IntVar() 
        self.Time.set(0)
        tk.Label(root, textvariable=self.Time).pack()
        tk.Button(root, text='+1', command=self.plus).pack()
        tk.Button(root, text='-1', command=self.minus).pack()


    def plus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_time = self.Time.get()
        cur_time += 1
        self.Time.set(cur_time)

    def minus(self):
        '''
        @description: 
        @param : 
        @return: 
        '''
        cur_time = self.Time.get()
        cur_time -= 1
        self.Time.set(cur_time)

root = tk.Tk()
test_tk = Person(root)
root.mainloop()



