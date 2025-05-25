# Detectando Rótulos Duplicados

Podemos verificar a existência de rótulos duplicados usando os métodos `Index.is_unique` e `Index.duplicated()`.

```python
# Verificando se o índice possui rótulos únicos
print(df1.index.is_unique)

# Verificando se as colunas possuem rótulos únicos
print(df1.columns.is_unique)

# Detectando rótulos duplicados no índice
print(df1.index.duplicated())
```
