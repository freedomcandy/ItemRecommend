# -*- coding: utf-8 -*-
from sklearn.naive_bayes import GaussianNB
import numpy as np
class NaiveBayes:
    #implements the naive Bayes algorithm for multinomially distributed data,
    # and is one of the two classic naive Bayes variants used in text classification
    def processDataWithGaussianNB(self,features_train,labels_train,feature_test):
        features_train = np.array(features_train)
        gnb = GaussianNB()
        #train data by using NaiveBayes
        gnb.fit(features_train, labels_train) 
        predict = gnb.predict(feature_test)
        return predict
