# Entraîner le modèle

Nous allons entraîner un modèle Isolation Forest avec les données d'entraînement.

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
