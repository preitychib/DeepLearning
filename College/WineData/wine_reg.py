import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

wine=pd.read_csv('winequality-red.csv',delimiter=';')

X=wine.drop('quality',axis=1)
y=wine['quality']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

scalar=StandardScaler()
scalar.fit(X_train)
X_train=scalar.transform(X_train)
X_test=scalar.transform(X_test)

#? training and predictions
mlp= MLPRegressor(hidden_layer_sizes=(100,50,25), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='adaptive' , learning_rate_init=0.007, max_iter=2000, random_state=42, early_stopping=True)
mlp.fit(X_train,y_train)
predictions=mlp.predict(X_test)

#? Evaluating
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
print("R-squared:", r2_score(y_test, predictions)) 
