# Gleitkommazahlen (float)

Verwenden Sie eine Dezimal- oder Exponentialnotation, um einen Gleitkomma-Wert anzugeben:

```python
a = 37.45
b = 4e5 # 4 x 10**5 oder 400.000
c = -1.345e-10
```

Gleitkommazahlen werden als Doppeltgenauigkeit mit der nativen CPU-Darstellung [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) dargestellt. Dies entspricht dem `double`-Typ in der Programmiersprache C.

> 17 Stellen Genauigkeit\
> Exponent von -308 bis 308

Bedenken Sie, dass Gleitkommazahlen bei der Darstellung von Dezimalzahlen ungenau sind.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

Dies ist **kein Python-Problem**, sondern die zugrunde liegende Gleitkomma-Hardware auf der CPU.

Häufige Operationen:

    x + y      Addieren
    x - y      Subtrahieren
    x * y      Multiplizieren
    x / y      Teilen
    x // y     Ganzzahldivision
    x % y      Modulo
    x ** y     Potenzieren
    abs(x)     Betrag

Dies sind die gleichen Operatoren wie bei Ganzzahlen, mit Ausnahme der bitweisen Operatoren. Weitere mathematische Funktionen finden Sie im `math`-Modul.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
