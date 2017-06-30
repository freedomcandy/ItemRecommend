# -*- coding: utf-8 -*-
import os
from sklearn.neural_network import MLPClassifier
from sklearn.cluster import AgglomerativeClustering
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder

SAVE_MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),"../save_model"))

class MultiLayerPerceptron:
    # define and use Multi-Layer Perceptron to predict the user next tap third-categoryId(serisId) 
    # that return backend maybe two more predicted ID list
    def processMLPClassifier(self, user_id, datas):
        #wish data
        select_feature = ['feature']
        features = datas[select_feature]
        labels = datas['label']
        predictFeatures = labels[len(labels)-1]
        
        #check train model
        os.chdir(SAVE_MODEL_PATH)
        mlp = None
        modelName = '%d_mlp_model.m'%user_id
        #process data with mlp
        if os.path.exists(modelName):
            mlp = joblib.load(modelName)
        else:
            mlp = MLPClassifier(hidden_layer_sizes=(30,20,10))
        mlp.fit(features, labels)
        y_predict = mlp.predict(predictFeatures)        
        
        joblib.dump(mlp,modelName)
        y = y_predict.tolist()[0]
        return y
    
    def getTargetItemCluster(self, features):
        select_feature = ["brand","series","third"]
        train_data = features[select_feature]
        #LabelEncode
        le = LabelEncoder()
        train_data["brand"] = le.fit_transform(train_data.loc[:, ("brand", )])
        #start Cluster 
        ac = AgglomerativeClustering(n_clusters = min(len(train_data), 8))
        y_predict = ac.fit_predict(train_data)
        itemCluster = y_predict[0]
        cluster_index = []
        for index, i in enumerate(y_predict):
            if i != itemCluster:
                continue
            cluster_index.append(index)
        return cluster_index

try:
    MLP
except NameError:
    MLP = MultiLayerPerceptron()
