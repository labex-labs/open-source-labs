# Contando el número de registros por categoría

Finalmente, contaremos el número de registros por categoría.

```python
# Contando el número de pasajeros en cada clase de camarote
passengers_per_class = titanic["Pclass"].value_counts()
# Imprimiendo el resultado
print(f"El número de pasajeros en cada clase de camarote es {passengers_per_class}")
```
