# -*- coding: utf-8 -*-
from sklearn.neural_network import MLPClassifier
import numpy as np

class MultiLayerPerceptron:
    # define and use Multi-Layer Perceptron to predict the user next tap third-categoryId(serisId) 
    # that return backend maybe two more predicted ID list
    def processMLPClassifier(self, features, labels, predictFeatures):
        print(type(features))
        features = np.array(features)
        thirdCategoryId = []
        mlp = MLPClassifier()
        for _ in range(4):
            mlp.fit(features, labels)
            y_predict = mlp.predict(predictFeatures)
            
        return thirdCategoryId
        
