# Загрузка данных

Далее мы загрузим набор данных ирисов (iris dataset) из библиотеки scikit-learn с использованием функции `load_iris`.

```python
data = load_iris()
X, y = data.data, data.target
```
