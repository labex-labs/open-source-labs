# Загрузка набора данных

Сначала нам нужно загрузить набор данных Iris с использованием встроенной функции `load_iris()` из scikit - learn.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```
