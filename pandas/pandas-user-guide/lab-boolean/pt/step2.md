# Indexação com valores NA

O Pandas permite a indexação com valores `NA` em um array booleano, que são tratados como `False`.

```python
# Criando uma Series do pandas
s = pd.Series([1, 2, 3])

# Criando um array booleano com valores NA
mask = pd.array([True, False, pd.NA], dtype="boolean")

# Indexando a série com o array booleano
s[mask] # Valores NA são tratados como False
```

Se você deseja manter os valores `NA`, você pode preenchê-los manualmente com `fillna(True)`.

```python
# Preenchendo valores NA com True e indexando a série
s[mask.fillna(True)]
```
