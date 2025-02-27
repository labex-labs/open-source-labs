# Fonction de prédiction d'anomalies

L'étape suivante consiste à définir une fonction de prédiction d'anomalies. Dans cet exemple, nous utilisons les algorithmes `LocalOutlierFactor` et `IsolationForest`. La fonction `compute_prediction` renvoie la note moyenne d'anomalie de X.

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"Calcul de la prédiction {model_name}...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
