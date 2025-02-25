# Types de données séquence

Python dispose de trois types de données _séquence_.

- Chaîne de caractères : `'Hello'`. Une chaîne de caractères est une séquence de caractères.
- Liste : `[1, 4, 5]`.
- Tuple : `('GOOG', 100, 490.1)`.

Toutes les séquences sont ordonnées, indexées par des entiers et ont une longueur.

```python
a = 'Hello'               # Chaîne de caractères
b = [1, 4, 5]             # Liste
c = ('GOOG', 100, 490.1)  # Tuple

# Ordre d'indexation
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Longueur de la séquence
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

Les séquences peuvent être replicées : `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Les séquences du même type peuvent être concaténées : `s + t`.

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
