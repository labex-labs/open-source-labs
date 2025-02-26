# Teil 1 : Zahlen

Numerische Berechnungen funktionieren in Python ungefähr so, wie Sie es erwarten würden. Beispielsweise:

```python
>>> 3 + 4*5
23
>>> 23.45 / 1e-02
2345.0
>>>
```

Bedenken Sie, dass die Ganzzahldivision in Python 2 und Python 3 unterschiedlich ist.

```python
>>> 7 / 4      # In python 2 wird dies abgeschnitten zu 1
1.75
>>> 7 // 4     # Abkürzende Division
1
>>>
```

Wenn Sie das Verhalten von Python 3 in Python 2 möchten, tun Sie Folgendes:

```python
>>> from __future__ import division
>>> 7 / 4
1.75
>>> 7 // 4      # Abkürzende Division
1
>>>
```

Zahlen haben eine kleine Menge an Methoden, von denen viele tatsächlich erst recht neu sind und von erfahrenen Python-Programmierern sogar übersehen werden. Testen Sie einige von ihnen.

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
