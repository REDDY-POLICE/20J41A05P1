#This code is for finding improtances of each column of Data

import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('dataset.csv')
print(data.head())

print(data.shape)

print(data.columns)

performance = data['PerformanceScore']

data = data.drop(columns=['Employee_Name', 'EmpID', 'State', 'Zip', 'Department', 'Sex',
                   'ManagerName', 'ManagerID', 'LastPerformanceReview_Date', 'PerformanceScore', 'PerfScoreID'])

enc = dict()
for i in data.columns:
    if data[i].dtype == 'object':
        enc[i] = preprocessing.LabelEncoder()
        data[i] = enc[i].fit_transform(data[i])

print(data.head())

train_x, test_x, train_y, test_y = train_test_split(data, performance, random_state = 3)

clf = RandomForestClassifier()
clf.fit(train_x, train_y)

pred = clf.predict(test_x)

print(accuracy_score(pred, test_y))
# print(classification_report(test_y, pred))

importance = [(i,j) for i,j in zip(clf.feature_importances_, data.columns)]
importances = sorted(importance, reverse=True)
print()
print(importances)





