import numpy as np
import pandas as pd
from sklearn import datasets,preprocessing
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# iris = datasets.load_iris()
# # path=('Iris.csv') needs to be changed
# # df=pd.read_csv(path,names=names)
# names=['sepal-length','sepal-width','petal-length','petal-width','Class']

# df= pd.DataFrame(data=iris.data,columns=['sepal-length','sepal-width','petal-length','petal-width'])
# df["Class"]=iris.target
# df["Class"]=df['Class'].replace({0:"Iris-setosa",1:"Iris-versicolor",2:"Iris-virginica"})
# # print(df)
df=pd.read_csv('Iris.csv')

# X=wine.drop('quality',axis=1)
# y=wine['quality']
# X=df.iloc[:,0:4]
X=df.drop(['Species'],axis=1)
# y=df.iloc[:,-1:]
y=df['Species']
# y=df[['Class']]
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
# y_train=y_train['Class']
# print(y_train)
# mlp.fit(X_train,y_train.values.ravel())
mlp.fit(X_train,y_train)
predictions=mlp.predict(X_test)
# print(predictions)

#? Evaluating
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
