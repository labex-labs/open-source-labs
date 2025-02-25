# Добавляем первый диаграмму

Добавляем первую диаграмму с использованием `sankey.add()` с `flows=[1, -1]` и `orientations=[0, 1]`.

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```
