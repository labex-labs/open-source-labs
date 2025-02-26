# Parte 1 : Números

Los cálculos numéricos funcionan más o menos como se esperaría en Python. Por ejemplo:

```python
>>> 3 + 4*5
23
>>> 23.45 / 1e-02
2345.0
>>>
```

Tenga en cuenta que la división entera es diferente en Python 2 y Python 3.

```python
>>> 7 / 4      # En python 2, esto se trunca a 1
1.75
>>> 7 // 4     # División truncante
1
>>>
```

Si desea el comportamiento de Python 3 en Python 2, haga lo siguiente:

```python
>>> from __future__ import division
>>> 7 / 4
1.75
>>> 7 // 4      # División truncante
1
>>>
```

Los números tienen un pequeño conjunto de métodos, muchos de los cuales son en realidad bastante recientes e ignorados incluso por los programadores de Python experimentados. Pruebe algunos de ellos.

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
