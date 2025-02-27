# Загрузка данных

Мы будем загружать датасет ирисов с использованием модуля `datasets` из Scikit-Learn. Мы будем использовать только два признака: длину чашелистика и длину лепестка.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```
