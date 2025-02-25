# Errores y excepciones

Las funciones informan de errores como excepciones. Una excepción hace que una función se detenga y puede hacer que todo su programa se detenga si no se maneja.

Pruebe esto en su intérprete interactivo de Python.

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

Para fines de depuración, el mensaje describe lo que sucedió, dónde ocurrió el error y una traza que muestra las otras llamadas a funciones que condujeron al fracaso.
