# Ejercicio 1.31: Manejo de errores

¿Qué pasa si intenta usar su función en un archivo con algunos campos faltantes?

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

En este momento, se enfrenta a una decisión. Para que el programa funcione, puede limpiar el archivo de entrada original eliminando las líneas incorrectas o puede modificar su código para manejar las líneas incorrectas de alguna manera.

Modifique el programa `pcost.py` para capturar la excepción, imprimir un mensaje de advertencia y continuar procesando el resto del archivo.
