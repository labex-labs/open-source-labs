# Выполнение операций с массивами с целочисленными значениями, допускающими значение `null`

Вы можете выполнять различные операции с массивами с целочисленными значениями, допускающими значение `null`, такие как арифметические операции, сравнения и извлечение срезов.

```python
# Create a Series with nullable integer type
s = pd.Series([1, 2, None], dtype="Int64")

# Perform arithmetic operation
s_plus_one = s + 1 # adds 1 to each element in the series

# Perform comparison
comparison = s == 1 # checks if each element in the series is equal to 1

# Perform slicing operation
sliced = s.iloc[1:3] # selects the second and third elements in the series
```
