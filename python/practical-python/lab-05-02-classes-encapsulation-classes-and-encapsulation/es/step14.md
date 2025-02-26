# Ejercicio 5.8: Agregando ranuras

Modifica la clase `Stock` de modo que tenga un atributo `__slots__`. Luego, verifica que no se puedan agregar nuevos atributos:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.blah = 42
... ver lo que pasa...
>>>
```

Cuando se utiliza `__slots__`, Python utiliza una representación interna más eficiente de los objetos. ¿Qué pasa si intentas inspeccionar el diccionario subyacente de `s` anterior?

```python
>>> s.__dict__
... ver lo que pasa...
>>>
```

Es importante destacar que `__slots__` se utiliza con más frecuencia como una optimización en clases que sirven como estructuras de datos. Usar ranuras hará que estos programas utilicen mucha menos memoria y ejecuten un poco más rápido. Sin embargo, probablemente debas evitar `__slots__` en la mayoría de las otras clases.
