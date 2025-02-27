# Configurer un transformateur pour produire des DataFrames

Pour configurer un estimateur tel que `preprocessing.StandardScaler` pour renvoyer des DataFrames, appelez `set_output`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
