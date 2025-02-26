# Ejercicio 3.9: Captura de excepciones

La función `parse_csv()` que escribiste se utiliza para procesar todo el contenido de un archivo. Sin embargo, en el mundo real, es posible que los archivos de entrada tengan datos dañados, faltantes o sucios. Intenta este experimento:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Modifica la función `parse_csv()` para capturar todas las excepciones `ValueError` generadas durante la creación de registros y mostrar un mensaje de advertencia para las filas que no se pueden convertir.

El mensaje debe incluir el número de fila y la información sobre el motivo por el cual falló. Para probar tu función, intenta leer el archivo `missing.csv` de arriba. Por ejemplo:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Fila 4: No se pudo convertir ['MSFT', '', '51.23']
Fila 4: Razón literal no válida para int() con base 10: ''
Fila 7: No se pudo convertir ['IBM', '', '70.44']
Fila 7: Razón literal no válida para int() con base 10: ''
>>>
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```
