# Использование if/истинностных выражений с Pandas

Pandas не поддерживает непосредственное использование if/истинностных выражений из-за неоднозначности. Вместо этого используйте методы, такие как `.any()`, `.all()` или `.empty()`.

```python
# Check if any value in the Series is True
if pd.Series([False, True, False]).any():
    print("At least one True value in the Series")
```
