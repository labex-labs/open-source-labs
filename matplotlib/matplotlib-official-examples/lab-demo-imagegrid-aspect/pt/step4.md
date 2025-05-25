# Definir a proporção (aspect ratio)

Definiremos a proporção (aspect ratio) das células nos ImageGrids para 2 usando a função `set_aspect()`.

```python
for i in [0, 1]:
    grid1[i].set_aspect(2)

for i in [1, 3]:
    grid2[i].set_aspect(2)
```
