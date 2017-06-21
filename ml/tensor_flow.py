# -*- coding: utf-8 -*-
import tensorflow as tf

class MGTensorFlow:
    #create add layer function,perceptron weight and biaes
    def add_layer(self,inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
        w = tf.Variable(tf.random_normal([in_size, out_size]))#weight
        b = tf.Variable(tf.zeros([1, out_size]) + 0.1)#biaes
        wx_plus_b = tf.matmul(inputs, w) + b #linear regression
        if activation_function is None:  #ex: relu  relu6  softmax  sigmod
           outputs = wx_plus_b
        else:
           outputs = activation_function(wx_plus_b)
        return outputs
