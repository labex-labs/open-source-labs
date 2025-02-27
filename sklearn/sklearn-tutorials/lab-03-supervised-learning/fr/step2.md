# Régression linéaire

Dans cette étape, nous explorerons le concept de régression linéaire et comment il peut être implémenté à l'aide de scikit-learn. Nous utiliserons l'ensemble de données sur le diabète, qui consiste en des variables physiologiques de patients et en leur évolution maladie après un an.

#### Charger l'ensemble de données sur le diabète

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### Créer et ajuster un modèle de régression linéaire

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### Faire des prédictions et calculer des métriques de performance

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
