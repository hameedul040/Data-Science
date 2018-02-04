# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:30:02 2017

@author: hameedul040
"""

#var = input("Please enter Pre Survey file location: ")
#print("You entered " + str(var))

def SurveyData():
    print("*********************SurveyData called***************")
    import numpy as np
    #from pandas import DataFrame, read_csv
    import pandas as pd
    #import matplotlib.pyplot as plt
    #import os
    import tkinter as tk
    from tkinter import filedialog
    
    root = tk.Tk()
    root.withdraw()
    print("Select file Smart meters Residential pre-trial survey data.csv")
    file_path = filedialog.askopenfilename()#opens window to choose file
    pre_survey_df= pd.read_csv(file_path, encoding='cp1252') 
    
    
     
       
    def createDF(dataFrame):#It creates 
    
    
        final = np.zeros(shape=(len(pre_survey_df),12)).astype(np.int16)
        final = pd.DataFrame(final,columns=('AptN','total_number_of_people', 'house_occupancy', 'area_of_home', 'total_usage_purpose', 'total_heavy_devices', 'total_light_devices', 'total_heavy_device_usage', 'total_light_device_usage', 'income_category', 'education', 'employment'))
              
        final["AptN"]=pre_survey_df["ID"]
        final_df=final
        return (final_df)
    
    def TotalPeople(dataFrame):
       
        for i in range(0,len(dataFrame)):
            #print(i)
            if pd.isnull(dataFrame.iloc[i,9]):     #bad data skip
                continue
            
            
            if dataFrame.iloc[i,9]==1: #only one persom lives
                     final_df.iloc[i,1] = 1
                     final_df.iloc[i,2] = 0 
                     #print("exit if")
            elif dataFrame.iloc[i,9]==2:#All are over 15 yrs
                    #print("enter elif")
                    final_df.iloc[i,1] = int(dataFrame.iloc[i,10])
                    
                    if int(dataFrame.iloc[i,11])!=8 and not pd.isnull(dataFrame.iloc[i,11]):
                        final_df.iloc[i,2] = int(dataFrame.iloc[i,11])
                        
                    elif int(dataFrame.iloc[i,11])==8:
                        final_df.iloc[i,2] =  0
                    #print("enter elif")
            else:#both above and and below 15 yrs of age ppl are in house
                    #print("enter else")
                    final_df.iloc[i,1]=int(dataFrame.iloc[i,10])+int(dataFrame.iloc[i,12])
                    
                    if int(dataFrame.iloc[i,11])!=8 and not pd.isnull(dataFrame.iloc[i,11]):
                        
                        final_df.iloc[i,2] = int(dataFrame.iloc[i,11])                    
                        
                    elif int(dataFrame.iloc[i,11])==8:
                        final_df.iloc[i,2] =  0
                        
                    if int(dataFrame.iloc[i,13]) !=8 and not pd.isnull(dataFrame.iloc[i,13]):
                        
                        final_df.iloc[i,2] =int(final_df.iloc[i,2]) + int(dataFrame.iloc[i,13])                    
                        
                    elif int(dataFrame.iloc[i,13]) ==8:
                        final_df.iloc[i,2] = int(final_df.iloc[i,2])+ 0
                        
    
        return 
    
    def AreaOfAptN(dataFrame):
        
        dataFrame = dataFrame.reset_index(drop=True)
        #final_df = final_df.reset_index(drop=True)
        final_df.iloc[:,3]=dataFrame.iloc[:,38]
        
        for i in range(0,len(dataFrame)):
            if int(dataFrame.iloc[i,38])==999999999:
                final_df.iloc[i,3]=-1
            if pd.isnull(dataFrame.iloc[i,39]):
                continue
            if dataFrame.iloc[i,39]=='2':
                final_df.iloc[i,3]=final_df.iloc[i,3]*0.093
    
        return
    
    
    
    def Usage(dataFrame):
        
        for i in range(0,len(dataFrame)):
            
            if int(dataFrame.iloc[i,42])==1 and not(pd.isnull(dataFrame.iloc[i,42])):
                final_df.iloc[i,4]=int(final_df.iloc[i,4]+1)
                
            if int(dataFrame.iloc[i,49])==1 and not(pd.isnull(dataFrame.iloc[i,49])):
                final_df.iloc[i,4]=int(final_df.iloc[i,4]+1)
                
            if int(dataFrame.iloc[i,50])==1 and not(pd.isnull(dataFrame.iloc[i,50])):
                final_df.iloc[i,4]=int(final_df.iloc[i,4]+1)
                
            if int(dataFrame.iloc[i,51])==1 and not(pd.isnull(dataFrame.iloc[i,51])):
                final_df.iloc[i,4]=int(final_df.iloc[i,4]+1)
                
            if int(dataFrame.iloc[i,59])==1 or dataFrame.iloc[i,59]==5 and not(pd.isnull(dataFrame.iloc[i,59])):
                final_df.iloc[i,4]=int(final_df.iloc[i,4]+1)
        for i in range(0,len(dataFrame)):
            for j in range(100,110):
                if not (pd.isnull(dataFrame.iloc[i,j])):
                    x=dataFrame.iloc[i,j]
                    if x==' ':
                        x=0.0
                    final_df.iloc[i,7]=final_df.iloc[i,7]+int(x)
        
        for i in range(0,len(dataFrame)):
            for j in range(110,115):
                if not (pd.isnull(pre_survey_df.iloc[i,j])):
                    x=pre_survey_df.iloc[i,j]
                    if x==' ':
                        x=0.0
                        
                    #
                    final_df.iloc[i,8]=final_df.iloc[i,8]+int(x)
        #print(final_df.iloc[i,8])
        return
    
    def CalcIncome(dataFrame):
        
        for i in range(0,len(dataFrame)):
            final_df.iloc[i,9]=dataFrame.iloc[i,144]
        
    #    income_slab=dataFrame.iloc[:,135:136]
    #    
    #    for i in range(0,len(dataFrame)):
    #        x=income_slab.iloc[i,0]
    #        
    #        if pd.isnull(x) or x in ['',' ']:
    #            x=CalcSlab(dataFrame,i)
    #            income_slab.iloc[i,0]=x
    #        print(x,"\t",end="")
    ##        if x==1:
    #            final_df.iloc[i,10]=15000
    #        elif x==2:
    #            final_df.iloc[i,10]=30000
    #        elif x==3:
    #            final_df.iloc[i,10]=50000
    #        elif x==4:
    #            final_df.iloc[i,10]=75000
    #        elif x==5:
    #            final_df.iloc[i,10]=100000
    #        elif x==6:
    #            final_df.iloc[i,10]=-1
    ##   
    #    for i in range(0,len(dataFrame)):
    #        if final_df.iloc[i,9]==6:
    #            final_df.iloc[i,9]=-1
    #        if income_slab.iloc[i,0]==9:
    #            final_df.iloc[i,9]=6
    #        else:
    #            final_df.iloc[i,9]=income_slab.iloc[i,0]
    #    
        return 
    
    def CalcSlab(dataFrame,i):
        y=dataFrame.iloc[i,134]
        z=dataFrame.iloc[i,136]
        #print(y,"YYY\n")
        if z==3:
            return y
        elif z==1:
            if y in [1,2,3]:
                return 7
            else:
                return 6
        elif z==2:
            return 9#change to 6 in final_df
        else:
            return 6
    
    def devices(dataframe):
        
        for i in range(0,len(dataframe)):
            final_df.iloc[i,5]=Sum(dataframe,i,80,89)-10
            final_df.iloc[i,6]=Sum(dataframe,i,95,99)-5
        return
    
    def Sum(dataframe,row_num,Col1,Col2):  #to be used in "devices" function
        sum=0
        for i in range(Col1,Col2+1):
            sum=sum+int(dataframe.iloc[row_num,i])
        return sum
    
    def education(dataFrame):
        for i in range(0,len(dataFrame)):
            if(dataFrame.iloc[i,133]==6):
                final_df.iloc[i,10]=-1
            else:
                final_df.iloc[i,10]=dataFrame.iloc[i,133]    
        return
    
    def employment(dataFrame):
        for i in range(0,len(dataFrame)):
            final_df.iloc[i,11]=dataFrame.iloc[i,3]    
        return    
     
    final_df=createDF(pre_survey_df)#coded coreectly
    TotalPeople(pre_survey_df)#coded coreectly
    AreaOfAptN(pre_survey_df)        #coded coreectly    
    Usage(pre_survey_df)#code correctly
    devices(pre_survey_df) #coded correctly
    CalcIncome(pre_survey_df)
    education(pre_survey_df)
    employment(pre_survey_df)
    
    pre_survey_df=pre_survey_df.rename(columns={"ID":"AptN"})
    
    filename="Features.csv"
    final_df.to_csv(filename, encoding='utf-8', index=False)       
    print("Features generated in Features.csv")
    #return