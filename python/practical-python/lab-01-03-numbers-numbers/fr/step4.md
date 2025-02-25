# Nombres à virgule flottante (float)

Utilisez une notation décimale ou exponentielle pour spécifier une valeur à virgule flottante :

```python
a = 37.45
b = 4e5 # 4 x 10**5 ou 400 000
c = -1.345e-10
```

Les flottants sont représentés en double précision en utilisant la représentation native de la CPU [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754). C'est la même chose que le type `double` dans le langage de programmation C.

> 17 chiffres de précision\
> Exposant de -308 à 308

Sachez que les nombres à virgule flottante sont imprécis lorsqu'ils représentent des décimales.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
Faux
>>> a
6.300000000000001
>>>
```

Ceci **n'est pas un problème de Python**, mais le matériel à virgule flottante sous-jacent de la CPU.

Opérations courantes :

    x + y      Addition
    x - y      Soustraction
    x * y      Multiplication
    x / y      Division
    x // y     Division entière
    x % y      Modulo
    x ** y     Puissance
    abs(x)     Valeur absolue

Ce sont les mêmes opérateurs que pour les entiers, sauf pour les opérateurs bit-à-bit. D'autres fonctions mathématiques se trouvent dans le module `math`.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
