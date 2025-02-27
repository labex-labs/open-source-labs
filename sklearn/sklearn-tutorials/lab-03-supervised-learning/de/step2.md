# Lineare Regression

In diesem Schritt werden wir das Konzept der linearen Regression erkunden und sehen, wie es mit scikit-learn implementiert werden kann. Wir werden den Diabetes-Datensatz verwenden, der aus physiologischen Variablen von Patienten und deren Krankheitsverlauf nach einem Jahr besteht.

#### Lade den Diabetes-Datensatz

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### Erstelle und trainiere ein lineares Regressionsmodell

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### Mache Vorhersagen und berechne Leistungsmesswerte

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
