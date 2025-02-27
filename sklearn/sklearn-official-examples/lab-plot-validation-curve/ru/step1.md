# Загрузка набора данных

Начнем с загрузки набора данных digits из scikit-learn и выбора подмножества данных для бинарной классификации цифр 1 и 2.

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # binary classification: 1 vs 2
X, y = X[subset_mask], y[subset_mask]
```
