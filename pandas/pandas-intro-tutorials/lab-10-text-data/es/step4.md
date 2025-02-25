# Extraer datos específicos de los pasajeros

A continuación, extraigamos los datos de los pasajeros que eran condesas a bordo del Titanic. Utilizaremos el método `str.contains()` para encontrar las filas en las que la columna `Nombre` contiene la palabra 'Condesa'.

```python
# Encontrar las filas donde 'Nombre' contiene 'Condesa'
condesas = titanic[titanic["Nombre"].str.contains("Condesa")]
```
