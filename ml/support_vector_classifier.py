# -*- coding: utf-8 -*-
from sklearn.svm import SVC
import numpy as np
class SupportVectorClassifier:
    #use support vector machine's Support Vector Classifier to resolve classification question
    # to do handle data
    def processSVMClassifier(self,features_train,labels_train,feature_test):
        
        feature_data = []
        for data in features_train:
            feature_data.append([data])
        
        features_train = np.array(feature_data) 
        clf = SVC()
        clf.fit(features_train,labels_train)
        predict = clf.predict(feature_test)
        return predict.tolist()
