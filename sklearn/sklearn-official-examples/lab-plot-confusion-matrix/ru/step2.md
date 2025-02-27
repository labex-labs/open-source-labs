# Загрузка данных

Мы будем использовать датасет iris из scikit-learn. Датасет содержит 150 образцов, каждый из которых имеет четыре признака и метку целевого класса.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
