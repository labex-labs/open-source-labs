# Trainiere das Modell

Jetzt erstellen wir ein lineares Regressionsobjekt und trainieren das Modell mit den Trainingssets.

```python
from sklearn import linear_model

# Erstelle lineares Regressionsobjekt
regr = linear_model.LinearRegression()

# Trainiere das Modell mit den Trainingssets
regr.fit(diabetes_X_train, diabetes_y_train)
```
