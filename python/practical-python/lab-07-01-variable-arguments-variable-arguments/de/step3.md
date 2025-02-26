# Kombinieren beider

Eine Funktion kann auch eine beliebige Anzahl von variablen Schlüsselwort- und Nicht-Schlüsselwortargumenten akzeptieren.

```python
def f(*args, **kwargs):
...
```

Funktionsaufruf:

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Die Argumente werden in positionale und Schlüsselwortkomponenten getrennt:

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
...
```

Diese Funktion nimmt beliebige Kombinationen von positionellen oder Schlüsselwortargumenten entgegen. Sie wird manchmal verwendet, wenn Wrapper geschrieben werden oder wenn Sie Argumente an eine andere Funktion weiterleiten möchten.
