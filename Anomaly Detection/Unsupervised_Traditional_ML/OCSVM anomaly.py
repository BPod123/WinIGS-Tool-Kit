# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 00:52:31 2022

@author: 16786
"""

import pandas as pd
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from numpy import where

data = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

df = data[["sepal_length", "sepal_width"]]

model = OneClassSVM(kernel = 'rbf', gamma = 0.001, nu = 0.03).fit(df)

y_pred = model.predict(df)
#print(y_pred)

outlier_index = where(y_pred == -1) 
outlier_values = df.iloc[outlier_index]
print(outlier_values)

plt.scatter(data["sepal_length"], df["sepal_width"])
plt.scatter(outlier_values["sepal_length"], outlier_values["sepal_width"], c = "r")