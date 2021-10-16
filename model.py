import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle

#importing the dataset
heart = pd.read_csv('heart.csv')
#list the first five  rows
heart.head()

X=heart.iloc[:,:-1].values 
y=heart.iloc[:,-1].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


ksclassifier = SVC(kernel = 'rbf' ,random_state = 0)
ksclassifier.fit(X_train , y_train)
y_pred = ksclassifier.predict(X_test)
cm = confusion_matrix(y_test , y_pred)
accuracy_score(y_test,y_pred)
print(f"Training accuracy {round(ksclassifier.score(X_train,y_train)*100,2)}%")
print(f"Testing accuracy {round(ksclassifier.score(X_test,y_test)*100,2)}%")
with open('model_pickle','wb') as f:
    pickle.dump(ksclassifier,f)

