# Operaciones lógicas de Kleene

Pandas implementa la Lógica de Kleene (lógica de tres valores) para operaciones lógicas como `&` (y), `|` (o) y `^` (o exclusivo). Esto difiere de cómo se comporta `np.nan` en las operaciones lógicas.

```python
# Demostrando la diferencia en las operaciones 'o' entre np.nan y NA
pd.Series([True, False, np.nan], dtype="object") | True # np.nan se comporta de manera diferente
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA sigue la lógica de Kleene

# Demostrando la diferencia en las operaciones 'y' entre np.nan y NA
pd.Series([True, False, np.nan], dtype="object") & True # np.nan se comporta de manera diferente
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA sigue la lógica de Kleene
```
