# Mutando con métodos de funciones definidas por el usuario (UDF)

Cuando se utiliza un método de pandas que toma una UDF, evite cambiar el DataFrame dentro de la UDF. En su lugar, haga una copia antes de realizar cambios.

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```
