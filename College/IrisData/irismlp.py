import pandas as pd
from sklearn import datasets,preprocessing
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

df=pd.read_csv('Iris.csv')
X=df.drop(['Species'],axis=1)
y=df['Species']
# print(x)
# print(y.Class.unique())
le=preprocessing.LabelEncoder()
y=le.fit_transform(y) 
# print(y)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)
# print(X_test)


#? feature Scaling
scalar=StandardScaler()
scalar.fit(X_train)
X_train=scalar.transform(X_train)
X_test=scalar.transform(X_test)


#? training and predictions
mlp=MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=1000)
mlp.fit(X_train,y_train)
predictions=mlp.predict(X_test)
print(predictions)

#? Evaluating
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
