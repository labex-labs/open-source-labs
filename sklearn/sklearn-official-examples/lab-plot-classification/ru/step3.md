# Подготавливаем данные

Мы возьмем только первые два признака датасета Iris, которые являются длиной чашелистика и шириной чашелистика. Затем мы разделим данные на матрицу признаков `X` и целевой вектор `y`.

```python
X = iris.data[:, :2]
y = iris.target
```
