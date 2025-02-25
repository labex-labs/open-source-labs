# Reemplazar valores en una columna

Finalmente, reemplazemos los valores en la columna `Sexo`: 'hombre' con 'M' y'mujer' con 'F'. Utilizaremos el método `replace()` para esto.

```python
# Reemplazar 'hombre' con 'M' y'mujer' con 'F' en la columna 'Sexo'
titanic["Sexo_corto"] = titanic["Sexo"].replace({"hombre": "M", "mujer": "F"})
```
