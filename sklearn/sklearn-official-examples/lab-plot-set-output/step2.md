# Configure a transformer to output DataFrames

To configure an estimator such as `preprocessing.StandardScaler` to return DataFrames, call `set_output`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
