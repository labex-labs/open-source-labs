# Convertendo um Record Array para um Structured Array

Para converter um record array de volta para um structured array, podemos usar o método `view` e especificar o dtype original do structured array.

```python
# Convert a record array to a structured array
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```
