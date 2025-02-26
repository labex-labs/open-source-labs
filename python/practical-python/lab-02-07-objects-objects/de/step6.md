# Flache Kopien

Listen und Dictionaries haben Methoden zum Kopieren.

```python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Mach eine Kopie
>>> a is b
False
```

Es ist eine neue Liste, aber die Listenelemente werden geteilt.

```python
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
>>>
```

Zum Beispiel wird die innere Liste `[100, 101, 102]` geteilt. Dies ist eine flache Kopie. Hier ist ein Diagramm.

![Shallow copy](../assets/shallow.png)
