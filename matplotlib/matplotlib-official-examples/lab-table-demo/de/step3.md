# Erstellen von Zeilenbezeichnungen

Wir werden Zeilenbezeichnungen für den Datensatz erstellen, um die Anzahl der Jahre darzustellen, für die die Verluste aufgezeichnet wurden. Wir werden eine Listenkomprehension verwenden, um die Zeilenbezeichnungen zu erstellen.

```python
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
```
