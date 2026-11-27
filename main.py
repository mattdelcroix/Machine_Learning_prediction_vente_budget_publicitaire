import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("data/advertising.csv")
# Explorons rapidement les données avec
print(df.head())
print(df.describe())


## Analyse bivariée
# Afficher le nuage de points des variables tv, radio et journaux en fonction des ventes.
# Tracer la ligne de régression pour chaque variable. 
fig, ax = plt.subplots(1,3, figsize = (15,5))

plt.subplot(1,3,1)
sns.regplot(x = df[['tv']], y  =  df.ventes)
plt.ylabel('ventes')
plt.xlabel('TV')
plt.title('ventes = a * tv  + b')
plt.grid()
sns.despine()

plt.subplot(1,3,2)
sns.regplot(x = df[['radio']], y  =  df.ventes)
plt.ylabel('ventes')
plt.xlabel('radio')
plt.title('ventes = a * radio + b')
plt.grid()
sns.despine()

plt.subplot(1,3,3)
res = sns.regplot(x = df[['journaux']], y  =  df.ventes)
plt.ylabel('ventes')
plt.xlabel('journaux')
plt.title('ventes = a * journaux + b')
plt.grid()
sns.despine()

# Le graphe montre que TV est plus prédictive des ventes que radio. Radio est plus prédictive que journaux. 
#plt.tight_layout()
#plt.show()

## Utilisation de la régression linéaire pour prédire les ventes.
reg = LinearRegression()

#on va scinder notre dataset en une partie d'entraînement et une partie d'évaluation en utilisant la fonction train_test_split de scikit-learn.
X = df[['tv','radio','journaux']]
y = df.ventes

#Notre jeu de données a 200 échantillons. Nous réservons 20% pour le test. 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#On entraine le modèle 
reg.fit(X_train, y_train)

#Obtenir les prédictions sur le jeux de test
y_pred_test = reg.predict(X_test)

#Utilisons la RMSE et la MAPE pour évaluer la performance du modèle 
print(f"RMSE: {mean_squared_error(y_test, y_pred_test)}")
print(f"MAPE: {mean_absolute_percentage_error(y_test, y_pred_test)}")
