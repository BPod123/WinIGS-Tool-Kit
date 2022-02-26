# Author: Marcus Parker
# 2/25/22
# Isolation tree using 500 values of ecg csv

import pandas as pd
from sklearn.ensemble import IsolationForest


def printData():
    df = pd.read_csv('C:/Users/marcu/OneDrive/Documents/tvalues.csv')
    # We can put a list of values into a csv and then detect any outliers from the data using an Isolation tree.
    df.head(500)

    model = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.1), max_features=1.0)
    # First we create a model for the isolation tree.  First is the number of estimators, think of this as the number
    # of base estimators or trees Next is the number of samples to be drawn to train each base estimator. Next is a
    # contamination parameter; it refers to the expected proportion of outliers in the data set. Last is max
    # features. It is the number of features to draw from the total features to train each tree.
    model.fit(df[['V']])
    # Identify target rows.
    df['scores'] = model.decision_function(df[['V']])
    # If a score is negative, the data point is an outlier.
    df['anomaly'] = model.predict(df[['V']])
    # The above is our outliers, predicted from the trees.
    df.head(500)
    anomaly = df.loc[df['anomaly'] == -1]
    #
    outliers_counter = len(df[df['V'] > 99999])
    # print outliers
    print(anomaly)
    # %error
    # print("Accuracy percentage:", 100 * list(df['anomaly']).count(-1) / (outliers_counter))


printData()
