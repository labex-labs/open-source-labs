# Загружаем датасет

Далее мы загрузим датасет Iris с использованием функции `load_iris()` из scikit-learn. Затем мы разделим переменные признаков (X) и целевой (y).

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
