# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:00:26 2017

@author: DELL
"""

def MakeGraphs(df):
    
    #import pandas as pd 
    #import numpy as np
    from matplotlib import pyplot as plt
    
    
    #df = pd.read_csv(r'C:\Users\DELL\Desktop\CER-Electricity-Subsidy-Prediction-master\newdf.csv')
    
    
    g1 = df.pivot_table(index='AptN',columns='total_heavy_devices', values='Avg_Yrly_energy')
    color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
    m=g1.plot(kind='box', color=color, figsize=[16,8])
   # g1.set_xlabel('No. of heavy devices', fontsize=18, color = 'r')
   # g1.set_ylabel('Average Energy consumption by year', fontsize=18, color = 'b')
   # fig = m.get_figure()
   # fig.savefig(r'C:\Users\DELL\Desktop\ECE689\hello.png')
    
    g2 = df.pivot_table(index='AptN',columns='income_category', values='Avg_Yrly_energy')
    color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
    g2.plot(kind='box', color=color, figsize=[16,8])
#    g2.set_xlabel('No. of heavy devices', fontsize=18, color = 'r')
#    g2.set_ylabel('Average Energy consumption by year', fontsize=18, color = 'b')
    
    
    g3 = df.pivot_table(index='AptN',columns='total_heavy_devices', values='Avg_Yrly_energy')
    color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
    g3.plot(kind='box', color=color, figsize=[16,8])
#    g3.set_xlabel('No. of heavy devices', fontsize=18, color = 'r')
#    g3.set_ylabel('Average Energy consumption by year', fontsize=18, color = 'b')
    
    df1=df[0:20]
    g4=df1.plot(x="AptN", y=["SleepingHoursConsumption", "WorkingHoursConsumption", "EveningHoursConsumption"], kind="line")
    
    
    return