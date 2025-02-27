# Загрузка данных

Мы загрузим датасет diabetes из scikit-learn с использованием метода load_diabetes.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```
