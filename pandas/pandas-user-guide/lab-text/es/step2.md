# Utilizar métodos de cadenas

Pandas proporciona una suite de métodos de procesamiento de cadenas que facilitan la operación sobre datos de cadena. Estos métodos excluyen automáticamente los valores faltantes/NA.

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# convertir a minúsculas
s.str.lower()

# convertir a mayúsculas
s.str.upper()

# calcular la longitud de cada cadena
s.str.len()
```
