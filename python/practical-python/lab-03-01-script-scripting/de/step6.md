# Funktionsdefinition

Funktionen können in beliebiger Reihenfolge _definiert_ werden.

```python
def foo(x):
    bar(x)

def bar(x):
    Anweisungen

# ODER
def bar(x):
    Anweisungen

def foo(x):
    bar(x)
```

Funktionen müssen nur vor ihrem tatsächlichen _Verwendung_ (oder Aufruf) während der Programmausführung definiert werden.

```python
foo(3)        # foo muss bereits definiert sein
```

Aus stilistischen Gründen ist es wahrscheinlich üblicher, Funktionen in einer _untere-zu-oben_ -Art und Weise zu definieren.
