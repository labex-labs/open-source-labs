# Entiers mutables

Les entiers Python sont normalement immuables. Cependant, supposons que vous vouliez créer un objet entier mutable. Commencez par créer une classe comme ceci :

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

Essayez-le :

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt object at 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'int'
>>>
```

Cela est très intéressant, sauf que rien ne fonctionne vraiment avec cet objet `MutInt` nouveau. L'affichage est horrible, aucun des opérateurs mathématiques ne fonctionne, et c'est globalement plutôt inutile. Eh bien, sauf le fait que sa valeur est mutable - il a bien cela.
