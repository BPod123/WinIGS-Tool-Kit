from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn import svm

from sklearn import metrics

import matplotlib.pyplot as plt



cancer = datasets.load_breast_cancer()

#print("Features: ", cancer.feature_names)

print("Labels: ", cancer.target_names)

print(cancer.data.shape)

#print(cancer.target)

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109) # 70% training and 30% test

kernelTypes = ["linear", "poly", "rbf", "sigmoid"]

for x in kernelTypes:
    print("\n" + x)
    clf = svm.SVC(kernel= x) 

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("Precision:",metrics.precision_score(y_test, y_pred))

    print("Recall:",metrics.recall_score(y_test, y_pred))
    
X = cancer.data[:, :2]
y = cancer.target    
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    