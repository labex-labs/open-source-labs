# Réconciliation des types

Dans la classe `Stock` actuelle, il y a une variable de classe `_types` qui fournit des conversions lors de la lecture à partir d'un fichier, mais il y a également des propriétés qui imposent des types. Qui est responsable de cette opération? Corrigez les définitions des propriétés de sorte qu'elles utilisent les types spécifiés dans la variable de classe `_types`. Assurez-vous que les propriétés fonctionnent lorsque les types sont modifiés par héritage. Par exemple :

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

**Discussion**

La classe `Stock` résultante à la fin de ce laboratoire est un véritable bordel de propriétés, de vérification de type, de constructeurs et d'autres détails. Imaginez à quel point il serait désagréable de maintenir un code comportant des dizaines voire des centaines de telles définitions de classe.

Nous allons découvrir comment simplifier considérablement les choses, mais cela va prendre du temps et des techniques plus avancées. Restez connecté.
