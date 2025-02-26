# Ejercicio 3.8: Lanzamiento de excepciones

La función `parse_csv()` que escribiste en la última sección permite la selección de columnas especificadas por el usuario, pero eso solo funciona si el archivo de datos de entrada tiene encabezados de columna.

Modifica el código para que se lance una excepción si se pasan ambos argumentos `select` y `has_headers=False`. Por ejemplo:

```python
>>> parse_csv('/home/labex/project/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

Luego de agregar esta comprobación, podrías preguntarte si deberías realizar otros tipos de comprobaciones de validez en la función. Por ejemplo, ¿deberías comprobar que el nombre de archivo sea una cadena, que tipos sea una lista o algo por el estilo?

Como regla general, por lo general es mejor omitir esas pruebas y simplemente dejar que el programa falle con entradas incorrectas. El mensaje de traza apuntará a la fuente del problema y puede ayudar en la depuración.

La principal razón para agregar la comprobación anterior es evitar ejecutar el código en un modo sin sentido (por ejemplo, usar una característica que requiere encabezados de columna, pero al mismo tiempo especificar que no hay encabezados).

Esto indica un error de programación en el código llamador. Comprobar casos que "no deben suceder" a menudo es una buena idea.
