# Función de predicción de valores atípicos

El siguiente paso es definir una función de predicción de valores atípicos. En este ejemplo, utilizamos los algoritmos `LocalOutlierFactor` e `IsolationForest`. La función `compute_prediction` devuelve la puntuación media de valores atípicos de X.

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"Calculando la predicción con {model_name}...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
