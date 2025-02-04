# -*- coding: utf-8 -*-
"""dataminingpr.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tueb4WG-hKcXzKvlZCfWWsuJaO3KkY8T
"""

# Commented out IPython magic to ensure Python compatibility.
#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression

#read data
test_data=pd.read_csv('test.csv')
train_data=pd.read_csv('train.csv')

#balance data
counts = train_data['Response'].value_counts()
zero_count = counts[0]
one_count = counts[1]
filtered_rows = train_data[train_data['Response'] == 0]
remaining_rows = filtered_rows.drop(filtered_rows.index[:(zero_count-one_count)])
df = pd.concat([train_data[train_data['Response'] != 0], remaining_rows])
train_data=df

#prepare data
train_data.drop('id',axis=1,inplace=True)
test_data.drop('id',axis=1,inplace=True)

#split features and target
X = train_data.drop("Response", axis=1)
y = train_data["Response"]
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

#train models
#CLF = RandomForestClassifier(n_estimators=100, random_state=42)
#CLF = xgb.XGBClassifier(colsample_bytree=0.6, learning_rate=0.01, max_depth=9, min_child_weight=10, n_estimators=300, subsample=0.6)
#CLF = DecisionTreeClassifier(criterion='gini' , min_samples_split=5 ,min_samples_leaf=3 ,max_features='sqrt' , max_depth=25, random_state=42)
CLF = LinearRegression(n_jobs=1)
CLF.fit(x_train,y_train)

#make predictions
y_predict = CLF.predict(test_data)

#save data
id=np.arange(len(y_predict))
datatest=pd.DataFrame({'id':id,'Response':y_predict})
datatest.to_csv('predicted.csv',index=False)