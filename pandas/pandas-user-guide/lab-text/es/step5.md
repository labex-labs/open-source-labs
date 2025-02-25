# Crear variables ficticias

Puedes crear variables ficticias a partir de datos de cadena utilizando el método `get_dummies`.

```python
# crear variables ficticias
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```
