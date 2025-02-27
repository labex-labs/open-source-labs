# Настройка трансформера для вывода DataFrame

Для настройки оценщика, такого как `preprocessing.StandardScaler`, чтобы он возвращал DataFrame, вызовите `set_output`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
