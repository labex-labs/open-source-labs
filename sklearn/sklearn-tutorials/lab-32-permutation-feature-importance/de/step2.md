# Trainiere das Modell

Als nächstes werden wir ein Regressionsmodell auf den Trainingsdaten trainieren. In diesem Beispiel werden wir ein Ridge-Regressionsmodell verwenden.

```python
from sklearn.linear_model import Ridge

# Trainiere das Ridge-Regressionsmodell
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```
