# Seleccionando filas y columnas específicas

Para seleccionar filas y columnas a la vez, usamos los operadores `loc` o `iloc`.

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```
