# Schlüsselwortvariable Argumente (\*\*kwargs)

Eine Funktion kann auch eine beliebige Anzahl von Schlüsselwortargumenten akzeptieren. Beispielsweise:

```python
def f(x, y, **kwargs):
...
```

Funktionsaufruf:

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Die zusätzlichen Schlüsselwörter werden in einem Wörterbuch übergeben.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
```
