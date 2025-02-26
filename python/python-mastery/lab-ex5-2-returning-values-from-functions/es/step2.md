# Devolviendo valores opcionales

A veces, una función puede devolver un valor opcional, posiblemente como un mecanismo para indicar éxito o fracaso. La convención más común es usar `None` como representación de un valor faltante. Modifica la función `parse_line()` anterior para que devuelva una tupla en caso de éxito o `None` si los datos son incorrectos. Por ejemplo:

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> parse_line('spam')       # Devuelve None
>>>
```

Discusión de diseño: ¿Sería mejor que la función `parse_line()` lanzara una excepción en caso de datos con formato incorrecto?
