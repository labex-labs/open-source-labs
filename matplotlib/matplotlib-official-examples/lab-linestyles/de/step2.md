# Definieren von Linienstilen

Es gibt verschiedene Möglichkeiten, Linienstile in Matplotlib zu definieren. Wir können vordefinierte Stile wie'solid' (fest), 'dashed' (gestrichelt), 'dotted' (punktiert) und 'dashdot' (gestrichelt-punktiert) verwenden. Wir können auch benutzerdefinierte Linienstile mit einem Dash-Tupel definieren.

```python
linestyle_str = [
     ('solid', 'fest'),      # Identisch mit (0, ()) oder '-'
     ('dotted', 'punktiert'),    # Identisch mit (0, (1, 1)) oder ':'
     ('dashed', 'gestrichelt'),    # Identisch mit '--'
     ('dashdot', 'gestrichelt-punktiert')]  # Identisch mit '-.'

linestyle_tuple = [
     ('lockerer punktiert',        (0, (1, 10))),
     ('punktiert',                (0, (1, 1))),
     ('dichter punktiert',        (0, (1, 1))),
     ('langer Strich mit Versatz', (5, (10, 3))),
     ('lockerer gestrichelt',        (0, (5, 10))),
     ('gestrichelt',                (0, (5, 5))),
     ('dichter gestrichelt',        (0, (5, 1))),

     ('lockerer gestrichelt-punktiert',    (0, (3, 10, 1, 10))),
     ('gestrichelt-punktiert',            (0, (3, 5, 1, 5))),
     ('dichter gestrichelt-punktiert',    (0, (3, 1, 1, 1))),

     ('gestrichelt-punktiert-punktiert',         (0, (3, 5, 1, 5, 1, 5))),
     ('lockerer gestrichelt-punktiert-punktiert', (0, (3, 10, 1, 10, 1, 10))),
     ('dichter gestrichelt-punktiert-punktiert', (0, (3, 1, 1, 1, 1, 1)))]
```
