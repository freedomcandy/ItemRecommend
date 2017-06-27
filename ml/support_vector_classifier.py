# -*- coding: utf-8 -*-
from sklearn.svm import SVC
from sklearn.externals import joblib
import os
# from matplotlib.pyplot import clf

SVM_SAVE_MODEL_PATH = '../svm_save_model'

class SupportVectorClassifier:
    #use support vector machine's Support Vector Classifier to resolve classification question
    # to do handle data
    def processSVMClassifier(self,datas):
        
        #handle data 
        select_feature = ['feature']
        features = datas[select_feature]
        print("------",features)
        labels = datas['label']
        print("======",labels)
        predictFeatures = labels[len(labels)-1]
        print("+++++",predictFeatures)
        
        #calculator with svc
        clf = SVC()
        clf.fit(features, labels)
        y_predict = clf.predict(predictFeatures)
        
        #transform
        y = y_predict.tolist()[0]
        print('111-----',y)
        return y
    
#     def processSVMClassifierLoadSve(self,user_id,datas):
#         #handle data 
#         select_feature = ['feature']
#         features = datas[select_feature]
#         print("------",features)
#         labels = datas['label']
#         print("======",labels)
#         predictFeatures = labels[len(labels)-1]
#         print("+++++",predictFeatures)
#         
#         #check train model
#         os.chdir(SVM_SAVE_MODEL_PATH)
#         clf = None
#         modelName = '%d_svm_model.m'%user_id
#         
#         y_predict = None
#         
#         #Load
#         #process data with SVC
#         if os.path.exists(modelName):
#             clf = joblib.load(modelName)
#             clf.fit(features, labels)
#             y_predict = clf.predict(predictFeatures)
#         else:
#             clf = SVC()
#             clf.fit(features, labels)
#             y_predict = clf.predict(predictFeatures)
#         
#         joblib.dump(clf,modelName)
#         y = y_predict.tolist()[0]
#         print('111-----',y)
#         return y
