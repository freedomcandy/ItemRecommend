# -*- coding: utf-8 -*-
from sklearn.neural_network import MLPClassifier
import numpy as np

class MultiLayerPerceptron:
    # define and use Multi-Layer Perceptron to predict the user next tap third-categoryId(serisId) 
    # that return backend maybe two more predicted ID list
    def processMLPClassifier(self, features, labels, predictFeatures):
        x_data = []
        for i in features:
            tempX = [i]
            x_data.append(tempX)
       
        features = np.array(x_data) 
#         thirdCategoryId = []
        mlp = MLPClassifier(hidden_layer_sizes=(30,20,10))
        mlp.fit(features, labels)
        y_predict = mlp.predict(predictFeatures)
        print(y_predict.tolist())
        return y_predict.tolist()
        
