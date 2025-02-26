# Ejercicio 5.5: Herencia

Crea una nueva clase que herede de `Stock`.

```python
>>> class NewStock(Stock):
        def yow(self):
            print('Yow!')

>>> n = NewStock('ACME', 50, 123.45)
>>> n.cost()
6172.50
>>> n.yow()
Yow!
>>>
```

La herencia se implementa extendiendo el proceso de búsqueda de atributos. El atributo `__bases__` tiene una tupla de los padres inmediatos:

```python
>>> NewStock.__bases__
(<class'stock.Stock'>,)
>>>
```

El atributo `__mro__` tiene una tupla de todos los padres, en el orden en que se buscarán atributos.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class'stock.Stock'>, <class 'object'>)
>>>
```

Aquí está cómo se encontraría el método `cost()` de la instancia `n` anterior:

```python
>>> for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

>>> cls
<class '__main__.Stock'>
>>> cls.__dict__['cost']
<function cost at 0x101aed598>
>>>
```
