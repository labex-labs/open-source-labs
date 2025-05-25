# Exercício 5.5: Herança (Inheritance)

Crie uma nova classe que herda de `Stock`.

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

A herança (inheritance) é implementada estendendo o processo de busca por atributos. O atributo `__bases__` possui uma tupla dos pais imediatos:

```python
>>> NewStock.__bases__
(<class 'stock.Stock'>,)
>>>
```

O atributo `__mro__` possui uma tupla de todos os pais, na ordem em que serão pesquisados os atributos.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class 'stock.Stock'>, <class 'object'>)
>>>
```

Veja como o método `cost()` da instância `n` acima seria encontrado:

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
