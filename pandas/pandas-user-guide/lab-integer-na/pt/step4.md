# Lidando com Valores Ausentes com pandas.NA

A classe `IntegerArray` usa `pandas.NA` como seu valor escalar ausente. Quando você fatia (slice) um único elemento que está ausente, ele retornará `pandas.NA`.

```python
# Criar um IntegerArray com um valor ausente
a = pd.array([1, None], dtype="Int64")

# Fatiar (slice) o segundo elemento que é um valor ausente
missing_value = a[1]
# Output: <NA>
```
