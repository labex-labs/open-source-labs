# Das Verständnis der Unterschiede zu NumPy

Pandas und NumPy haben geringfügige Unterschiede in der Berechnung der Varianz. Dies ist bei der Umschaltung zwischen den beiden Bibliotheken zu berücksichtigen.

```python
# Varianz in pandas
var_pandas = df.var()

# Varianz in NumPy
var_numpy = np.var(df.values)
```
