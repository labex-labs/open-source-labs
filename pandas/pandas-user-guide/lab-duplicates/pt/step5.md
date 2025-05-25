# Impedindo Rótulos Duplicados

Se necessário, podemos impedir rótulos duplicados usando o método `set_flags(allows_duplicate_labels=False)`.

```python
# Impedindo rótulos duplicados em uma Series
try:
    pd.Series([0, 1, 2], index=["a", "b", "b"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)

# Impedindo rótulos duplicados em um DataFrame
try:
    pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "B", "C"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)
```
