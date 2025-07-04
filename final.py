# -*- coding: utf-8 -*-
"""final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19296zDTY0fDQlAr3AmAQZEZE8LlFEV5X
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

train=pd.read_csv("/content/train_LZdllcl.csv")
test=pd.read_csv("/content/test_2umaH9m.csv")
sample=pd.read_csv("/content/sample_submission_M0L0uXE.csv")

print(test.shape)
test

print(train.shape)
train

train.head()

test.head()

train.tail()

test.tail()

train.info()

test.info()

train.describe()

test.describe()

train.dtypes

train.isnull().sum()

test.isnull().sum()

train['education'] = train['education'].fillna(train['education'].mode()[0])

train['previous_year_rating'] = train['previous_year_rating'].fillna(train['previous_year_rating'].median())

sns.countplot(data=train, x='is_promoted')
plt.title('Count of Promoted Employees')
plt.show()

test['education']=test['education'].fillna(test['education'].mode()[0],inplace=True)
test['previous_year_rating'] = test['previous_year_rating'].fillna(test['previous_year_rating'].median(),inplace=True)

#DUPLICATES
train.duplicated().sum()

from sklearn.preprocessing import LabelEncoder
cat_col=['department','education','gender','recruitment_channel', 'region']
le=LabelEncoder()
for col in cat_col:
  train[col]=le.fit_transform(train[col])
  test[col]=le.fit_transform(test[col])

le=LabelEncoder()
train['is_promoted']=le.fit_transform(train['is_promoted'])
train['education']=le.fit_transform(train['education'])
test['education']=le.fit_transform(test['education'])

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

train_X[num_cols] = scaler.fit_transform(train_X[num_cols])
test[num_cols] = scaler.transform(test[num_cols])

from xgboost import XGBClassifier # Ensure XGBClassifier is available
xgb_clf = XGBClassifier(use_label_encoder=False,eval_metric='logloss')
xgb_clf.fit(x_train, y_train)
y_pred = xgb_clf.predict(x_test)

xgb_clf.fit(x_train, y_train)
y_pred = xgb_clf.predict(x_test)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train_scaled=sc.fit_transform(x_train)
x_test_scaled=sc.transform(x_test)
test_scaled=sc.transform(test)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,f1_score

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
y_pred

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)
y_pred

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(x_train,y_train)
y_pred=rf.predict(x_test)
y_pred

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.ensemble import GradientBoostingClassifier
gb=GradientBoostingClassifier()
gb.fit(x_train,y_train)
y_pred=gb.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
nb=GaussianNB()
nb.fit(x_train,y_train)
y_pred=nb.predict(x_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
svc=SVC()
svc.fit(x_train,y_train)
y_pred=svc.predict(x_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn. neural_network import MLPClassifier
mlp=MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=1000)
mlp.fit(x_train,y_train)
y_pred=mlp.predict(x_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from xgboost import XGBClassifier
xgb_clf = XGBClassifier()
xgb_clf.fit(x_train, y_train)
y_pred = xgb_clf.predict(x_test)
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.ensemble import GradientBoostingClassifier
gb=GradientBoostingClassifier()
gb.fit(x_train,y_train)
y_pred=gb.predict(x_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=50)
rf.fit(x_train,y_train)
y_pred=rf.predict(x_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))



from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=200)
rf.fit(x_train,y_train)
y_pred=rf.predict(x_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=100)
rf.fit(x_train,y_train)
y_pred=rf.predict(x_test)
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

submission=pd.read_csv("/content/sample_submission_M0L0uXE.csv")
# Generate predictions on the original test data
y_pred_test = xgb_clf.predict(test_scaled)
submission['is_promoted']=y_pred_test
submission.to_csv('submission.csv',index=False)