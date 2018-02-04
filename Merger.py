# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:31:47 2017

@author: hameedul040
"""

print("*********************Collection called********************")

def Merger():
    
    #from pandas import DataFrame, read_csv
    import pandas as pd
    #import matplotlib.pyplot as plt
    #import os
    import tkinter as tk
    from tkinter import filedialog    
    
    root = tk.Tk()
    root.withdraw()
    print("Select Features.csv")
    file_path = filedialog.askopenfilename()#opens window to choose file
    feature_df= pd.read_csv(file_path, encoding='cp1252')    
    
    print("slect AptNXXXX-XXXX.CSV file for which re-arranging is done")
    file_path = filedialog.askopenfilename()#opens window to choose file
    Preprocess= pd.read_csv(file_path, encoding='cp1252')
    
    #############logic to slect and bind multiple csv files
#    print("slect AptNXXXX-XXXX.CSV file for which re-arranging is done")
#    file_path = filedialog.askopenfilename()#opens window to choose file
#    df1= pd.read_csv(file_path, encoding='cp1252')
#    print("slect AptNXXXX-XXXX.CSV file for which re-arranging is done")
#    file_path = filedialog.askopenfilename()#opens window to choose file
#    df2= pd.read_csv(file_path, encoding='cp1252')
#    print("slect AptNXXXX-XXXX.CSV file for which re-arranging is done")
#    file_path = filedialog.askopenfilename()#opens window to choose file
#    df3= pd.read_csv(file_path, encoding='cp1252')
#    print("slect AptNXXXX-XXXX.CSV file for which re-arranging is done")
#    file_path = filedialog.askopenfilename()#opens window to choose file
#    df4= pd.read_csv(file_path, encoding='cp1252')
#    print("slect AptNXXXX-XXXX.CSV file for which re-arranging is done")
#    df5 = filedialog.askopenfilename()#opens window to choose file
#    Preprocess= pd.read_csv(file_path, encoding='cp1252')    
#    print("slect AptNXXXX-XXXX.CSV file for which re-arranging is done")
#    file_path = filedialog.askopenfilename()#opens window to choose file
#    df6= pd.read_csv(file_path, encoding='cp1252')
#    
#    frames = [df1, df2, df3, df4, df5, df6]
#
#    Preprocess = pd.concat(frames)
    ###############################
    
    merged_df = pd.merge(Preprocess,feature_df, on='AptN')
        
    del merged_df["house_occupancy"]
    del merged_df["area_of_home"]
    
    merged_df["Avg_Yrly_energy"]=0
    
    for i in range(0,len(merged_df)):
        
        merged_df["Avg_Yrly_energy"][i]=(merged_df["SleepingHoursConsumption"][i]+merged_df["WorkingHoursConsumption"][i]+merged_df["EveningHoursConsumption"][i])*16*60
        
      
        
    return merged_df