# Ejercicio 7.8: Simplificando Llamadas a Funciones

En el ejemplo anterior, los usuarios pueden encontrar llamadas como `typedproperty('shares', int)` un poco verbosas para escribir, especialmente si se repiten muchas veces. Agregue las siguientes definiciones al archivo `typedproperty.py`:

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

Ahora, reescriba la clase `Stock` para usar estas funciones en lugar de las anteriores:

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, eso es un poco mejor. La principal lección aquí es que las cerraduras y `lambda` a menudo se pueden usar para simplificar el código y eliminar la repetición molesta. Esto suele ser bueno.
