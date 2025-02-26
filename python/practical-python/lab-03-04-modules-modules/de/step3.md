# Globale Definitionen

Alles, was im _globalen_ Bereich definiert ist, füllt den Modulnamenraum. Betrachten Sie zwei Module, die die gleiche Variable `x` definieren.

```python
# foo.py
x = 42
def grok(a):
 ...
```

```python
# bar.py
x = 37
def spam(a):
 ...
```

In diesem Fall beziehen sich die `x`-Definitionen auf unterschiedliche Variablen. Eine ist `foo.x` und die andere ist `bar.x`. Verschiedene Module können die gleichen Namen verwenden, und diese Namen werden nicht miteinander in Konflikt geraten.

**Module sind isoliert.**
