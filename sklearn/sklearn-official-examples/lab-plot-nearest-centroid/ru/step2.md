# Загружаем данные

Далее мы загружаем набор данных iris из Scikit-learn и выбираем только первые два признака для визуализации.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
