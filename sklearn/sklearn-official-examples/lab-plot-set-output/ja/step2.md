# トランスフォーマーを設定して DataFrame を出力する

`preprocessing.StandardScaler` などの推定器を設定して DataFrame を返すには、`set_output` を呼び出します。

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
