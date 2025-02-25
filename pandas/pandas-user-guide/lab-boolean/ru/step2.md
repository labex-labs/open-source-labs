# Индексирование с значениями NA

Pandas позволяет индексировать с помощью значений `NA` в булевом массиве, которые обрабатываются как `False`.

```python
# Creating a pandas Series
s = pd.Series([1, 2, 3])

# Creating a boolean array with NA values
mask = pd.array([True, False, pd.NA], dtype="boolean")

# Indexing the series with the boolean array
s[mask] # NA values are treated as False
```

Если вы хотите сохранить значения `NA`, вы можете вручную заполнить их `fillna(True)`.

```python
# Filling NA values with True and indexing the series
s[mask.fillna(True)]
```
