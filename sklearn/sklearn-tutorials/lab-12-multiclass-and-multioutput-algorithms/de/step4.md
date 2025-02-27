# Multioutput-Regression

#### Problem-Beschreibung

Multioutput-Regression prognostiziert mehrere numerische Eigenschaften für jede Probe. Jede Eigenschaft ist eine numerische Variable, und die Anzahl der Eigenschaften kann größer oder gleich zwei sein.

#### Zielformat

Eine gültige Darstellung von Multioutput-Regressionszielen ist eine dichte Matrix, wobei jede Zeile eine Probe und jede Spalte eine unterschiedliche Eigenschaft repräsentiert.

#### Beispiel

Lassen Sie uns ein Multioutput-Regressionsproblem mit der make_regression-Funktion erstellen:

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Generiere ein Multioutput-Regressionsproblem
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Trainiere ein Multioutput-lineares Regressionsmodell
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Mache Vorhersagen
predictions = model.predict(X)
print(predictions)
```
