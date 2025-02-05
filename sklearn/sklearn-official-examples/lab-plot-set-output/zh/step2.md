# 配置变换器以输出DataFrame

要配置像`preprocessing.StandardScaler`这样的估计器以返回DataFrame，请调用`set_output`。

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
