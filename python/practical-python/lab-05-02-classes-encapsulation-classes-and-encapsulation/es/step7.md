# Propiedades

Existe un enfoque alternativo al patrón anterior.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Se esperaba un int')
        self._shares = value
```

El acceso a atributos normales ahora activa los métodos getter y setter debajo de `@property` y `@shares.setter`.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Activa @property
50
>>> s.shares = 75    # Activa @shares.setter
>>>
```

Con este patrón, no es necesario hacer _ningún cambio_ en el código fuente. El nuevo _setter_ también se llama cuando hay una asignación dentro de la clase, incluyendo dentro del método `__init__()`.

```python
class Stock:
    def __init__(self, name, shares, price):
     ...
        # Esta asignación llama al setter debajo
        self.shares = shares
     ...

  ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Se esperaba un int')
        self._shares = value
```

A menudo hay confusión entre una propiedad y el uso de nombres privados. Aunque una propiedad utiliza internamente un nombre privado como `_shares`, el resto de la clase (no la propiedad) puede continuar utilizando un nombre como `shares`.

Las propiedades también son útiles para atributos de datos calculados.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
  ...
```

Esto te permite omitir los paréntesis adicionales, ocultando el hecho de que en realidad es un método:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # Variable de instancia
100
>>> s.cost   # Valor calculado
49010.0
>>>
```
