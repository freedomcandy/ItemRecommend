# -*- coding: utf-8 -*-
from sklearn.svm import SVC

class SupportVectorClassifier:
    def processSVMClassifier(self,features_train,labels_train,feature_test):
        clf = svm.SVC()
        clf.fit(features_train,labels_train)
        predict = clf.predict(feature_test)
        return predict
