#This Code is for Prediction
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

clf_loaded = load('model.joblib')
enc = load('encoder.joblib')

def get_performance(a,b,c,d,e,f,g):
    X = [a, b, c, enc['DateofHire'].fit_transform([d])[0], e, enc['DOB'].fit_transform([f])[0] , g]
    return(clf_loaded.predict([X]))


if __name__ == '__main__':
    a = int(input('No. of Days on Leave: '))
    b = float(input('Engagement Survey Score: '))
    c = int(input("Salary: "))
    d = input("Hiring Date in D/M/YYYY: ")
    e = int(input("Absences: "))
    f = input("DOB in D/M/YYYY: ")
    g = float(input("Employee Satisfaction: "))
    print(get_performance(a,b,c,d,e,f,g))
