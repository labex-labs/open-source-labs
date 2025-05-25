# Contando o Número de Registros por Categoria

Finalmente, contaremos o número de registros por categoria.

```python
# Counting the number of passengers in each of the cabin classes
passengers_per_class = titanic["Pclass"].value_counts()
# Printing the result
print(f"The number of passengers in each of the cabin classes is {passengers_per_class}")
```
