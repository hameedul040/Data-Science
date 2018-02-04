def DataArranger(td):



    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    from functools import reduce;
    #td=pd.read_table(r"C:\Users\hameedul040\Desktop\File1.txt", delim_whitespace=True, names=('AptN','Time', 'Energy'))
    print("File read!!")
    td["Day"]=td["Time"]//100#extracting Day
    td["Hour"]=td["Time"].mod(100)#extracting Hour
    td["Hour"]=td["Hour"].mod(48)#extracting Hour
    td["Hour"].replace([0], 48,inplace=True)#replacing 0 with 48
    
    td=td[["AptN", "Time","Day","Hour","Energy"]]#reordering columns
    
    td["newHour"]=td["Hour"].replace([1,2,3,4,37,38,39,40,41,42,43,44,45,46,47,48], 300)
    td["newHour"].replace([21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], 200,inplace=True)
    td["newHour"].replace([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 100,inplace=True)
    
    
    avg_energy_consumption=td.groupby(['AptN'])['Energy'].mean()
    avg_energy_consumption = avg_energy_consumption.to_frame().reset_index()
    
    avg_energy_consumption=avg_energy_consumption.rename(columns={"Power":"Avg Energy"})#reanming columns
    #avg_energy_consumption.to_csv("avg_energy_consumption.csv", encoding='utf-8', index=False)#to write into CSV file
    
    avg_energy_consumption_newHour=td.groupby(['AptN','newHour'])['Energy'].mean()
    avg_energy_consumption_newHour = avg_energy_consumption_newHour.to_frame().reset_index()
    
    avg_energy_consumption_newHour["HourLabel"]=avg_energy_consumption_newHour["newHour"]
    
    newHour1=avg_energy_consumption_newHour.loc[avg_energy_consumption_newHour['newHour']==100]
    newHour2=avg_energy_consumption_newHour.loc[avg_energy_consumption_newHour['newHour']==200]
    newHour3=avg_energy_consumption_newHour.loc[avg_energy_consumption_newHour['newHour']==300]
    
    avg_energy_consumption_newHour["HourLabel"].replace([100], "Sleeping Hours",inplace=True)
    avg_energy_consumption_newHour["HourLabel"].replace([200], "Working Hours",inplace=True)
    avg_energy_consumption_newHour["HourLabel"].replace([300], "Evening Hours",inplace=True)
    
    
    
    merged = pd.merge(newHour1,newHour2, on='AptN')#merging 
    merged = pd.merge(merged,newHour3, on='AptN')
     
    merged=merged[['AptN','Energy_x','Energy_y','Energy']]#selecting Columns
    
    merged=merged.rename(columns={"Energy_x":"SleepingHoursConsumption"})#reanming columns
    merged=merged.rename(columns={"Energy_y":"WorkingHoursConsumption"})#reanming columns
    merged=merged.rename(columns={"Energy":"EveningHoursConsumption"})#reanming columns
    
    ###############################
    #Yearly
    td['Year']=pd.cut(td.Day, bins=[194,365,731], labels=[1,2])
    
    avg_yearly=td.groupby(['AptN','Year'])['Energy'].sum()
    avg_yearly = avg_yearly.to_frame().reset_index()
    avg_yearly=avg_yearly.rename(columns={"Energy":"Total Energy"})#reanming columns
    
    print(avg_yearly.loc[avg_yearly['AptN'] == 1492])
    
    newYear1=avg_yearly.loc[avg_yearly['Year']==1]
    newYear2=avg_yearly.loc[avg_yearly['Year']==2]
    
    mergedByYear = pd.merge(newYear1,newYear2, on='AptN')#merging
    mergedByYear=mergedByYear[['AptN','Total Energy_x','Total Energy_y']]#selecting Columns
    mergedByYear=mergedByYear.rename(columns={"Total Energy_x":"Year1Energy"})#reanming columns
    mergedByYear=mergedByYear.rename(columns={"Total Energy_y":"Year2Energy"})#reanming columns
    
    ###############################################
    #monthly
    td['Month']=td['Day']
    td["Month"]=td["Month"].mod(365)#extracting Month
    
    td["Month"].replace([0], "365",inplace=True)
    
    td['Month']=pd.cut(pd.to_numeric(td.Month), bins=[0,31,59,90,120,151,181,212,243,273,304,334,365], labels=[1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200])
    
    avg_monthly=td.groupby(['AptN','Month'])['Energy'].sum()
    avg_monthly = avg_monthly.to_frame().reset_index()
    avg_monthly=avg_monthly.rename(columns={"Energy":"Total Energy"})
    
    print(avg_monthly.loc[avg_monthly['AptN'] == 1950])
    
    newMonth1=avg_monthly.loc[avg_monthly['Month']==1100]
    newMonth2=avg_monthly.loc[avg_monthly['Month']==1200]
    newMonth3=avg_monthly.loc[avg_monthly['Month']==1300]
    newMonth4=avg_monthly.loc[avg_monthly['Month']==1400]
    newMonth5=avg_monthly.loc[avg_monthly['Month']==1500]
    newMonth6=avg_monthly.loc[avg_monthly['Month']==1600]
    newMonth7=avg_monthly.loc[avg_monthly['Month']==1700]
    newMonth8=avg_monthly.loc[avg_monthly['Month']==1800]
    newMonth9=avg_monthly.loc[avg_monthly['Month']==1900]
    newMonth10=avg_monthly.loc[avg_monthly['Month']==2000]
    newMonth11=avg_monthly.loc[avg_monthly['Month']==2100]
    newMonth12=avg_monthly.loc[avg_monthly['Month']==2200]
    
    
    
    data_frames=[newMonth1,newMonth2,newMonth3,newMonth4,newMonth5,newMonth6,newMonth7,newMonth8,newMonth9,newMonth10,newMonth11,newMonth12]
    
    mergedByMonth = reduce(lambda  left,right: pd.merge(left,right,on=['AptN'],
                                                how='inner'), data_frames)
    mergedByMonth=mergedByMonth.iloc[:, [0,2,4,6,8,10,12,14,16,18,20,22,24]]##selecting columns
    mergedByMonth.columns.values[1] = 'Jan Energy'#renaming Columns
    mergedByMonth.columns.values[2] = 'Feb Energy'
    mergedByMonth.columns.values[3] = 'Mar Energy'
    mergedByMonth.columns.values[4] = 'Apr Energy'
    mergedByMonth.columns.values[5] = 'May Energy'
    mergedByMonth.columns.values[6] = 'Jun Energy'
    mergedByMonth.columns.values[7] = 'Jul Energy'
    mergedByMonth.columns.values[8] = 'Aug Energy'
    mergedByMonth.columns.values[9] = 'Sep Energy'
    mergedByMonth.columns.values[10] = 'Oct Energy'
    mergedByMonth.columns.values[11] = 'Nov Energy'
    mergedByMonth.columns.values[12] = 'Dec Energy'
    
    ###############getting Average AptN Energy consumption
    avg_energy_AptN=td.groupby(['AptN'])['Energy'].mean()#mean
    avg_energy_AptN = avg_energy_AptN.to_frame().reset_index()#assigning column name
    avg_energy_AptN=avg_energy_AptN.rename(columns={"Total Energy":"Avg Energy"})#assigning column name
    
    ########################Merging All files and generating CSV
    mergedData=[merged,mergedByMonth,mergedByYear,avg_energy_AptN]
    AptNStats= reduce(lambda  left,right: pd.merge(left,right,on=['AptN'],
                                                how='inner'), mergedData)
    start=min(AptNStats.AptN)   
    end=max(AptNStats.AptN)
    
    filename2="AptN"+str(start)+"-"+str(end)+".csv"
    AptNStats.to_csv(filename2, encoding='utf-8', index=False)#to write into CSV file
    filename1="AvgPerDayEnergy"+filename2
    avg_energy_consumption.to_csv(filename1, encoding='utf-8', index=False)
    print("File processed and generated  ",filename1)
    return

