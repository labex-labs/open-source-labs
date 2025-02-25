# Zuordnen der Legendenlinien zu den ursprünglichen Linien

Wir werden die Legendenlinien zu den ursprünglichen Linien mithilfe eines Wörterbuchs zuordnen.

```python
lines = [line1, line2]
lined = {}  # Wird die Legendenlinien zu den ursprünglichen Linien zuordnen.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Aktivieren der Auswahl auf der Legendenlinie.
    lined[legline] = origline
```
