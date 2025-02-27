# Загрузка датасета Iris

Мы будем загружать датасет Iris с использованием встроенной функции `load_iris` из Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # мы берем только первые два признака.
y = iris.target
```
