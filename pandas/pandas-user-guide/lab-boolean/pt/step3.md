# Operações lógicas de Kleene

O Pandas implementa a Lógica de Kleene (lógica de três valores) para operações lógicas como `&` (and - E), `|` (or - OU) e `^` (exclusive-or - OU exclusivo). Isso difere de como `np.nan` se comporta em operações lógicas.

```python
# Demonstrando a diferença nas operações 'or' entre np.nan e NA
pd.Series([True, False, np.nan], dtype="object") | True # np.nan se comporta de forma diferente
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA segue a lógica de Kleene

# Demonstrando a diferença nas operações 'and' entre np.nan e NA
pd.Series([True, False, np.nan], dtype="object") & True # np.nan se comporta de forma diferente
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA segue a lógica de Kleene
```
