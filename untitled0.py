# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:12:41 2022

@author: rithi
"""


class item():
    def __init__(self,name:str,voice:float,age=0):
        
        assert voice == 2
        self.name=name
        self.voice=voice
        self.age=age
        



item1=item("Rudra",5)
item2=item("jyotidas",2)