# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:22:53 2017

@author: hameedul040
"""

def MyAlgorithm(dataframe):    
    import pandas as pd 
    import numpy as np
    from matplotlib import pyplot as pl
    from sklearn import svm
    
    trainData=dataframe.loc[dataframe["income_category"]!=-1]
#    trainLabel=trainData["income_category"]
#    del trainData["income_category"]
#    
#    testData=dataframe.loc[dataframe["income_category"]==-1]    
#    del testData["income_category"]     
#    
#    testLabel=pd.DataFrame(np.zeros(shape=(len(train),1)),columns=({"income_category"}))
    
#    clf = svm.SVR(kernel="rbf")
#    clf.fit(train, trainLabel)
#    
#    Labels=clf.predict(test)
    
    from sklearn.linear_model import RidgeClassifier
    from sklearn.naive_bayes import BernoulliNB, GaussianNB
    from sklearn.tree import ExtraTreeClassifier, DecisionTreeClassifier
    from sklearn.neighbors import NearestCentroid, KNeighborsClassifier
    from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
    
    from sklearn.model_selection import cross_validate

    
    names = ['RidgeClassifier', 'BernoulliNB', 'GaussianNB', 'ExtraTreeClassifier', 'DecisionTreeClassifier',
             'NearestCentroid', 'KNeighborsClassifier', 'ExtraTreesClassifier', 'RandomForestClassifier','SVC with linear kernel',
	   'LinearSVC (linear kernel)','SVC with RBF kernel', 'SVC with polynomial (degree 3) kernel']
    classifiers = [RidgeClassifier(), BernoulliNB(), GaussianNB(), ExtraTreeClassifier(), DecisionTreeClassifier(),
                    NearestCentroid(), KNeighborsClassifier(), ExtraTreesClassifier(), RandomForestClassifier(),svm.SVC(kernel='linear'),
                    svm.LinearSVC(),svm.SVC(kernel='rbf'),svm.SVC(kernel='poly')]
    test_scores, train_scores, fit_time, score_time = [], [], [], []
    
    for clf in classifiers:
        
        scores = cross_validate(clf, trainData.iloc[:, :-1], trainData.income_category)
        test_scores.append(scores['test_score'].mean())
        train_scores.append(scores['train_score'].mean())
        fit_time.append(scores['fit_time'].mean())
        score_time.append(scores['score_time'].mean())
        print("done")
    Stats=pd.DataFrame({'Classifier': names,'Test_Score': test_scores,'Train_Score': train_scores,'Fit_Time': fit_time,'Score_Time': score_time})
    print(Stats)
    
    
    return Stats

