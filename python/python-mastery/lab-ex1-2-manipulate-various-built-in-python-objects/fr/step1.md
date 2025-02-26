# Partie 1 : Nombres

Les calculs numériques fonctionnent comme vous l'attendez en Python. Par exemple :

```python
>>> 3 + 4*5
23
>>> 23.45 / 1e-02
2345.0
>>>
```

Attention, la division entière est différente en Python 2 et en Python 3.

```python
>>> 7 / 4      # En python 2, cela s'arrondit à 1
1.75
>>> 7 // 4     # Division tronquée
1
>>>
```

Si vous voulez le comportement de Python 3 en Python 2, faites ceci :

```python
>>> from __future__ import division
>>> 7 / 4
1.75
>>> 7 // 4      # Division tronquée
1
>>>
```

Les nombres ont un petit ensemble de méthodes, dont beaucoup sont relativement récentes et ignorées même par les programmeurs Python expérimentés. Essayez-en quelques-unes.

```python
>>> x = 1172.5
>>> x.as_integer_ratio()
(2345, 2)
>>> x.is_integer()
False
>>> y = 12345
>>> y.numerator
12345
>>> y.denominator
1
>>> y.bit_length()
14
>>>
```
