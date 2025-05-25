# Adicionar o primeiro diagrama

Adicionamos o primeiro diagrama usando `sankey.add()` com `flows=[1, -1]` e `orientations=[0, 1]`.

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```
