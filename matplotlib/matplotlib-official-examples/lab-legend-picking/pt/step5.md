# Mapear Linhas da Legenda para as Linhas Originais

Mapearemos as linhas da legenda para as linhas originais usando um dicionário.

```python
lines = [line1, line2]
lined = {}  # Will map legend lines to original lines.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Enable picking on the legend line.
    lined[legline] = origline
```
