# Загрузка датасета

Мы загрузим датасет по недвижимости в Калифорнии с использованием функции `fetch_california_housing` из scikit-learn. Этот датасет содержит 20640 образцов и 8 признаков.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"Датасет содержит {n_samples} образцов и {n_features} признаков")
```
