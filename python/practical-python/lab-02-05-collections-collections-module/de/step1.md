# Beispiel: Zählen von Dingen

Angenommen, Sie möchten die Gesamtanteile jeder Aktie tabellieren.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

In dieser Liste gibt es zwei Einträge für `IBM` und zwei Einträge für `GOOG`. Die Anteile müssen auf irgend eine Weise zusammengefasst werden.
