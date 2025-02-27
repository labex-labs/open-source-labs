# Trainiere das Modell

Wir werden ein Isolation Forest-Modell mit den Trainingsdaten trainieren.

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
