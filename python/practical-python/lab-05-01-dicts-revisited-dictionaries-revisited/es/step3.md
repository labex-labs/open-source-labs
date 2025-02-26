# Diccionarios y Objetos

Los objetos definidos por el usuario también utilizan diccionarios tanto para los datos de instancia como para las clases. De hecho, todo el sistema de objetos es en gran medida una capa adicional que se coloca encima de los diccionarios.

Un diccionario contiene los datos de instancia, `__dict__`.

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG','shares' : 100, 'price': 490.1 }
```

Se llena este diccionario (y la instancia) al asignar a `self`.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Los datos de instancia, `self.__dict__`, se ven así:

```python
{
    'name': 'GOOG',
   'shares': 100,
    'price': 490.1
}
```

**Cada instancia tiene su propio diccionario privado.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

Si creas 100 instancias de una clase determinada, hay 100 diccionarios almacenando datos.
