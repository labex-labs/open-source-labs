# Wie Vererbung funktioniert

Klassen können von anderen Klassen erben.

```python
class A(B, C):
  ...
```

Die Basisklassen werden in einem Tupel in jeder Klasse gespeichert.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

Dies liefert einen Link zu den Elternklassen.
