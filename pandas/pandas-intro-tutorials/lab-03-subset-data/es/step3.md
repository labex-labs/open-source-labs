# Seleccionando múltiples columnas

Para seleccionar múltiples columnas, use una lista de nombres de columnas dentro de los corchetes de selección `[]`.

```python
# Select the 'Age' and 'Sex' columns
age_sex = titanic[["Age", "Sex"]]

# Display the first 5 rows
age_sex.head()
```
