#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-30 02:10:53
# @Last Modified by:   Your name
# @Last Modified time: 2022-05-30 02:28:11


from threading import Thread


class MyThread(Thread):
    def __init__(self, function):
        super().__init__()
        self.function = function()
        # initialize your thread, use arguments in the constructor if needed

    def run(self):
        print("Thread running")
        self.function