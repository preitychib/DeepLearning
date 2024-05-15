import numpy as np
import pandas as pd
from sklearn import datasets,preprocessing
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

wine=pd.read_csv('winequality-red.csv',delimiter=';')

X=wine.iloc[:,0:11]
y=wine['quality']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)

scalar=StandardScaler()
scalar.fit(X_train)
X_train=scalar.transform(X_train)
X_test=scalar.transform(X_test)

#? training and predictions
mlp=MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=1500)
mlp.fit(X_train,y_train)
predictions=mlp.predict(X_test)

#? Evaluating
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions,zero_division=0))
