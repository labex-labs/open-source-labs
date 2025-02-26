# Ejercicio 3.10: Silenciar errores

Modifica la función `parse_csv()` para que los mensajes de error de análisis se puedan silenciar si el usuario lo desea explícitamente. Por ejemplo:

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```

El manejo de errores es una de las cosas más difíciles de hacer bien en la mayoría de los programas. Como regla general, no debes ignorar silenciosamente los errores. En cambio, es mejor informar sobre los problemas y dar a los usuarios la opción de silenciar el mensaje de error si lo eligen.
