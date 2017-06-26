# -*- coding: utf-8 -*-
from sklearn.neural_network import MLPClassifier
from sklearn.cluster import AgglomerativeClustering
from sklearn.externals import joblib
import numpy as np
import os

SAVE_MODEL_PATH = './save_model'

class MultiLayerPerceptron:
    # define and use Multi-Layer Perceptron to predict the user next tap third-categoryId(serisId) 
    # that return backend maybe two more predicted ID list
    def processMLPClassifier(self, user_id, features, labels, predictFeatures):
        #wish data
        x_data = []
        for i in features:
            tempX = [i]
            x_data.append(tempX)
        features = np.array(x_data)
        
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
        return y_predict.tolist()
           
        
        
         
#        
       
    
    
    
    def getTargetItemCluster(self,features=None):
        ac = AgglomerativeClustering(n_clusters= 3)
        featrue = [[1,2],[1,3],[1,1],[2,1],[2,0],[2,2],[3,3],[2,1],[3,2],[3,1],[1,5]]
        y_predict = ac.fit_predict(featrue)
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
        return cluster_index
        

if __name__ == '__main__':
    MultiLayerPerceptron().getTargetItemCluster()
        
