# -*- coding: utf-8 -*-
from sklearn.neural_network import MLPClassifier
from sklearn.cluster import AgglomerativeClustering
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np
import os
from scipy import cluster

SAVE_MODEL_PATH = '../save_model'

class MultiLayerPerceptron:
    # define and use Multi-Layer Perceptron to predict the user next tap third-categoryId(serisId) 
    # that return backend maybe two more predicted ID list
    def processMLPClassifier(self, user_id, datas):
        #wish data
        select_feature = ['feature']
        features = datas[select_feature]
        print("------",features)
        labels = datas['label']
        print("======",labels)
        predictFeatures = labels[len(labels)-1]
        print("+++++",predictFeatures)
        
        #check train model
        os.chdir(SAVE_MODEL_PATH)
        mlp = None
        modelName = '%d_mlp_model.m'%user_id
        
        y_predict = None
        
        #process data with mlp
        if os.path.exists(modelName):
           mlp = joblib.load(modelName)
           mlp.fit(features, labels)
           y_predict = mlp.predict(predictFeatures)
        else:
            mlp = MLPClassifier(hidden_layer_sizes=(30,20,10))
            mlp.fit(features, labels)
            y_predict = mlp.predict(predictFeatures)
        
        
        joblib.dump(mlp,modelName)
        y = y_predict.tolist()[0]
        print('111-----',y)
        return y
           
        
        
         
#        
       
    
    
    
    def getTargetItemCluster(self,features):
#         print("=======",features)
#         print(type(features))
        select_feature = ["brand","series","third"]
        train_data = features[select_feature]
#         print(type(train_data))
#         print(train_data)
        #check data is  Null,Nan,"",etc
        train_data["brand"] = train_data["brand"].fillna("其他")
        #LabelEncode
        le = LabelEncoder()
        train_data["brand"] = le.fit_transform(train_data["brand"])
        #start Cluster 
        ac = AgglomerativeClustering(n_clusters= 3)
        y_predict = ac.fit_predict(train_data)
        itemCluster = y_predict[0]
        cluster_index = []
        index = 0
        for i in y_predict:
            if i == itemCluster:
                cluster_index.append(index)
            index+=1  
#         print(itemCluster)
#         print(y_predict)
#         print(cluster_index)
        print("=======",cluster_index)
        return cluster_index
        
        

if __name__ == '__main__':
    MultiLayerPerceptron().getTargetItemCluster()
        
