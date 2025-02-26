# Un vrai décorateur

Indication : Complétez ce qui suit dans le fichier `validate.py`

Dans l'exercice 6.6, vous avez créé une classe appelable `ValidatedFunction` qui imposait des annotations de type. Réécrivez cette classe sous forme d'une fonction décoratrice appelée `validated`. Elle devrait vous permettre d'écrire du code comme ceci :

```python
from validate import Integer, validated

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y
```

Voici comment les fonctions décorées devraient fonctionner :

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>

>>> pow(2, 3)
8
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
```

Votre décorateur devrait essayer de corriger les exceptions pour qu'elles montrent des informations plus utiles comme indiqué. De plus, le décorateur `@validated` devrait fonctionner dans les classes (vous n'avez pas besoin de faire quoi que ce soit de spécial).

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
```

Note : Cette partie ne nécessite pas beaucoup de code, mais il y a beaucoup de détails fastidieux de bas niveau. La solution va ressembler presque exactement à celle de l'exercice 6.6. N'hésitez pas à regarder le code de la solution cependant.
