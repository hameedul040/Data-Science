# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:53:53 2017

@author: DELL
"""
def OptimalCluster(dataframe):
    
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    
    x=list(range(21))
    x=x[2:]
    
    avg=[]
    i=2    
    for i in x:
        
        w=[]
        for j in range(0,100):
            kmine = KMeans(n_clusters=i, random_state=0).fit(dataframe)
            w.append(kmine.inertia_)
        avg_inertia=sum(w)/len(w)    
        avg.append(avg_inertia)
    
    plt.plot(x,avg)
    plt.xlabel("Number of clusters")
    plt.ylabel("Average Total Within Sum of Squares")
    plt.savefig('Elbow.png')
        
    return   
        
        
        
     
    
    
