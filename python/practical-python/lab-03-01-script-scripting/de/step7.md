# Untere-zu-oben - Stil

Funktionen werden als Bausteine behandelt. Die kleineren / einfacheren Blöcke kommen zuerst.

```python
# myprogram.py
def foo(x):
  ...

def bar(x):
  ...
    foo(x)          # Obige Definition
  ...

def spam(x):
  ...
    bar(x)          # Obige Definition
  ...

spam(42)            # Der Code, der die Funktionen verwendet, erscheint am Ende
```

Später definierte Funktionen bauen auf früher definierten Funktionen auf. Dies ist wiederum nur ein stilistischer Aspekt. Das Wichtigste im obigen Programm ist, dass der Aufruf von `spam(42)` am Ende steht.
