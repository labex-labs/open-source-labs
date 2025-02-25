# Convertir los caracteres de cadena a minúsculas

A continuación, convertiremos todos los caracteres de la columna `Name` a minúsculas. Utilizaremos el método `str.lower()` para lograr esto.

```python
# Convertir todos los caracteres de la columna 'Name' a minúsculas
titanic["Name"] = titanic["Name"].str.lower()
```
