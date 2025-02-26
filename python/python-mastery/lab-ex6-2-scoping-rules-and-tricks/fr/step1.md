# Préparation

Dans l'exercice précédent, vous avez créé une classe `Structure` qui a facilité la définition de structures de données. Par exemple :

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

Cela fonctionne bien, sauf que beaucoup de choses sont assez étranges dans la fonction `__init__()`. Par exemple, si vous demandez de l'aide en utilisant `help(Stock)`, vous ne recevez pas de type de signature utile. De plus, la passe d'arguments par mot clé ne fonctionne pas. Par exemple :

```python
>>> help(Stock)
... regardez la sortie...

>>> s = Stock(name='GOOG', shares=100, price=490.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() a reçu un argument de mot clé inattendu 'price'
>>>
```

Dans cet exercice, nous allons examiner une approche différente du problème.
