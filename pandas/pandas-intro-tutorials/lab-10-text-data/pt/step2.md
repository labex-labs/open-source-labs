# Converter Caracteres de String para Minúsculas

Em seguida, converteremos todos os caracteres na coluna `Name` para minúsculas. Usaremos o método `str.lower()` para conseguir isso.

```python
# Converter todos os caracteres na coluna 'Name' para minúsculas
titanic["Name"] = titanic["Name"].str.lower()
```
