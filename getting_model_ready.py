import pandas as pd
from sklearn import preprocessing
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load


data = pd.read_csv('dataset.csv')
print(data.head())
print(data.shape)
print(data.columns)

performance = data['PerformanceScore']

data = data[['DaysLateLast30', 'EngagementSurvey', 'Salary',
             'DateofHire', 'Absences', 'DOB', 'EmpSatisfaction']]

enc = dict()
for i in data.columns:
    if data[i].dtype == 'object':
        enc[i] = preprocessing.LabelEncoder()
        data[i] = enc[i].fit_transform(data[i])

print(data.head())


clf = RandomForestClassifier()
clf.fit(data, performance)

X = [0, 4.60, 199000, enc['DateofHire'].fit_transform(['7/5/2011'])[0], 0, enc['DOB'].fit_transform(['23/05/1997'])[0] , 4.6]
print(X)

dump(clf, 'model.joblib')
dump(enc, 'encoder.joblib')

clf_loaded = load('model.joblib')
print(clf_loaded.predict([X]))






