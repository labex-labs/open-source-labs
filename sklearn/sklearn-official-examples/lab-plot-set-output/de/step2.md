# Konfiguriere einen Transformator, um DataFrames auszugeben

Um einen Schätzer wie `preprocessing.StandardScaler` so zu konfigurieren, dass er DataFrames zurückgibt, rufe `set_output` auf.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
