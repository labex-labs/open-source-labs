# Mapper les lignes de la légende aux lignes originales

Nous allons mapper les lignes de la légende aux lignes originales à l'aide d'un dictionnaire.

```python
lines = [line1, line2]
lined = {}  # Va mapper les lignes de la légende aux lignes originales.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Active la sélection sur la ligne de la légende.
    lined[legline] = origline
```
