# Conversión de un array estructurado a un array de registros

Podemos convertir un array estructurado en un array de registros utilizando el método `view` y especificando el tipo `np.recarray`.

```python
# Convierte un array estructurado en un array de registros
recordarr = x.view(np.recarray)
```
