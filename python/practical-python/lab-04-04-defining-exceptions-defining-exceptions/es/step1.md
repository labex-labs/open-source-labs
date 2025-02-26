# Ejercicio 4.11: Definiendo una excepción personalizada

A menudo es una buena práctica para las bibliotecas definir sus propias excepciones.

Esto facilita distinguir entre las excepciones de Python generadas en respuesta a errores de programación comunes y las excepciones intencionalmente generadas por una biblioteca para señalar un problema de uso específico.

Modifique la función `create_formatter()` del último ejercicio para que lance una excepción personalizada `FormatError` cuando el usuario proporciona un nombre de formato incorrecto.

Por ejemplo:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
