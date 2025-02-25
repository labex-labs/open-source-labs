# Sequenzdatentypen

Python hat drei _Sequenz_-Datentypen.

- String: `'Hello'`. Ein String ist eine Sequenz von Zeichen.
- Liste: `[1, 4, 5]`.
- Tupel: `('GOOG', 100, 490.1)`.

Alle Sequenzen sind geordnet, durch ganze Zahlen indiziert und haben eine Länge.

```python
a = 'Hello'               # String
b = [1, 4, 5]             # Liste
c = ('GOOG', 100, 490.1)  # Tupel

# Indizierte Reihenfolge
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Länge der Sequenz
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Sequenzen können repliziert werden: `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Sequenzen vom gleichen Typ können konkateniert werden: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```
