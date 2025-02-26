# Positionalvariable Argumente (\*args)

Eine Funktion, die eine beliebige Anzahl von Argumenten akzeptiert, wird als Funktion mit variablen Argumenten bezeichnet. Beispielsweise:

```python
def f(x, *args):
 ...
```

Funktionsaufruf:

```python
f(1,2,3,4,5)
```

Die zusätzlichen Argumente werden als Tupel übergeben.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```
