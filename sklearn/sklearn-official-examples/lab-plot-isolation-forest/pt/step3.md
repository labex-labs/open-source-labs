# Treinar o Modelo

Vamos treinar um modelo Isolation Forest com os dados de treino.

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
