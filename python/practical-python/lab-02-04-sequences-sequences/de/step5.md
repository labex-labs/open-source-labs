# Iteration über eine Sequenz

Die for-Schleife iteriert über die Elemente in einer Sequenz.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

Bei jeder Iteration der Schleife erhalten Sie ein neues Element, mit dem Sie arbeiten können. Dieser neue Wert wird in die Iterationsvariable eingefügt. In diesem Beispiel ist die Iterationsvariable `x`:

```python
for x in s:         # `x` ist eine Iterationsvariable
  ...statements
```

Bei jeder Iteration wird der vorherige Wert der Iterationsvariable überschrieben (sofern vorhanden). Nachdem die Schleife beendet ist, behält die Variable den letzten Wert bei.
