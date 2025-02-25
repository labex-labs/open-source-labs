# Обработка пропущенных значений с использованием pandas.NA

Класс `IntegerArray` использует `pandas.NA` в качестве скалярного пропущенного значения. Когда вы выбираете отдельный пропущенный элемент, оно вернет `pandas.NA`.

```python
# Create an IntegerArray with a missing value
a = pd.array([1, None], dtype="Int64")

# Slice the second element which is a missing value
missing_value = a[1]
# Output: <NA>
```
