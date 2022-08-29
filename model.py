#importation de panda
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pickle
import requests
import json
%matplotlib inline

#La lecture du fichier CSV 
data=pd.read_csv('https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/rains.csv', sep=',', header=0)
data.head()

#Remplacement des valeurs manquants pour les variables numériques par la moyenne
data['MinTemp']=data['MinTemp'].fillna(data['MinTemp'].mean())
data['MaxTemp']=data['MaxTemp'].fillna(data['MaxTemp'].mean())
data['Rainfall']=data['Rainfall'].fillna(data['Rainfall'].mean())
data['Evaporation']=data['Evaporation'].fillna(data['Evaporation'].mean())
data['Sunshine']=data['Sunshine'].fillna(data['Sunshine'].mean())
data['WindGustSpeed']=data['WindGustSpeed'].fillna(data['WindGustSpeed'].mean())
data['WindSpeed9am']=data['WindSpeed9am'].fillna(data['WindSpeed9am'].mean())
data['WindSpeed3pm']=data['WindSpeed3pm'].fillna(data['WindSpeed3pm'].mean())
data['Humidity9am']=data['Humidity9am'].fillna(data['Humidity9am'].mean())
data['Humidity3pm']=data['Humidity3pm'].fillna(data['Humidity3pm'].mean())
data['Pressure9am']=data['Pressure9am'].fillna(data['Pressure9am'].mean())
data['Pressure3pm']=data['Pressure3pm'].fillna(data['Pressure3pm'].mean())
data['Cloud9am']=data['Cloud9am'].fillna(data['Cloud9am'].mean())
data['Cloud3pm']=data['Cloud3pm'].fillna(data['Cloud3pm'].mean())
data['Temp9am']=data['Temp9am'].fillna(data['Temp9am'].mean())
data['Temp3pm']=data['Temp3pm'].fillna(data['Temp3pm'].mean())
#Remplacement des valeurs manquants par No pour les variables RainToday et RainTomorow
data['RainToday'] = data['RainToday'].fillna('No')
data['RainTomorrow'] = data['RainTomorrow'].fillna('No')
#Test pour voir si ça a marché
data.isna().any(axis=0)
data_vf=data.replace(['Yes','No'],[1,0])
X = data_vf[['MinTemp','MaxTemp','Rainfall','Evaporation','Sunshine','WindGustSpeed','WindSpeed9am','WindSpeed3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm','RainToday']]
y = data_vf['RainTomorrow']
y.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2)

X_2=X.copy()

# On applique l'algorithme des KMeans pour un nombre de clusters égal à 2 
kmeans_2=KMeans(n_clusters=2, random_state=42)
kmeans_2.fit_predict(X_2)

y_pred = kmeans_2.predict(X_test)

y_pred

pickle.dump(kmeans_2, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb')) 

print(model.predict(X_test))