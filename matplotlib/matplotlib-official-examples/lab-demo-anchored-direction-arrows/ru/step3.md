# Создаем простую стрелку

Теперь мы создадим простую направленную стрелку с привязкой с использованием класса `AnchoredDirectionArrows`. Эта стрелка будет показывать направления по осям X и Y на графике.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
