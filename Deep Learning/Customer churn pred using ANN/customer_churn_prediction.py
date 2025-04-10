# -*- coding: utf-8 -*-
"""customer churn prediction.ipynb


"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("/content/WA_Fn-UseC_-Telco-Customer-Churn.csv")

df

df.drop('customerID',axis=1,inplace=True)

df.dtypes

df.TotalCharges.values

# feature containing spaces retrieve the rows the no of rows
pd.to_numeric(df.TotalCharges,errors='coerce').isnull().sum()

df[pd.to_numeric(df.TotalCharges,errors='coerce').isnull()]

df.shape

df.iloc[488]

df1=df[df.TotalCharges!=' ']
df1

df1.TotalCharges=pd.to_numeric(df1.TotalCharges)

df1.TotalCharges.dtypes

# visualization
tenure_churn_no=df1[df1.Churn=='No'].tenure
tenure_churn_yes=df1[df1.Churn=='Yes'].tenure

plt.hist([tenure_churn_no,tenure_churn_yes],color=['green','red'],label=['churn_yes','churn_no'])
plt.legend()

for column in df:
  print(column)
  print(df1[column].unique())

import warnings
warnings.filterwarnings('ignore')
df1.replace('No phone service','No',inplace=True)
df1.replace('No internet service','No',inplace=True)

yes_no=['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity',
        'OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies',
        'PaperlessBilling','Churn']

for col in yes_no:
  df1[col].replace({'Yes':1,'No':0},inplace=True)

df1

df1['gender'].replace({'Female':0,'Male':1},inplace=True)

df1

df1.PaymentMethod.values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df1['PaymentMethod']=le.fit_transform(df1['PaymentMethod'])
df1['InternetService']=le.fit_transform(df1['InternetService'])
df1['Contract']=le.fit_transform(df1['Contract'])

df1.replace({'True':1,'False':0},inplace=True)

df1.dtypes

x=df1.drop('Churn',axis=1)
y=df1['Churn']

x.shape

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=5,test_size=0.2)

x_train.shape

import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(19, input_shape=(19,), activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(14,activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=20)

model.evaluate(x_test,y_test)

yp=model.predict(x_test)
yp

y_pred=[]
for element in yp:
  if element>0.5:
    y_pred.append(1)
  else:
    y_pred.append(0)

y_pred[0:5]

y_test[0:5]

from sklearn import metrics
print(metrics.classification_report(y_test,y_pred))

import seaborn as sns
cm=metrics.confusion_matrix(y_pred,y_test)
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True,fmt='d')
plt.xlabel('predicted')
plt.ylabel('truth')

# accuracy finding
round((669+298)/(669+330+110+298),2)
