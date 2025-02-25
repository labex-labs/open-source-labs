# Conversión de un array de registros a un array estructurado

Para convertir un array de registros de nuevo en un array estructurado, podemos utilizar el método `view` y especificar el tipo de datos (`dtype`) original del array estructurado.

```python
# Convierte un array de registros en un array estructurado
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```
