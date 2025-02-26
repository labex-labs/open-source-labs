# Ajustando los tipos

En la clase `Stock` actual, hay una variable de clase `_types` que proporciona conversiones al leer desde un archivo, pero también hay propiedades que están aplicando comprobaciones de tipos. ¿Quién está a cargo de todo esto? Corrige las definiciones de las propiedades para que usen los tipos especificados en la variable de clase `_types`. Asegúrate de que las propiedades funcionen cuando los tipos se cambian a través de la subclasificación. Por ejemplo:

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        _types = (str, int, Decimal)

>>> s = DStock('AA', 50, Decimal('91.1'))
>>> s.price = 92.3
Traceback (most recent call last):
...
TypeError: Expected a Decimal
>>>
```

**Discusión**

La clase `Stock` resultante al final de este laboratorio es un desorden confuso de propiedades, comprobación de tipos, constructores y otros detalles. Imagina lo incómodo que sería mantener código que tuviera docenas o cientos de definiciones de clase como esta.

Vamos a descubrir cómo simplificar las cosas considerablemente, pero tomará un tiempo y algunas técnicas más avanzadas. Manten la atención.
