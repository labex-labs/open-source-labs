# Entrenar el modelo

Entrenaremos un modelo de Isolation Forest con los datos de entrenamiento.

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
