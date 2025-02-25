# Setzen des Seitenverhältnisses

Wir werden das Seitenverhältnis der Zellen in den ImageGrids auf 2 setzen, indem wir die `set_aspect()`-Funktion verwenden.

```python
for i in [0, 1]:
    grid1[i].set_aspect(2)

for i in [1, 3]:
    grid2[i].set_aspect(2)
```
