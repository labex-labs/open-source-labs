# Кросс-таблицы

Кросс-таблица - это метод для количественного анализа взаимосвязи между несколькими переменными.

```python
# Cross tabulation between row and col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
