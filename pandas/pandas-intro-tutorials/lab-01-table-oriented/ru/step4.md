# Выполняем базовую статистику

Pandas предоставляет много функций для выполнения статистики. Например, вы можете найти максимальное значение в столбце с помощью `max()`.

```python
# Finding the maximum age
df["Age"].max()
```

Вы также можете получить быстрый обзор числовых данных в DataFrame с помощью `describe()`.

```python
# Describing the numerical data
df.describe()
```
