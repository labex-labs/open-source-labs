# Definition von Hilfsfunktionen

Wir definieren zwei Hilfsfunktionen. Die erste Funktion, `to_ordinal`, wandelt eine Ganzzahl in einen ordinalen String um (z.B. 2 -> '2nd'). Die zweite Funktion, `format_score`, erstellt Score-Labels für die rechte y-Achse, indem der Testname gefolgt von der Maßeinheit (falls vorhanden) über zwei Zeilen aufgeteilt wird.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
