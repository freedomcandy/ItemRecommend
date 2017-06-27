# -*- coding: utf-8 -*-
from sklearn.naive_bayes import GaussianNB
# from sklearn.externals import joblib
# import os

class NaiveBayes:
    #implements the naive Bayes algorithm for multinomially distributed data,
    # and is one of the two classic naive Bayes variants used in text classification
    def processDataWithGaussianNB(self,datas):
        
        #handle data 
        select_feature = ['feature']
        features = datas[select_feature]
#         print("------",features)
        labels = datas['label']
#         print("======",labels)
        predictFeatures = labels[len(labels)-1]
#         print("+++++",predictFeatures)
        
        #calculator with GaussianNB
        clf = GaussianNB()
        clf.fit(features, labels)
        y_predict = clf.predict(predictFeatures)
        
        #transform
        y = y_predict.tolist()[0]
        print('y_predict:',y)
        return y
        