from sklearn.neural_network import MLPClassifier

class MultiLayerPerceptron:
    #define and use Multi-Layer Perceptron to predict the user next tap third-categoryId(serisId) 
    #that return backend maybe two more predicted ID list
    def processMLPClassifier(self,features,labels,predictFeatures):
        thirdCategoryId = []
        mlp = MLPClassifier()
        for i in range(4):
            mlp.fit(features, labels)
            y_predict = mlp.predict(predictFeatures)
            
        return thirdCategoryId
        