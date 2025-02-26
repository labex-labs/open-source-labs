# Creación de una clase

Recuerde, de ejercicios anteriores, que definimos una clase simple `Stock` que se veía así:

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares
```

Lo que vamos a hacer aquí es crear la clase manualmente. Comencemos definiendo los métodos como funciones normales de Python.

```python
>>> def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

>>> def cost(self):
        return self.shares*self.price

>>> def sell(self,nshares):
        self.shares -= nshares

>>>
```

A continuación, cree un diccionario de métodos:

```python
>>> methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell }

>>>
```

Finalmente, cree el objeto de clase `Stock`:

```python
>>> Stock = type('Stock',(object,),methods)
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>> s.sell(25)
>>> s.shares
75
>>>
```

Felicitaciones, acaba de crear una clase. Una clase realmente no es más que un nombre, una tupla de clases base y un diccionario que contiene todos los contenidos de la clase. `type()` es un constructor que crea una clase para usted si suministra estas tres partes.
