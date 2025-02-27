# Загрузка данных

Сначала мы загрузим набор данных о диабете.

```python
diabetes = datasets.load_diabetes()
X, y = diabetes.data, diabetes.target
```
