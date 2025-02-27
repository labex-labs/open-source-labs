# Configurar un transformador para que produzca DataFrames

Para configurar un estimador como `preprocessing.StandardScaler` para que devuelva DataFrames, llame a `set_output`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
