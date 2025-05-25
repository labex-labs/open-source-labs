# Configurar um transformador para produzir DataFrames

Para configurar um estimador, como `preprocessing.StandardScaler`, para retornar DataFrames, chame `set_output`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
