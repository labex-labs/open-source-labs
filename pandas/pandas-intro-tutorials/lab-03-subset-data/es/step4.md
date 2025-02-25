# Filtrando filas específicas

Para seleccionar filas basadas en una expresión condicional, use la condición dentro de los corchetes de selección `[]`.

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```
