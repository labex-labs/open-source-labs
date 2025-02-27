# Ausreißerprädiktionsfunktion

Der nächste Schritt besteht darin, eine Ausreißerprädiktionsfunktion zu definieren. In diesem Beispiel verwenden wir die Algorithmen `LocalOutlierFactor` und `IsolationForest`. Die `compute_prediction`-Funktion gibt den durchschnittlichen Ausreißerscore von X zurück.

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"Berechne {model_name} Vorhersage...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
