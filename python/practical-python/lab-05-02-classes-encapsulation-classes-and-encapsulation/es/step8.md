# Acceso uniforme

El último ejemplo muestra cómo poner una interfaz más uniforme en un objeto. Si no haces esto, un objeto puede resultar confuso de usar:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> a = s.cost() # Método
49010.0
>>> b = s.shares # Atributo de datos
100
>>>
```

¿Por qué se requiere `()` para el costo, pero no para las acciones? Una propiedad puede solucionar esto.
