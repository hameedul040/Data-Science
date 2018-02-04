# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:01:46 2017

@author: hameedul040
"""
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

td1=pd.read_table(r"C:\Users\hameedul040\Desktop\File1.txt", delim_whitespace=True, names=('AptN','Time', 'Energy'))
td2=pd.read_table(r"C:\Users\hameedul040\Desktop\File2.txt", delim_whitespace=True, names=('AptN','Time', 'Energy'))
td3=pd.read_table(r"C:\Users\hameedul040\Desktop\File3.txt", delim_whitespace=True, names=('AptN','Time', 'Energy'))
td4=pd.read_table(r"C:\Users\hameedul040\Desktop\File4.txt", delim_whitespace=True, names=('AptN','Time', 'Energy'))
td5=pd.read_table(r"C:\Users\hameedul040\Desktop\File5.txt", delim_whitespace=True, names=('AptN','Time', 'Energy'))
td6=pd.read_table(r"C:\Users\hameedul040\Desktop\File6.txt", delim_whitespace=True, names=('AptN','Time', 'Energy'))

import DataArranger as p        #filename in which the called function is defined
p.DataArranger(td1)

import SurveyData as f
f.SurveyData()

import Merger as c
DFforPlots= c.Merger()

import MakeGraphs as m
m.MakeGraphs(DFforPlots)

import OptimalCluster as e
e.OptimalCluster(DFforPlots)

import MyAlgorithm as a
a.MyAlgorithm(DFforPlots)


