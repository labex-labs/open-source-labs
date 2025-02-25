# Obtener el Tipo de Datos de una Matriz

Para determinar el tipo de datos de una matriz, puedes acceder al atributo `dtype`. Por ejemplo:

```python
z.dtype
# devuelve el dtype de la matriz z, que es uint8
```

El objeto `dtype` también contiene información sobre el tipo, como su ancho en bits y el orden de los bytes. Puedes usar el objeto `dtype` para consultar propiedades del tipo, como si es un entero. Por ejemplo:

```python
d = np.dtype(int)
# crea un objeto dtype para int

np.issubdtype(d, np.integer)
# devuelve True, lo que indica que d es un subdtype de np.integer

np.issubdtype(d, np.floating)
# devuelve False, lo que indica que d no es un subdtype de np.floating
```
