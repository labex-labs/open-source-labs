# Загрузка данных

Первым шагом является загрузка набора данных о диабете из Scikit-Learn.

```python
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
```
