# -*- coding: utf-8 -*-
from sklearn.naive_bayes import GaussianNB
import numpy as np
class NaiveBayes:
    #implements the naive Bayes algorithm for multinomially distributed data,
    # and is one of the two classic naive Bayes variants used in text classification
    def processDataWithGaussianNB(self,features_train,labels_train,feature_test):
        
        feature_data = []
        for data in features_train:
            feature_data.append([data])
        
        gnb = GaussianNB()
        #train data by using NaiveBayes
        gnb.fit(feature_data, labels_train) 
        predict = gnb.predict(feature_test)
        return predict.tolist()
